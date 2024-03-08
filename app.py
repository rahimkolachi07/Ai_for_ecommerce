import pandas as pd
import os
import gradio as gr
from main import product_exp, translated
import time

def process_csv1(product):
    a=1
    while a==1:
        try:
            df1 = pd.read_csv(product.name)
            df1=product_exp(df1)
            df1.to_csv(product.name, index=False)
            a=0
            return product.name
        except:
            df1 = pd.read_csv(product.name)
            df1.to_csv(product.name, index=False)
            return product.name
        
def process_csv2(translate):
    a=1
    while a==1:
        try:

            df2 = pd.read_csv(translate.name)
            df2=translated(df2)
            df2.to_csv(translate.name, index=False)
            a=0
            return translate.name
        except:

            df2 = pd.read_csv(translate.name)
            df2.to_csv(translate.name, index=False)
            return translate.name

with gr.Blocks() as iface:
    gr.Markdown("AI tool")
    with gr.Row():
        inp = gr.File()
        out = gr.File()
    btn = gr.Button("Run")
    btn.click(fn=process_csv1, inputs=inp, outputs=out)
    with gr.Row():
        inp = gr.File()
        out = gr.File()
    btn1 = gr.Button("Run1")
    btn1.click(fn=process_csv2, inputs=inp, outputs=out)


# Enable the queue
iface.queue()

# Launch the Interface
iface.launch(share=True,inbrowser=True)
