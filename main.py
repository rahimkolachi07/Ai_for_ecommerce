import pandas as pd
import gradio as gr
from gemini.gemini import g_model
import time

def product_exp(data):
    for i, b in enumerate(data["Body (HTML)"]):
        z=1
        while z==1:
            try:
                if "str" in str(type(b)):
                    text = g_model(f"Translate  into Netherlands. {data.loc[i, 'Body (HTML)']}")
                    print(text)
                    data.loc[i, 'Body (HTML)'] = text
                    z=0
            except:
                z=1
    return data
            

def translated(data):
    # Ensure the 'Translated content' column is of type object
    data['Translated content'] = data['Translated content'].astype(object)
    
    for i, b in enumerate(data["Locale"]):
        z=1
        while z==1:
            try:
                if "str" in str(type(b)):
                    text = g_model(f"must translate this text = {data['Default content'][i]} into = {b} language")
                    print(text)
                    data.loc[i, 'Translated content'] = text
                    z=0
            except:
                z=1
                print("error")
                pass
    return data
