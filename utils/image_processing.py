from PIL import Image

# Predefined sizes
IMAGE_SIZES = {
    "300x250": (300, 250),
    "728x90": (728, 90),
    "160x600": (160, 600),
    "300x600": (300, 600),
}

def resize_image(image, size):
    """Resize an image to the specified size."""
    return image.resize(size, Image.LANCZOS)
 
