import os
import shutil

def process_file(input_file):
    # Open the file with the proper encoding
    with open(input_file, 'r', encoding='utf-16') as f:
        lines = f.readlines()

    namesList = []

    for i, line in enumerate(lines, start=1):
        # Skip the first 5 lines.
        if i <= 5:
            continue

        # Remove leading/trailing whitespace.
        line_stripped = line.strip()

        if '_ProIntlk,' in line_stripped:
            newLine = line_stripped.split('_', 3)[2]
            namesList.append(newLine)

        if '_Intlk,' in line_stripped:
            newLine = line_stripped.split('_', 3)[2]
            namesList.append(newLine)

    return namesList
