import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import time

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
os.environ['GOOGLE_API_KEY']="AIzaSyC9GswG0iCGEQEg9Ys4zWqJuKF6KO6h8yU"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    pass
def g_model(text):
   model = genai.GenerativeModel('gemini-pro')
   response = model.generate_content(text)
   print("+++")
   time.sleep(2)
   return response.text