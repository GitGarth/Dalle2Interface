import openai
import os

OPENAI_KEY_FILE = os.path.join(
    os.path.expanduser("."),
    "openai_key.txt")


def read_file(filename):
    with open(filename, "r") as f:
        lines = "".join(f.readlines())
        return lines


class GPT3(object):
    def __init__(self, key_file=OPENAI_KEY_FILE):
        self.open_ai_key = read_file(key_file)
        openai.api_key = self.open_ai_key

    @staticmethod
    def gpt_completion(prompt, model="text-davinci-002", temp=0.5, max_tokens=1000, presence_penalty=0):
        response = openai.Completion.create(
            prompt=prompt,
            model=model,
            temperature=temp,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty
        )['choices'][0]['text'].strip()
        return response

    @staticmethod
    def gpt_embedding(text, engine="text-similarity-davinci-001"):
        response = openai.Embedding.create(
            input=text,
            engine=engine)['data'][0]['embedding']
        return response

    @staticmethod
    def gpt_edit(text, instruction, model="text-davinci-edit-001"):
        response = openai.Edit.create(
            input=text,
            instruction=instruction,
            model=model)['choices'][0]['text']
        return response['data']['url']

    @staticmethod
    def gpt_image(text, response_format="url"):
        response = openai.Image.create(prompt=text, n=1, size="1024x1024", response_format=response_format)
        return response


if __name__ == "__main__":
    gpt3 = GPT3()
    gpt3_response = gpt3.gpt_completion(prompt="Write a sentence.")
    vector = gpt3.gpt_embedding(text=gpt3_response)
    print(vector)
    edit = gpt3.gpt_edit(text=gpt3_response, instruction="Replace all nouns in input with the phrase, 'I like bacon.'")
    print(vector, gpt3_response, edit)

