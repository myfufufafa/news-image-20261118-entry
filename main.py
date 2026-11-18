"""news-image-20261118 entry (Python 3.13, standard library only).

The entry is the image this repository holds: entry.png, a front page
summing up the world news of Wednesday 18 November 2026. The program
copies that image to the output directory as entry.png, byte for byte,
so both runs of the program write identical output.

Run locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")

# The copy must be exact: the judge sees exactly these bytes.
assert (OUTPUT_DIR / "entry.png").stat().st_size == (HERE / "entry.png").stat().st_size
