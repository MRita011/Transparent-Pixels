# requires: pip install pillow

from PIL import Image

# Load the image and convert to RGBA (includes alpha channel for transparency)
# the image needs to be in this folder 
image = Image.open('your_image.png').convert('RGBA')

# Get the pixel data
pixels = image.getdata()

# Color to be made transparent (converted from hexadecimal to RGB)
target_color = (34, 177, 76)  # Color #22b14c in RGB

# Create a new list to store pixels with applied transparency
new_pixels = []
for pixel in pixels:
    r, g, b, a = pixel
    # If the pixel matches the specified color, make it transparent
    if (r, g, b) == target_color:
        new_pixels.append((r, g, b, 0))  # Transparent pixel
    else:
        new_pixels.append((r, g, b, a))  # Original pixel

# Update the image with the new pixels
image.putdata(new_pixels)

# Save the image with transparency
image.save('new_image.png')