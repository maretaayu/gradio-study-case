import gradio as gr

# Data harga mata kuliah
harga_matkul = {
    "Matematika": 500000,
    "Fisika": 450000,
    "Kimia": 400000,
}

# Fungsi hitung total dengan `map()`
def hitung_total(pilihan):
    if not pilihan:
        return "Silakan pilih minimal 1 mata kuliah."
    
    total = sum(map(harga_matkul.get, pilihan))  # Menggunakan map() untuk mengambil harga dan menjumlahkan
    return f"Total biaya: Rp {total:,}"

# UI Gradio
demo=gr.Interface(
    fn=hitung_total,
    inputs=gr.CheckboxGroup(list(harga_matkul), label="Pilih Mata Kuliah"),  # Langsung list dictionary keys
    outputs="text"
)

demo.launch()