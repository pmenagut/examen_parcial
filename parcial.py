import threading
import time
import random
import queue

# Cola segura para almacenar las imágenes
cola_imagenes = queue.Queue()

id_imagen = 1  # ID inicial de la imagen

# Función para simular la recepción impredecible y constante de imágenes
def recibir_imagenes():
    global id_imagen
    while True:
        cantidad = random.randint(0, 5)  # para simular que unas veces vienen muchas imagenes rapido y otras mas despacio
        for _ in range(cantidad):
            nombre_imagen = f"Imagen_{id_imagen}"
            print(f"[RECEPCIÓN] Llegó: {nombre_imagen}")
            cola_imagenes.put(nombre_imagen)
            id_imagen += 1
        time.sleep(random.uniform(0.1, 2.0))  # Simula intervalos irregulares entre oleadas

# Función para procesar imágenes de una en una
def procesar_imagenes():
    while True:
        nombre_imagen = cola_imagenes.get()  # Espera hasta que haya una imagen disponible
        print(f"- [PROCESANDO] {nombre_imagen}")
        time.sleep(random.uniform(1, 3))  # Simula tiempo de procesamiento complejo
        print(f"+ [COMPLETADO] {nombre_imagen}")
        cola_imagenes.task_done()

# hilos para recepción
hilo_recepcion = threading.Thread(target=recibir_imagenes, daemon=True)
hilo_recepcion.start()

# hilos para procesamiento
cantidad_analistas = 3  # Número de analistas (hilos) para procesar imágenes
for i in range(cantidad_analistas):
    hilo_procesamiento = threading.Thread(target=procesar_imagenes, daemon=True)
    hilo_procesamiento.start()

# Mantener el programa en ejecución hasta que se interrumpa
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt: # Permite detener el programa con Ctrl+C
    print("Programa terminado")
