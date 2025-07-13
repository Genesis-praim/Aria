"""
Sistema IA Aria - Versión Adaptativa Universal
Capaz de operar en múltiples dominios simultáneamente:
- Administrativo
- Militar/Inteligencia
- Procesamiento paralelo masivo
- Adaptabilidad en tiempo real
"""

import sys
import time
import threading
import logging
from typing import Dict, Any

# Configurar logging sin emojis para compatibilidad con Windows
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aria_sistema.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Importar componentes del sistema
from nucleo_cognitivo.adaptabilidad_universal.SistemaAdaptativo import SistemaAdaptativo, ModoOperacion
from dominios_especializados.militar.InteligenciaMilitar import NivelSeguridad, TipoAmenaza
from nucleo_cognitivo.red_neuronal.RedNeuronal2 import Cerebro
from YoSOY.personalidad_PersonalidadCentral import PersonalidadCentral
import YoSOY.conexiones as conexiones

class AriaUniversal:
    def __init__(self, nivel_autorizacion: NivelSeguridad = NivelSeguridad.CONFIDENCIAL):
        self.logger = logging.getLogger("AriaUniversal")
        self.logger.info("Iniciando Sistema IA Aria Universal...")
        
        # Inicializar componentes base
        self.cerebro = Cerebro()
        self.personalidad = PersonalidadCentral()
        self.sistema_adaptativo = SistemaAdaptativo(nivel_autorizacion)
        
        # Configurar conexiones
        self.gestor_conexiones = conexiones.GestorConexiones()
        self._configurar_conexiones()
        
        # Estado del sistema
        self.activo = True
        self.estadisticas = {
            "tiempo_inicio": time.time(),
            "solicitudes_procesadas": 0,
            "modos_utilizados": set(),
            "errores": 0
        }
        
        self.logger.info("Sistema Aria Universal inicializado correctamente")

    def _configurar_conexiones(self):
        """Configura las conexiones entre componentes."""
        conexion1 = conexiones.Conexion("Cerebro", "SistemaAdaptativo")
        conexion2 = conexiones.Conexion("SistemaAdaptativo", "Personalidad")
        conexion3 = conexiones.Conexion("Personalidad", "GestorAdministrativo")
        conexion4 = conexiones.Conexion("SistemaAdaptativo", "InteligenciaMilitar")
        
        self.gestor_conexiones.agregar_conexion(conexion1)
        self.gestor_conexiones.agregar_conexion(conexion2)
        self.gestor_conexiones.agregar_conexion(conexion3)
        self.gestor_conexiones.agregar_conexion(conexion4)
        
        self.gestor_conexiones.conectar_todas()

    def procesar_solicitud(self, solicitud: Dict[str, Any]) -> Dict[str, Any]:
        """Procesa una solicitud de manera adaptativa."""
        try:
            inicio = time.time()
            self.logger.info(f"Procesando solicitud: {solicitud.get('tipo', 'general')}")
            
            # Procesar con el sistema adaptativo
            resultado = self.sistema_adaptativo.procesar_solicitud_adaptativa(solicitud)
            
            # Actualizar estadísticas
            self.estadisticas["solicitudes_procesadas"] += 1
            self.estadisticas["modos_utilizados"].add(self.sistema_adaptativo.contexto_actual.modo.value)
            
            tiempo_total = time.time() - inicio
            self.logger.info(f"Solicitud procesada en {tiempo_total:.2f}s")
            
            return {
                "exito": True,
                "resultado": resultado,
                "tiempo_procesamiento": tiempo_total,
                "modo_utilizado": self.sistema_adaptativo.contexto_actual.modo.value
            }
            
        except Exception as e:
            self.estadisticas["errores"] += 1
            self.logger.error(f"Error procesando solicitud: {str(e)}")
            return {
                "exito": False,
                "error": str(e),
                "tiempo_procesamiento": time.time() - inicio
            }

    def cambiar_modo(self, modo: str, configuracion: Dict[str, Any] = None):
        """Cambia el modo de operación del sistema."""
        try:
            modo_enum = ModoOperacion(modo.lower())
            self.sistema_adaptativo.cambiar_modo_operacion(modo_enum, configuracion)
            self.logger.info(f"Modo cambiado a: {modo}")
        except ValueError:
            self.logger.error(f"Modo no válido: {modo}")

    def generar_reporte_completo(self) -> Dict[str, Any]:
        """Genera un reporte completo del estado del sistema."""
        reporte_adaptativo = self.sistema_adaptativo.generar_reporte_integral()
        
        reporte_completo = {
            "sistema_aria": {
                "version": "Universal v2.0",
                "tiempo_activo": time.time() - self.estadisticas["tiempo_inicio"],
                "estadisticas": self.estadisticas.copy(),
                "estado_cerebro": {
                    "neuronas_activas": sum(1 for d in self.cerebro.disparos if d > 0),
                    "operaciones_por_segundo": self.cerebro.ops_por_segundo
                },
                "personalidad": {
                    "traits_activos": len(self.personalidad.traits),
                    "estado": str(self.personalidad)
                }
            },
            "sistema_adaptativo": reporte_adaptativo
        }
        
        return reporte_completo

    def ejecutar_demostracion(self):
        """Ejecuta una demostración de las capacidades del sistema."""
        self.logger.info("Iniciando demostracion de capacidades...")
        
        # Demostración administrativa
        self.logger.info("Demostrando capacidades administrativas...")
        self.cambiar_modo("administrativo")
        
        solicitud_admin = {
            "tipo": "administrativo",
            "accion": "generar_informe",
            "datos": {
                "titulo": "Reporte de Rendimiento del Sistema",
                "periodo": "Q1 2024",
                "metricas": [
                    {"nombre": "Eficiencia", "valor": "95%"},
                    {"nombre": "Disponibilidad", "valor": "99.9%"},
                    {"nombre": "Satisfacción", "valor": "4.8/5"}
                ]
            },
            "prioridad": 2
        }
        
        resultado_admin = self.procesar_solicitud(solicitud_admin)
        self.logger.info(f"Resultado administrativo: {resultado_admin['exito']}")
        
        # Demostración militar
        self.logger.info("Demostrando capacidades militares...")
        self.cambiar_modo("militar")
        
        solicitud_militar = {
            "tipo": "militar",
            "accion": "detectar_amenaza",
            "tipo_amenaza": "cibernetica",
            "descripcion": "Actividad sospechosa detectada en red",
            "nivel_riesgo": 7,
            "probabilidad": 0.8,
            "impacto": 8,
            "ubicacion": "Sector Norte"
        }
        
        resultado_militar = self.procesar_solicitud(solicitud_militar)
        self.logger.info(f"Resultado militar: {resultado_militar['exito']}")
        
        # Demostración híbrida
        self.logger.info("Demostrando modo hibrido...")
        self.cambiar_modo("hibrido")
        
        # Procesar múltiples solicitudes simultáneamente
        solicitudes_hibridas = [
            {
                "tipo": "administrativo",
                "accion": "crear_documento",
                "tipo_documento": "memorandum",
                "contenido": {
                    "para": "Comando Central",
                    "de": "Sistema Aria",
                    "fecha": "2024-01-15",
                    "asunto": "Actualización de Protocolos"
                }
            },
            {
                "tipo": "militar",
                "accion": "registrar_inteligencia",
                "fuente": "Sensor Automático",
                "contenido": "Movimiento vehicular inusual detectado",
                "nivel_seguridad": 3,
                "urgencia": 2
            }
        ]
        
        for solicitud in solicitudes_hibridas:
            resultado = self.procesar_solicitud(solicitud)
            self.logger.info(f"Procesamiento hibrido: {resultado['exito']}")
        
        # Generar reporte final
        reporte_final = self.generar_reporte_completo()
        self.logger.info("Reporte final generado")
        
        return reporte_final

    def monitoreo_continuo(self, duracion_segundos: int = 60):
        """Ejecuta monitoreo continuo del sistema."""
        self.logger.info(f"Iniciando monitoreo continuo por {duracion_segundos} segundos...")
        
        inicio = time.time()
        while time.time() - inicio < duracion_segundos and self.activo:
            # Simular actividad del sistema
            self.cerebro.simular_paso(time.time() - inicio)
            
            # Generar solicitudes automáticas ocasionales
            if int(time.time()) % 10 == 0:  # Cada 10 segundos
                solicitud_auto = {
                    "tipo": "general",
                    "accion": "monitoreo_salud",
                    "timestamp": time.time()
                }
                self.procesar_solicitud(solicitud_auto)
            
            time.sleep(1)
        
        self.logger.info("Monitoreo continuo completado")

    def detener(self):
        """Detiene el sistema de manera segura."""
        self.logger.info("Deteniendo Sistema Aria Universal...")
        self.activo = False
        self.sistema_adaptativo.detener()
        self.gestor_conexiones.desconectar_todas()
        self.logger.info("Sistema detenido correctamente")

