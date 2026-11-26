"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single line roasting a smart fridge, 200 characters
at most.
It sent a firmware update at 2 a.m. and now judges midnight snacks
in a push notification. The fridge is not an appliance anymore;
it is a critic with a camera and opinions about the milk.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
