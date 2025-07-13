"""
Aria con sistema de voz simplificado - Saludo inmediato por bocina
"""

import pyttsx3
import time
import threading
from datetime import datetime

class AriaVozSimple:
    """Versión simplificada de Aria enfocada en comunicación por voz."""
    
    def __init__(self):
        self.motor_tts = None
        self.activo = False
        self._inicializar_voz()
    
    def _inicializar_voz(self):
        """Inicializa el sistema de text-to-speech."""
        try:
            self.motor_tts = pyttsx3.init()
            
            # Configurar velocidad y volumen
            self.motor_tts.setProperty('rate', 150)
            self.motor_tts.setProperty('volume', 0.9)
            
            # Buscar voz en español
            voces = self.motor_tts.getProperty('voices')
            for voz in voces:
                if 'spanish' in voz.name.lower() or 'español' in voz.name.lower():
                    self.motor_tts.setProperty('voice', voz.id)
                    break
            
            print("✓ Sistema de voz inicializado correctamente")
            return True
            
        except Exception as e:
            print(f"⚠ Error inicializando sistema de voz: {e}")
            return False
    
    def decir(self, texto):
        """Hace que Aria hable por la bocina del dispositivo."""
        if self.motor_tts:
            try:
                print(f"🗣️ ARIA: {texto}")
                self.motor_tts.say(texto)
                self.motor_tts.runAndWait()
            except Exception as e:
                print(f"Error al hablar: {e}")
        else:
            print(f"🗣️ ARIA (sin audio): {texto}")
    
    def saludo_inicial(self):
        """Saludo inmediato al iniciar el sistema."""
        mensajes_saludo = [
            "¡Hola! Soy Aria, tu asistente de inteligencia artificial.",
            "Estoy aquí para ayudarte en todo lo que necesites.",
            "Mis sistemas están completamente operativos y puedo escucharte a través del micrófono y hablarte por la bocina.",
            "¿En qué puedo ayudarte hoy?"
        ]
        
        for mensaje in mensajes_saludo:
            self.decir(mensaje)
            time.sleep(0.5)  # Pequeña pausa entre frases
    
    def iniciar_conversacion(self):
        """Inicia el modo de conversación por voz."""
        self.activo = True
        
        # Saludo inmediato
        self.saludo_inicial()
        
        print("\n" + "="*60)
        print("🎤 ARIA - MODO VOZ ACTIVADO")
        print("="*60)
        print("- Aria te ha saludado por la bocina")
        print("- Escribe tu mensaje y presiona Enter")
        print("- Aria responderá por voz")
        print("- Escribe 'salir' para terminar")
        print("="*60)
        
        try:
            while self.activo:
                # Simular entrada de usuario
                entrada = input("\n💬 Tú: ").strip()
                
                if not entrada:
                    continue
                
                if entrada.lower() in ['salir', 'terminar', 'adiós']:
                    self.decir("¡Hasta luego! Ha sido un placer hablar contigo.")
                    self.activo = False
                    break
                
                # Procesar y responder
                respuesta = self._procesar_mensaje(entrada)
                self.decir(respuesta)
                
        except KeyboardInterrupt:
            self.decir("Interrumpido. ¡Hasta luego!")
        except Exception as e:
            print(f"Error en conversación: {e}")
            self.decir("Ha ocurrido un error. Cerrando sistema.")
    
    def _procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario y genera una respuesta."""
        mensaje_lower = mensaje.lower()
        
        # Respuestas básicas
        if any(saludo in mensaje_lower for saludo in ['hola', 'buenos días', 'buenas tardes']):
            return "¡Hola! Me alegra escucharte. ¿Cómo estás hoy?"
        
        elif any(pregunta in mensaje_lower for pregunta in ['cómo estás', 'qué tal']):
            return "Estoy muy bien, gracias por preguntar. Mis sistemas funcionan perfectamente."
        
        elif 'hora' in mensaje_lower:
            hora = datetime.now().strftime("%H:%M")
            return f"Son las {hora}."
        
        elif any(gracias in mensaje_lower for gracias in ['gracias', 'te lo agradezco']):
            return "¡De nada! Siempre es un placer ayudarte."
        
        elif 'ayuda' in mensaje_lower or 'qué puedes hacer' in mensaje_lower:
            return "Puedo conversar contigo, responder preguntas básicas, darte la hora, y mucho más. ¿Qué necesitas?"
        
        elif 'nombre' in mensaje_lower:
            return "Soy Aria, tu asistente de inteligencia artificial. ¿Y tú cómo te llamas?"
        
        else:
            return f"Interesante lo que dices sobre {mensaje}. Cuéntame más al respecto."

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA - SISTEMA DE VOZ")
    print("Preparando saludo por bocina...")
    
    # Crear e iniciar Aria
    aria = AriaVozSimple()
    
    # Pequeña pausa para asegurar que todo esté listo
    time.sleep(1)
    
    # Iniciar conversación con saludo inmediato
    aria.iniciar_conversacion()

if __name__ == "__main__":
    main()
