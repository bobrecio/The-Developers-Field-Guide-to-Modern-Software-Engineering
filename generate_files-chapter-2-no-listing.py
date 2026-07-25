import os
from pathlib import Path

# Define base directory
base_dir = Path("../test-files")
base_dir.mkdir(exist_ok=True)

# Sample content
lorem = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
)

# Base files to generate
base_files = [
    "year-2013-1.txt",
    "year-2014.txt",
    "year-2015.txt",
    "year-2016-a.txt",
    "year-2016-b.txt",
    "year-2017.txt"
]

# Create base files in test-files/
for filename in base_files:
    text = lorem
    if "2016-b" in filename:
        text += " Jeremy was here."
    with open(base_dir / filename, "w") as f:
        f.write(text)

# Create subdirectories inside test-files/
for i in range(1, 4):
    subdir = base_dir / f"additional-{i}"
    subdir.mkdir(parents=True, exist_ok=True)
    for filename in base_files:
        parts = filename.split("-")
        year_part = parts[1]
        suffix = str(i + 1)
        new_filename = f"year-{year_part.replace('.txt','').replace('a','').replace('b','')}-{suffix}.txt"
        text = lorem
        if "2016-b" in filename:
            text += " Jeremy was here."
        (subdir / new_filename).write_text(text)
