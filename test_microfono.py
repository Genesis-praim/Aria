"""
Prueba del sistema de micrófono para Aria
"""

import speech_recognition as sr
import time

def probar_microfono():
    """Prueba básica del sistema de reconocimiento de voz."""
    print("🎤 PRUEBA DEL SISTEMA DE MICRÓFONO")
    print("="*50)
    
    try:
        # Inicializar reconocedor
        reconocedor = sr.Recognizer()
        
        # Listar micrófonos disponibles
        print("Micrófonos disponibles:")
        for i, mic in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{i}: {mic}")
        
        # Usar micrófono por defecto
        microfono = sr.Microphone()
        
        print("\n📢 Calibrando para ruido ambiente...")
        with microfono as source:
            reconocedor.adjust_for_ambient_noise(source, duration=2)
        
        print("✅ Calibración completada")
        print("\n🎤 Ahora habla algo (tienes 10 segundos)...")
        
        with microfono as source:
            audio = reconocedor.listen(source, timeout=10, phrase_time_limit=5)
        
        print("🔄 Procesando lo que dijiste...")
        
        # Intentar reconocer en español
        try:
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"✅ ¡Perfecto! Escuché: '{texto}'")
            return True
        except sr.UnknownValueError:
            print("❌ No pude entender lo que dijiste")
            return False
        except sr.RequestError as e:
            print(f"❌ Error en el servicio de reconocimiento: {e}")
            return False
            
    except sr.WaitTimeoutError:
        print("⏰ No escuché nada en el tiempo esperado")
        return False
    except Exception as e:
        print(f"❌ Error general: {e}")
        return False

def main():
    print("Iniciando prueba del micrófono...")
    time.sleep(1)
    
    if probar_microfono():
        print("\n🎉 ¡El micrófono funciona correctamente!")
        print("Ahora puedes usar aria_conversacion_completa.py")
    else:
        print("\n⚠️ Hay problemas con el micrófono")
        print("Verifica que:")
        print("- Tu micrófono esté conectado y funcionando")
        print("- Tengas conexión a internet (para Google Speech Recognition)")
        print("- Los permisos de micrófono estén habilitados")

if __name__ == "__main__":
    main()
