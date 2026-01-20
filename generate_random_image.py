#!/usr/bin/env python3
"""Generate a single random image with random type, size, and content.

The generated file is named `random_image.<ext>` where `<ext>` is chosen
randomly from supported types (png, jpg, gif).

Usage:
  python generate_random_image.py [--outdir output_dir]

If Pillow is not installed, install it with `pip install -r requirements.txt`.
"""

import argparse
import os
import random
from pathlib import Path

try:
    from PIL import Image
except Exception:
    print('Pillow is required. Install with: pip install -r requirements.txt')
    raise


TYPES = ['png', 'jpg', 'gif']


def generate_random_image(outdir: Path) -> Path:
    ext = random.choice(TYPES)
    width = random.randint(16, 1024)
    height = random.randint(16, 1024)
    mode = 'RGB'

    # Random pixel bytes
    data = os.urandom(width * height * 3)
    img = Image.frombytes(mode, (width, height), data)

    outdir.mkdir(parents=True, exist_ok=True)
    filename = outdir / f'random_image.{ext}'

    # JPEG expects 'JPEG' format name
    fmt = 'JPEG' if ext == 'jpg' else ext.upper()
    img.save(filename, format=fmt)
    return filename


def parse_args():
    p = argparse.ArgumentParser(description='Generate one random image file')
    p.add_argument('--outdir', '-o', default='.', help='Output directory')
    return p.parse_args()


def main():
    args = parse_args()
    outdir = Path(args.outdir)
    path = generate_random_image(outdir)
    print(f'Generated: {path}')


if __name__ == '__main__':
    main()
