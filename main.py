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
                    print("zz")
                    z=0
                else:
                    z=0
            except:
                print("zzz")
                z=1
            print("zzaa")
        print("zza")
    print("zzac")
    return data
            

def translated(data):
    # Ensure the 'Translated content' column is of type object
    data['Translated content'] = data['Translated content'].astype(object)
    
    for i, b in enumerate(data["Locale"]):
        z=1
        while z==1:
            try:
                if "str" in str(type(b)):
                    if b=="de":
                        lang=" Germany"
                        print(lang)
                    if b=="en":
                        lang=" english"
                        print(lang)
                    if b=="es":
                        lang=" Spanish"
                        print(lang)
                    if b=="fr":
                        lang=" French"
                        print(lang)

                    text = g_model(f"must translate this text =[ {data['Default content'][i]}] into {lang} language. ")
                    print(text)
                    print("zz")
                    data.loc[i, 'Translated content'] = text
                    print("z")
                    z=0
                else:
                    z=0
            except:
                z=1
                print("error")
                pass
        print("z")
    print("z")
    return data