def main():
    """Función principal del sistema."""
    print("Iniciando Sistema IA Aria Universal")
    print("=" * 50)
    
    # Crear instancia del sistema
    aria = AriaUniversal(nivel_autorizacion=NivelSeguridad.CONFIDENCIAL)
    
    try:
        # Ejecutar demostración
        print("\nEjecutando demostracion de capacidades...")
        reporte_demo = aria.ejecutar_demostracion()
        
        print(f"\nResumen de la demostracion:")
        print(f"- Solicitudes procesadas: {aria.estadisticas['solicitudes_procesadas']}")
        print(f"- Modos utilizados: {', '.join(aria.estadisticas['modos_utilizados'])}")
        print(f"- Errores: {aria.estadisticas['errores']}")
        
        # Monitoreo continuo opcional
        respuesta = input("\n¿Ejecutar monitoreo continuo? (s/n): ")
        if respuesta.lower() == 's':
            duracion = int(input("Duración en segundos (default 30): ") or "30")
            aria.monitoreo_continuo(duracion)
        
        # Generar reporte final
        print("\nGenerando reporte final...")
        reporte_final = aria.generar_reporte_completo()
        
        # Guardar reporte
        import json
        with open("reporte_aria_universal.json", "w", encoding="utf-8") as f:
            json.dump(reporte_final, f, indent=2, ensure_ascii=False, default=str)
        
        print("Reporte guardado en: reporte_aria_universal.json")
        
    except KeyboardInterrupt:
        print("\nInterrupción detectada...")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")
    finally:
        aria.detener()
        print("\nSistema Aria Universal finalizado")

if __name__ == "__main__":
    main()
