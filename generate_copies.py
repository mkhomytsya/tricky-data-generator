#!/usr/bin/env python3
"""Generate many files with tricky filenames by copying a placeholder's content.

Usage:
  python generate_copies.py --type image --placeholder path/to/placeholder.png --outdir output

If the placeholder path does not exist, the script will use the placeholder string
as textual content for each generated file.
"""

import argparse
import os
import sys
from pathlib import Path


IMAGE_NAMES = [
    'simple.jpg',
    'image.png',
    'my image.jpg',
    'photo with spaces.png',
    'image-2024.jpg',
    'photo_test_01.png',
    'file.name.jpg',
    'my"photo.jpg',
    '"quoted".jpg',
    'image"with"quotes.png',
    'φωτογραφία.jpg',
    '照片.jpg',
    'фото.png',
    'imágen.jpg',
    'Bild_ñ.png',
    'my (photo) [2024].jpg',
    'image #1 @home.png',
    'file&name.jpg',
    'this_is_a_very_long_filename_that_might_cause_issues_in_some_systems.jpg',
    '1.jpg',
    'a.png',
    '..jpg',
    'file name with  double  spaces.jpg',
    'my%20image.jpg',
    'file%22with%22quotes.png',
]

TEXT_NAMES = [name.rsplit('.', 1)[0] + '.txt' for name in IMAGE_NAMES]

AUDIO_NAMES = [
    n.rsplit('.', 1)[0] + ext
    for n in IMAGE_NAMES
    for ext in ('.mp3', '.wav')
]

VIDEO_NAMES = [
    n.rsplit('.', 1)[0] + ext
    for n in IMAGE_NAMES
    for ext in ('.mp4', '.mov')
]

TYPE_MAP = {
    'image': IMAGE_NAMES,
    'text': TEXT_NAMES,
    'audio': AUDIO_NAMES,
    'video': VIDEO_NAMES,
}


def parse_args():
    p = argparse.ArgumentParser(description='Create many files with tricky filenames.')
    p.add_argument('--type', '-t', choices=TYPE_MAP.keys(), required=True,
                   help='Type of targets to generate: text, image, audio, video')
    p.add_argument('--placeholder', '-p', required=True,
                   help='Path to placeholder file (or a string to use as content if file missing)')
    p.add_argument('--outdir', '-o', default='output', help='Output directory')
    return p.parse_args()


def load_placeholder(path: str) -> bytes:
    p = Path(path)
    if p.exists() and p.is_file():
        return p.read_bytes()
    # If file doesn't exist, treat the placeholder argument as text content
    return path.encode('utf-8')


def safe_write(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(data)


def main():
    args = parse_args()
    content = load_placeholder(args.placeholder)
    names = TYPE_MAP.get(args.type)
    if not names:
        print('Unknown type:', args.type, file=sys.stderr)
        sys.exit(2)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    created = []
    for name in names:
        target = outdir / name
        try:
            safe_write(target, content)
            created.append(str(target))
        except Exception as e:
            print(f'Failed to write {target}: {e}', file=sys.stderr)

    print(f'Wrote {len(created)} files to {outdir!s}')


if __name__ == '__main__':
    main()
