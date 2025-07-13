"""
Sistema IA Aria Universal - Punto de entrada principal con acceso total
Integra capacidades sensoriales y control administrativo completo
"""

import logging
import time
import os
import sys
from typing import Dict, Any, Optional, List
from datetime import datetime

# Importaciones con manejo de errores
def importar_modulo_seguro(modulo, nombre_clase=None):
    """Importa un módulo de manera segura, retornando None si falla."""
    try:
        if nombre_clase:
            mod = __import__(modulo, fromlist=[nombre_clase])
            return getattr(mod, nombre_clase)
        else:
            return __import__(modulo)
    except ImportError as e:
        print(f"Advertencia: No se pudo importar {modulo}: {e}")
        return None

# Importar componentes principales
try:
    from nucleo_cognitivo.red_neuronal.RedNeuronal2 import Cerebro
    from nucleo_cognitivo.procesamiento_paralelo.GestorTareas import GestorTareas, PrioridadTarea, Tarea
    from nucleo_cognitivo.adaptabilidad_universal.SistemaAdaptativo import SistemaAdaptativo, ModoOperacion
    print("✓ Núcleo cognitivo cargado")
except ImportError as e:
    print(f"⚠ Error cargando núcleo cognitivo: {e}")
    Cerebro = None
    GestorTareas = None
    SistemaAdaptativo = None

# Importar módulo avanzado
from D.X2.mejoras.modulo_avanzado import aria_avanzada

# Importar módulo de conexiones y transferencia
from conexiones import gestor_conexiones
from conexiones.transferencia import transferencia_datos

# Importar sistema sensorial
try:
    from interfaz_sensorial.integrador_sensorial import IntegradorSensorial
    from interfaz_sensorial.ojos import SistemaVisual
    from interfaz_sensorial.oido import SistemaAuditivo
    from interfaz_sensorial.voz import SistemaVocal
    print("✓ Sistema sensorial cargado")
except ImportError as e:
    print(f"⚠ Error cargando sistema sensorial: {e}")
    IntegradorSensorial = None
    SistemaVisual = None
    SistemaAuditivo = None
    SistemaVocal = None

# Importar procesamiento de lenguaje
try:
    from lenguaje_y_abstraccion.gramatica_espanol import GramaticaEspanol
    from lenguaje_y_abstraccion.LenguajeYAbstraccion import LenguajeYAbstraccion
    print("✓ Procesamiento de lenguaje cargado")
except ImportError as e:
    print(f"⚠ Error cargando procesamiento de lenguaje: {e}")
    GramaticaEspanol = None
    LenguajeYAbstraccion = None

# Importar dominios especializados
try:
    from dominios_especializados.administrativo.GestorAdministrativo import GestorAdministrativo
    from dominios_especializados.militar.InteligenciaMilitar import InteligenciaMilitar, NivelSeguridad
    print("✓ Dominios especializados cargados")
except ImportError as e:
    print(f"⚠ Error cargando dominios especializados: {e}")
    GestorAdministrativo = None
    InteligenciaMilitar = None

# Importar personalidad
try:
    from personalidad.personalidad.PersonalidadCentral import PersonalidadCentral
    print("✓ Personalidad cargada")
except ImportError as e:
    print(f"⚠ Error cargando personalidad: {e}")
    PersonalidadCentral = None

# Importar conexiones
try:
    from conexiones.local import ConexionLocal
    from conexiones.nube import ConexionNube
    from conexiones.onedrive import ConexionOneDrive
    from conexiones.sd import ConexionSD
    from conexiones.servidor import ConexionServidor
    from conexiones.contenedor import Contenedor
    print("✓ Conexiones cargadas")
except ImportError as e:
    print(f"⚠ Error cargando conexiones: {e}")
    ConexionLocal = None
    ConexionNube = None
    ConexionOneDrive = None
    ConexionSD = None
    ConexionServidor = None
    Contenedor = None

