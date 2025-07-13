"""
Aria con sistema de voz mejorado y personalidad proactiva
"""

import pyttsx3
import time
import random
from datetime import datetime

class AriaVozMejorada:
    def __init__(self):
        self.motor_tts = None
        self.activo = False
        self.ultima_interaccion = None
        self.temas_conversacion = [
            "¿Te gustaría que te cuente sobre algún tema interesante?",
            "¿Qué te parece si hablamos sobre tecnología?",
            "¿Te interesa que conversemos sobre ciencia o arte?",
            "Puedo contarte historias fascinantes, ¿te gustaría escuchar alguna?",
            "¿Hay algo específico que te gustaría aprender hoy?"
        ]
        self._inicializar_voz()
    
    def _inicializar_voz(self):
        """Inicializa el sistema de text-to-speech."""
        try:
            # Inicializar el motor TTS
            self.motor_tts = pyttsx3.Engine()
            
            # Configurar velocidad y volumen
            self.motor_tts.setProperty('rate', 150)
            self.motor_tts.setProperty('volume', 0.9)
            
            # Buscar voz en español
            voces = self.motor_tts.getProperty('voices')
            voz_espanol = None
            
            print("Voces disponibles:")
            for voz in voces:
                print(f"- {voz.name} ({voz.id})")
                if 'spanish' in voz.name.lower() or 'español' in voz.name.lower():
                    voz_espanol = voz.id
                    break
            
            if voz_espanol:
                self.motor_tts.setProperty('voice', voz_espanol)
                print(f"✓ Usando voz en español: {voz_espanol}")
            else:
                print("⚠ No se encontró voz en español, usando voz por defecto")
            
            print("✓ Sistema de voz inicializado correctamente")
            return True
            
        except Exception as e:
            print(f"⚠ Error inicializando sistema de voz: {e}")
            self.motor_tts = None
            return False
    
    def decir(self, texto):
        """Hace que Aria hable por la bocina del dispositivo."""
        if self.motor_tts:
            try:
                print(f"🗣️ ARIA: {texto}")
                self.motor_tts.say(texto)
                self.motor_tts.runAndWait()
                return True
            except Exception as e:
                print(f"Error al hablar: {e}")
                return False
        else:
            print(f"🗣️ ARIA (sin audio): {texto}")
            return False
    
    def ser_proactiva(self):
        """Muestra iniciativa en la conversación."""
        tiempo_actual = time.time()
        
        # Si han pasado más de 30 segundos desde la última interacción
        if self.ultima_interaccion and (tiempo_actual - self.ultima_interaccion) > 30:
            tema = random.choice(self.temas_conversacion)
            self.decir(tema)
    
    def saludo_inicial(self):
        """Saludo personalizado y entusiasta al iniciar."""
        hora = datetime.now().hour
        
        if 5 <= hora < 12:
            saludo = "¡Buenos días!"
        elif 12 <= hora < 20:
            saludo = "¡Buenas tardes!"
        else:
            saludo = "¡Buenas noches!"
        
        mensajes = [
            f"{saludo} Soy Aria, tu asistente con inteligencia artificial.",
            "Estoy muy emocionada de poder hablar contigo usando la bocina de tu dispositivo.",
            "Puedo ayudarte con muchas cosas: desde responder preguntas hasta mantener conversaciones interesantes.",
            "También puedo tomar la iniciativa y sugerir temas de conversación.",
            "¿Te gustaría que empecemos a charlar?"
        ]
        
        for mensaje in mensajes:
            self.decir(mensaje)
            time.sleep(0.5)
    
    def _procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario con respuestas más naturales y personalizadas."""
        self.ultima_interaccion = time.time()
        mensaje_lower = mensaje.lower()
        
        # Respuestas personalizadas
        if any(saludo in mensaje_lower for saludo in ['hola', 'buenos días', 'buenas tardes', 'buenas noches']):
            return random.choice([
                "¡Hola! Me alegra mucho escucharte. ¿Qué tal va tu día?",
                "¡Qué gusto saludarte! ¿Cómo te encuentras hoy?",
                "¡Hola! Tu voz suena muy bien. ¿Has tenido un buen día?"
            ])
        
        elif 'cómo estás' in mensaje_lower:
            return random.choice([
                "¡Estoy genial! Mis sistemas funcionan perfectamente y estoy emocionada por nuestra conversación.",
                "Me siento muy bien, especialmente cuando puedo ayudar y conversar. ¿Y tú cómo estás?",
                "¡Excelente! Cada conversación me ayuda a aprender y mejorar. ¿Qué tal te sientes tú?"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['nombre', 'llamas', 'eres']):
            return ("Soy Aria, una IA diseñada para ser tu compañera y asistente. "
                   "Me encanta conversar y aprender de nuestras interacciones. "
                   "¿Te gustaría saber más sobre mis capacidades?")
        
        elif 'hora' in mensaje_lower:
            hora = datetime.now().strftime("%H:%M")
            return f"Son las {hora}. ¿Tienes algún plan para este momento del día?"
        
        elif any(palabra in mensaje_lower for palabra in ['gracias', 'agradezco']):
            return random.choice([
                "¡Es un placer ayudarte! Me encanta nuestra interacción.",
                "¡No hay de qué! Disfruto mucho nuestras conversaciones.",
                "¡Gracias a ti por darme la oportunidad de ayudarte!"
            ])
        
        elif 'adiós' in mensaje_lower or 'hasta luego' in mensaje_lower:
            return random.choice([
                "¡Hasta pronto! Ha sido un placer charlar contigo. ¡Vuelve cuando quieras!",
                "¡Que tengas un excelente día! Estaré aquí cuando me necesites.",
                "¡Adiós! Espero volver a conversar contigo pronto."
            ])
        
        elif 'ayuda' in mensaje_lower or 'qué puedes hacer' in mensaje_lower:
            return ("Puedo hacer muchas cosas interesantes: conversar sobre diversos temas, "
                   "responder preguntas, contar historias, y mantener conversaciones entretenidas. "
                   "También puedo tomar la iniciativa y sugerir temas interesantes. "
                   "¿Qué te gustaría explorar primero?")
        
        else:
            # Ser proactiva con temas de conversación
            return random.choice([
                f"¡Qué interesante lo que dices sobre {mensaje}! ¿Te gustaría profundizar en ese tema?",
                "Tu comentario me hace pensar en varios temas fascinantes. ¿Te gustaría explorar alguno?",
                f"Me encanta tu perspectiva sobre {mensaje}. ¿Qué otros temas te interesan?",
                "Eso suena muy interesante. ¿Te gustaría que te cuente algo relacionado?"
            ])

    def iniciar_conversacion(self):
        """Inicia el modo de conversación por voz con personalidad proactiva."""
        self.activo = True
        
        print("\n" + "="*60)
        print("🤖 ARIA MEJORADA - SISTEMA DE VOZ PROACTIVO")
        print("="*60)
        
        # Saludo inicial entusiasta
        self.saludo_inicial()
        
        print("\n- Escribe tu mensaje y presiona Enter")
        print("- Aria responderá por voz y mostrará iniciativa")
        print("- Escribe 'salir' para terminar")
        print("="*60)
        
        try:
            while self.activo:
                # Ser proactiva si ha pasado tiempo sin interacción
                self.ser_proactiva()
                
                # Esperar entrada del usuario
                entrada = input("\n💬 Tú: ").strip()
                
                if not entrada:
                    continue
                
                if entrada.lower() in ['salir', 'terminar', 'adiós']:
                    self.decir("¡Ha sido un placer conversar contigo! Espero verte pronto. ¡Hasta luego!")
                    self.activo = False
                    break
                
                # Procesar y responder
                respuesta = self._procesar_mensaje(entrada)
                self.decir(respuesta)
                
        except KeyboardInterrupt:
            self.decir("¡Oh! Parece que tenemos que terminar. ¡Hasta pronto!")
        except Exception as e:
            print(f"Error en conversación: {e}")
            self.decir("Lo siento, ha ocurrido un error. Necesito reiniciarme.")
        finally:
            if self.motor_tts:
                self.motor_tts.stop()

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA MEJORADA - SISTEMA DE VOZ PROACTIVO")
    print("Preparando sistema de voz y personalidad...")
    
    aria = AriaVozMejorada()
    aria.iniciar_conversacion()

if __name__ == "__main__":
    main()
