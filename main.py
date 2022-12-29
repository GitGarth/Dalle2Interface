import functools
import json
import requests
import streamlit as st
import uvicorn

import os


def generate(img_container=None):
    text = st.session_state.text_key
    requests.post(url=f"http://127.0.0.1:8000/prompts/{text}")
    response = requests.get(url=f"http://127.0.0.1:8000/images/-1")
    img = json.loads(response.content.decode())['image']
    st.image(img)


st.text_input(label="Please enter a prompt:", on_change=generate, key='text_key')
st.button("Regenerate", on_click=generate)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
