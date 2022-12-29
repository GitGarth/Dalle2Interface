import uuid
from fastapi import FastAPI
from img_generator import ImageGenerator
app = FastAPI()

ig = ImageGenerator()

prompts = []
images = []


# @app.get("/prompts/{idx}")
# async def get_prompt(idx: int):
#     return {"prompt": prompts[idx]}
#
#
# @app.post("/prompts/{prompt}")
# def post_prompt(prompt: str):
#     prompts.append(prompt)
#     return prompt

@app.get("/")
def home():
    return {}


@app.get("/prompts/{idx}")
async def get_prompt(idx: int):
    return {"image": prompts[idx]}


@app.get("/images/{idx}")
async def get_image(idx: int):
    return {"image": images[idx]}


@app.post("/prompts/{prompt}")
async def post_prompt(prompt: str):
    prompts.append(prompt)
    image = ig.get_image(text=prompt)
    images.append(image)
    return prompt
