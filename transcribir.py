"""
🎯 transcribir.py
📌 Este script toma un archivo de audio (MP3 o WAV) en la carpeta principal,
lo transcribe a texto y guarda el resultado en la carpeta 'textos'.
"""

import whisper
import os

def transcribir_audio(archivo_audio: str, modelo: str = "small") -> str:
    """
    📌 Función que transcribe un archivo de audio usando Whisper.
    
    Parámetros:
    - archivo_audio (str): nombre del archivo MP3 o WAV
    - modelo (str): tiny, base, small, medium o large
    
    Retorna:
    - El texto transcrito.
    """
    print(f"⏳ Cargando modelo Whisper: {modelo}")
    model = whisper.load_model(modelo)

    print(f"🎧 Transcribiendo archivo: {archivo_audio}")
    resultado = model.transcribe(archivo_audio, language="es")

    return resultado["text"]

if __name__ == "__main__":
    # 1️⃣ Cambia aquí el nombre de tu archivosi
    archivo = "PresATaxiviris.mp3"   # 👈 Escribe el nombre EXACTO de tu archivo

    # 2️⃣ Verifica que el archivo exista
    if not os.path.exists(archivo):
        print(f"❌ No encuentro el archivo '{archivo}' en esta carpeta.")
        exit()

    # 3️⃣ Crea la carpeta 'textos' si no existe
    os.makedirs("textos", exist_ok=True)

    # 4️⃣ Transcribe el audio
    texto = transcribir_audio(archivo, modelo="small")

    # 5️⃣ Muestra el texto en pantalla
    print("\n📜 TRANSCRIPCIÓN COMPLETA:\n")
    print(texto)

    # 6️⃣ Guarda el texto en la carpeta 'textos'
    nombre_txt = os.path.splitext(archivo)[0] + ".txt"
    ruta_salida = os.path.join("textos", nombre_txt)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"\n✅ Transcripción guardada en: {ruta_salida}")
