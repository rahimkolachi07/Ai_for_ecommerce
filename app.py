import pandas as pd
import os
import gradio as gr
from main import product_exp, translated
import time

def process_csv(product, translate):
    df1 = pd.read_csv(product.name)
    df1=product_exp(df1)
    time.sleep(2)
    df2 = pd.read_csv(translate.name)
    df2=translated(df2)
    # Save the dataframes as CSV files with the same names as the input files
    df1.to_csv(product.name, index=False)
    df2.to_csv(translate.name, index=False)
    
    # Return the paths of the CSV files
    return product.name, translate.name

iface = gr.Interface(
    fn=process_csv, 
    inputs=["file", "file"], 
    outputs=["file", "file"],
    theme=gr.themes.Glass(primary_hue="blue", secondary_hue="blue", neutral_hue="blue")
)

# Enable the queue
iface.queue()

# Launch the Interface
iface.launch(share=True,inbrowser=True)
