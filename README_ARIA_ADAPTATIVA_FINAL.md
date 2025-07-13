# 🤖 ARIA - Sistema de Conversación Adaptativa

## 📋 Descripción General

Aria Conversación Adaptativa es un sistema inteligente que se adapta dinámicamente al usuario mediante:

- **🧠 Bodega de Conocimiento**: Almacenamiento inteligente de información
- **🎯 Adaptación al Usuario**: Aprendizaje de preferencias y estilo de comunicación
- **🎭 Sistema de Personalidad**: Gestión emocional y comportamental
- **🗣️ Conversación por Voz**: Reconocimiento y síntesis de voz integrados

## 🚀 Características Principales

### 1. Sistema de Bodega de Conocimiento
- Almacenamiento categorizado por tipo e importancia
- Búsqueda inteligente con múltiples criterios
- Persistencia automática en archivos JSON
- Limpieza automática de datos antiguos
- Indexación para búsquedas rápidas

### 2. Adaptación Dinámica al Usuario
- **Análisis de Estilo de Comunicación**:
  - Formalidad (formal ↔ informal)
  - Verbosidad (conciso ↔ detallado)
  - Proactividad (reactivo ↔ proactivo)
  - Emocionalidad (neutral ↔ emocional)

- **Detección de Temas de Interés**:
  - Tecnología
  - Ciencia
  - Arte
  - Deportes
  - Negocios

- **Perfiles Personalizados**:
  - Historial de interacciones
  - Horarios de actividad
  - Feedback positivo/negativo
  - Nivel de engagement

### 3. Sistema de Personalidad
- Estados emocionales dinámicos
- Rasgos de personalidad adaptativos
- Memoria emocional
- Respuestas contextuales

### 4. Conversación Inteligente
- **Reconocimiento de Voz**: Google Speech Recognition
- **Síntesis de Voz**: Windows SAPI nativo
- **Proactividad Adaptativa**: Iniciativa basada en perfil del usuario
- **Respuestas Contextuales**: Adaptadas al estilo y preferencias

## 📁 Estructura del Proyecto

```
aria_adaptativa/
├── aria_conversacion_adaptativa.py    # Sistema principal
├── bodega/
│   ├── __init__.py
│   └── BodegaConocimiento.py          # Gestión de conocimiento
├── adaptacion_usuario/
│   ├── __init__.py
│   └── AdaptacionUsuario.py           # Adaptación al usuario
├── personalidad/
│   ├── __init__.py
│   └── personalidad/
│       ├── __init__.py
│       └── PersonalidadCentral.py     # Sistema de personalidad
├── test_aria_completo.py              # Tests completos
├── requirements.txt                   # Dependencias
└── README_ARIA_ADAPTATIVA_FINAL.md    # Esta documentación
```

## 🛠️ Instalación y Configuración

### Requisitos del Sistema
- **Sistema Operativo**: Windows 10/11
- **Python**: 3.8 o superior
- **Micrófono**: Para reconocimiento de voz
- **Altavoces**: Para síntesis de voz

### Instalación de Dependencias

```bash
# Instalar dependencias principales
pip install SpeechRecognition pyaudio

# Para sistemas Windows (opcional, mejora la calidad de audio)
pip install pywin32
```

### Configuración Inicial

1. **Clonar o descargar el proyecto**
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Verificar micrófono y altavoces**
4. **Ejecutar tests**:
   ```bash
   python test_aria_completo.py
   ```

## 🎮 Uso del Sistema

### Ejecución Principal

```bash
python aria_conversacion_adaptativa.py
```

### Modos de Operación

#### 1. Modo Conversación por Voz
- Habla naturalmente al micrófono
- Aria responde por voz y texto
- Adaptación automática en tiempo real

#### 2. Modo Conversación por Texto
- Escribe mensajes en la consola
- Aria responde por voz y texto
- Ideal para entornos silenciosos

### Comandos de Control

- **Salir**: "salir", "adiós", "chao", "terminar"
- **Ctrl+C**: Salida de emergencia

## 🧪 Testing y Validación

### Tests Automatizados

```bash
# Test completo del sistema
python test_aria_completo.py

# Test específico de componentes
python test_aria_adaptativa.py
```

### Tests Incluidos

