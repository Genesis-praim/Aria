import threading
import queue
import time

# Importar main para iniciar el sistema
import main

# Cola para preguntas y respuestas
preguntas_queue = queue.Queue()
respuestas_queue = queue.Queue()

def buscar_en_web(pregunta):
    # Función simulada para buscar en la web
    # Aquí se puede integrar un motor de búsqueda real o API
    # Por ahora, devuelve None para simular que no encontró respuesta
    return None

def generar_respuesta(pregunta):
    # Intentar buscar respuesta en la web
    respuesta = buscar_en_web(pregunta)
    if respuesta:
        return respuesta
    else:
        # Si no hay respuesta, crear una respuesta generada
        return f"No encontré información en la web para: '{pregunta}'. Pero puedo ayudarte a crearla."

def hilo_preguntas():
    while True:
        pregunta = preguntas_queue.get()
        if pregunta == "salir":
            respuestas_queue.put("Saliendo del sistema.")
            break
        respuesta = generar_respuesta(pregunta)
        respuestas_queue.put(respuesta)

def interfaz_usuario():
    print("Iniciando sistema Aria. Escribe tus preguntas o 'salir' para terminar.")
    hilo = threading.Thread(target=hilo_preguntas)
    hilo.start()

    while True:
        pregunta = input("Pregunta: ")
        preguntas_queue.put(pregunta)
        if pregunta == "salir":
            break
        respuesta = respuestas_queue.get()
        print(f"Aria: {respuesta}")

    hilo.join()
    print("Sistema detenido.")

if __name__ == "__main__":
    # Iniciar el sistema principal
    main.main()
    # Iniciar la interfaz de usuario para preguntas y respuestas
    interfaz_usuario()
