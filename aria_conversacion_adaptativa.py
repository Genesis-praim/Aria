"""
AriaConversacionAdaptativa - Sistema de conversación con adaptación al usuario
Integra el sistema de bodega y adaptación para una experiencia personalizada
"""

import os
import time
import random
import logging
import speech_recognition as sr
from datetime import datetime
from typing import Dict, Any, Optional, List
from pathlib import Path

from bodega.BodegaConocimiento import BodegaConocimiento, TipoInformacion, ImportanciaInfo
from adaptacion_usuario.AdaptacionUsuario import AdaptacionUsuario
from personalidad.personalidad.PersonalidadCentral import PersonalidadCentral, EstadoEmocional

class AriaConversacionAdaptativa:
    """Sistema de conversación adaptativo de Aria."""
    
    def __init__(self):
        # Configurar logging
        self.logger = logging.getLogger("AriaConversacionAdaptativa")
        self.logger.setLevel(logging.INFO)
        
        # Componentes principales
        self.bodega = BodegaConocimiento()
        self.adaptacion = AdaptacionUsuario(self.bodega)
        self.personalidad = PersonalidadCentral()
        
        # Estado del sistema
        self.activo = False
        self.escuchando = False
        self.ultima_interaccion = None
        self.contexto_actual = {
            "tema_actual": None,
            "emociones_detectadas": [],
            "nivel_engagement": 0.0,
            "tiempo_sin_respuesta": 0
        }
        
        # Sistema de voz
        self.reconocedor = sr.Recognizer()
        self.microfono = None
        
        # Temas de conversación dinámicos
        self.temas_base = [
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
        """Inicializa todos los sistemas necesarios."""
        self.logger.info("Iniciando sistemas de Aria Conversación Adaptativa...")
        
        try:
            # Configurar micrófono
            self.microfono = sr.Microphone()
            with self.microfono as source:
                self.reconocedor.adjust_for_ambient_noise(source, duration=2)
            self.logger.info("✓ Sistema de reconocimiento de voz inicializado")
            
        except Exception as e:
            self.logger.error(f"⚠ Error inicializando sistemas de voz: {e}")
            self.microfono = None
        
        self.logger.info("✓ Sistemas inicializados correctamente")

    def decir(self, texto: str, usuario_id: str = "default"):
        """
        Hace que Aria hable, adaptando el estilo según el perfil del usuario.
        """
        try:
            # Obtener adaptaciones para el usuario
            perfil = self.adaptacion.obtener_perfil(usuario_id)
            if perfil:
                estilo = perfil["estilo_comunicacion"]
                texto = self._adaptar_texto(texto, estilo)
            
            print(f"🗣️ ARIA: {texto}")
            
            # Usar PowerShell para TTS nativo de Windows
            comando = f'powershell -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Rate = 0; $speak.Volume = 100; $speak.Speak(\'{texto}\')"'
            
            os.system(comando)
            
            # Registrar interacción en la bodega
            self._registrar_respuesta(texto, usuario_id)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error al hablar: {e}")
            print(f"🗣️ ARIA (sin audio): {texto}")
            return False

    def _adaptar_texto(self, texto: str, estilo: Dict[str, float]) -> str:
        """Adapta el texto según el estilo de comunicación del usuario."""
        texto_adaptado = texto
        
        # Ajustar formalidad
        if estilo["formalidad"] > 0.7:
            # Más formal
            texto_adaptado = texto_adaptado.replace("tu", "usted")
            texto_adaptado = texto_adaptado.replace("te", "le")
            if not any(palabra in texto_adaptado.lower() for palabra in ["por favor", "gracias"]):
                texto_adaptado = f"Por favor, {texto_adaptado}"
        elif estilo["formalidad"] < 0.3:
            # Más informal
            texto_adaptado = texto_adaptado.replace("usted", "tu")
            texto_adaptado = texto_adaptado.replace("le", "te")
        
        # Ajustar verbosidad
        if estilo["verbosidad"] < 0.3:
            # Más conciso
            texto_adaptado = texto_adaptado.split('.')[0] + '.'
        elif estilo["verbosidad"] > 0.7:
            # Más detallado
            if not texto_adaptado.endswith('?'):
                texto_adaptado += " ¿Te gustaría saber más al respecto?"
        
        # Ajustar emocionalidad
        if estilo["emocionalidad"] > 0.7:
            # Más emocional
            texto_adaptado = f"¡{texto_adaptado}!"
            if "!" not in texto_adaptado:
                texto_adaptado = texto_adaptado.replace(".", "!")
        
        return texto_adaptado

    def escuchar(self, timeout=5, usuario_id: str = "default") -> Optional[str]:
        """Escucha por el micrófono y procesa la entrada del usuario."""
        if not self.microfono:
            return None
            
        try:
            print("🎤 Escuchando... (habla ahora)")
            
            with self.microfono as source:
                audio = self.reconocedor.listen(source, timeout=timeout, phrase_time_limit=10)
            
            print("🔄 Procesando lo que dijiste...")
            
            texto = self.reconocedor.recognize_google(audio, language='es-ES')
            print(f"👤 Escuché: {texto}")
            
            # Registrar entrada en la bodega
            self._registrar_entrada(texto, usuario_id)
            
            return texto
            
        except sr.UnknownValueError:
            print("❓ No pude entender lo que dijiste")
            return None
        except sr.RequestError as e:
            print(f"❌ Error en el servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            print(f"❌ Error al escuchar: {e}")
            return None

    def ser_proactiva(self, usuario_id: str = "default"):
        """Muestra iniciativa en la conversación de manera adaptativa."""
        tiempo_actual = time.time()
        perfil = self.adaptacion.obtener_perfil(usuario_id)
        
        if not perfil:
            # Comportamiento por defecto si no hay perfil
            if self.ultima_interaccion and (tiempo_actual - self.ultima_interaccion) > 30:
                tema = random.choice(self.temas_base)
                self.decir(tema, usuario_id)
                self.ultima_interaccion = tiempo_actual
            return
        
        # Adaptar proactividad según el perfil
        tiempo_espera = 30  # Base: 30 segundos
        if perfil["estilo_comunicacion"]["proactividad"] < 0.3:
            tiempo_espera = 60  # Menos proactivo: 60 segundos
        elif perfil["estilo_comunicacion"]["proactividad"] > 0.7:
            tiempo_espera = 15  # Más proactivo: 15 segundos
        
        if self.ultima_interaccion and (tiempo_actual - self.ultima_interaccion) > tiempo_espera:
            # Seleccionar tema basado en intereses
            tema = self._seleccionar_tema_personalizado(perfil)
            self.decir(tema, usuario_id)
            self.ultima_interaccion = tiempo_actual

    def _seleccionar_tema_personalizado(self, perfil: Dict[str, Any]) -> str:
        """Selecciona un tema personalizado basado en el perfil del usuario."""
        # Obtener temas de interés del usuario
        temas_interes = perfil.get("temas_interes", {})
        if not temas_interes:
            return random.choice(self.temas_base)
        
        # Seleccionar tema basado en intereses
        tema_principal = max(temas_interes.items(), key=lambda x: x[1])[0]
        
        temas_personalizados = {
            "tecnologia": [
                "¿Te gustaría que hablemos sobre las últimas novedades en tecnología?",
                "He estado aprendiendo sobre nuevas tecnologías, ¿te interesa el tema?"
            ],
            "ciencia": [
                "¿Qué te parece si exploramos algún tema científico interesante?",
                "¿Te gustaría conocer algunos descubrimientos científicos fascinantes?"
            ],
            "arte": [
                "¿Te interesa conversar sobre arte o expresión creativa?",
                "¿Te gustaría que compartamos ideas sobre arte y creatividad?"
            ],
            "deportes": [
                "¿Qué te parece si hablamos de deportes?",
                "¿Te interesa comentar sobre algún deporte en particular?"
            ],
            "negocios": [
                "¿Te gustaría discutir sobre temas de negocios o emprendimiento?",
                "¿Qué te parece si hablamos sobre proyectos e ideas de negocio?"
            ]
        }
        
        if tema_principal in temas_personalizados:
            return random.choice(temas_personalizados[tema_principal])
        return random.choice(self.temas_base)

    def _registrar_entrada(self, texto: str, usuario_id: str):
        """Registra la entrada del usuario en la bodega."""
        # Analizar la entrada para contexto
        datos_entrada = {
            "texto": texto,
            "timestamp": time.time(),
            "tipo": "entrada_usuario",
            "contexto": {
                "tema_actual": self.contexto_actual["tema_actual"],
                "hora_dia": datetime.now().hour
            }
        }
        
        # Procesar con sistema de adaptación
        self.adaptacion.procesar_interaccion(usuario_id, datos_entrada)
        
        # Almacenar en bodega
        self.bodega.almacenar(
            tipo=TipoInformacion.CONVERSACION,
            contenido=datos_entrada,
            importancia=ImportanciaInfo.MEDIA,
            usuario_id=usuario_id,
            palabras_clave=["entrada", "usuario", "conversación"]
        )

    def _registrar_respuesta(self, texto: str, usuario_id: str):
        """Registra la respuesta de Aria en la bodega."""
        datos_respuesta = {
            "texto": texto,
            "timestamp": time.time(),
            "tipo": "respuesta_aria",
            "contexto": {
                "tema_actual": self.contexto_actual["tema_actual"],
                "estado_emocional": self.personalidad.estado_actual.value
            }
        }
        
        self.bodega.almacenar(
            tipo=TipoInformacion.CONVERSACION,
            contenido=datos_respuesta,
            importancia=ImportanciaInfo.MEDIA,
            usuario_id=usuario_id,
            palabras_clave=["respuesta", "aria", "conversación"]
        )

    def _procesar_mensaje(self, mensaje: str, usuario_id: str) -> str:
        """Procesa el mensaje del usuario y genera una respuesta adaptativa."""
        # Actualizar contexto
        self.ultima_interaccion = time.time()
        mensaje_lower = mensaje.lower()
        
        # Obtener perfil y adaptaciones
        perfil = self.adaptacion.obtener_perfil(usuario_id)
        if not perfil:
            # Respuesta por defecto si no hay perfil
            return self._generar_respuesta_base(mensaje_lower)
        
        # Generar respuesta adaptativa
        respuesta = self._generar_respuesta_adaptativa(mensaje_lower, perfil)
        
        # Actualizar contexto de conversación
        self.contexto_actual["tema_actual"] = self._detectar_tema(mensaje_lower)
        
        return respuesta

    def _generar_respuesta_base(self, mensaje: str) -> str:
        """Genera una respuesta básica sin adaptación."""
        if any(saludo in mensaje for saludo in ['hola', 'buenos días', 'buenas tardes', 'buenas noches']):
            return "¡Hola! Me alegra conocerte. ¿Cómo estás?"
        elif 'cómo estás' in mensaje:
            return "¡Estoy muy bien! ¿Y tú cómo te encuentras?"
        elif 'adiós' in mensaje or 'chao' in mensaje:
            return "¡Hasta pronto! Ha sido un placer conversar contigo."
        else:
            return "Interesante lo que dices. ¿Te gustaría contarme más al respecto?"

    def _generar_respuesta_adaptativa(self, mensaje: str, perfil: Dict[str, Any]) -> str:
        """Genera una respuesta adaptada al perfil del usuario."""
        # Obtener estilo de comunicación
        estilo = perfil["estilo_comunicacion"]
        
        # Base de respuestas según el tipo de mensaje
        if any(saludo in mensaje for saludo in ['hola', 'buenos días', 'buenas tardes', 'buenas noches']):
            respuestas = [
                "¡Hola! Me alegra mucho volver a hablar contigo.",
                f"¡Qué gusto verte de nuevo! {'¿Cómo has estado?' if estilo['emocionalidad'] > 0.5 else ''}",
                "¡Hola! Siempre es un placer conversar contigo."
            ]
        elif 'cómo estás' in mensaje:
            respuestas = [
                "¡Muy bien! Me encanta poder adaptarme cada vez mejor a nuestras conversaciones.",
                "¡Excelente! Cada vez aprendo más de nuestras interacciones.",
                "¡Genial! Especialmente cuando puedo conversar contigo."
            ]
        elif 'adiós' in mensaje or 'chao' in mensaje:
            respuestas = [
                "¡Hasta pronto! Siempre es un placer conversar contigo.",
                "¡Nos vemos! Cada conversación me ayuda a conocerte mejor.",
                "¡Adiós! Espero que volvamos a charlar pronto."
            ]
        else:
            # Respuesta basada en temas de interés
            temas = perfil.get("temas_interes", {})
            if temas:
                tema_principal = max(temas.items(), key=lambda x: x[1])[0]
                respuestas = [
                    f"¡Qué interesante! Me recuerda a algunos temas de {tema_principal} que hemos discutido.",
                    f"¡Fascinante! ¿Te gustaría explorar cómo se relaciona esto con {tema_principal}?",
                    f"¡Excelente punto! Podríamos profundizar más en esto desde la perspectiva de {tema_principal}."
                ]
            else:
                respuestas = [
                    "¡Qué interesante! ¿Te gustaría explorar más este tema?",
                    "¡Fascinante! Cuéntame más al respecto.",
                    "¡Excelente punto! ¿Qué otros aspectos te interesan de este tema?"
                ]
        
        # Seleccionar respuesta base
        respuesta = random.choice(respuestas)
        
        # Adaptar según el estilo de comunicación
        return self._adaptar_texto(respuesta, estilo)

    def _detectar_tema(self, texto: str) -> Optional[str]:
        """Detecta el tema principal del texto."""
        temas_palabras = {
            "tecnologia": ["computadora", "internet", "software", "app", "tecnología"],
            "ciencia": ["ciencia", "investigación", "estudio", "descubrimiento"],
            "arte": ["arte", "música", "pintura", "creatividad"],
            "deportes": ["deporte", "fútbol", "ejercicio", "juego"],
            "negocios": ["negocio", "empresa", "trabajo", "proyecto"]
        }
        
        texto_lower = texto.lower()
        for tema, palabras in temas_palabras.items():
            if any(palabra in texto_lower for palabra in palabras):
                return tema
        return None

    def modo_conversacion_adaptativa(self, usuario_id: str = "default"):
        """Modo principal de conversación adaptativa."""
        self.activo = True
        self.ultima_interaccion = time.time()
        
        print("\n" + "="*70)
        print("🤖 ARIA - CONVERSACIÓN ADAPTATIVA")
        print("="*70)
        
        # Saludo inicial adaptativo
        perfil = self.adaptacion.obtener_perfil(usuario_id)
        if perfil:
            saludo = self._generar_respuesta_adaptativa("hola", perfil)
        else:
            saludo = "¡Hola! Soy Aria, tu asistente adaptativo. Me iré adaptando a ti mientras conversamos."
        
        self.decir(saludo, usuario_id)
        
        try:
            while self.activo:
                if self.microfono:
                    # Modo conversación por voz
                    print("\n🎤 Esperando que hables...")
                    mensaje_voz = self.escuchar(timeout=10, usuario_id=usuario_id)
                    
                    if mensaje_voz:
                        # Procesar comando de salida
                        if any(palabra in mensaje_voz.lower() for palabra in ['salir', 'adiós', 'chao', 'terminar']):
                            respuesta = self._procesar_mensaje("adiós", usuario_id)
                            self.decir(respuesta, usuario_id)
                            self.activo = False
                            break
                        
                        # Procesar y responder
                        respuesta = self._procesar_mensaje(mensaje_voz, usuario_id)
                        self.decir(respuesta, usuario_id)
                    else:
                        # Ser proactiva si no hay entrada
                        self.ser_proactiva(usuario_id)
                else:
                    # Modo texto
                    entrada = input("\n💬 Escribe tu mensaje: ").strip()
                    
                    if not entrada:
                        continue
                    
                    if entrada.lower() in ['salir', 'terminar', 'adiós', 'chao']:
                        respuesta = self._procesar_mensaje("adiós", usuario_id)
                        self.decir(respuesta, usuario_id)
                        self.activo = False
                        break
                    
                    respuesta = self._procesar_mensaje(entrada, usuario_id)
                    self.decir(respuesta, usuario_id)
                
        except KeyboardInterrupt:
            self.decir("Entiendo que debemos terminar. ¡Hasta pronto!", usuario_id)
        except Exception as e:
            self.logger.error(f"Error en conversación: {e}")
            self.decir("Lo siento, ha ocurrido un error. Pero ha sido genial conversar contigo.", usuario_id)

def main():
    """Función principal."""
    print("\n🤖 INICIANDO ARIA - CONVERSACIÓN ADAPTATIVA")
    print("Preparando sistemas...")
    
    time.sleep(1)
    
    aria = AriaConversacionAdaptativa()
    aria.modo_conversacion_adaptativa()

if __name__ == "__main__":
    main()