1. **Bodega de Conocimiento**:
   - Almacenamiento y recuperación
   - Búsquedas complejas
   - Estadísticas del sistema

2. **Adaptación al Usuario**:
   - Procesamiento de interacciones
   - Generación de perfiles
   - Adaptaciones dinámicas

3. **Sistema de Personalidad**:
   - Estados emocionales
   - Procesamiento de entradas
   - Persistencia de estado

4. **Integración Completa**:
   - Flujo de conversación completo
   - Coordinación entre componentes
   - Adaptación en tiempo real

## 📊 Métricas y Monitoreo

### Estadísticas Disponibles

- **Bodega de Conocimiento**:
  - Total de entradas almacenadas
  - Distribución por tipo e importancia
  - Espacio utilizado en disco
  - Usuarios activos

- **Adaptación al Usuario**:
  - Número de interacciones por usuario
  - Temas de interés identificados
  - Nivel de engagement
  - Evolución del estilo de comunicación

- **Sistema de Personalidad**:
  - Cambios de estado emocional
  - Distribución de traits
  - Tiempo de actividad
  - Memoria emocional

## 🔧 Configuración Avanzada

### Personalización de Parámetros

```python
# En aria_conversacion_adaptativa.py
class AriaConversacionAdaptativa:
    def __init__(self):
        # Configurar timeouts de escucha
        self.timeout_escucha = 10  # segundos
        
        # Configurar proactividad
        self.tiempo_proactividad_base = 30  # segundos
        
        # Configurar adaptación
        self.factor_adaptacion = 0.2  # velocidad de adaptación
```

### Configuración de Voz

```python
# Configurar reconocimiento de voz
self.reconocedor.energy_threshold = 300
self.reconocedor.dynamic_energy_threshold = True
self.reconocedor.pause_threshold = 0.8
```

## 🚨 Solución de Problemas

### Problemas Comunes

1. **Error de Micrófono**:
   ```
   Error: No se puede acceder al micrófono
   Solución: Verificar permisos y dispositivos de audio
   ```

2. **Error de Reconocimiento**:
   ```
   Error: speech_recognition no funciona
   Solución: pip uninstall speech_recognition && pip install SpeechRecognition
   ```

3. **Error de Síntesis de Voz**:
   ```
   Error: PowerShell no disponible
   Solución: Verificar que PowerShell esté instalado y accesible
   ```

### Logs y Debugging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔮 Funcionalidades Futuras

### Próximas Mejoras

1. **Integración con APIs Externas**:
   - OpenAI GPT para respuestas más sofisticadas
   - APIs de traducción para soporte multiidioma
   - Servicios de análisis de sentimientos

2. **Interfaz Gráfica**:
   - GUI con tkinter o PyQt
   - Visualización de métricas en tiempo real
   - Configuración visual de parámetros

3. **Aprendizaje Profundo**:
   - Redes neuronales para mejor adaptación
   - Procesamiento de lenguaje natural avanzado
   - Reconocimiento de emociones por voz

4. **Conectividad**:
   - Sincronización en la nube
   - Múltiples dispositivos
   - Integración con asistentes existentes

## 📄 Licencia y Contribuciones

### Licencia
Este proyecto está bajo licencia MIT. Ver archivo LICENSE para más detalles.

### Contribuciones
Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crear una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crear un Pull Request

## 👥 Créditos

- **Desarrollador Principal**: Sistema Aria
- **Arquitectura**: Modular y extensible
- **Tecnologías**: Python, SpeechRecognition, Windows SAPI

## 📞 Soporte

Para soporte técnico o preguntas:

1. **Issues**: Crear un issue en el repositorio
2. **Documentación**: Consultar este README
3. **Tests**: Ejecutar tests para diagnosticar problemas

---

## 🎯 Resumen de Capacidades

✅ **Conversación por voz y texto**  
✅ **Adaptación dinámica al usuario**  
✅ **Almacenamiento inteligente de conocimiento**  
✅ **Sistema de personalidad emocional**  
✅ **Proactividad contextual**  
✅ **Tests automatizados completos**  
✅ **Documentación exhaustiva**  
✅ **Arquitectura modular y extensible**  

**Aria está lista para proporcionar una experiencia de conversación verdaderamente adaptativa y personalizada.**
