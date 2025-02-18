import sys
from PIL import Image

def resize_and_pad_image(input_path, output_path):
    # Open the image
    image = Image.open(input_path)
    
    # Get original dimensions
    original_width, original_height = image.size
    
    # Calculate new dimensions
    new_width = original_width // 2
    
    # Resize the image width to 50% while keeping the height the same
    resized_image = image.resize((new_width, original_height))
    
    # Create a new image with white padding
    new_image = Image.new("RGB", (original_width, original_height), "white")
    
    # Paste the resized image onto the new image with padding on the left
    new_image.paste(resized_image, (original_width - new_width, 0))
    
    # Save the new image
    new_image.save(output_path)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    resize_and_pad_image(input_path, output_path)
