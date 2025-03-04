# Langkah 1: Impor Library yang Dibutuhkan
import pandas as pd
import gradio as gr
from transformers import pipeline

# Langkah 2: Buat Tabel Pegawai
data = {
    "Nama": ["Budi", "Siti", "Rina"],
    "Jabatan": ["Manager", "Staf", "Supervisor"],
    "Gaji": ["10 Juta", "7 Juta", "9 Juta"]
}
df = pd.DataFrame(data)  # Mengubah dictionary menjadi tabel DataFrame

# Langkah 3: Load Model TAPAS
tqa = pipeline("table-question-answering", model="google/tapas-large-finetuned-wtq")

# Konversi tabel ke format dictionary agar bisa dibaca oleh TAPAS
table = df.to_dict(orient="list")

# Langkah 4: Buat Fungsi untuk Menjawab Pertanyaan
def answer_question(question):
    
    result = tqa(table=table, query=question)
    return result["answer"]

# Langkah 5: Buat Antarmuka Gradio
iface = gr.Interface(
    fn=answer_question, 
    inputs=gr.Textbox(label="Masukkan pertanyaan tentang tabel"),
    outputs=gr.Textbox(label="Jawaban"),
    title="Table Question Answering dengan TAPAS",
    description="Masukkan pertanyaan tentang tabel, dan model TAPAS akan memberikan jawabannya."
)

# Jalankan Aplikasi Gradio
iface.launch()