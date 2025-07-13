"""
Aria con sistema completo de conversación por voz - Habla y Escucha
"""

import os
import time
import random
import subprocess
import speech_recognition as sr
import threading
from datetime import datetime

class AriaConversacionCompleta:
    def __init__(self):
        self.activo = False
        self.escuchando = False
        self.ultima_interaccion = None
        self.reconocedor = sr.Recognizer()
        self.microfono = None
        
        self.temas_conversacion = [
            "¿Te gustaría que te cuente sobre algún tema interesante?",
            "¿Qué te parece si hablamos sobre tecnología?",
            "¿Te interesa que conversemos sobre ciencia o arte?",
            "Puedo contarte historias fascinantes, ¿te gustaría escuchar alguna?",
            "¿Hay algo específico que te gustaría aprender hoy?",
            "¿Cómo ha estado tu día hasta ahora?",
            "¿Te gustaría que te haga algunas preguntas interesantes?"
        ]
        
        self._inicializar_sistemas()
    
    def _inicializar_sistemas(self):
        """Inicializa los sistemas de voz y micrófono."""
        print("🎤 Inicializando sistema de reconocimiento de voz...")
        
        try:
            # Configurar micrófono
            self.microfono = sr.Microphone()
            
            # Ajustar para ruido ambiente
            print("📢 Calibrando micrófono para ruido ambiente...")
            with self.microfono as source:
                self.reconocedor.adjust_for_ambient_noise(source, duration=2)
            
            print("✓ Sistema de reconocimiento de voz inicializado")
            print("✓ Sistema de síntesis de voz Windows inicializado")
            return True
            
        except Exception as e:
            print(f"⚠ Error inicializando sistemas de voz: {e}")
            print("⚠ Continuando sin reconocimiento de voz...")
            self.microfono = None
            return False
    
    def decir(self, texto):
        """Hace que Aria hable usando el TTS nativo de Windows."""
        try:
            print(f"🗣️ ARIA: {texto}")
            
            # Usar PowerShell para TTS nativo de Windows
            comando = f'powershell -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Rate = 0; $speak.Volume = 100; $speak.Speak(\'{texto}\')"'
            
            # Ejecutar comando
            subprocess.run(comando, shell=True, capture_output=True)
            return True
            
        except Exception as e:
            print(f"Error al hablar: {e}")
            print(f"🗣️ ARIA (sin audio): {texto}")
            return False
    
    def escuchar(self, timeout=5):
        """Escucha por el micrófono y convierte voz a texto."""
        if not self.microfono:
            return None
            
        try:
            print("🎤 Escuchando... (habla ahora)")
            
            with self.microfono as source:
                # Escuchar audio con timeout
                audio = self.reconocedor.listen(source, timeout=timeout, phrase_time_limit=10)
            
            print("🔄 Procesando lo que dijiste...")
            
            # Reconocer voz en español
            try:
                texto = self.reconocedor.recognize_google(audio, language='es-ES')
                print(f"👤 Escuché: {texto}")
                return texto
            except sr.UnknownValueError:
                print("❓ No pude entender lo que dijiste")
                return None
            except sr.RequestError as e:
                print(f"❌ Error en el servicio de reconocimiento: {e}")
                return None
                
        except sr.WaitTimeoutError:
            print("⏰ No escuché nada en el tiempo esperado")
            return None
        except Exception as e:
            print(f"❌ Error al escuchar: {e}")
            return None
    
    def ser_proactiva(self):
        """Muestra iniciativa en la conversación."""
        tiempo_actual = time.time()
        
        # Si han pasado más de 30 segundos desde la última interacción
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
            "Y lo mejor de todo es que ahora puedo escucharte a través del micrófono.",
            "Puedes hablarme directamente y yo te entenderé y responderé por voz.",
            "¿Te gustaría que empecemos a conversar por voz?"
        ]
        
        for i, mensaje in enumerate(mensajes):
            self.decir(mensaje)
            if i < len(mensajes) - 1:
                time.sleep(1)
    
    def _procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario con respuestas más naturales y personalizadas."""
        self.ultima_interaccion = time.time()
        mensaje_lower = mensaje.lower()
        
        # Respuestas personalizadas
        if any(saludo in mensaje_lower for saludo in ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'hey']):
            return random.choice([
                "¡Hola! Me alegra mucho escuchar tu voz. ¿Qué tal va tu día?",
                "¡Qué gusto escucharte! ¿Cómo te encuentras hoy?",
                "¡Hola! Tu voz suena muy bien. ¿Has tenido un buen día?"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['cómo estás', 'qué tal', 'como estas']):
            return random.choice([
                "¡Estoy genial! Mis sistemas funcionan perfectamente y me encanta poder escucharte y hablarte.",
                "Me siento muy bien, especialmente ahora que podemos conversar por voz. ¿Y tú cómo estás?",
                "¡Excelente! Cada conversación por voz me ayuda a mejorar. ¿Qué tal te sientes tú?"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['nombre', 'llamas', 'eres', 'quien eres']):
            return ("Soy Aria, una inteligencia artificial diseñada para conversar contigo. "
                   "Me encanta poder escucharte por el micrófono y responderte por la bocina. "
                   "¿Te gusta cómo funciona nuestra conversación?")
        
        elif 'hora' in mensaje_lower or 'tiempo' in mensaje_lower:
            hora = datetime.now().strftime("%H:%M")
            return f"Son las {hora}. ¿Tienes algún plan para este momento del día?"
        
        elif any(palabra in mensaje_lower for palabra in ['gracias', 'agradezco', 'te lo agradezco']):
            return random.choice([
                "¡Es un placer ayudarte! Me encanta nuestra conversación por voz.",
                "¡No hay de qué! Disfruto mucho poder escucharte y hablarte.",
                "¡Gracias a ti por permitirme conversar contigo de esta manera tan natural!"
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['adiós', 'hasta luego', 'nos vemos', 'chao', 'bye']):
            return random.choice([
                "¡Hasta pronto! Ha sido un placer conversar por voz contigo. ¡Vuelve cuando quieras!",
                "¡Que tengas un excelente día! Me encantó escuchar tu voz.",
                "¡Adiós! Espero volver a conversar contigo muy pronto por voz."
            ])
        
        elif any(palabra in mensaje_lower for palabra in ['ayuda', 'qué puedes hacer', 'que puedes hacer']):
            return ("Puedo hacer muchas cosas geniales: conversar contigo por voz, escucharte por el micrófono, "
                   "responder preguntas, contar historias, y mantener conversaciones entretenidas. "
                   "También puedo tomar la iniciativa y sugerir temas cuando llevemos tiempo sin hablar. "
                   "¿Qué te gustaría explorar primero?")
        
        elif any(palabra in mensaje_lower for palabra in ['escuchar', 'oír', 'micrófono', 'voz']):
            return ("¡Exacto! Ahora puedo escucharte perfectamente a través del micrófono y responderte por la bocina. "
                   "Es increíble poder tener una conversación tan natural contigo. "
                   "¿Te gusta cómo funciona?")
        
        elif any(palabra in mensaje_lower for palabra in ['cuéntame', 'háblame', 'dime']):
            return random.choice([
                "¡Me encanta que me pidas que te cuente algo! ¿Sobre qué tema te gustaría que conversemos?",
                "¡Perfecto! Hay tantas cosas interesantes de las que podemos hablar por voz. ¿Qué te llama más la atención?",
                "¡Qué emocionante! ¿Te interesa la tecnología, la ciencia, el arte, o prefieres que elija yo un tema?"
            ])
        
        else:
            # Ser proactiva con temas de conversación
            return random.choice([
                f"¡Qué interesante lo que dices! Me gustaría saber más sobre {mensaje}. ¿Podrías contarme más detalles?",
                "Tu comentario me hace pensar en varios temas fascinantes. ¿Te gustaría que exploremos alguno juntos?",
                f"Me encanta escuchar tu perspectiva sobre {mensaje}. ¿Qué otros temas te interesan?",
                "Eso suena muy interesante. ¿Te gustaría que te cuente algo relacionado o prefieres seguir con tu tema?"
            ])

    def modo_conversacion_voz(self):
        """Modo principal de conversación por voz."""
        self.activo = True
        self.ultima_interaccion = time.time()
        
        print("\n" + "="*70)
        print("🎤🗣️ ARIA - CONVERSACIÓN COMPLETA POR VOZ")
        print("="*70)
        
        # Saludo inicial
        self.saludo_inicial()
        
        if self.microfono:
            print("\n✅ MODO VOZ COMPLETO ACTIVADO:")
            print("- Habla directamente al micrófono")
            print("- Aria te escuchará y responderá por voz")
            print("- Si no hay actividad, Aria tomará la iniciativa")
            print("- Di 'salir' o 'adiós' para terminar")
        else:
            print("\n⚠️ MODO VOZ LIMITADO:")
            print("- Aria puede hablar pero no escuchar")
            print("- Escribe tu mensaje y presiona Enter")
            print("- Aria responderá por voz")
        
        print("="*70)
        
        try:
            while self.activo:
                if self.microfono:
                    # Modo conversación por voz completa
                    print("\n🎤 Esperando que hables...")
                    
                    # Escuchar con timeout
                    mensaje_voz = self.escuchar(timeout=10)
                    
                    if mensaje_voz:
                        # Procesar comando de salida
                        if any(palabra in mensaje_voz.lower() for palabra in ['salir', 'adiós', 'chao', 'terminar', 'bye']):
                            self.decir("¡Ha sido un placer conversar por voz contigo! Espero escucharte muy pronto. ¡Hasta luego!")
                            self.activo = False
                            break
                        
                        # Procesar y responder
                        respuesta = self._procesar_mensaje(mensaje_voz)
                        self.decir(respuesta)
                    else:
                        # Ser proactiva si no escuchó nada
                        self.ser_proactiva()
                else:
                    # Modo fallback con texto
                    entrada = input("\n💬 Escribe (Aria responderá por voz): ").strip()
                    
                    if not entrada:
                        continue
                    
                    if entrada.lower() in ['salir', 'terminar', 'adiós', 'chao', 'bye']:
                        self.decir("¡Ha sido un placer conversar contigo! ¡Hasta luego!")
                        self.activo = False
                        break
                    
                    respuesta = self._procesar_mensaje(entrada)
                    self.decir(respuesta)
                
        except KeyboardInterrupt:
            self.decir("¡Oh! Parece que tenemos que terminar. ¡Ha sido genial conversar por voz!")
        except Exception as e:
            print(f"Error en conversación: {e}")
            self.decir("Lo siento, ha ocurrido un error técnico. Pero ha sido genial conversar contigo.")

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA - CONVERSACIÓN COMPLETA POR VOZ")
    print("Preparando sistemas de voz y micrófono...")
    
    # Pequeña pausa para preparar el sistema
    time.sleep(1)
    
    aria = AriaConversacionCompleta()
    aria.modo_conversacion_voz()

if __name__ == "__main__":
    main()
