#!/usr/bin/env python3

import argparse
import sys

def get_file_extension(filename):
    """
    Extracts the file extension from a filename.
    """

    #This line splits the name of the file to the right on the occurence of a dot. If there is more than one dot in the name of the file
    #the name of the file is split on the last dot.
    parts = filename.rsplit('.', 1)
    if len(parts) == 1:
        raise ValueError("File extension not found")
    return f"Extension: {parts[1]}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts the file extension from a filename.")
    parser.add_argument("filename", help="The name of the file")
    args = parser.parse_args()

    try:
        extension = get_file_extension(args.filename)
        print(extension)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(14)
