import pandas as pd
import gradio as gr
from transformers import pipeline

# Buat tabel data pegawai
data = {
    "Nama": ["Budi", "Siti", "Rina"],
    "Jabatan": ["Manager", "Staf", "Supervisor"],
    "Gaji": ["10 Juta", "7 Juta", "100000"]
}
df = pd.DataFrame(data)  # Mengubah dictionary menjadi tabel DataFrame

# Load model TAPAS
tqa = pipeline("table-question-answering", model="google/tapas-large-finetuned-wtq")

# Konversi tabel ke format yang dibutuhkan TAPAS
table = df.to_dict(orient="list")

# Fungsi untuk menampilkan tabel dan menjawab pertanyaan
def answer_question(question):
    result = tqa(table=table, query=question)
    return result["answer"], df  # Kembalikan jawaban + tabel untuk ditampilkan

# Buat antarmuka Gradio dengan tabel
iface = gr.Interface(
    fn=answer_question, 
    inputs=gr.Textbox(label="Masukkan pertanyaan tentang tabel"),
    outputs=[gr.Textbox(label="Jawaban"), gr.Dataframe(label="Tabel Pegawai")],  # Tambah tabel di UI
    title="Table Question Answering dengan TAPAS",
    description="Masukkan pertanyaan tentang tabel, dan model TAPAS akan memberikan jawabannya. Tabel juga ditampilkan di bawah."
)

# Jalankan aplikasi Gradio
iface.launch()