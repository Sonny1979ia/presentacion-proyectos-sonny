"""
🎯 transcribir_all.py
📌 Este script:
   ✅ Busca todos los archivos MP3 y WAV en la carpeta 'audios'
   ✅ Transcribe cada uno con Whisper
   ✅ Guarda la transcripción en la carpeta 'textos' con el mismo nombre del audio + .txt
   este es una modificacion el dia 8 de agosto de 2025 a las  7:45 pm
"""

import whisper
import os

def transcribir_audio(modelo, archivo_audio: str) -> str:
    """
    📌 Función para transcribir un archivo de audio con Whisper.

    Parámetros:
    - modelo: modelo Whisper ya cargado
    - archivo_audio (str): nombre del archivo MP3 o WAV

    Retorna:
    - El texto transcrito como string
    """
    print(f"🎧 Transcribiendo archivo: {archivo_audio}")
    resultado = modelo.transcribe(archivo_audio, language="es")
    return resultado["text"]

if __name__ == "__main__":
    # 📂 1️⃣ Definir carpetas de trabajo
    carpeta_audios = "audios"   # donde estarán los MP3/WAV
    carpeta_textos = "textos"   # donde guardaremos los .txt

    # ✅ 2️⃣ Crear la carpeta 'textos' si no existe
    os.makedirs(carpeta_textos, exist_ok=True)

    # 🔍 3️⃣ Verificar si existe la carpeta 'audios'
    if not os.path.exists(carpeta_audios):
        print(f"❌ No encontré la carpeta '{carpeta_audios}'. Créala y coloca ahí tus audios.")
        exit()

    # 📥 4️⃣ Buscar archivos de audio en la carpeta 'audios'
    audios = [f for f in os.listdir(carpeta_audios) if f.lower().endswith((".mp3", ".wav"))]

    if not audios:
        print(f"❌ No encontré archivos MP3 ni WAV en la carpeta '{carpeta_audios}'.")
        exit()

    print(f"🔍 Encontrados {len(audios)} archivo(s) de audio para transcribir.")

    # ⚙️ 5️⃣ Cargar el modelo Whisper (una sola vez para optimizar)
    modelo_nombre = "small"  # puedes cambiar a tiny, base, medium, large
    print(f"⏳ Cargando modelo Whisper '{modelo_nombre}'...")
    modelo = whisper.load_model(modelo_nombre)

    # 🚀 6️⃣ Procesar cada audio
    for archivo in audios:
        ruta_audio = os.path.join(carpeta_audios, archivo)
        print(f"\n▶️ Procesando: {archivo}")

        # 📝 Transcribir
        texto = transcribir_audio(modelo, ruta_audio)

        # 💾 Guardar transcripción con el mismo nombre en 'textos'
        nombre_txt = os.path.splitext(archivo)[0] + ".txt"
        ruta_salida = os.path.join(carpeta_textos, nombre_txt)

        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"✅ Transcripción guardada: {ruta_salida}")

    print("\n🎉 ¡Proceso completado! Todos los audios fueron transcritos.")
