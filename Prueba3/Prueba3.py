import threading
import time
import json
import logging
from queue import Queue

# Configuración del registro
logging.basicConfig(filename='procesamiento.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Parte 1: Multiprocesamiento ---
def imprimir_pares():
    for num in range(2, 201, 2):
        print(f"Par: {num}")
        time.sleep(0.5)

def imprimir_impares():
    for num in range(1, 200, 2):
        print(f"Impar: {num}")
        time.sleep(0.5)

# Creación de hilos para imprimir números pares e impares
hilo_par = threading.Thread(target=imprimir_pares)
hilo_impar = threading.Thread(target=imprimir_impares)

# Inicio de los hilos
hilo_par.start()
hilo_impar.start()

# --- Parte 2: Lectura y procesamiento del archivo JSON ---

# Función para procesar cada elemento del archivo JSON
def procesar_elemento(id_elemento, datos, nombre_dispositivo):
    logging.info(f"Procesando elemento ID: {id_elemento} del dispositivo {nombre_dispositivo}")

    # Convertir los datos de string a lista de enteros
    lista_datos = []
    for cadena in datos:
        numeros = list(map(int, cadena.split()))
        lista_datos.extend(numeros)

    # Imprimir y registrar el promedio antes de la normalización
    promedio_antes = sum(lista_datos) / len(lista_datos)
    logging.info(f"Promedio antes de la normalización para ID {id_elemento}: {promedio_antes:.2f}")

    # Normalización de los datos de 0 a 1
    valor_maximo = max(lista_datos)
    if valor_maximo != 0:
        datos_normalizados = [x / valor_maximo for x in lista_datos]
    else:
        datos_normalizados = lista_datos  # Evitar la división por cero

    # Imprimir y registrar el promedio después de la normalización
    promedio_despues = sum(datos_normalizados) / len(datos_normalizados)
    logging.info(f"Promedio después de la normalización para ID {id_elemento}: {promedio_despues:.2f}")

    # Imprimir y registrar el tamaño de los datos
    logging.info(f"Tamaño de los datos para ID {id_elemento}: {len(lista_datos)}")

def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, 'r') as file:
        datos_json = json.load(file)
        return datos_json

def worker(queue):
    while True:
        id_elemento, contenido = queue.get()
        if id_elemento is None:
            break
        procesar_elemento(id_elemento, contenido['data'], contenido['deviceName'])  # Usar los nombres correctos
        queue.task_done()

def main():
    ruta_archivo_json = './sample-03-01-json.json'
    datos_json = leer_archivo_json(ruta_archivo_json)

    # Crear una cola de trabajos
    queue = Queue()

    # Crear un pool de hilos
    max_hilos = 4
    hilos = []
    for _ in range(max_hilos):
        hilo = threading.Thread(target=worker, args=(queue,))
        hilo.start()
        hilos.append(hilo)

    # Agregar trabajos a la cola
    for id_elemento, contenido in datos_json.items():
        queue.put((id_elemento, contenido))

    # Esperar a que todos los trabajos terminen
    queue.join()

    # Detener los hilos trabajadores
    for _ in range(max_hilos):
        queue.put((None, None))
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    # Ejecución de la Parte 1
    hilo_par.join()
    hilo_impar.join()

    # Ejecución de la Parte 2
    main()
