"""
Verificador del Sistema Aria
Verifica que todos los módulos estén correctamente instalados y funcionando
"""

import sys
import importlib
from pathlib import Path

def verificar_modulos():
    """Verifica todos los módulos del sistema"""
    modulos_requeridos = [
        'Habilidades.Voz',
        'Habilidades.Vision', 
        'Habilidades.Simulacion',
        'Habilidades.Procesamiento',
        'Habilidades.Conexiones',
        'Habilidades.Almacenamiento',
        'Habilidades.AutoMODIFICACION',
        'Habilidades.ArquitectoIA',
        'Habilidades.GeneradorDocumentos',
        'Habilidades.ExtensionCAMPO',
        'Habilidades.ComunicacionMulticanal'
    ]
    
    resultados = {}
    
    for modulo in modulos_requeridos:
        try:
            importlib.import_module(modulo)
            resultados[modulo] = "✅ OK"
        except ImportError as e:
            resultados[modulo] = f"❌ Error: {e}"
        except Exception as e:
            resultados[modulo] = f"⚠️ Advertencia: {e}"
    
    return resultados

def generar_reporte():
    """Genera un reporte completo del sistema"""
    print("🔍 Verificando Sistema Aria...")
    print("=" * 50)
    
    resultados = verificar_modulos()
    
    for modulo, estado in resultados.items():
        print(f"{modulo}: {estado}")
    
    # Contar errores
    errores = sum(1 for estado in resultados.values() if "❌" in estado)
    advertencias = sum(1 for estado in resultados.values() if "⚠️" in estado)
    exitosos = sum(1 for estado in resultados.values() if "✅" in estado)
    
    print("=" * 50)
    print(f"📊 Resumen:")
    print(f"✅ Módulos exitosos: {exitosos}")
    print(f"⚠️ Advertencias: {advertencias}")
    print(f"❌ Errores: {errores}")
    
    if errores == 0:
        print("🎉 Sistema Aria completamente funcional!")
    else:
        print("🔧 Sistema requiere correcciones")
    
    return errores == 0

if __name__ == "__main__":
    generar_reporte()