# 🤖 ARIA - Sistema de Conversación por Voz

## 📋 Descripción
Aria es un asistente de inteligencia artificial que puede mantener conversaciones completas por voz. Puede escucharte a través del micrófono y responderte por la bocina de tu dispositivo.

## 🚀 Características Principales

✅ **Saludo Inmediato**: Aria te saluda automáticamente al iniciar
✅ **Reconocimiento de Voz**: Escucha y entiende lo que dices por el micrófono
✅ **Síntesis de Voz**: Responde hablando por la bocina usando TTS nativo de Windows
✅ **Personalidad Proactiva**: Toma la iniciativa y sugiere temas de conversación
✅ **Conversación Natural**: Reconoce diferentes tipos de mensajes y responde apropiadamente
✅ **Modo Fallback**: Si el micrófono no funciona, puedes escribir y ella responde por voz

## 📁 Archivos Disponibles

### Versiones Principales:
- **`aria_conversacion_completa.py`** - ⭐ **RECOMENDADO** - Versión completa con voz bidireccional
- **`aria_voz_windows.py`** - Solo habla (no escucha), usa TTS nativo
- **`aria_voz_mejorada.py`** - Versión con pyttsx3

### Archivos de Prueba:
- **`test_microfono.py`** - Prueba si tu micrófono funciona correctamente
- **`test_voz.py`** - Prueba básica del sistema de síntesis de voz

## 🛠️ Instalación

### 1. Instalar Dependencias
```bash
pip install SpeechRecognition pyaudio pyttsx3 pywin32 comtypes
```

### 2. Verificar Micrófono
```bash
python test_microfono.py
```

### 3. Ejecutar Aria
```bash
python aria_conversacion_completa.py
```

## 🎯 Cómo Usar

### Inicio Automático:
1. Ejecuta `python aria_conversacion_completa.py`
2. Aria te saludará inmediatamente por la bocina
3. Después del saludo, podrás hablarle directamente

### Conversación por Voz:
- **Habla directamente** al micrófono cuando veas "🎤 Esperando que hables..."
- Aria te **escuchará** y **responderá por voz**
- Si no hablas por un tiempo, Aria **tomará la iniciativa**

### Comandos de Voz:
- Di **"Hola"** para saludar
- Pregunta **"¿Cómo estás?"** para conocer su estado
- Di **"¿Qué hora es?"** para saber la hora
- Pregunta **"¿Qué puedes hacer?"** para conocer sus capacidades
- Di **"Adiós"** o **"Salir"** para terminar

## 🔧 Solución de Problemas

### Si el micrófono no funciona:
1. Verifica que tu micrófono esté conectado
2. Asegúrate de tener conexión a internet (usa Google Speech Recognition)
3. Ejecuta `python test_microfono.py` para diagnosticar
4. Si falla, Aria funcionará en modo texto (escribes, ella habla)

### Si la voz no se escucha:
1. Verifica que tu bocina/altavoces estén encendidos
2. Ajusta el volumen del sistema
3. El sistema usa TTS nativo de Windows

### Si hay errores de instalación:
```bash
# Reinstalar dependencias
pip uninstall SpeechRecognition pyaudio pyttsx3 -y
pip install SpeechRecognition pyaudio pyttsx3
```

## 🎨 Personalización

### Cambiar Idioma de Reconocimiento:
En `aria_conversacion_completa.py`, línea ~95:
```python
texto = self.reconocedor.recognize_google(audio, language='es-ES')  # Español
# texto = self.reconocedor.recognize_google(audio, language='en-US')  # Inglés
```

### Ajustar Tiempo de Escucha:
En `aria_conversacion_completa.py`, línea ~200:
```python
mensaje_voz = self.escuchar(timeout=10)  # 10 segundos de espera
```

### Modificar Temas de Conversación:
En `aria_conversacion_completa.py`, líneas ~20-27:
```python
self.temas_conversacion = [
    "Tu tema personalizado aquí",
    # ... más temas
]
```

## 🌟 Ejemplos de Conversación

```
🗣️ ARIA: ¡Buenas tardes! Soy Aria, tu asistente con inteligencia artificial.
🎤 Tú: "Hola Aria, ¿cómo estás?"
🗣️ ARIA: ¡Hola! Me alegra mucho escuchar tu voz. ¿Qué tal va tu día?
🎤 Tú: "Muy bien, ¿qué puedes hacer?"
🗣️ ARIA: Puedo conversar contigo por voz, responder preguntas, contar historias...
```

## 📞 Soporte

Si tienes problemas:
1. Ejecuta `python test_microfono.py` para diagnosticar el micrófono
2. Verifica que tengas conexión a internet
3. Asegúrate de que los permisos de micrófono estén habilitados
4. Usa `aria_voz_windows.py` como alternativa (solo habla, no escucha)

## 🎉 ¡Disfruta conversando con Aria!

Aria está diseñada para ser tu compañera de conversación inteligente. Puede hablar sobre diversos temas, responder preguntas, y mantener conversaciones naturales por voz.
