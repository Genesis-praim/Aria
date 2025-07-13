"""
Demostración del Sistema Sensorial Integrado de Aria
Muestra las capacidades principales del sistema en acción
"""

import time
import logging
from typing import Dict, Any
from main_sensorial_integrado import SistemaAriaIntegrado
from interfaz_sensorial import IntegradorSensorial
from lenguaje_y_abstraccion import LenguajeYAbstraccion
from emocion_y_personalidad import EmocionYMotivacion

class DemoSistemaSensorial:
    """Demostración interactiva del sistema sensorial."""
    
    def __init__(self):
        self.logger = logging.getLogger("DemoSistemaSensorial")
        self.sistema = None
        self.demo_activa = False
    
    def configurar_logging(self):
        """Configura el sistema de logging para la demo."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('demo_sensorial.log')
            ]
        )
    
    def mostrar_bienvenida(self):
        """Muestra mensaje de bienvenida."""
        print("\n" + "="*60)
        print("🤖 DEMOSTRACIÓN DEL SISTEMA SENSORIAL INTEGRADO DE ARIA")
        print("="*60)
        print("\nEste demo mostrará las capacidades principales del sistema:")
        print("• 🎤 Procesamiento de audio y reconocimiento de voz")
        print("• 👁️  Captura de video y detección visual")
        print("• 🗣️  Síntesis de voz y respuestas adaptativas")
        print("• 🧠 Integración sensorial y análisis contextual")
        print("• 💭 Sistema emocional y personalidad adaptativa")
        print("• 📝 Procesamiento de lenguaje natural")
        print("\n" + "="*60)
    
    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n📋 MENÚ DE DEMOSTRACIÓN:")
        print("1. 🎤 Demo de Sistema de Audio (Oído)")
        print("2. 👁️  Demo de Sistema Visual (Ojos)")
        print("3. 🗣️  Demo de Síntesis de Voz")
        print("4. 🧠 Demo de Integración Sensorial")
        print("5. 💭 Demo de Sistema Emocional")
        print("6. 📝 Demo de Procesamiento de Lenguaje")
        print("7. 🤖 Demo Completo Integrado")
        print("8. 📊 Mostrar Estadísticas del Sistema")
        print("9. ⚙️  Configurar Sistema")
        print("0. 🚪 Salir")
        print("-" * 40)
    
    def demo_audio(self):
        """Demostración del sistema de audio."""
        print("\n🎤 DEMO: Sistema de Audio")
        print("-" * 30)
        
        try:
            from interfaz_sensorial.oido import Oido
            
            oido = Oido()
            print("✅ Sistema de audio inicializado")
            
            # Configurar oído
            oido.configurar(
                energia_minima=300,
                energia_dinamica=True,
                pausa_threshold=0.8
            )
            print("⚙️  Configuración aplicada")
            
            print("\n🎯 Prueba de escucha (5 segundos)...")
            print("💬 Habla algo al micrófono...")
            
            resultado = oido.escuchar(timeout=5)
            
            if resultado.get("exito"):
                print(f"✅ Texto reconocido: '{resultado.get('texto', 'N/A')}'")
                print(f"📊 Confianza: {resultado.get('confianza', 0):.2f}")
            else:
                print(f"❌ Error: {resultado.get('error', 'Desconocido')}")
            
            # Mostrar estadísticas
            stats = oido.obtener_estadisticas()
            print(f"\n📈 Estadísticas:")
            print(f"   • Intentos de escucha: {stats['intentos_escucha']}")
            print(f"   • Reconocimientos exitosos: {stats['reconocimientos_exitosos']}")
            
        except Exception as e:
            print(f"❌ Error en demo de audio: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_visual(self):
        """Demostración del sistema visual."""
        print("\n👁️  DEMO: Sistema Visual")
        print("-" * 30)
        
        try:
            from interfaz_sensorial.ojos import Ojos
            
            ojos = Ojos()
            print("✅ Sistema visual inicializado")
            
            # Configurar cámara
            ojos.configurar(
                resolucion=(640, 480),
                fps=30
            )
            print("⚙️  Configuración aplicada")
            
            print("\n📸 Capturando imagen...")
            resultado_imagen = ojos.capturar_imagen()
            
            if resultado_imagen.get("exito"):
                print("✅ Imagen capturada exitosamente")
                print(f"📏 Dimensiones: {resultado_imagen.get('dimensiones', 'N/A')}")
            else:
                print(f"❌ Error capturando imagen: {resultado_imagen.get('error')}")
            
            print("\n👤 Detectando rostros...")
            resultado_rostros = ojos.detectar_rostros()
            
            if resultado_rostros.get("exito"):
                rostros = resultado_rostros.get("rostros_detectados", 0)
                print(f"✅ Rostros detectados: {rostros}")
                
                if rostros > 0:
                    print("👥 Detalles de rostros:")
                    for i, rostro in enumerate(resultado_rostros.get("rostros", [])):
                        print(f"   Rostro {i+1}: x={rostro['x']}, y={rostro['y']}, "
                              f"ancho={rostro['ancho']}, alto={rostro['alto']}")
            else:
                print(f"❌ Error detectando rostros: {resultado_rostros.get('error')}")
            
            print("\n🏃 Detectando movimiento...")
            resultado_movimiento = ojos.detectar_movimiento()
            
            if resultado_movimiento.get("exito"):
                movimiento = resultado_movimiento.get("movimiento_detectado", False)
                print(f"✅ Movimiento detectado: {'Sí' if movimiento else 'No'}")
                
                if movimiento:
                    intensidad = resultado_movimiento.get("intensidad", 0)
                    print(f"📊 Intensidad del movimiento: {intensidad:.2f}")
            else:
                print(f"❌ Error detectando movimiento: {resultado_movimiento.get('error')}")
            
            # Cerrar sistema visual
            ojos.cerrar()
            print("\n🔒 Sistema visual cerrado")
            
        except Exception as e:
            print(f"❌ Error en demo visual: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_voz(self):
        """Demostración del sistema de voz."""
        print("\n🗣️  DEMO: Sistema de Voz")
        print("-" * 30)
        
        try:
            from interfaz_sensorial.voz import Voz
            
            voz = Voz()
            print("✅ Sistema de voz inicializado")
            
            # Configurar voz
            voz.configurar(
                velocidad=0,
                volumen=100
            )
            print("⚙️  Configuración aplicada")
            
            # Pruebas de síntesis
            textos_prueba = [
                "Hola, soy Aria, tu asistente inteligente.",
                "Este es un demo del sistema de síntesis de voz.",
                "Puedo hablar con diferentes velocidades y volúmenes.",
                "¡Espero que disfrutes esta demostración!"
            ]
            
            for i, texto in enumerate(textos_prueba, 1):
                print(f"\n🔊 Reproduciendo mensaje {i}/4...")
                print(f"💬 Texto: '{texto}'")
                
                resultado = voz.hablar(texto)
                
                if resultado.get("exito"):
                    print("✅ Síntesis exitosa")
                    time.sleep(1)  # Pausa entre mensajes
                else:
                    print(f"❌ Error: {resultado.get('error')}")
            
            # Mostrar estadísticas
            stats = voz.obtener_estadisticas()
            if 'mensajes_sintetizados' in stats and 'caracteres_procesados' in stats:
                print(f"\n📈 Estadísticas:")
                print(f"   • Mensajes sintetizados: {stats['mensajes_sintetizados']}")
                print(f"   • Caracteres procesados: {stats['caracteres_procesados']}")
            else:
                print("⚠️ Estadísticas incompletas o no disponibles.")
            
        except Exception as e:
            print(f"❌ Error en demo de voz: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_integracion(self):
        """Demostración de integración sensorial."""
        print("\n🧠 DEMO: Integración Sensorial")
        print("-" * 30)
        
        try:
            integrador = IntegradorSensorial()
            print("✅ Integrador sensorial inicializado")
            
            eventos_recibidos = []
            
            def callback_demo(datos):
                eventos_recibidos.append(datos)
                print(f"📨 Evento recibido: {datos.get('tipo', 'desconocido')}")
            
            # Registrar callbacks
            integrador.registrar_callback("audio", callback_demo)
            integrador.registrar_callback("visual", callback_demo)
            integrador.registrar_callback("integrado", callback_demo)
            
            print("🔗 Callbacks registrados")
            
            # Iniciar integrador
            print("\n▶️  Iniciando integración sensorial...")
            integrador.iniciar()
            
            print("⏱️  Capturando eventos por 10 segundos...")
            print("💬 Habla o muévete frente a la cámara para generar eventos")
            
            time.sleep(10)
            
            # Detener integrador
            integrador.detener()
            print("\n⏹️  Integración detenida")
            
            # Mostrar resultados
            print(f"\n📊 Eventos capturados: {len(eventos_recibidos)}")
            
            if eventos_recibidos:
                tipos_eventos = {}
                for evento in eventos_recibidos:
                    tipo = evento.get('tipo', 'desconocido')
                    tipos_eventos[tipo] = tipos_eventos.get(tipo, 0) + 1
                
                print("📈 Distribución de eventos:")
                for tipo, cantidad in tipos_eventos.items():
                    print(f"   • {tipo}: {cantidad}")
            
            # Estadísticas del integrador
            stats = integrador.obtener_estadisticas()
            print(f"\n📋 Estadísticas del integrador:")
            print(f"   • Estado: {stats['estado']}")
            print(f"   • Modo de atención: {stats['modo_atencion']}")
            
        except Exception as e:
            print(f"❌ Error en demo de integración: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_emocional(self):
        """Demostración del sistema emocional."""
        print("\n💭 DEMO: Sistema Emocional")
        print("-" * 30)
        
        try:
            emocion = EmocionYMotivacion()
            print("✅ Sistema emocional inicializado")
            
            # Mostrar estado inicial
            estado_inicial = emocion.obtener_estado_emocional()
            print(f"\n😊 Estado emocional inicial:")
            print(f"   • Emoción: {estado_inicial['emocion_actual']}")
            print(f"   • Intensidad: {estado_inicial['intensidad']:.2f}")
            
            # Simular diferentes estímulos
            estimulos = [
                ("interaccion_positiva", 0.8, "Usuario dice 'gracias'"),
                ("nuevo_conocimiento", 0.7, "Aprendiendo algo nuevo"),
                ("problema_complejo", 0.6, "Enfrentando un desafío"),
                ("logro_objetivo", 0.9, "Completando una tarea")
            ]
            
            print("\n🎭 Simulando diferentes estímulos emocionales...")
            
            for estimulo, intensidad, descripcion in estimulos:
                print(f"\n🎯 Estímulo: {descripcion}")
                
                nuevo_estado = emocion.procesar_estimulo(estimulo, intensidad)
                
                print(f"   • Nueva emoción: {nuevo_estado.tipo.value}")
                print(f"   • Intensidad: {nuevo_estado.intensidad:.2f}")
                print(f"   • Causa: {nuevo_estado.causa}")
                
                # Generar respuesta emocional
                respuesta = emocion.generar_respuesta_emocional()
                print(f"   • Respuesta: '{respuesta}'")
                
                time.sleep(2)
            
            # Mostrar motivaciones
            motivaciones = emocion.obtener_motivaciones()
            print(f"\n🎯 Estado de motivaciones:")
            for nombre, datos in motivaciones.items():
                print(f"   • {nombre}: {datos['nivel']:.2f} (prioridad: {datos['prioridad']})")
            
            # Estadísticas
            stats = emocion.obtener_estadisticas()
            print(f"\n📊 Estadísticas emocionales:")
            print(f"   • Estados registrados: {stats['total_estados_registrados']}")
            print(f"   • Motivación dominante: {stats['motivacion_dominante']['nombre']}")
            
        except Exception as e:
            print(f"❌ Error en demo emocional: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_lenguaje(self):
        """Demostración del procesamiento de lenguaje."""
        print("\n📝 DEMO: Procesamiento de Lenguaje")
        print("-" * 30)
        
        try:
            lenguaje = LenguajeYAbstraccion()
            print("✅ Sistema de lenguaje inicializado")
            
            # Textos de prueba
            textos_prueba = [
                "Hola, ¿cómo estás hoy?",
                "Me siento muy feliz de poder ayudarte con tus preguntas.",
                "La inteligencia artificial es un campo fascinante de estudio.",
                "¿Podrías explicarme qué es el aprendizaje automático?"
            ]
            
            print("\n🔍 Analizando diferentes textos...")
            
            for i, texto in enumerate(textos_prueba, 1):
                print(f"\n📄 Texto {i}: '{texto}'")
                
                # Análisis semántico
                analisis = lenguaje.analizar_texto(texto)
                
                print(f"   • Tokens: {len(analisis.tokens)}")
                print(f"   • Sentimiento: {analisis.sentimiento}")
                print(f"   • Intención: {analisis.intencion}")
                print(f"   • Complejidad: {analisis.complejidad:.2f}")
                
                if analisis.temas:
                    print(f"   • Temas: {', '.join(analisis.temas)}")
                
                if analisis.conceptos_abstractos:
                    print(f"   • Conceptos: {', '.join(analisis.conceptos_abstractos)}")
                
                # Generar respuesta
                respuesta = lenguaje.generar_respuesta_adaptativa(analisis)
                print(f"   • Respuesta: '{respuesta}'")
            
            # Demostrar abstracción conceptual
            print(f"\n🧠 Generando abstracción conceptual...")
            conceptos = ["conocimiento", "inteligencia", "comunicacion"]
            abstraccion = lenguaje.generar_abstraccion(conceptos)
            
            if "error" not in abstraccion:
                print(f"   • Categoría: {abstraccion['categoria']}")
                print(f"   • Nivel de abstracción: {abstraccion['nivel_abstraccion']}")
                print(f"   • Confianza: {abstraccion['confianza']:.2f}")
            
            # Estadísticas
            stats = lenguaje.obtener_estadisticas()
            print(f"\n📈 Estadísticas de lenguaje:")
            print(f"   • Textos procesados: {stats['estadisticas_generales']['textos_procesados']}")
            print(f"   • Conceptos registrados: {stats['conceptos_registrados']}")
            
        except Exception as e:
            print(f"❌ Error en demo de lenguaje: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def demo_completo(self):
        """Demostración completa del sistema integrado."""
        print("\n🤖 DEMO: Sistema Completo Integrado")
        print("-" * 40)
        
        try:
            print("🚀 Iniciando sistema completo...")
            self.sistema = SistemaAriaIntegrado()
            
            # Iniciar sistema
            self.sistema.iniciar(usuario_id="demo_user")
            print("✅ Sistema iniciado exitosamente")
            
            print("\n🎯 El sistema está ahora:")
            print("   • 🎤 Escuchando audio del micrófono")
            print("   • 👁️  Capturando video de la cámara")
            print("   • 🧠 Procesando información en tiempo real")
            print("   • 💭 Adaptando respuestas emocionales")
            print("   • 📝 Analizando lenguaje natural")
            
            print("\n💬 Interactúa con el sistema:")
            print("   • Habla al micrófono")
            print("   • Muévete frente a la cámara")
            print("   • El sistema responderá automáticamente")
            
            print("\n⏱️  Demo activo por 30 segundos...")
            
            # Mantener sistema activo
            for i in range(30):
                time.sleep(1)
                if i % 10 == 9:  # Cada 10 segundos
                    stats = self.sistema.obtener_estadisticas()
                    print(f"📊 Estado: {stats['estado']} - "
                          f"Modo: {stats['contexto']['modo']}")
            
            print("\n⏹️  Deteniendo sistema...")
            self.sistema.detener()
            
            # Mostrar estadísticas finales
            stats_finales = self.sistema.obtener_estadisticas()
            print(f"\n📈 Estadísticas finales:")
            print(f"   • Estado final: {stats_finales['estado']}")
            print(f"   • Contexto: {stats_finales['contexto']['modo']}")
            
        except Exception as e:
            print(f"❌ Error en demo completo: {e}")
            if self.sistema:
                self.sistema.detener()
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema."""
        print("\n📊 ESTADÍSTICAS DEL SISTEMA")
        print("-" * 40)
        
        if not self.sistema:
            print("⚠️  Sistema no inicializado. Iniciando...")
            self.sistema = SistemaAriaIntegrado()
        
        try:
            stats = self.sistema.obtener_estadisticas()
            
            print(f"🤖 Estado general: {stats['estado']}")
            print(f"👤 Usuario actual: {stats.get('usuario_actual', 'Ninguno')}")
            
            if 'contexto' in stats:
                contexto = stats['contexto']
                print(f"\n🧠 Contexto:")
                print(f"   • Modo: {contexto['modo']}")
                print(f"   • Tema actual: {contexto.get('tema_actual', 'Ninguno')}")
            
            if 'integrador' in stats:
                integrador = stats['integrador']
                print(f"\n🔗 Integrador sensorial:")
                print(f"   • Estado: {integrador['estado']}")
                print(f"   • Modo atención: {integrador['modo_atencion']}")
            
            if 'bodega' in stats:
                bodega = stats['bodega']
                print(f"\n📚 Bodega de conocimiento:")
                print(f"   • Entradas totales: {bodega.get('total_entradas', 0)}")
                print(f"   • Usuarios registrados: {bodega.get('usuarios_registrados', 0)}")
            
        except Exception as e:
            print(f"❌ Error obteniendo estadísticas: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def configurar_sistema(self):
        """Permite configurar parámetros del sistema."""
        print("\n⚙️  CONFIGURACIÓN DEL SISTEMA")
        print("-" * 40)
        
        print("Opciones de configuración:")
        print("1. Configurar sistema de audio")
        print("2. Configurar sistema visual")
        print("3. Configurar sistema emocional")
        print("4. Volver al menú principal")
        
        try:
            opcion = input("\nSelecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                self._configurar_audio()
            elif opcion == "2":
                self._configurar_visual()
            elif opcion == "3":
                self._configurar_emocional()
            elif opcion == "4":
                return
            else:
                print("❌ Opción no válida")
                
        except Exception as e:
            print(f"❌ Error en configuración: {e}")
        
        input("\n⏸️  Presiona Enter para continuar...")
    
    def _configurar_audio(self):
        """Configura el sistema de audio."""
        print("\n🎤 Configuración de Audio:")
        
        try:
            energia = input("Energía mínima (100-1000, actual: 300): ").strip()
            if energia:
                energia = int(energia)
                print(f"✅ Energía mínima configurada: {energia}")
            
            dinamica = input("¿Energía dinámica? (s/n, actual: s): ").strip().lower()
            dinamica = dinamica != 'n'
            print(f"✅ Energía dinámica: {'Sí' if dinamica else 'No'}")
            
        except ValueError:
            print("❌ Valor no válido")
    
    def _configurar_visual(self):
        """Configura el sistema visual."""
        print("\n👁️  Configuración Visual:")
        
        try:
            fps = input("FPS de captura (10-60, actual: 30): ").strip()
            if fps:
                fps = int(fps)
                print(f"✅ FPS configurado: {fps}")
            
            resolucion = input("Resolución (ej: 640x480, actual: 640x480): ").strip()
            if resolucion and 'x' in resolucion:
                ancho, alto = map(int, resolucion.split('x'))
                print(f"✅ Resolución configurada: {ancho}x{alto}")
            
        except ValueError:
            print("❌ Valor no válido")
    
    def _configurar_emocional(self):
        """Configura el sistema emocional."""
        print("\n💭 Configuración Emocional:")
        
        try:
            decaimiento = input("Factor de decaimiento (0.01-1.0, actual: 0.1): ").strip()
            if decaimiento:
                decaimiento = float(decaimiento)
                print(f"✅ Factor de decaimiento: {decaimiento}")
            
            umbral = input("Umbral de cambio (0.1-1.0, actual: 0.3): ").strip()
            if umbral:
                umbral = float(umbral)
                print(f"✅ Umbral de cambio: {umbral}")
            
        except ValueError:
            print("❌ Valor no válido")
    
    def ejecutar_demo(self):
        """Ejecuta la demostración principal."""
        self.configurar_logging()
        self.mostrar_bienvenida()
        
        while True:
            try:
                self.mostrar_menu()
                opcion = input("Selecciona una opción (0-9): ").strip()
                
                if opcion == "0":
                    print("\n👋 ¡Gracias por probar el Sistema Sensorial de Aria!")
                    if self.sistema:
                        self.sistema.detener()
                    break
                elif opcion == "1":
                    self.demo_audio()
                elif opcion == "2":
                    self.demo_visual()
                elif opcion == "3":
                    self.demo_voz()
                elif opcion == "4":
                    self.demo_integracion()
                elif opcion == "5":
                    self.demo_emocional()
                elif opcion == "6":
                    self.demo_lenguaje()
                elif opcion == "7":
                    self.demo_completo()
                elif opcion == "8":
                    self.mostrar_estadisticas()
                elif opcion == "9":
                    self.configurar_sistema()
                else:
                    print("❌ Opción no válida. Intenta de nuevo.")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupción detectada. Cerrando demo...")
                if self.sistema:
                    self.sistema.detener()
                break
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                self.logger.error(f"Error en demo: {e}")

def main():
    """Función principal."""
    demo = DemoSistemaSensorial()
    demo.ejecutar_demo()

if __name__ == "__main__":
    main()
