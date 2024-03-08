import pandas as pd
import gradio as gr
from gemini.gemini import g_model
import time

def product_exp(data):
    for i, b in enumerate(data["Body (HTML)"]):
        if "str" in str(type(b)):
            text = g_model(f"Translate  into Netherlands. {data.loc[i, 'Body (HTML)']}")
            print(text)
            data.loc[i, 'Body (HTML)'] = text
    return data

def translated(data):
    # Ensure the 'Translated content' column is of type object
    data['Translated content'] = data['Translated content'].astype(object)
    
    for i, b in enumerate(data["Locale"]):
        try:
            if "str" in str(type(b)):
                text = g_model(f"translate this text = {data['Default content'][i]} into = {b} language")
                print(text)
                data.loc[i, 'Translated content'] = text
        except:
            print("error")
            pass
    return data
