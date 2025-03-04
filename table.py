# Langkah 1: Impor Library yang Dibutuhkan

import pandas as pd  # pandas: Digunakan untuk membuat dan mengolah tabel (data dalam bentuk tabel).

from transformers import pipeline # pipeline dari transformers: Ini digunakan untuk memanggil model TAPAS (model AI dari Google) yang bisa menjawab pertanyaan berdasarkan tabel.


# Langkah 2: Buat Tabel Pegawai
# Membuat dictionary data, yang berisi:
# 	•	Kolom Nama: Budi, Siti, Rina
# 	•	Kolom Jabatan: Manager, Staf, Supervisor
# 	•	Kolom Gaji: 10 Juta, 7 Juta, 9 Juta
data = {
    "Nama": ["Budi", "Siti", "Rina"],
    "Jabatan": ["Manager", "Staf", "Supervisor"],
    "Gaji": ["10 Juta", "7 Juta", "9 Juta"]
}

df = pd.DataFrame(data) # Mengubah dictionary menjadi tabel (DataFrame) pakai pd.DataFrame(data).
print("Tabel Pegawai:") # Cetak tabel ke layar biar kita bisa lihat hasilnya.

print(df)

# Langkah 3: Load Model TAPAS (AI untuk Menjawab Pertanyaan dari Tabel)
tqa = pipeline("table-question-answering", model="google/tapas-large-finetuned-wtq")
# - pipeline("table-question-answering") → Ini memberitahu bahwa kita mau pakai model TAPAS yang bisa menjawab pertanyaan berdasarkan tabel.
# - model="google/tapas-large-finetuned-wtq" → Ini model yang sudah dilatih oleh Google untuk memahami tabel dan menjawab pertanyaan tentangnya.

# Konversi tabel ke format dictionary
	# •	Mengubah DataFrame ke dictionary dengan format list.
	# •	Supaya TAPAS bisa membaca tabel dalam bentuk yang lebih mudah dipahami AI.
table = df.to_dict(orient="list")

# Ajukan pertanyaan
question = "Siapa yang bekerja sebagai Manager?"
result = tqa(table=table, query=question)

# Tampilkan hasil
print("\nJawaban:", result["answer"])  # Output: Budi