import time

def tiempo_actual():
    """Devuelve el tiempo actual en segundos desde la época (Epoch)."""
    return time.time()

def dormir(segundos):
    """Pausa la ejecución durante el número de segundos indicado."""
    time.sleep(segundos)
