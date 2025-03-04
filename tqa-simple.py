from transformers import pipeline

# Load model TQA
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Teks sebagai sumber informasi
document = "Python adalah bahasa pemrograman yang banyak digunakan untuk pengembangan web, analisis data, dan kecerdasan buatan."

# Pertanyaan pengguna
question = "python bisa buat apa?"

# Mendapatkan jawaban
result = qa_pipeline(question=question, context=document)
print("Jawaban:", result["answer"])