class AriaUniversal:
    """Sistema IA Aria Universal con acceso total y capacidades sensoriales."""
    
    def __init__(self, modo_admin: bool = True):
        # Configurar logging avanzado
        os.makedirs('logs', exist_ok=True)
        logging.basicConfig(
            filename=f'logs/aria_sistema_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
            level=logging.INFO if not modo_admin else logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("AriaUniversal")
        
        # Modo administrador
        self.modo_admin = modo_admin
        self.permisos_admin = {
            "control_total": True,
            "acceso_sistema": True,
            "modificar_codigo": True,
            "ejecutar_comandos": True,
            "acceso_red": True
        } if modo_admin else {}
        
        # Inicializar núcleo cognitivo
        self.cerebro = Cerebro() if Cerebro else None
        self.gestor_tareas = GestorTareas() if GestorTareas else None
        self.sistema_adaptativo = SistemaAdaptativo() if SistemaAdaptativo else None
        self.personalidad = PersonalidadCentral() if PersonalidadCentral else None
        
        # Inicializar sistema sensorial
        self.sistema_sensorial = IntegradorSensorial() if IntegradorSensorial else None
        
        # Inicializar procesamiento de lenguaje
        self.gramatica = GramaticaEspanol() if GramaticaEspanol else None
        self.procesador_lenguaje = LenguajeYAbstraccion() if LenguajeYAbstraccion else None
        
        # Inicializar dominios especializados con acceso total
        self.gestor_administrativo = GestorAdministrativo() if GestorAdministrativo else None
        self.inteligencia_militar = InteligenciaMilitar() if InteligenciaMilitar else None
        
        # Estado del sistema
        self.estado = {
            "inicio_sesion": datetime.now(),
            "modo_admin": modo_admin,
            "sistemas_activos": [],
            "conexiones_activas": [],
            "tareas_pendientes": [],
            "estado_sensorial": None
        }
        
        # Inicializar conexiones
        self.conexiones = {}
        if ConexionLocal:
            self.conexiones["local"] = ConexionLocal()
        if ConexionNube:
            self.conexiones["nube"] = ConexionNube()
        if ConexionOneDrive:
            self.conexiones["onedrive"] = ConexionOneDrive()
        if ConexionSD:
            self.conexiones["sd"] = ConexionSD()
        if ConexionServidor:
            self.conexiones["servidor"] = ConexionServidor()
        if Contenedor:
            self.conexiones["contenedor"] = Contenedor()

    def inicializar(self) -> bool:
        """Inicializa el sistema."""
        try:
            self.logger.info("Iniciando Sistema IA Aria Universal...")
            
            # Inicializar sistema sensorial
            if self.sistema_sensorial:
                self.sistema_sensorial.iniciar()
                self.estado["sistemas_activos"].append("sensorial")
                self.logger.info("Sistema sensorial iniciado")
                
                # Mensaje de bienvenida por voz inmediato
                self.sistema_sensorial.decir(
                    "¡Hola! Soy Aria, tu asistente de inteligencia artificial. "
                    "Estoy aquí para ayudarte. Mis sistemas están completamente operativos "
                    "y puedo escucharte a través del micrófono y hablarte por la bocina. "
                    "¿En qué puedo ayudarte hoy?"
                )
            
            # Inicializar conexiones con privilegios de administrador
            for nombre, conexion in self.conexiones.items():
                try:
                    if conexion.inicializar():
                        self.logger.info(f"Conexión {nombre} inicializada")
                        self.estado["conexiones_activas"].append(nombre)
                    else:
                        self.logger.warning(f"No se pudo inicializar conexión {nombre}")
                except Exception as e:
                    self.logger.error(f"Error inicializando conexión {nombre}: {str(e)}")
            
            # Verificar permisos de administrador
            if self.modo_admin:
                self.logger.info("Modo administrador activado - Acceso total concedido")
                if self.sistema_sensorial:
                    self.sistema_sensorial.decir(
                        "Modo administrador activado. Tengo acceso total a todos los sistemas."
                    )
            
            self.logger.info("Sistema Aria Universal inicializado correctamente")
            self.estado["estado"] = "activo"
            return True
        except Exception as e:
            self.logger.error(f"Error inicializando sistema: {str(e)}")
            return False

    def procesar_solicitud(self, tipo: str, datos: Dict[str, Any], prioridad_admin: bool = False) -> Dict[str, Any]:
        """Procesa una solicitud con opción de prioridad administrativa."""
        try:
            inicio = time.time()
            
            # Crear tarea con prioridad administrativa si corresponde
            prioridad = PrioridadTarea.CRITICA if (self.modo_admin and prioridad_admin) else PrioridadTarea.ALTA
            
            tarea = Tarea(
                id=f"TAREA-{int(time.time())}",
                funcion=self._procesar_segun_tipo,
                argumentos={"tipo": tipo, "datos": datos},
                prioridad=prioridad
            )
            
            # Registrar tarea en estado
            self.estado["tareas_pendientes"].append({
                "id": tarea.id,
                "tipo": tipo,
                "prioridad": prioridad.name,
                "inicio": datetime.now().isoformat()
            })
            
            # Agregar tarea al gestor
            self.gestor_tareas.agregar_tarea(tarea)
            
            # Esperar resultado
            while not tarea.completada and not tarea.error:
                time.sleep(0.1)
            
            tiempo_proceso = time.time() - inicio
            self.logger.info(f"Solicitud procesada en {tiempo_proceso:.2f}s")
            
            # Notificar resultado por voz si es relevante
            if self.sistema_sensorial and (tarea.error or self.modo_admin):
                mensaje = "Error en la tarea" if tarea.error else "Tarea completada exitosamente"
                self.sistema_sensorial.decir(mensaje)

            return {
                "resultado": tarea.resultado if not tarea.error else None,
                "error": tarea.error,
                "tiempo_proceso": tiempo_proceso,
                "modo_admin": self.modo_admin,
                "prioridad": prioridad.name
            }
        except Exception as e:
            self.logger.error(f"Error procesando solicitud: {str(e)}")
            return {"error": str(e)}

    def _procesar_segun_tipo(self, tipo: str, datos: Dict[str, Any]) -> Any:
        """Procesa una solicitud según su tipo."""
        if tipo == "administrativo":
            from dominios_especializados.administrativo.GestorAdministrativo import TipoDocumento, NivelPrioridad
            
            # Convertir string a enum
            tipo_doc = datos.get("tipo_documento", "informe")
            if isinstance(tipo_doc, str):
                tipo_doc = getattr(TipoDocumento, tipo_doc.upper(), TipoDocumento.INFORME)
            
            prioridad = datos.get("prioridad", "media")
            if isinstance(prioridad, str):
                prioridad = getattr(NivelPrioridad, prioridad.upper(), NivelPrioridad.MEDIA)
            
            return self.gestor_administrativo.generar_documento(
                tipo=tipo_doc,
                contenido=datos,
                prioridad=prioridad
            )
        elif tipo == "militar":
            from dominios_especializados.militar.InteligenciaMilitar import TipoAmenaza, NivelSeguridad
            
            # Convertir string a enum
            tipo_amenaza = datos.get("tipo_amenaza", "cibernetica")
            if isinstance(tipo_amenaza, str):
                # Mapear nombres especiales
                if tipo_amenaza == "hibrida":
                    tipo_amenaza = TipoAmenaza.HIBRIDA
                else:
                    tipo_amenaza = getattr(TipoAmenaza, tipo_amenaza.upper(), TipoAmenaza.CIBERNETICA)
            
            return self.inteligencia_militar.analizar_amenaza(
                datos=datos,
                tipo=tipo_amenaza
            )
        else:
            return self.sistema_adaptativo.procesar_solicitud_adaptativa({
                "tipo": tipo,
                "datos": datos
            })

    def ejecutar_comando_admin(self, comando: str) -> Dict[str, Any]:
        """Ejecuta un comando administrativo con privilegios totales."""
        if not self.modo_admin:
            return {"error": "Acceso denegado - Se requiere modo administrador"}
            
        try:
            self.logger.debug(f"Ejecutando comando administrativo: {comando}")
            
            if comando.startswith("sistema:"):
                # Comandos de sistema
                if comando == "sistema:estado":
                    return {"resultado": self.obtener_estado_completo()}
                elif comando == "sistema:reiniciar":
                    self.reiniciar()
                    return {"resultado": "Sistema reiniciado"}
                    
            elif comando.startswith("sensorial:"):
                # Comandos del sistema sensorial
                if not self.sistema_sensorial:
                    return {"error": "Sistema sensorial no disponible"}
                    
                if comando == "sensorial:iniciar":
                    self.sistema_sensorial.iniciar()
                    return {"resultado": "Sistema sensorial iniciado"}
                elif comando == "sensorial:detener":
                    self.sistema_sensorial.detener()
                    return {"resultado": "Sistema sensorial detenido"}
                    
            elif comando.startswith("red:"):
                # Comandos de red y conexiones
                partes = comando.split(":")
                if len(partes) >= 3:
                    conexion = partes[1]
                    accion = partes[2]
                    if conexion in self.conexiones:
                        if accion == "reconectar":
                            self.conexiones[conexion].cerrar()
                            self.conexiones[conexion].inicializar()
                            return {"resultado": f"Conexión {conexion} reconectada"}
                            
            return {"error": "Comando no reconocido"}
            
        except Exception as e:
            self.logger.error(f"Error ejecutando comando administrativo: {str(e)}")
            return {"error": str(e)}

    def reiniciar(self):
        """Reinicia todos los sistemas con privilegios de administrador."""
        if not self.modo_admin:
            self.logger.warning("Intento de reinicio sin privilegios de administrador")
            return
            
        self.logger.info("Reiniciando sistema con privilegios de administrador...")
        
        # Detener sistemas
        self.detener()
        
        # Limpiar estado
        self.estado = {
            "inicio_sesion": datetime.now(),
            "modo_admin": self.modo_admin,
            "sistemas_activos": [],
            "conexiones_activas": [],
            "tareas_pendientes": [],
            "estado_sensorial": None
        }
        
        # Reiniciar sistemas
        self.inicializar()

    def obtener_estado_completo(self) -> Dict[str, Any]:
        """Obtiene el estado completo del sistema."""
        estado = {
            "sistema": self.estado,
            "modo_admin": self.modo_admin,
            "permisos": self.permisos_admin,
            "timestamp": datetime.now().isoformat(),
            "sistemas": {
                "cerebro": self.cerebro is not None,
                "gestor_tareas": self.gestor_tareas is not None,
                "adaptativo": self.sistema_adaptativo is not None,
                "personalidad": self.personalidad is not None,
                "sensorial": self.sistema_sensorial is not None
            },
            "conexiones": {
                nombre: conexion.esta_activa() 
                for nombre, conexion in self.conexiones.items()
            }
        }
        
        # Agregar estado sensorial si está disponible
        if self.sistema_sensorial:
            estado["sensorial"] = self.sistema_sensorial.obtener_estado_completo()
            
        return estado

    def _modo_voz_continua(self):
        """Modo de comunicación continua por voz."""
        self.logger.info("Iniciando modo de voz continua")
        
        # Variables de control
        modo_respuesta = "voz"  # "voz" o "escrito"
        activo = True
        
        try:
            while activo:
                # Escuchar comando de voz
                if self.sistema_sensorial:
                    # Simular escucha continua (en implementación real sería un callback)
                    print("🎤 Escuchando... (Presiona Enter para simular comando de voz)")
                    comando_simulado = input("Simular comando de voz: ").strip()
                    
                    if not comando_simulado:
                        continue
                    
                    # Procesar comando
                    comando_lower = comando_simulado.lower()
                    
                    # Comandos especiales de control
                    if comando_lower in ['salir', 'terminar', 'apagar']:
                        self.sistema_sensorial.decir("Entendido, cerrando sistema. Hasta luego.")
                        activo = False
                        break
                    elif 'por escrito' in comando_lower:
                        modo_respuesta = "escrito"
                        self.sistema_sensorial.decir("Perfecto, ahora responderé por escrito.")
                        continue
                    elif 'por voz' in comando_lower:
                        modo_respuesta = "voz"
                        self.sistema_sensorial.decir("Perfecto, ahora responderé por voz.")
                        continue
                    
                    # Procesar comando normal
                    respuesta = self._procesar_comando_voz(comando_simulado)
                    
                    # Responder según el modo configurado
                    if modo_respuesta == "voz":
                        self.sistema_sensorial.decir(respuesta)
                    else:
                        print(f"🤖 ARIA (escrito): {respuesta}")
                        
                else:
                    print("Sistema sensorial no disponible")
                    break
                    
        except KeyboardInterrupt:
            print("\n⏹️ Interrumpido por usuario")
            if self.sistema_sensorial:
                self.sistema_sensorial.decir("Interrumpido. Cerrando sistema.")
        except Exception as e:
            self.logger.error(f"Error en modo voz continua: {e}")
            if self.sistema_sensorial:
                self.sistema_sensorial.decir("Ha ocurrido un error. Cerrando sistema.")

    def _procesar_comando_voz(self, comando: str) -> str:
        """Procesa un comando de voz y retorna la respuesta."""
        try:
            comando_lower = comando.lower()
            
            # Comandos administrativos
            if 'estado del sistema' in comando_lower or 'cómo estás' in comando_lower:
                estado = self.obtener_estado_completo()
                sistemas_activos = len(estado['sistemas'])
                return f"Estoy funcionando correctamente. Tengo {sistemas_activos} sistemas activos y acceso administrativo total."
            
            elif 'qué hora es' in comando_lower:
                hora_actual = datetime.now().strftime("%H:%M")
                return f"Son las {hora_actual}."
            
            elif 'reiniciar sistema' in comando_lower:
                if self.modo_admin:
                    self.reiniciar()
                    return "Sistema reiniciado correctamente."
                else:
                    return "No tengo permisos para reiniciar el sistema."
            
            elif 'conexiones' in comando_lower:
                conexiones_activas = len(self.estado.get('conexiones_activas', []))
                return f"Tengo {conexiones_activas} conexiones activas."
            
            # Comandos de procesamiento cognitivo
            elif 'analizar' in comando_lower or 'procesar' in comando_lower:
                if self.sistema_adaptativo:
                    resultado = self.sistema_adaptativo.procesar_solicitud_adaptativa({
                        "tipo": "comando_voz",
                        "contenido": comando,
                        "timestamp": datetime.now().isoformat()
                    })
                    return resultado.get("respuesta", "Análisis completado.")
                else:
                    return "Sistema de análisis no disponible."
            
            # Comandos de personalidad
            elif 'cómo te sientes' in comando_lower or 'estado emocional' in comando_lower:
                if self.personalidad:
                    estado_emocional = self.personalidad.obtener_estado_emocional()
                    return f"Mi estado emocional es {estado_emocional.get('estado_principal', 'neutral')}."
                else:
                    return "Sistema de personalidad no disponible."
            
            # Comandos generales
            elif 'hola' in comando_lower or 'buenos días' in comando_lower or 'buenas tardes' in comando_lower:
                return "¡Hola! Soy Aria, tu asistente de inteligencia artificial. ¿En qué puedo ayudarte?"
            
            elif 'gracias' in comando_lower:
                return "De nada, es un placer ayudarte."
            
            elif 'ayuda' in comando_lower or 'qué puedes hacer' in comando_lower:
                return ("Puedo ayudarte con análisis de datos, gestión administrativa, "
                       "procesamiento de información, control de sistemas y mucho más. "
                       "Solo háblame naturalmente.")
            
            else:
                # Comando no reconocido, intentar procesamiento adaptativo
                if self.sistema_adaptativo:
                    resultado = self.sistema_adaptativo.procesar_solicitud_adaptativa({
                        "tipo": "comando_general",
                        "contenido": comando,
                        "timestamp": datetime.now().isoformat()
                    })
                    return resultado.get("respuesta", "He procesado tu solicitud.")
                else:
                    return "No he entendido completamente tu solicitud, pero estoy aquí para ayudarte."
                    
        except Exception as e:
            self.logger.error(f"Error procesando comando de voz: {e}")
            return "Ha ocurrido un error procesando tu solicitud."

    def detener(self):
        """Detiene el sistema con gestión de recursos."""
        self.logger.info("Deteniendo Sistema Aria Universal...")
        
        # Mensaje de despedida por voz
        if self.sistema_sensorial:
            self.sistema_sensorial.decir(
                "Iniciando proceso de apagado. Gracias por tu trabajo."
            )
            self.sistema_sensorial.detener()
        
        # Detener sistemas principales
        if self.sistema_adaptativo:
            self.sistema_adaptativo.detener()
        
        # Cerrar conexiones ordenadamente
        for nombre, conexion in self.conexiones.items():
            try:
                if conexion.cerrar():
                    self.logger.info(f"Conexión {nombre} cerrada")
                else:
                    self.logger.warning(f"Error cerrando conexión {nombre}")
            except Exception as e:
                self.logger.error(f"Error cerrando conexión {nombre}: {str(e)}")
        
        # Actualizar estado
        self.estado["estado"] = "detenido"
        self.estado["fin_sesion"] = datetime.now().isoformat()
        
        self.logger.info("Sistema detenido correctamente")
        
        # Cerrar logger
        logging.shutdown()

def main():
    """Función principal con modo de comunicación por voz."""
    # Crear sistema con acceso de administrador
    sistema = AriaUniversal(modo_admin=True)
    
    if sistema.inicializar():
        try:
            print("\n" + "="*60)
            print("🤖 ARIA UNIVERSAL - MODO ADMINISTRADOR")
            print("="*60)
            print("\nSistema iniciado con acceso total.")
            print("Capacidades disponibles:")
            print("  - Control administrativo completo")
            print("  - Sistema sensorial integrado (VOZ PRINCIPAL)")
            print("  - Procesamiento cognitivo avanzado")
            print("  - Gestión de conexiones")
            print("  - Micrófono siempre activo")
            print("  - Respuestas por voz prioritarias")
            
            # Configurar modo de comunicación por voz
            if sistema.sistema_sensorial:
                print("\n🎤 MODO VOZ ACTIVADO")
                print("- Habla naturalmente, Aria te escucha siempre")
                print("- Aria responderá por voz principalmente")
                print("- Di 'por escrito' si quieres respuesta escrita")
                print("- Di 'salir' para terminar")
                
                # Mensaje de bienvenida por voz
                sistema.sistema_sensorial.decir(
                    "Hola, soy Aria. Estoy en modo administrador con acceso total. "
                    "Mi micrófono está siempre activo y te responderé principalmente por voz. "
                    "Si quieres que responda por escrito, solo dímelo."
                )
                
                # Modo de escucha continua
                sistema._modo_voz_continua()
            else:
                print("\n⚠️ Sistema sensorial no disponible, usando modo texto")
                print("\nComandos disponibles:")
                print("  - sistema:estado    - Ver estado completo")
                print("  - sistema:reiniciar - Reiniciar sistema")
                print("  - sensorial:iniciar - Iniciar sistema sensorial")
                print("  - sensorial:detener - Detener sistema sensorial")
                print("  - red:<conexion>:reconectar - Reconectar servicio")
                
                # Mantener sistema activo en modo texto
                while True:
                    comando = input("\nComando (o 'salir' para terminar): ").strip()
                    
                    if comando.lower() == 'salir':
                        break
                        
                    resultado = sistema.ejecutar_comando_admin(comando)
                    print(f"\nResultado: {resultado}")
            
        finally:
            sistema.detener()

if __name__ == "__main__":
    main()
