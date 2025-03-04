import pandas as pd
from transformers import pipeline

data = {
    "Nama": ["Geo", "Faiz", "Deby"],
    "Jurusan": ["Sastra Mesin", "Akuntasi", "Teknik Informatika"],
    "Nilai": ["A", "B", "C"]
}

df = pd.DataFrame(data)
print("Tabel Nilai Mahasiswa:")
print(df)

tqa = pipeline("table-question-answering", model="google/tapas-large-finetuned-wtq")

table = df.to_dict(orient="list")

question = "Siapa yang memiliki nilai C?"
result = tqa(table=table, query=question)

print("\nJawaban:", result["answer"])