import gradio as gr

def count_characters(text):
    """Menghitung jumlah karakter dalam teks yang dimasukkan pengguna."""
    return f"Jumlah karakter: {len(text)}"

# Membuat interface dengan input teks dan output teks
demo = gr.Interface(
    fn=count_characters, 
    inputs= gr.Textbox(label="Masukkan teks"),
    outputs="text", 
    title="Penghitung Karakter",
    description="Masukkan teks dan lihat jumlah karakternya!"
)

# Menjalankan aplikasi
demo.launch()