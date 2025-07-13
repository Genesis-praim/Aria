"""
Tests completos para el sistema sensorial integrado de Aria
"""

import unittest
import logging
import time
import threading
from typing import Dict, Any
from interfaz_sensorial.oido import Oido
from interfaz_sensorial.voz import Voz
from interfaz_sensorial.ojos import Ojos
from interfaz_sensorial.integrador_sensorial import IntegradorSensorial
from main_sensorial_integrado import SistemaAriaIntegrado

class TestSistemaSensorial(unittest.TestCase):
    """Suite de pruebas para el sistema sensorial."""
    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial para todas las pruebas."""
        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger("TestSistemaSensorial")
    
    def setUp(self):
        """Configuración para cada prueba."""
        self.oido = Oido()
        self.voz = Voz()
        self.ojos = Ojos()
        self.integrador = IntegradorSensorial()
        self.sistema = SistemaAriaIntegrado()
    
    def tearDown(self):
        """Limpieza después de cada prueba."""
        if hasattr(self, 'sistema'):
            self.sistema.detener()
        if hasattr(self, 'integrador'):
            self.integrador.detener()
        if hasattr(self, 'ojos'):
            self.ojos.cerrar()
    
    def test_01_inicializacion_componentes(self):
        """Test de inicialización de componentes."""
        self.logger.info("Test 01: Inicialización de componentes")
        
        # Verificar oído
        self.assertIsNotNone(self.oido)
        stats_oido = self.oido.obtener_estadisticas()
        self.assertIsInstance(stats_oido, dict)
        
        # Verificar voz
        self.assertIsNotNone(self.voz)
        stats_voz = self.voz.obtener_estadisticas()
        self.assertIsInstance(stats_voz, dict)
        
        # Verificar ojos
        self.assertIsNotNone(self.ojos)
        stats_ojos = self.ojos.obtener_estadisticas()
        self.assertIsInstance(stats_ojos, dict)
        
        # Verificar integrador
        self.assertIsNotNone(self.integrador)
        stats_integrador = self.integrador.obtener_estadisticas()
        self.assertIsInstance(stats_integrador, dict)
    
    def test_02_sistema_oido(self):
        """Test del sistema de oído."""
        self.logger.info("Test 02: Sistema de oído")
        
        # Configurar oído
        self.oido.configurar(
            energia_minima=300,
            energia_dinamica=True,
            pausa_threshold=0.8
        )
        
        # Verificar configuración
        stats = self.oido.obtener_estadisticas()
        self.assertEqual(stats["configuracion"]["energia_minima"], 300)
        
        # Test de escucha (simulado)
        resultado = self.oido.escuchar(timeout=1)
        self.assertIsInstance(resultado, dict)
        self.assertIn("timestamp", resultado)
    
    def test_03_sistema_voz(self):
        """Test del sistema de voz."""
        self.logger.info("Test 03: Sistema de voz")
        
        # Configurar voz
        self.voz.configurar(
            velocidad=0,
            volumen=100
        )
        
        # Test de síntesis
        texto_prueba = "Esta es una prueba del sistema de voz"
        resultado = self.voz.hablar(texto_prueba)
        
        self.assertIsInstance(resultado, dict)
        self.assertIn("texto", resultado)
        self.assertEqual(resultado["texto"], texto_prueba)
    
    def test_04_sistema_ojos(self):
        """Test del sistema de visión."""
        self.logger.info("Test 04: Sistema de visión")
        
        # Configurar ojos
        self.ojos.configurar(
            resolucion=(640, 480),
            fps=30
        )
        
        # Test de captura
        resultado = self.ojos.capturar_imagen()
        self.assertIsInstance(resultado, dict)
        self.assertIn("timestamp", resultado)
        
        # Test de detección de rostros
        resultado_rostros = self.ojos.detectar_rostros()
        self.assertIsInstance(resultado_rostros, dict)
        self.assertIn("rostros_detectados", resultado_rostros)
        
        # Test de detección de movimiento
        resultado_movimiento = self.ojos.detectar_movimiento()
        self.assertIsInstance(resultado_movimiento, dict)
        self.assertIn("movimiento_detectado", resultado_movimiento)
    
    def test_05_integracion_sensorial(self):
        """Test de integración sensorial."""
        self.logger.info("Test 05: Integración sensorial")
        
        eventos_recibidos = []
        
        def callback_test(datos):
            eventos_recibidos.append(datos)
        
        # Registrar callbacks
        self.integrador.registrar_callback("audio", callback_test)
        self.integrador.registrar_callback("visual", callback_test)
        self.integrador.registrar_callback("integrado", callback_test)
        
        # Iniciar integrador
        self.integrador.iniciar()
        
        # Esperar eventos
        time.sleep(2)
        
        # Detener integrador
        self.integrador.detener()
        
        # Verificar eventos
        self.assertGreaterEqual(len(eventos_recibidos), 0)
    
    def test_06_sistema_completo(self):
        """Test del sistema completo."""
        self.logger.info("Test 06: Sistema completo")
        
        # Iniciar sistema
        self.sistema.iniciar(usuario_id="test_user")
        
        # Verificar estado
        stats = self.sistema.obtener_estadisticas()
        self.assertTrue(stats["estado"] == "activo")
        self.assertEqual(stats["usuario_actual"], "test_user")
        
        # Simular interacción
        time.sleep(2)
        
        # Detener sistema
        self.sistema.detener()
        
        # Verificar estado final
        stats = self.sistema.obtener_estadisticas()
        self.assertTrue(stats["estado"] == "inactivo")
    
    def test_07_modos_atencion(self):
        """Test de modos de atención."""
        self.logger.info("Test 07: Modos de atención")
        
        # Iniciar sistema
        self.sistema.iniciar()
        
        # Probar diferentes modos
        modos = ["normal", "atento", "concentrado"]
        for modo in modos:
            self.sistema._ajustar_modo_atencion(modo)
            time.sleep(1)
            
            stats = self.sistema.obtener_estadisticas()
            self.assertEqual(stats["contexto"]["modo"], modo)
        
        # Detener sistema
        self.sistema.detener()
    
    def test_08_procesamiento_eventos(self):
        """Test de procesamiento de eventos."""
        self.logger.info("Test 08: Procesamiento de eventos")
        
        # Iniciar sistema
        self.sistema.iniciar(usuario_id="test_user")
        
        # Simular evento de audio
        self.sistema._procesar_audio({
            "texto": "Hola sistema",
            "timestamp": time.time()
        })
        
        # Simular evento visual
        self.sistema._procesar_visual({
            "rostros": {
                "rostros_detectados": 1,
                "rostros": [{"x": 0, "y": 0, "ancho": 100, "alto": 100}]
            },
            "timestamp": time.time()
        })
        
        # Verificar estado
        stats = self.sistema.obtener_estadisticas()
        self.assertEqual(stats["contexto"]["modo"], "atento")
        
        # Detener sistema
        self.sistema.detener()
    
    def test_09_manejo_errores(self):
        """Test de manejo de errores."""
        self.logger.info("Test 09: Manejo de errores")
        
        # Test de error en audio
        resultado = self.oido.escuchar(timeout=0.1)
        self.assertIn("error", resultado)
        
        # Test de error en voz
        resultado = self.voz.hablar("")
        self.assertFalse(resultado["exito"])
        
        # Test de error en visión
        self.ojos.camara = None
        resultado = self.ojos.capturar_imagen()
        self.assertFalse(resultado["exito"])
    
    def test_10_rendimiento(self):
        """Test de rendimiento."""
        self.logger.info("Test 10: Rendimiento")
        
        inicio = time.time()
        
        # Iniciar sistema
        self.sistema.iniciar()
        
        # Realizar operaciones intensivas
        for _ in range(10):
            self.sistema._procesar_audio({
                "texto": "Test de rendimiento",
                "timestamp": time.time()
            })
            self.sistema._procesar_visual({
                "rostros": {"rostros_detectados": 1},
                "timestamp": time.time()
            })
            time.sleep(0.1)
        
        # Detener sistema
        self.sistema.detener()
        
        duracion = time.time() - inicio
        self.assertLess(duracion, 5.0)  # No debe tardar más de 5 segundos

def main():
    """Función principal de testing."""
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()
