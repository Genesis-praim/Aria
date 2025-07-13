"""
Test completo del sistema Aria Conversación Adaptativa
"""
# crealas las acrpetas y archivos ocn su codigo correspondiente
# las import archivo de python
import time
import logging
# las from son carpetas, el . es una carpeta dentro de otra carpeta 
from bodega.BodegaConocimiento import BodegaConocimiento, TipoInformacion, ImportanciaInfo
from adaptacion_usuario.AdaptacionUsuario import AdaptacionUsuario
from personalidad.personalidad.PersonalidadCentral import PersonalidadCentral, EstadoEmocional

def test_bodega_conocimiento():
    """Test del sistema de bodega de conocimiento."""
    print("\n🧠 TESTING BODEGA DE CONOCIMIENTO")
    print("="*50)
    
    bodega = BodegaConocimiento()
    
    # Test 1: Almacenar información
    print("📝 Test 1: Almacenando información...")
    id_conversacion = bodega.almacenar(
        tipo=TipoInformacion.CONVERSACION,
        contenido={"texto": "Hola, me gusta la tecnología", "usuario": "test_user"},
        importancia=ImportanciaInfo.ALTA,
        usuario_id="test_user",
        palabras_clave=["saludo", "tecnología"]
    )
    print(f"✓ Conversación almacenada con ID: {id_conversacion}")
    
    # Test 2: Buscar información
    print("\n🔍 Test 2: Buscando información...")
    resultados = bodega.buscar({
        "tipo": TipoInformacion.CONVERSACION,
        "usuario_id": "test_user",
        "palabras_clave": ["tecnología"]
    })
    print(f"✓ Encontrados {len(resultados)} resultados")
    
    # Test 3: Obtener estadísticas
    print("\n📊 Test 3: Obteniendo estadísticas...")
    stats = bodega.obtener_estadisticas()
    print(f"✓ Total entradas: {stats.get('total_entradas', 0)}")
    print(f"✓ Espacio en disco: {stats.get('espacio_disco', 'N/A')}")
    
    return bodega

def test_adaptacion_usuario(bodega):
    """Test del sistema de adaptación al usuario."""
    print("\n🎯 TESTING ADAPTACIÓN AL USUARIO")
    print("="*50)
    
    adaptacion = AdaptacionUsuario(bodega)
    
    # Test 1: Procesar interacción
    print("💬 Test 1: Procesando interacción...")
    datos_interaccion = {
        "texto": "Me encanta la programación y la inteligencia artificial",
        "tipo": "entrada_usuario",
        "contexto": {
            "tema_actual": "tecnología",
            "hora_dia": 14
        }
    }
    
    adaptaciones = adaptacion.procesar_interaccion("test_user", datos_interaccion)
    print(f"✓ Adaptaciones generadas: {len(adaptaciones)} elementos")
    
    # Test 2: Obtener perfil
    print("\n👤 Test 2: Obteniendo perfil de usuario...")
    perfil = adaptacion.obtener_perfil("test_user")
    if perfil:
        print(f"✓ Perfil obtenido para usuario: {perfil['usuario_id']}")
        print(f"✓ Total interacciones: {perfil['estadisticas']['total_interacciones']}")
        print(f"✓ Temas de interés: {list(perfil['temas_interes'].keys())}")
    else:
        print("⚠ No se encontró perfil")
    
    # Test 3: Procesar múltiples interacciones
    print("\n🔄 Test 3: Procesando múltiples interacciones...")
    interacciones_test = [
        {"texto": "¿Qué opinas sobre machine learning?", "tipo": "pregunta"},
        {"texto": "Gracias por la información", "tipo": "agradecimiento"},
        {"texto": "Me interesa mucho la ciencia de datos", "tipo": "declaración"}
    ]
    
    for i, interaccion in enumerate(interacciones_test):
        adaptacion.procesar_interaccion("test_user", interaccion)
        print(f"✓ Interacción {i+1} procesada")
    
    return adaptacion

