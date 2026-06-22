from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAX_MB = 5.0


TEXT_EXT = {
    ".py",
    ".md",
    ".txt",
    ".csv",
    ".tex",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".gitignore",
}

FORBIDDEN_PATTERNS = [
    "G:" + r"\\",
    "G:" + "/",
    "C:" + r"\\Users\\Administrator",
    "/home/" + "test",
    r"10\.110\.3\.71",
    r"192\.168\.96\.54",
    "我的" + "论文",
    "第十" + "八篇",
    r"@qq\.com",
    r"@163\.com",
    r"@gmail\.com",
]


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXT or path.name in {".gitignore"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--max-file-mb", type=float, default=DEFAULT_MAX_MB)
    args = parser.parse_args()

    problems: list[str] = []
    max_bytes = args.max_file_mb * 1024 * 1024
    patterns = [re.compile(p, re.I) for p in FORBIDDEN_PATTERNS]

    for path in args.root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.stat().st_size > max_bytes:
            problems.append(f"oversized file: {path.relative_to(args.root)} ({path.stat().st_size / 1024 / 1024:.2f} MB)")
        if path.is_file() and is_text_file(path):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError as exc:
                problems.append(f"cannot read: {path.relative_to(args.root)} ({exc})")
                continue
            for pat in patterns:
                if pat.search(text):
                    problems.append(f"forbidden pattern {pat.pattern!r}: {path.relative_to(args.root)}")
                    break

    if problems:
        print("Release verification failed:")
        for item in problems[:50]:
            print(f"- {item}")
        raise SystemExit(1)

    print("Release verification passed.")


if __name__ == "__main__":
    main()
