

"""Migration utility to reload and reserialize rainbow table files.

This script loads a serialized rainbow table (pickled `.rt` or similar),
rebuilds any missing internal structures (the loader already attempts
that), and writes the table back to disk. Use this to upgrade old
serialized tables so that future loads don't need to rebuild trees.
"""

import argparse
import os
import sys
from rainbowtable import RainbowTable


def main():
    parser = argparse.ArgumentParser(description="Migrate/re-save a rainbow table file to rebuild internal structures")
    parser.add_argument("input_file", help="Path to the input serialized rainbow table file")
    parser.add_argument("-o", "--output", help="Output file path; if omitted the input file will be overwritten")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Input file '{args.input_file}' not found")
        sys.exit(1)

    try:
        print(f"Loading table from {args.input_file}...")
        rt = RainbowTable.load_from_file(args.input_file)
    except Exception as e:
        print(f"Failed to load table: {e}")
        sys.exit(1)

    out_path = args.output if args.output else args.input_file
    # If output is same as input, we'll overwrite the file after successful load
    try:
        print(f"Saving migrated table to {out_path}...")
        success = rt.save_to_file(out_path)
        if success:
            print("Migration completed successfully.")
            sys.exit(0)
        else:
            print("Failed to write output file.")
            sys.exit(2)
    except Exception as e:
        print(f"Failed to save migrated table: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