def test_personalidad():
    """Test del sistema de personalidad."""
    print("\n🎭 TESTING SISTEMA DE PERSONALIDAD")
    print("="*50)
    
    personalidad = PersonalidadCentral()
    
    # Test 1: Estado inicial
    print("🎯 Test 1: Estado inicial...")
    estado_inicial = personalidad.obtener_estado()
    print(f"✓ Estado emocional: {estado_inicial['estado_emocional']}")
    print(f"✓ Traits disponibles: {len(estado_inicial['traits'])}")
    
    # Test 2: Procesar entrada positiva
    print("\n😊 Test 2: Procesando entrada positiva...")
    entrada_positiva = {
        "texto": "¡Excelente trabajo! Me encanta cómo funciona",
        "contexto": {"tipo_tarea": "analisis"}
    }
    
    resultado = personalidad.procesar_entrada(entrada_positiva)
    print(f"✓ Estado después de entrada positiva: {resultado.get('estado', 'N/A')}")
    
    # Test 3: Procesar entrada negativa
    print("\n😔 Test 3: Procesando entrada negativa...")
    entrada_negativa = {
        "texto": "Esto no funciona bien, hay problemas",
        "contexto": {"situacion_critica": True}
    }
    
    resultado = personalidad.procesar_entrada(entrada_negativa)
    print(f"✓ Estado después de entrada negativa: {resultado.get('estado', 'N/A')}")
    
    # Test 4: Guardar estado
    print("\n💾 Test 4: Guardando estado...")
    guardado = personalidad.guardar_estado()
    print(f"✓ Estado guardado: {'Sí' if guardado else 'No'}")
    
    return personalidad

def test_integracion_completa():
    """Test de integración completa del sistema."""
    print("\n🔗 TESTING INTEGRACIÓN COMPLETA")
    print("="*50)
    
    # Inicializar componentes
    bodega = BodegaConocimiento()
    adaptacion = AdaptacionUsuario(bodega)
    personalidad = PersonalidadCentral()
    
    # Simular conversación completa
    print("💬 Simulando conversación completa...")
    
    conversacion = [
        "Hola, ¿cómo estás?",
        "Me interesa mucho la inteligencia artificial",
        "¿Puedes explicarme sobre machine learning?",
        "Gracias, eso fue muy útil",
        "¿Qué otros temas de tecnología recomiendas?"
    ]
    
    for i, mensaje in enumerate(conversacion):
        print(f"\n👤 Usuario: {mensaje}")
        
        # Procesar con adaptación
        datos_interaccion = {
            "texto": mensaje,
            "tipo": "entrada_usuario",
            "contexto": {"turno": i+1}
        }
        
        adaptaciones = adaptacion.procesar_interaccion("usuario_test", datos_interaccion)
        
        # Procesar con personalidad
        entrada_personalidad = {
            "texto": mensaje,
            "contexto": {"conversacion": True}
        }
        
        estado_personalidad = personalidad.procesar_entrada(entrada_personalidad)
        
        # Almacenar en bodega
        bodega.almacenar(
            tipo=TipoInformacion.CONVERSACION,
            contenido=datos_interaccion,
            importancia=ImportanciaInfo.MEDIA,
            usuario_id="usuario_test",
            palabras_clave=["conversacion", "test"]
        )
        
        print(f"🤖 Estado emocional: {estado_personalidad.get('estado', 'N/A')}")
        
        # Simular respuesta adaptativa
        perfil = adaptacion.obtener_perfil("usuario_test")
        if perfil and perfil["temas_interes"]:
            tema_principal = max(perfil["temas_interes"].items(), key=lambda x: x[1])[0]
            print(f"🎯 Tema de interés detectado: {tema_principal}")
    
    # Resumen final
    print(f"\n📊 RESUMEN FINAL:")
    perfil_final = adaptacion.obtener_perfil("usuario_test")
    if perfil_final:
        print(f"✓ Total interacciones: {perfil_final['estadisticas']['total_interacciones']}")
        print(f"✓ Temas identificados: {len(perfil_final['temas_interes'])}")
        print(f"✓ Nivel de engagement: {perfil_final['estadisticas']['engagement']:.2f}")
    
    stats_bodega = bodega.obtener_estadisticas()
    print(f"✓ Entradas en bodega: {stats_bodega.get('total_entradas', 0)}")
    
    estado_final = personalidad.obtener_estado()
    print(f"✓ Estado emocional final: {estado_final['estado_emocional']}")
    print(f"✓ Total cambios de estado: {estado_final['estadisticas']['cambios_estado']}")

def main():
    """Función principal de testing."""
    print("🚀 INICIANDO TESTS COMPLETOS DE ARIA ADAPTATIVA")
    print("="*70)
    
    # Configurar logging para tests
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Tests individuales
        bodega = test_bodega_conocimiento()
        adaptacion = test_adaptacion_usuario(bodega)
        personalidad = test_personalidad()
        
        # Test de integración
        test_integracion_completa()
        
        print("\n🎉 TODOS LOS TESTS COMPLETADOS EXITOSAMENTE")
        print("="*70)
        print("✅ Sistema Aria Conversación Adaptativa funcionando correctamente")
        
    except Exception as e:
        print(f"\n❌ ERROR EN TESTS: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
