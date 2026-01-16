import sys
from PIL import Image, ImageOps

def invert_image(input_path, output_image_path, border_size):
    img = Image.open(input_path)
    # Add border
    bordered_img = ImageOps.expand(img, border=border_size, fill='black')

    # Save the output image
    bordered_img.save(output_image_path)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_image_path> <output_border_path> <border_size>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    border_size = int(sys.argv[3])

    invert_image(input_path, output_path, border_size)
