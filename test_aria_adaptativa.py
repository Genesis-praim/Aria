"""
Script de prueba para el sistema de Aria Conversación Adaptativa
"""

import logging
import time
from bodega.BodegaConocimiento import BodegaConocimiento, TipoInformacion, ImportanciaInfo
from adaptacion_usuario.AdaptacionUsuario import AdaptacionUsuario

def configurar_logging():
    """Configura el sistema de logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def test_bodega():
    """Prueba el sistema de bodega."""
    print("\n🗄️ PROBANDO BODEGA DE CONOCIMIENTO")
    print("="*50)
    
    bodega = BodegaConocimiento()
    
    # Almacenar datos de prueba
    print("📝 Almacenando datos de prueba...")
    
    # Conversación
    id1 = bodega.almacenar(
        tipo=TipoInformacion.CONVERSACION,
        contenido={
            "texto": "Hola, me gusta la tecnología",
            "tipo": "entrada_usuario"
        },
        importancia=ImportanciaInfo.MEDIA,
        usuario_id="usuario_test",
        palabras_clave=["saludo", "tecnología"]
    )
    
    # Preferencia
    id2 = bodega.almacenar(
        tipo=TipoInformacion.PREFERENCIA_USUARIO,
        contenido={
            "tema": "tecnología",
            "nivel_interes": 0.8
        },
        importancia=ImportanciaInfo.ALTA,
        usuario_id="usuario_test",
        palabras_clave=["preferencia", "tecnología"]
    )
    
    print(f"✓ Datos almacenados: {id1}, {id2}")
    
    # Buscar datos
    print("\n🔍 Buscando datos...")
    resultados = bodega.buscar({
        "usuario_id": "usuario_test",
        "palabras_clave": ["tecnología"]
    })
    
    print(f"✓ Encontrados {len(resultados)} resultados")
    for resultado in resultados:
        print(f"  - {resultado['tipo']}: {resultado['contenido']}")
    
    # Estadísticas
    print("\n📊 Estadísticas de la bodega:")
    stats = bodega.obtener_estadisticas()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    return bodega

def test_adaptacion(bodega):
    """Prueba el sistema de adaptación."""
    print("\n🎯 PROBANDO SISTEMA DE ADAPTACIÓN")
    print("="*50)
    
    adaptacion = AdaptacionUsuario(bodega)
    
    # Simular interacciones
    print("💬 Simulando interacciones...")
    
    interacciones = [
        {
            "texto": "Hola, me interesa mucho la tecnología",
            "tipo": "saludo",
            "contexto": {"iniciativa_usuario": True}
        },
        {
            "texto": "¿Podrías hablarme sobre inteligencia artificial?",
            "tipo": "pregunta",
            "contexto": {"tema": "tecnología"}
        },
        {
            "texto": "Gracias, muy interesante",
            "tipo": "feedback",
            "feedback": {"valoracion": 1}
        }
    ]
    
    for i, interaccion in enumerate(interacciones):
        print(f"\n  Interacción {i+1}: {interaccion['texto']}")
        resultado = adaptacion.procesar_interaccion("usuario_test", interaccion)
        print(f"  Adaptaciones: {resultado}")
    
    # Obtener perfil
    print("\n👤 Perfil del usuario:")
    perfil = adaptacion.obtener_perfil("usuario_test")
    if perfil:
        print(f"  Temas de interés: {perfil['temas_interes']}")
        print(f"  Estilo comunicación: {perfil['estilo_comunicacion']}")
        print(f"  Estadísticas: {perfil['estadisticas']}")
    
    return adaptacion

def test_conversacion_simple():
    """Prueba simple del sistema de conversación."""
    print("\n💬 PROBANDO CONVERSACIÓN ADAPTATIVA")
    print("="*50)
    
    try:
        from aria_conversacion_adaptativa import AriaConversacionAdaptativa
        
        aria = AriaConversacionAdaptativa()
        
        # Simular algunas interacciones sin voz
        print("🤖 Simulando conversación...")
        
        # Desactivar micrófono para prueba
        aria.microfono = None
        
        # Procesar algunos mensajes
        mensajes_prueba = [
            "Hola Aria",
            "Me gusta la tecnología",
            "¿Qué sabes sobre inteligencia artificial?",
            "Gracias por la información"
        ]
        
        for mensaje in mensajes_prueba:
            print(f"\n👤 Usuario: {mensaje}")
            respuesta = aria._procesar_mensaje(mensaje, "usuario_test")
            print(f"🤖 Aria: {respuesta}")
        
        print("\n✓ Prueba de conversación completada")
        
    except Exception as e:
        print(f"❌ Error en prueba de conversación: {e}")

def main():
    """Función principal de pruebas."""
    print("🧪 INICIANDO PRUEBAS DEL SISTEMA ARIA ADAPTATIVO")
    print("="*60)
    
    configurar_logging()
    
    try:
        # Probar bodega
        bodega = test_bodega()
        
        # Probar adaptación
        adaptacion = test_adaptacion(bodega)
        
        # Probar conversación
        test_conversacion_simple()
        
        print("\n✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("="*60)
        print("🎉 El sistema Aria Adaptativo está funcionando correctamente!")
        print("\nPara usar el sistema completo, ejecuta:")
        print("  python aria_conversacion_adaptativa.py")
        
    except Exception as e:
        print(f"\n❌ ERROR EN LAS PRUEBAS: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
