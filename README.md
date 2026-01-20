# Tricky Data Generator

🎲 A comprehensive toolkit for generating edge-case test data to break parsers, validators, and applications.

## Overview

Tricky Data Generator produces problematic, edge-case, and "evil" test data to help you uncover bugs before they reach users. It focuses on creating inputs that commonly cause parsing, validation, or security issues.

## Focus for Now

At the moment this project concentrates on:

- `FilenameGenerator` — produce tricky filenames (quotes, Unicode, control characters, very long names, path traversal attempts, empty names, etc.)
- `ImageGenerator` — create sample image files with unusual metadata, tricky filenames, and binary edge patterns
- `SoundGenerator` (maybe) — generate or synthesize audio files with edge-case metadata and content
- `VideoGenerator` (maybe) — generate small video samples with unusual metadata or container quirks

The remaining categories are documented below as TODO items to be implemented later.

## Why This Project?

Real bugs are often exposed by inputs that are valid-but-unusual or outright malformed. This toolkit helps you stress-test systems by generating:

- Filenames with quotes, mixed encodings, or special Unicode
- Malformed headers and metadata
- Binary patterns and invalid encodings
- Injection and format-breaking payloads

If your application can safely handle these inputs in test environments, it will be much more robust in production.

## Features (Planned and Partial)

### Filename Generation

- Quotes and escaped quotes
- Unicode (international characters, emoji, right-to-left, zero-width)
- Control and special characters (null bytes, newlines, separators)
- Extremely long names and empty names
- Path traversal and reserved device names
- Variants suitable for `Content-Disposition`-style parsing

### Media Generators (Images / Audio / Video)

- Produce files with tricky filenames and metadata
- Create minimal sample images with unusual EXIF or other headers
- Generate binary blobs that simulate corrupted or borderline-valid media

## Quick Start (Pseudo)

Here are simple usage examples in pseudocode (implementation-agnostic):

```
// Generate tricky filenames
gen = new FilenameGenerator()
for name in gen.getAll():
    print(name)

// Create sample image file with a tricky name
imgGen = new ImageGenerator()
img = imgGen.createSampleImage("photo\"weird.jpg")
writeFile(img.path, img.data)

// Later: generate sample audio/video similarly
```

## Use Cases

- Test file upload handlers with strange filenames
- Validate parser robustness for metadata and headers
- Security testing for injection and encoding issues
- Fuzzing inputs for format-parsing libraries
## Included tools & Usage

This repository includes small helper tools and a `Makefile` to run common workflows:

- `generate_copies.py`: create many files with tricky filenames by copying a placeholder's content into multiple target names.
- `generate_random_image.py`: generate a single random image file named `random_image.<ext>` where `<ext>` is chosen randomly (png/jpg/gif).
- `Makefile`: convenience targets to prepare the environment and run the generators (see quick commands below).

Quick commands (run from the project root):

```
# create environment and install dependencies (via Makefile)
make venv

# generate one random image into ./output
make random-image

# generate copies (uses placeholder path configured in the Makefile target)
make copies

# run both generators
make generate

# cleanup generated files
make clean
```

Notes:

- The `venv`/environment setup is handled by the `Makefile` so you can run the included tools consistently.
- Adjust the `copies` target or call `generate_copies.py` directly if you want a different placeholder or output directory.

## TODO

- Implement and harden `FilenameGenerator` (priority)
- Implement `ImageGenerator` (priority)
- Prototype `SoundGenerator` and `VideoGenerator` (optional)
- Add generators for malformed headers and metadata
- Add content generators (malformed JSON/XML, injection payloads, XSS strings)
- Add utilities to write sample files to disk and produce test suites
- Add tests and example harnesses

## Contributing

Contributions are welcome. To contribute:

1. Fork the project
2. Add edge cases to the appropriate generator
3. Include a test case demonstrating the issue
4. Submit a pull request

## License

MIT License — Break things responsibly! ⚠️

## Warning

This tool generates data designed to break applications. Use only in controlled testing environments. Do not use these inputs maliciously or against production systems.

---

If your application can handle these inputs, it can handle almost anything your users throw at it.
# tricky-data-generator
A comprehensive toolkit for generating edge-case test data to break your parsers, validators, and applications.
