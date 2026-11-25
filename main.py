#!/usr/bin/env python3
"""news-image-20261124 v2 (Builder B): copy the bundled entry.png to the output dir.
Standard library only. Deterministic: identical bytes on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
os.chmod(OUT, 0o644)
print("wrote", OUT)
