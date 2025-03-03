import gradio as gr

def penjumlahan(first, second):
    return f"Hasil penjumlahan dari {first} dan {second} adalah {first + second}"

demo = gr.Interface(
    fn=penjumlahan,
    inputs=['number', 'number'],
    outputs='label'
)

demo.launch()