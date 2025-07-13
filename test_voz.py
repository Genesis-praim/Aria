"""
Prueba simple del sistema de voz de Aria
"""

import pyttsx3
import time

def probar_voz():
    """Prueba básica del sistema TTS."""
    try:
        # Inicializar motor TTS
        motor = pyttsx3.init()
        
        # Configurar velocidad y volumen
        motor.setProperty('rate', 150)
        motor.setProperty('volume', 0.8)
        
        # Buscar voz en español
        voces = motor.getProperty('voices')
        print("Voces disponibles:")
        for i, voz in enumerate(voces):
            print(f"{i}: {voz.name} - {voz.languages}")
        
        # Intentar configurar voz en español
        voz_espanol = None
        for voz in voces:
            if 'spanish' in voz.name.lower() or 'español' in voz.name.lower():
                voz_espanol = voz.id
                break
        
        if voz_espanol:
            motor.setProperty('voice', voz_espanol)
            print(f"Usando voz en español: {voz_espanol}")
        else:
            print("Usando voz por defecto")
        
        # Mensaje de prueba
        mensaje = "¡Hola! Soy Aria, tu asistente de inteligencia artificial. Estoy aquí para ayudarte. ¿En qué puedo ayudarte hoy?"
        
        print(f"Diciendo: {mensaje}")
        motor.say(mensaje)
        motor.runAndWait()
        
        print("Prueba de voz completada exitosamente")
        return True
        
    except Exception as e:
        print(f"Error en prueba de voz: {e}")
        return False

if __name__ == "__main__":
    print("=== PRUEBA DEL SISTEMA DE VOZ DE ARIA ===")
    probar_voz()
