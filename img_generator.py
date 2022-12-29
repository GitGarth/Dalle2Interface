from base64 import b64decode
from gpt_core import GPT3

import os


class ImageGenerator(GPT3):
    def __init__(self):
        super().__init__()

    def get_image(self, text):
        response = self.gpt_image(text)
        image_url = response['data'][0]['url']
        return image_url