import tkinter as tk
from tkinter import filedialog
import threading
import os
import sys
from faster_whisper import WhisperModel

# --- Configuración ---
MODEL_SIZE = "tiny"
COMPUTE_TYPE = "int8"

def obtener_ruta_base():
    """ Devuelve la ruta donde está el .exe o el script .py """
    if getattr(sys, 'frozen', False):
        # Si es un .exe (PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # Si es un script .py normal
        return os.path.dirname(os.path.abspath(__file__))

def iniciar_transcripcion():
    # 1. Abrir selector de archivos
    archivo = filedialog.askopenfilename(
        title="Selecciona el video o audio",
        filetypes=[("Archivos de media", "*.mp3 *.wav *.mp4 *.mkv *.m4a *.ogg *.flac"), ("Todos", "*.*")]
    )
    
    if not archivo:
        return 

    # Desactivar botón y cambiar texto
    btn_accion.config(state="disabled", text="Trabajando...")
    lbl_estado.config(text="Cargando modelo... (Esto tarda la primera vez)", fg="blue")
    
    # Hilo en segundo plano
    hilo = threading.Thread(target=procesar_audio, args=(archivo,))
    hilo.start()

def procesar_audio(archivo_origen):
    try:
        # --- LÓGICA DE CARPETAS ---
        ruta_base = obtener_ruta_base()
        carpeta_salida = os.path.join(ruta_base, "transcripciones")
        
        # Crear la carpeta si no existe
        os.makedirs(carpeta_salida, exist_ok=True)
    
        # Cargar modelo
        model = WhisperModel(MODEL_SIZE, device="cpu", compute_type=COMPUTE_TYPE)
        
        ventana.after(0, lambda: lbl_estado.config(text="Transcribiendo... (Paciencia)"))
        
        # Transcribir
        segments, info = model.transcribe(archivo_origen, beam_size=1)
        
        # Definir nombre del archivo de salida dentro de la carpeta
        nombre_base = os.path.basename(archivo_origen) # Ej: "video.mp4"
        ruta_final_txt = os.path.join(carpeta_salida, nombre_base + ".txt")
        
        # Guardar texto
        with open(ruta_final_txt, "w", encoding="utf-8") as f:
            for segment in segments:
                f.write(segment.text + " ")
        
        # Avisar éxito
        ventana.after(0, lambda: lbl_estado.config(text=f"¡LISTO!\nGuardado en carpeta 'transcripciones'", fg="green"))
        
        # Opcional: Abrir la carpeta automáticamente al terminar para facilitarle la vida
        os.startfile(carpeta_salida) 
        
    except Exception as e:
        ventana.after(0, lambda: lbl_estado.config(text=f"Error: {str(e)}", fg="red"))
    
    # Reactivar botón
    ventana.after(0, lambda: btn_accion.config(state="normal", text="Elegir otro archivo"))

# --- Interfaz Gráfica ---
ventana = tk.Tk()
ventana.title("Transcriptor")
ventana.geometry("400x350")
ventana.resizable(False, False)

frame = tk.Frame(ventana)
frame.pack(expand=True)

lbl_instruccion = tk.Label(frame, text="Transcriptor Automático", font=("Arial", 16, "bold"))
lbl_instruccion.pack(pady=10)

btn_accion = tk.Button(frame, text="Elegir Archivo", font=("Arial", 14), command=iniciar_transcripcion, height=2, width=20)
btn_accion.pack(pady=20)

lbl_estado = tk.Label(frame, text="Los textos se guardarán en la carpeta\n'transcripciones'", font=("Arial", 10), wraplength=350, justify="center", fg="gray")
lbl_estado.pack(pady=10)

lbl_firma = tk.Label(ventana, text="Transcriptor de archivos de audio y video", font=("Arial", 8), fg="gray")
lbl_firma.pack(side="bottom", pady=5)

ventana.mainloop()