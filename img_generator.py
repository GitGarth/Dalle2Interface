from base64 import b64decode
from gpt_core import GPT3
from PIL import Image

import os


class ImageGenerator(GPT3):
    def __init__(self):
        super().__init__()
        self.title = None
        self.image = None

    def get_image(self, text, title):
        response = self.gpt_image(text)
        self.image = b64decode(response['data'][0]['b64_json'])

    def save_image(self):
        file_path = os.path.join(os.path.curdir, "images", f"{self.title}.png")
        with open(file_path, "wb") as png:
            png.write(self.image)

    def display_image(self):
        Image.open(f"images/{self.title}.png").show()

    def create_image(self, text, title):
        self.title = title
        self.get_image(text, title)
        self.save_image()

    def render_new(self, text, title):
        self.get_image(text, title)
        self.save_image()
        self.display_image()
