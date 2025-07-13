"""
Aria usando la API nativa de Windows Speech Recognition
"""

import win32com.client
import pythoncom
import time
import random
from datetime import datetime

class AriaVozWin32:
    def __init__(self):
        self.activo = False
        self.ultima_interaccion = None
        self.speaker = None
        self.recognizer = None
        
        self.temas_conversacion = [
            "¿Te gustaría que te cuente sobre algún tema interesante?",
            "¿Qué te parece si hablamos sobre tecnología?",
            "¿Te interesa que conversemos sobre ciencia o arte?",
            "Puedo contarte historias fascinantes, ¿te gustaría escuchar alguna?",
            "¿Hay algo específico que te gustaría aprender hoy?"
        ]
        
        self._inicializar_voz()
    
    def _inicializar_voz(self):
        """Inicializa los sistemas de voz de Windows."""
        try:
            # Inicializar SAPI para hablar
            self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
            
            # Buscar voces en español
            voices = self.speaker.GetVoices()
            for voice in voices:
                if "spanish" in voice.GetDescription().lower():
                    self.speaker.Voice = voice
                    break
            
            # Configurar velocidad y volumen
            self.speaker.Rate = 0  # -10 a 10
            self.speaker.Volume = 100  # 0 a 100
            
            print("✓ Sistema de voz Windows inicializado")
            return True
            
        except Exception as e:
            print(f"⚠ Error inicializando sistema de voz: {e}")
            self.speaker = None
            return False
    
    def decir(self, texto):
        """Hace que Aria hable usando SAPI."""
        if self.speaker:
            try:
                print(f"🗣️ ARIA: {texto}")
                self.speaker.Speak(texto)
                return True
            except Exception as e:
                print(f"Error al hablar: {e}")
                print(f"🗣️ ARIA (sin audio): {texto}")
                return False
        else:
            print(f"🗣️ ARIA (sin audio): {texto}")
            return False
    
    def escuchar(self):
        """Escucha usando el reconocimiento de voz de Windows."""
        try:
            # Crear reconocedor
            engine = win32com.client.Dispatch("SAPI.SpInprocRecognizer")
            context = engine.CreateRecoContext()
            
            # Configurar gramática para dictado
            grammar = context.CreateGrammar()
            grammar.DictationSetState(1)
            
            print("🎤 Escuchando... (habla ahora)")
            
            # Esperar audio
            time.sleep(0.1)  # Pequeña pausa para inicializar
            
            # Obtener resultado
            result = context.WaitForRecognition(10000)  # 10 segundos timeout
            if result:
                texto = result.PhraseInfo.GetText()
                print(f"👤 Escuché: {texto}")
                return texto
            else:
                print("⏰ No escuché nada claro")
                return None
                
        except Exception as e:
            print(f"❌ Error al escuchar: {e}")
            return None
    
    def ser_proactiva(self):
        """Muestra iniciativa en la conversación."""
        tiempo_actual = time.time()
        
        if self.ultima_interaccion and (tiempo_actual - self.ultima_interaccion) > 30:
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
            "Y lo mejor es que ahora puedo escucharte a través del micrófono.",
            "Puedes hablarme directamente y yo te entenderé y responderé por voz.",
            "¿Te gustaría que empecemos a conversar?"
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
        """Inicia el modo de conversación por voz."""
        self.activo = True
        
        print("\n" + "="*60)
        print("🤖 ARIA - SISTEMA DE VOZ WINDOWS")
        print("="*60)
        
        # Saludo inicial entusiasta
        self.saludo_inicial()
        
        print("\n- Habla directamente al micrófono")
        print("- Aria te escuchará y responderá por voz")
        print("- Si no hablas, Aria tomará la iniciativa")
        print("- Di 'salir' o 'adiós' para terminar")
        print("="*60)
        
        try:
            while self.activo:
                # Ser proactiva si ha pasado tiempo sin interacción
                self.ser_proactiva()
                
                # Escuchar entrada de voz
                mensaje_voz = self.escuchar()
                
                if mensaje_voz:
                    if mensaje_voz.lower() in ['salir', 'terminar', 'adiós']:
                        self.decir("¡Ha sido un placer conversar contigo! Espero verte pronto. ¡Hasta luego!")
                        self.activo = False
                        break
                    
                    # Procesar y responder
                    respuesta = self._procesar_mensaje(mensaje_voz)
                    self.decir(respuesta)
                
        except KeyboardInterrupt:
            self.decir("¡Oh! Parece que tenemos que terminar. ¡Hasta pronto!")
        except Exception as e:
            print(f"Error en conversación: {e}")
            self.decir("Lo siento, ha ocurrido un error. Necesito reiniciarme.")

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA - SISTEMA DE VOZ WINDOWS")
    print("Preparando sistema de voz y reconocimiento...")
    
    # Inicializar COM para el hilo principal
    pythoncom.CoInitialize()
    
    try:
        aria = AriaVozWin32()
        aria.iniciar_conversacion()
    finally:
        # Limpiar COM
        pythoncom.CoUninitialize()

if __name__ == "__main__":
    main()
