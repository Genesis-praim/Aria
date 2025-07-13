# Sistema Sensorial Integrado de Aria

## Descripción General

El Sistema Sensorial Integrado de Aria es una arquitectura completa que combina capacidades de percepción auditiva, visual y síntesis de voz en un sistema unificado. Este sistema permite a Aria interactuar de manera natural con su entorno, procesando múltiples flujos de información sensorial de forma simultánea y coordinada.

## Arquitectura del Sistema

### Componentes Principales

#### 1. Interfaz Sensorial (`interfaz_sensorial/`)

**Oído (`oido.py`)**
- Captura y procesamiento de audio en tiempo real
- Reconocimiento de voz usando speech_recognition
- Detección de energía vocal y filtrado de ruido
- Configuración adaptativa de sensibilidad

**Voz (`voz.py`)**
- Síntesis de texto a voz usando pyttsx3
- Control de velocidad, volumen y voz
- Soporte para múltiples idiomas
- Gestión de cola de reproducción

**Ojos (`ojos.py`)**
- Captura de video usando OpenCV
- Detección de rostros con Haar Cascades
- Detección de movimiento por diferencia de frames
- Captura continua con callbacks

**Integrador Sensorial (`integrador_sensorial.py`)**
- Coordinación de todos los sistemas sensoriales
- Procesamiento paralelo con hilos dedicados
- Análisis de correlación temporal
- Sistema de callbacks para eventos integrados

#### 2. Sistema Principal (`main_sensorial_integrado.py`)

**SistemaAriaIntegrado**
- Orquestación completa del sistema
- Integración con bodega de conocimiento
- Adaptación automática de usuario
- Gestión de contexto y estados

#### 3. Lenguaje y Abstracción (`lenguaje_y_abstraccion/`)

**LenguajeYAbstraccion (`LenguajeYAbstraccion.py`)**
- Procesamiento de lenguaje natural
- Análisis semántico y conceptual
- Identificación de entidades y temas
- Generación de respuestas adaptativas

**GramaticaEspanol (`gramatica_espanol.py`)**
- Análisis gramatical del español
- Identificación de tipos de palabras
- Estructura sintáctica básica
- Clasificación morfológica

#### 4. Emoción y Personalidad (`emocion_y_personalidad/`)

**EmocionYMotivacion (`emocion_y_motivacion.py`)**
- Sistema de estados emocionales
- Gestión de motivaciones
- Patrones de respuesta emocional
- Adaptación emocional contextual

**PersonalidadCentral (`personalidad/personalidad/PersonalidadCentral.py`)**
- Definición de rasgos de personalidad
- Valores personales fundamentales
- Patrones de comportamiento
- Adaptación de personalidad

## Flujo de Procesamiento

### 1. Captura Sensorial
```
Audio Input → Oído → Procesamiento de Voz → Texto
Video Input → Ojos → Detección Visual → Eventos
```

### 2. Integración
```
Eventos Audio + Visual → Integrador → Análisis Temporal → Eventos Integrados
```

### 3. Procesamiento Cognitivo
```
Eventos → Lenguaje → Análisis Semántico → Comprensión
Comprensión → Emoción → Estado Emocional → Respuesta
```

### 4. Generación de Respuesta
```
Análisis → Personalidad → Adaptación → Respuesta Personalizada
Respuesta → Voz → Síntesis → Audio Output
```

## Características Principales

### Procesamiento en Tiempo Real
- Captura continua de audio y video
- Procesamiento paralelo con hilos dedicados
- Latencia mínima en respuestas
- Sincronización temporal precisa

### Adaptación Inteligente
- Ajuste automático a preferencias del usuario
- Aprendizaje de patrones de interacción
- Personalización de respuestas
- Evolución de personalidad

### Análisis Multimodal
- Correlación entre audio y video
- Detección de interacciones cara a cara
- Análisis de atención visual
- Integración contextual

### Sistema Emocional
- Estados emocionales dinámicos
- Motivaciones adaptativas
- Respuestas empáticas
- Memoria emocional

## Configuración y Uso

### Instalación de Dependencias

```bash
pip install speech_recognition
pip install pyttsx3
pip install opencv-python
pip install numpy
pip install pyaudio
```

### Uso Básico

```python
from main_sensorial_integrado import SistemaAriaIntegrado

# Crear sistema
sistema = SistemaAriaIntegrado()

# Iniciar con usuario específico
sistema.iniciar(usuario_id="usuario_001")

# El sistema procesará automáticamente:
# - Audio del micrófono
# - Video de la cámara
# - Generará respuestas adaptativas

# Detener sistema
sistema.detener()
```

### Configuración Avanzada

```python
# Configurar integrador sensorial
sistema.integrador.configurar_modo_atencion("focalizado")

# Configurar sistema emocional
sistema.adaptacion.configurar_sistema(
    factor_adaptacion=0.3,
    umbral_cambio_emocional=0.2
)

# Registrar callbacks personalizados
def mi_callback(datos):
    print(f"Evento recibido: {datos}")

sistema.integrador.registrar_callback("integrado", mi_callback)
```

## Modos de Operación

