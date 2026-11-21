import os
from pathlib import Path


JOKE = "I narrate our live demos while my AI agent fixes bugs. Today it removed the crashing feature halfway through my sentence, so I became the roadmap."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
