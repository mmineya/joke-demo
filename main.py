import os
from pathlib import Path


JOKE = "My AI coding agent recorded my instructions during our live demo. I thought it was learning from me. It saved them as repro.py."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