### Modo Pasivo
- Monitoreo básico del entorno
- Respuesta solo cuando se le habla directamente
- Consumo mínimo de recursos

### Modo Activo
- Monitoreo continuo de audio y video
- Respuesta proactiva a eventos
- Análisis de contexto mejorado

### Modo Focalizado
- Máxima atención a la interacción
- Análisis detallado de rostros y emociones
- Respuestas altamente personalizadas

## Estructura de Datos

### Estado Emocional
```python
{
    "emocion_actual": "alegria",
    "intensidad": 0.7,
    "duracion_restante": 180.5,
    "causa": "interaccion_positiva",
    "timestamp": 1640995200.0
}
```

### Análisis Sensorial
```python
{
    "timestamp": 1640995200.0,
    "audio": {
        "texto": "Hola, ¿cómo estás?",
        "confianza": 0.95
    },
    "visual": {
        "rostros_detectados": 1,
        "movimiento_detectado": True
    },
    "analisis": {
        "sincronizacion": True,
        "interaccion_cara_a_cara": True
    }
}
```

### Perfil de Personalidad
```python
{
    "rasgos": {
        "apertura": 0.8,
        "responsabilidad": 0.9,
        "extroversion": 0.6,
        "amabilidad": 0.85,
        "estabilidad": 0.75
    },
    "valores": {
        "ayuda": 0.9,
        "conocimiento": 0.85,
        "eficiencia": 0.8,
        "etica": 0.95,
        "adaptabilidad": 0.75
    }
}
```

## Testing y Validación

### Suite de Pruebas
```bash
python test_sistema_sensorial.py
```

### Pruebas Incluidas
- Inicialización de componentes
- Procesamiento de audio
- Síntesis de voz
- Captura de video
- Integración sensorial
- Sistema emocional
- Adaptación de personalidad
- Manejo de errores
- Rendimiento

### Métricas de Rendimiento
- Latencia de respuesta < 500ms
- Precisión de reconocimiento > 90%
- Estabilidad emocional
- Adaptación efectiva

## Extensibilidad

### Agregar Nuevos Sensores
```python
class NuevoSensor:
    def capturar(self):
        # Implementar captura
        pass
    
    def procesar(self, datos):
        # Implementar procesamiento
        pass

# Integrar con el sistema
sistema.integrador.agregar_sensor(NuevoSensor())
```

### Personalizar Emociones
```python
from emocion_y_personalidad import TipoEmocion, EstadoEmocional

# Definir nueva emoción
nueva_emocion = TipoEmocion.NUEVA_EMOCION

# Crear estado emocional
estado = EstadoEmocional(
    tipo=nueva_emocion,
    intensidad=0.6,
    duracion=300.0
)

sistema.emocion.procesar_estimulo("nuevo_estimulo", 0.7)
```

### Agregar Idiomas
```python
# En gramatica_espanol.py
class GramaticaIngles(GramaticaEspanol):
    def _cargar_diccionarios(self):
        # Implementar diccionarios en inglés
        pass

# Integrar nuevo idioma
sistema.lenguaje.agregar_idioma("ingles", GramaticaIngles())
```

## Consideraciones de Rendimiento

### Optimizaciones Implementadas
- Procesamiento paralelo con hilos
- Colas eficientes para eventos
- Decaimiento automático de emociones
- Límites en historial de eventos

### Recomendaciones de Hardware
- CPU: Mínimo dual-core 2.0 GHz
- RAM: Mínimo 4 GB
- Cámara: 720p o superior
- Micrófono: Calidad media o superior

### Configuración de Rendimiento
```python
# Ajustar para mejor rendimiento
sistema.ojos.configurar(fps=15)  # Reducir FPS
sistema.integrador.configurar_modo_atencion("pasivo")  # Modo eficiente
```

## Troubleshooting

### Problemas Comunes

**Audio no se detecta**
- Verificar permisos de micrófono
- Comprobar dispositivos de audio
- Ajustar umbral de energía

**Video no funciona**
- Verificar permisos de cámara
- Comprobar drivers de video
- Verificar índice de cámara

**Respuestas lentas**
- Reducir calidad de video
- Ajustar modo de atención
- Verificar recursos del sistema

### Logs y Debugging
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Los logs mostrarán información detallada
# sobre el procesamiento del sistema
```

## Roadmap Futuro

### Mejoras Planificadas
- Reconocimiento de emociones faciales
- Procesamiento de lenguaje natural avanzado
- Integración con APIs de IA externa
- Soporte para múltiples usuarios simultáneos
- Análisis de sentimientos en tiempo real
- Memoria a largo plazo mejorada

### Integraciones Futuras
- Sistemas de domótica
- Asistentes virtuales externos
- Bases de datos de conocimiento
- Servicios en la nube
- Dispositivos IoT

## Contribución

Para contribuir al desarrollo del sistema:

1. Fork del repositorio
2. Crear rama de feature
3. Implementar mejoras
4. Agregar tests
5. Documentar cambios
6. Crear pull request

## Licencia

Este sistema es parte del proyecto Aria y está sujeto a las mismas condiciones de licencia del proyecto principal.

---

*Documentación actualizada: Diciembre 2024*
*Versión del sistema: 1.0.0*
