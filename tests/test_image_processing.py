import unittest
from PIL import Image
from utils.image_processing import resize_image, IMAGE_SIZES

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        self.image = Image.new("RGB", (1000, 1000), "blue")  # Create a test image

    def test_resize(self):
        for size_name, size in IMAGE_SIZES.items():
            resized = resize_image(self.image, size)
            self.assertEqual(resized.size, size, f"Failed resizing to {size_name}")

if __name__ == "__main__":
    unittest.main()
