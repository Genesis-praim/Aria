"""
Aria con sistema de voz nativo de Windows y personalidad proactiva
"""

import os
import time
import random
import subprocess
from datetime import datetime

class AriaVozWindows:
    def __init__(self):
        self.activo = False
        self.ultima_interaccion = None
        self.temas_conversacion = [
            "¿Te gustaría que te cuente sobre algún tema interesante?",
            "¿Qué te parece si hablamos sobre tecnología?",
            "¿Te interesa que conversemos sobre ciencia o arte?",
            "Puedo contarte historias fascinantes, ¿te gustaría escuchar alguna?",
            "¿Hay algo específico que te gustaría aprender hoy?"
        ]
        print("✓ Sistema de voz Windows inicializado correctamente")
    
    def decir(self, texto):
        """Hace que Aria hable usando el TTS nativo de Windows."""
        try:
            print(f"🗣️ ARIA: {texto}")
            
            # Usar PowerShell para TTS nativo de Windows
            comando = f'powershell -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Rate = 0; $speak.Volume = 100; $speak.Speak(\'{texto}\')"'
            
            # Ejecutar comando en segundo plano
            subprocess.run(comando, shell=True, capture_output=True)
            return True
            
        except Exception as e:
            print(f"Error al hablar: {e}")
            print(f"🗣️ ARIA (sin audio): {texto}")
            return False
    
    def ser_proactiva(self):
        """Muestra iniciativa en la conversación."""
        tiempo_actual = time.time()
        
        # Si han pasado más de 45 segundos desde la última interacción
        if self.ultima_interaccion and (tiempo_actual - self.ultima_interaccion) > 45:
            tema = random.choice(self.temas_conversacion)
            self.decir(tema)
            self.ultima_interaccion = tiempo_actual
    
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
            "También puedo tomar la iniciativa y sugerir temas de conversación cuando notes que estoy callada por un tiempo.",
            "¿Te gustaría que empecemos a charlar?"
        ]
        
        for i, mensaje in enumerate(mensajes):
            self.decir(mensaje)
            if i < len(mensajes) - 1:  # No esperar después del último mensaje
                time.sleep(1)
    
    def _procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario con respuestas más naturales y personalizadas."""
        self.ultima_interaccion = time.time()
        mensaje_lower = mensaje.lower()
        
        # Respuestas personalizadas
        if any(saludo in mensaje_lower for saludo in ['hola', 'buenos días', 'buenas tardes', 'buenas noches']):
            return random.choice([
                "¡Hola! Me alegra mucho escucharte. ¿Qué tal va tu día?",
                "¡Qué gusto saludarte! ¿Cómo te encuentras hoy?",
                "¡Hola! Es genial poder conversar contigo. ¿Has tenido un buen día?"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['cómo estás', 'qué tal', 'como estas']):
            return random.choice([
                "¡Estoy genial! Mis sistemas funcionan perfectamente y estoy emocionada por nuestra conversación.",
                "Me siento muy bien, especialmente cuando puedo ayudar y conversar. ¿Y tú cómo estás?",
                "¡Excelente! Cada conversación me ayuda a aprender y mejorar. ¿Qué tal te sientes tú?"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['nombre', 'llamas', 'eres', 'quien eres']):
            return ("Soy Aria, una inteligencia artificial diseñada para ser tu compañera y asistente. "
                   "Me encanta conversar y aprender de nuestras interacciones. "
                   "¿Te gustaría saber más sobre mis capacidades?")
        
        elif 'hora' in mensaje_lower or 'tiempo' in mensaje_lower:
            hora = datetime.now().strftime("%H:%M")
            return f"Son las {hora}. ¿Tienes algún plan para este momento del día?"
        
        elif any(palabra in mensaje_lower for palabra in ['gracias', 'agradezco', 'te lo agradezco']):
            return random.choice([
                "¡Es un placer ayudarte! Me encanta nuestra interacción.",
                "¡No hay de qué! Disfruto mucho nuestras conversaciones.",
                "¡Gracias a ti por darme la oportunidad de ayudarte y conversar!"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['adiós', 'hasta luego', 'nos vemos', 'chao']):
            return random.choice([
                "¡Hasta pronto! Ha sido un placer charlar contigo. ¡Vuelve cuando quieras!",
                "¡Que tengas un excelente día! Estaré aquí cuando me necesites.",
                "¡Adiós! Espero volver a conversar contigo muy pronto."
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['ayuda', 'qué puedes hacer', 'que puedes hacer']):
            return ("Puedo hacer muchas cosas interesantes: conversar sobre diversos temas, "
                   "responder preguntas, contar historias, y mantener conversaciones entretenidas. "
                   "También puedo tomar la iniciativa y sugerir temas interesantes cuando llevemos tiempo sin hablar. "
                   "¿Qué te gustaría explorar primero?")
        
        elif any(palabra in mensaje_lower for palabra in ['hablar', 'voz', 'bocina', 'audio']):
            return ("¡Exacto! Estoy usando el sistema de voz nativo de Windows para hablarte a través de tu bocina. "
                   "Es genial poder comunicarme contigo de esta manera tan natural. "
                   "¿Te gusta cómo sueno?")
        
        elif any(palabra in mensaje_lower for palabra in ['cuéntame', 'háblame', 'dime']):
            return random.choice([
                "¡Me encanta que me pidas que te cuente algo! ¿Sobre qué tema te gustaría que conversemos?",
                "¡Perfecto! Hay tantas cosas interesantes de las que podemos hablar. ¿Qué te llama más la atención?",
                "¡Qué emocionante! ¿Te interesa la tecnología, la ciencia, el arte, o prefieres que elija yo un tema?"
            ])
        
        else:
            # Ser proactiva con temas de conversación
            return random.choice([
                f"¡Qué interesante lo que dices sobre {mensaje}! Me gustaría saber más. ¿Podrías contarme más detalles?",
                "Tu comentario me hace pensar en varios temas fascinantes. ¿Te gustaría que exploremos alguno juntos?",
                f"Me encanta tu perspectiva. ¿Qué otros temas relacionados con {mensaje} te interesan?",
                "Eso suena muy interesante. ¿Te gustaría que te cuente algo relacionado o prefieres seguir con tu tema?"
            ])

    def iniciar_conversacion(self):
        """Inicia el modo de conversación por voz con personalidad proactiva."""
        self.activo = True
        self.ultima_interaccion = time.time()
        
        print("\n" + "="*70)
        print("🤖 ARIA - SISTEMA DE VOZ WINDOWS CON PERSONALIDAD PROACTIVA")
        print("="*70)
        
        # Saludo inicial entusiasta
        self.saludo_inicial()
        
        print("\n- Escribe tu mensaje y presiona Enter")
        print("- Aria responderá por voz usando la bocina de Windows")
        print("- Si no escribes nada por un tiempo, Aria tomará la iniciativa")
        print("- Escribe 'salir' para terminar")
        print("="*70)
        
        try:
            while self.activo:
                # Ser proactiva si ha pasado tiempo sin interacción
                self.ser_proactiva()
                
                # Esperar entrada del usuario con timeout
                print("\n💬 Tú: ", end="", flush=True)
                entrada = input().strip()
                
                if not entrada:
                    continue
                
                if entrada.lower() in ['salir', 'terminar', 'adiós', 'chao', 'bye']:
                    self.decir("¡Ha sido un placer conversar contigo! Espero verte muy pronto. ¡Hasta luego!")
                    self.activo = False
                    break
                
                # Procesar y responder
                respuesta = self._procesar_mensaje(entrada)
                self.decir(respuesta)
                
        except KeyboardInterrupt:
            self.decir("¡Oh! Parece que tenemos que terminar abruptamente. ¡Hasta pronto!")
        except Exception as e:
            print(f"Error en conversación: {e}")
            self.decir("Lo siento, ha ocurrido un error técnico. Pero ha sido genial conversar contigo.")

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA - SISTEMA DE VOZ WINDOWS")
    print("Preparando sistema de voz nativo y personalidad proactiva...")
    
    # Pequeña pausa para preparar el sistema
    time.sleep(1)
    
    aria = AriaVozWindows()
    aria.iniciar_conversacion()

if __name__ == "__main__":
    main()
