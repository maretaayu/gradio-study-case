import gradio as gr

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("### Masukkan Nama Anda")  # Heading
    name_input = gr.Textbox(label="Nama")  # Input teks
    submit_btn = gr.Button("Submit")  # Tombol
    output_text = gr.Textbox(label="Hasil")  # Output teks

    submit_btn.click(fn=greet, inputs=name_input, outputs=output_text)  # Event tombol

demo.launch()