import functools
import json
import requests
import streamlit as st

from PIL import Image


def generate(img_container=None):
    text = st.session_state.text_key
    j_text = json.dumps(text)
    requests.post(url=f"http://127.0.0.1:8000/prompts/{text}", data=j_text)
    response = requests.get(url=f"http://127.0.0.1:8000/images/-1")
    j_response = json.loads(response.content.decode('utf-8'))
    img_name = j_response['image']
    img = Image.open(f"images/{img_name}")
    st.image(img)
    return img


st.text_input(label="Please enter a prompt:", on_change=generate, key='text_key')
st.button("Regenerate", on_click=generate)

# if prompt:
#     img_name = generate(text=prompt)
#     img_name
#     img = Image.open(f"images/{img_name}")
#     st.image(img)
