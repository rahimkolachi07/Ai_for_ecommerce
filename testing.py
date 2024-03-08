import gradio as gr
def update(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("AI tool")
    with gr.Row():
        inp = gr.File()
        out = gr.File()
    btn = gr.Button("Run")
    btn.click(fn=update, inputs=inp, outputs=out)
    with gr.Row():
        inp = gr.File()
        out = gr.File()
    btn1 = gr.Button("Run1")
    btn1.click(fn=update, inputs=inp, outputs=out)


demo.launch()