import gradio as gr
import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe(audio_file):
    try:
        # Membaca file audio dari filepath yang diberikan
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)  # Merekam audio dari file
            text = recognizer.recognize_google(audio_data)  # Konversi ke teks
        
        return text  # Mengembalikan teks hasil transkripsi
    except Exception as e:
        return str(e)  # Jika terjadi error, tampilkan pesan error

# Pakai type="filepath" agar Gradio mengirimkan path file audio, bukan numpy array
demo = gr.Interface(fn=transcribe, inputs=gr.Audio(type="filepath"), outputs="text")

demo.launch()