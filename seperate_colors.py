import sys
from PIL import Image, ImageChops

def extract_specific_color(input_path, output_path, target_rgb):
    img = Image.open(input_path).convert("RGB")
    r, g, b = img.split()

    # Create a mask based on the proximity to the target color
    target_r, target_g, target_b = target_rgb
    mask_r = ImageChops.difference(r, Image.new('L', r.size, target_r))
    mask_g = ImageChops.difference(g, Image.new('L', g.size, target_g))
    mask_b = ImageChops.difference(b, Image.new('L', b.size, target_b))

    # Combine the masks
    mask = ImageChops.add(mask_r, mask_g)
    mask = ImageChops.add(mask, mask_b)

    # Invert the mask to highlight the target color
    mask = ImageChops.invert(mask)

    # Apply the mask to the original image
    result = Image.composite(img, Image.new('RGB', img.size, (0, 0, 0)), mask)
    result.save(output_path)

# Example usage
if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) != 6:
        print("Usage: python seperate_colors.py <input_image_path> <output_image_path> <r> <g> <b>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    target_rgb = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    print(target_rgb)
    extract_specific_color(input_path, output_path, target_rgb)