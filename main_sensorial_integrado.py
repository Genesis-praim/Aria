"""
Sistema principal de integración sensorial de Aria
Coordina los sistemas de oído, voz y visión
"""

import logging
import time
import threading
from typing import Dict, Any
from interfaz_sensorial.integrador_sensorial import IntegradorSensorial
from bodega.BodegaConocimiento import BodegaConocimiento, TipoInformacion, ImportanciaInfo
from adaptacion_usuario.AdaptacionUsuario import AdaptacionUsuario

class SistemaAriaIntegrado:
    """Sistema principal de Aria con integración sensorial completa."""
    
    def __init__(self):
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("SistemaAriaIntegrado")
        
        # Inicializar componentes
        self.bodega = BodegaConocimiento()
        self.adaptacion = AdaptacionUsuario(self.bodega)
        self.integrador = IntegradorSensorial()
        
        # Estado del sistema
        self.activo = False
        self.usuario_actual = None
        self.contexto_actual = {
            "modo": "normal",  # normal, atento, concentrado
            "ultima_interaccion": None,
            "tema_actual": None,
            "emociones_detectadas": []
        }
        
        # Registrar callbacks
        self._registrar_callbacks()
    
    def _registrar_callbacks(self):
        """Registra callbacks para procesar eventos sensoriales."""
        self.integrador.registrar_callback("audio", self._procesar_audio)
        self.integrador.registrar_callback("visual", self._procesar_visual)
        self.integrador.registrar_callback("integrado", self._procesar_integrado)
    
    def _procesar_audio(self, datos: Dict[str, Any]):
        """
        Procesa eventos de audio.
        
        Args:
            datos: Datos del evento de audio
        """
        if not datos.get("texto"):
            return
            
        try:
            # Actualizar contexto
            self.contexto_actual["ultima_interaccion"] = time.time()
            
            # Procesar con adaptación de usuario
            if self.usuario_actual:
                self.adaptacion.procesar_interaccion(
                    self.usuario_actual,
                    {
                        "tipo": "audio",
                        "texto": datos["texto"],
                        "contexto": self.contexto_actual
                    }
                )
            
            # Almacenar en bodega
            self.bodega.almacenar(
                tipo=TipoInformacion.CONVERSACION,
                contenido={
                    "texto": datos["texto"],
                    "tipo": "entrada_usuario",
                    "timestamp": datos["timestamp"]
                },
                importancia=ImportanciaInfo.MEDIA,
                usuario_id=self.usuario_actual,
                palabras_clave=["audio", "conversacion"]
            )
            
            # Generar respuesta si es necesario
            self._generar_respuesta(datos["texto"])
            
        except Exception as e:
            self.logger.error(f"Error procesando audio: {e}")
    
    def _procesar_visual(self, datos: Dict[str, Any]):
        """
        Procesa eventos visuales.
        
        Args:
            datos: Datos del evento visual
        """
        try:
            # Procesar detección de rostros
            if "rostros" in datos:
                rostros = datos["rostros"]
                if rostros["rostros_detectados"] > 0:
                    self._ajustar_modo_atencion("atento")
                    
                    # Almacenar en bodega
                    self.bodega.almacenar(
                        tipo=TipoInformacion.EXPERIENCIA,
                        contenido={
                            "tipo": "deteccion_rostro",
                            "rostros": rostros["rostros"],
                            "timestamp": datos["timestamp"]
                        },
                        importancia=ImportanciaInfo.ALTA,
                        usuario_id=self.usuario_actual,
                        palabras_clave=["visual", "rostro"]
                    )
            
            # Procesar detección de movimiento
            if "movimiento" in datos:
                movimiento = datos["movimiento"]
                if movimiento["movimiento_detectado"]:
                    if movimiento["intensidad"] > 0.5:  # Movimiento significativo
                        self._ajustar_modo_atencion("atento")
                    
                    # Almacenar en bodega
                    self.bodega.almacenar(
                        tipo=TipoInformacion.EXPERIENCIA,
                        contenido={
                            "tipo": "deteccion_movimiento",
                            "intensidad": movimiento["intensidad"],
                            "areas": movimiento["areas_movimiento"],
                            "timestamp": datos["timestamp"]
                        },
                        importancia=ImportanciaInfo.MEDIA,
                        usuario_id=self.usuario_actual,
                        palabras_clave=["visual", "movimiento"]
                    )
            
        except Exception as e:
            self.logger.error(f"Error procesando visual: {e}")
    
    def _procesar_integrado(self, datos: Dict[str, Any]):
        """
        Procesa eventos integrados.
        
        Args:
            datos: Datos integrados de audio y video
        """
        try:
            analisis = datos.get("analisis", {})
            
            # Procesar interacción cara a cara
            if analisis.get("interaccion_cara_a_cara"):
                self._ajustar_modo_atencion("concentrado")
                
                # Almacenar experiencia
                self.bodega.almacenar(
                    tipo=TipoInformacion.EXPERIENCIA,
                    contenido={
                        "tipo": "interaccion_cara_a_cara",
                        "timestamp": datos["timestamp"],
                        "analisis": analisis
                    },
                    importancia=ImportanciaInfo.ALTA,
                    usuario_id=self.usuario_actual,
                    palabras_clave=["interaccion", "cara_a_cara"]
                )
            
            # Procesar nivel de atención
            if "atencion_visual" in analisis:
                if analisis["atencion_visual"] == "alta":
                    self._ajustar_modo_atencion("atento")
            
            # Actualizar adaptación de usuario
            if self.usuario_actual:
                self.adaptacion.procesar_interaccion(
                    self.usuario_actual,
                    {
                        "tipo": "integrado",
                        "datos": datos,
                        "contexto": self.contexto_actual
                    }
                )
            
        except Exception as e:
            self.logger.error(f"Error procesando datos integrados: {e}")
    
    def _ajustar_modo_atencion(self, modo: str):
        """
        Ajusta el modo de atención del sistema.
        
        Args:
            modo: Nuevo modo de atención
        """
        if modo != self.contexto_actual["modo"]:
            self.contexto_actual["modo"] = modo
            self.integrador.configurar_modo_atencion(
                "focalizado" if modo == "concentrado" else
                "activo" if modo == "atento" else
                "pasivo"
            )
            
            self.logger.info(f"Modo de atención ajustado a: {modo}")
    
    def _generar_respuesta(self, texto_entrada: str):
        """
        Genera una respuesta basada en la entrada del usuario.
        
        Args:
            texto_entrada: Texto de entrada del usuario
        """
        try:
            # Obtener adaptaciones recomendadas
            if self.usuario_actual:
                adaptaciones = self.adaptacion.obtener_perfil(self.usuario_actual)
                
                # Ajustar respuesta según preferencias
                if adaptaciones:
                    estilo = adaptaciones.get("estilo_comunicacion", {})
                    
                    # Generar respuesta adaptada
                    respuesta = self._adaptar_respuesta(
                        texto_entrada,
                        formalidad=estilo.get("formalidad", 0.5),
                        verbosidad=estilo.get("verbosidad", 0.5)
                    )
                    
                    # Reproducir respuesta
                    self.integrador.hablar(respuesta)
                    
        except Exception as e:
            self.logger.error(f"Error generando respuesta: {e}")
    
    def _adaptar_respuesta(self, texto_entrada: str, formalidad: float, verbosidad: float) -> str:
        """
        Adapta la respuesta según preferencias del usuario.
        
        Args:
            texto_entrada: Texto de entrada
            formalidad: Nivel de formalidad (0-1)
            verbosidad: Nivel de verbosidad (0-1)
            
        Returns:
            Respuesta adaptada
        """
        # Implementar lógica de adaptación de respuesta
        # Por ahora, respuesta simple
        return f"He entendido tu mensaje: {texto_entrada}"
    
    def iniciar(self, usuario_id: str = None):
        """
        Inicia el sistema integrado.
        
        Args:
            usuario_id: ID del usuario (opcional)
        """
        if self.activo:
            self.logger.warning("El sistema ya está activo")
            return
        
        try:
            self.activo = True
            self.usuario_actual = usuario_id
            
            # Iniciar integrador sensorial
            self.integrador.iniciar()
            
            # Mensaje de bienvenida
            if usuario_id:
                perfil = self.adaptacion.obtener_perfil(usuario_id)
                if perfil:
                    nombre = perfil.get("nombre", "usuario")
                    self.integrador.hablar(f"Bienvenido de nuevo, {nombre}")
                else:
                    self.integrador.hablar("Bienvenido al sistema Aria")
            else:
                self.integrador.hablar("Sistema Aria iniciado")
            
            self.logger.info("Sistema integrado iniciado")
            
        except Exception as e:
            self.logger.error(f"Error iniciando sistema: {e}")
            self.detener()
    
    def detener(self):
        """Detiene el sistema integrado."""
        if not self.activo:
            return
            
        try:
            # Mensaje de despedida
            self.integrador.hablar("Deteniendo sistema Aria")
            
            # Detener integrador
            self.integrador.detener()
            
            self.activo = False
            self.usuario_actual = None
            
            self.logger.info("Sistema integrado detenido")
            
        except Exception as e:
            self.logger.error(f"Error deteniendo sistema: {e}")
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas del sistema.
        
        Returns:
            Dict con estadísticas completas
        """
        return {
            "estado": "activo" if self.activo else "inactivo",
            "usuario_actual": self.usuario_actual,
            "contexto": self.contexto_actual,
            "integrador": self.integrador.obtener_estadisticas(),
            "bodega": self.bodega.obtener_estadisticas()
        }

def main():
    """Función principal."""
    try:
        # Crear y configurar sistema
        sistema = SistemaAriaIntegrado()
        
        # Iniciar sistema
        sistema.iniciar()
        
        # Mantener sistema activo
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nDeteniendo sistema...")
        finally:
            sistema.detener()
            
    except Exception as e:
        logging.error(f"Error en sistema principal: {e}")

if __name__ == "__main__":
    main()
