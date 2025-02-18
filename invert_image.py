import sys
from PIL import Image, ImageOps

def invert_image(input_path, output_path):
    image = Image.open(input_path)
    inverted_image = ImageOps.invert(image)
    inverted_image.save(output_path)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    invert_image(input_path, output_path)
