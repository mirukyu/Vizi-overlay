from PIL import Image
from vizi_overlay import add_vizi_overlay
import sys


def usage():
    print(f"Usage: {sys.argv[0]} <input_image> <output_image>")
    sys.exit(1)


def main():
    # ensure proper number of command-line args
    if len(sys.argv) != 3:
        usage()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        img = Image.open(input_file)
    except Exception as e:
        print(f"Failed to open input file '{input_file}': {e}")
        sys.exit(1)

    try:
        result = add_vizi_overlay(img, input_file)
    except Exception as e:
        print(f"Error while adding overlay: {e}")
        sys.exit(1)

    try:
        result.save(output_file)
    except Exception as e:
        print(f"Failed to save output file '{output_file}': {e}")
        sys.exit(1)

    print("Overlay added successfully")


if __name__ == '__main__':
    main()