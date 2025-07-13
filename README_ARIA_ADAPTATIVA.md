# Aria Conversación Adaptativa

Sistema de inteligencia artificial conversacional que se adapta al usuario, mantiene conversaciones naturales y almacena información importante en una "bodega" de conocimiento.

## 🚀 Características Principales

### 1. Sistema de Bodega de Conocimiento
- **Almacenamiento Inteligente**: Guarda automáticamente datos importantes de las conversaciones
- **Categorización Automática**: Organiza la información por tipo, importancia y contexto
- **Búsqueda Eficiente**: Encuentra información relevante usando múltiples criterios
- **Gestión de Importancia**: Prioriza datos según su relevancia

### 2. Adaptación al Usuario
- **Perfiles Dinámicos**: Crea y actualiza perfiles de usuario automáticamente
- **Aprendizaje de Preferencias**: Identifica temas de interés y estilos de comunicación
- **Personalización**: Adapta respuestas según el perfil del usuario
- **Memoria de Interacciones**: Recuerda conversaciones previas

### 3. Conversación Natural
- **Voz y Texto**: Soporta conversación por voz y texto
- **Proactividad Adaptativa**: Toma iniciativa según las preferencias del usuario
- **Contexto Persistente**: Mantiene el hilo de la conversación
- **Respuestas Personalizadas**: Ajusta el estilo según el usuario

## 📁 Estructura del Proyecto

```
├── bodega/
│   ├── __init__.py
│   └── BodegaConocimiento.py      # Sistema de almacenamiento
├── adaptacion_usuario/
│   ├── __init__.py
│   └── AdaptacionUsuario.py       # Sistema de adaptación
├── aria_conversacion_adaptativa.py # Sistema principal
├── test_aria_adaptativa.py       # Pruebas del sistema
└── README_ARIA_ADAPTATIVA.md     # Esta documentación
```

## 🛠️ Instalación

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

2. **Configurar micrófono** (opcional para voz):
   - Asegúrate de tener un micrófono conectado
   - En Windows, verifica que el micrófono esté habilitado

## 🎯 Uso

### Ejecutar el Sistema Completo
```bash
python aria_conversacion_adaptativa.py
```

### Ejecutar Pruebas
```bash
python test_aria_adaptativa.py
```

### Uso Programático

```python
from aria_conversacion_adaptativa import AriaConversacionAdaptativa

# Crear instancia
aria = AriaConversacionAdaptativa()

# Iniciar conversación
aria.modo_conversacion_adaptativa(usuario_id="mi_usuario")
```

## 🧠 Componentes del Sistema

### BodegaConocimiento
Gestiona el almacenamiento inteligente de información:

```python
from bodega import BodegaConocimiento, TipoInformacion, ImportanciaInfo

bodega = BodegaConocimiento()

# Almacenar información
id_elemento = bodega.almacenar(
    tipo=TipoInformacion.CONVERSACION,
    contenido={"texto": "Me gusta la tecnología"},
    importancia=ImportanciaInfo.ALTA,
    usuario_id="usuario1",
    palabras_clave=["tecnología", "preferencia"]
)

# Buscar información
resultados = bodega.buscar({
    "usuario_id": "usuario1",
    "palabras_clave": ["tecnología"]
})
```

### AdaptacionUsuario
Maneja la adaptación al comportamiento del usuario:

```python
from adaptacion_usuario import AdaptacionUsuario

adaptacion = AdaptacionUsuario(bodega)

# Procesar interacción
resultado = adaptacion.procesar_interaccion("usuario1", {
    "texto": "Hola, me interesa la ciencia",
    "tipo": "saludo",
    "contexto": {"iniciativa_usuario": True}
})

# Obtener perfil
perfil = adaptacion.obtener_perfil("usuario1")
```

## 📊 Tipos de Información Almacenada

### TipoInformacion
- `CONVERSACION`: Diálogos y mensajes
- `PREFERENCIA_USUARIO`: Gustos y preferencias
- `CONOCIMIENTO_GENERAL`: Información factual
- `EXPERIENCIA`: Experiencias vividas
- `EMOCION`: Estados emocionales
- `CONTEXTO`: Información contextual
- `APRENDIZAJE`: Datos de aprendizaje

### ImportanciaInfo
- `CRITICA` (5): Información crítica
- `ALTA` (4): Muy importante
- `MEDIA` (3): Importancia normal
- `BAJA` (2): Poco importante
- `MINIMA` (1): Información mínima

## 🎨 Adaptación de Estilo

El sistema adapta automáticamente:

### Formalidad
- **Formal**: Uso de "usted", "por favor"
- **Informal**: Uso de "tu", lenguaje casual

### Verbosidad
- **Conciso**: Respuestas breves y directas
- **Detallado**: Explicaciones extensas

### Proactividad
- **Reactivo**: Espera iniciativa del usuario
- **Proactivo**: Toma iniciativa frecuentemente

### Emocionalidad
- **Neutral**: Tono objetivo
- **Emocional**: Expresiones emotivas

## 📈 Funcionalidades Avanzadas

### Búsqueda Inteligente
```python
# Buscar por múltiples criterios
resultados = bodega.buscar({
    "tipo": TipoInformacion.PREFERENCIA_USUARIO,
    "importancia_min": ImportanciaInfo.MEDIA,
    "usuario_id": "usuario1",
    "palabras_clave": ["tecnología", "ciencia"],
    "fecha_desde": timestamp_inicio,
    "limite": 10
})
```

### Estadísticas de Usuario
```python
# Obtener resumen del usuario
resumen = bodega.obtener_resumen_usuario("usuario1")
print(f"Total interacciones: {resumen['total_entradas']}")
print(f"Temas frecuentes: {resumen['temas_frecuentes']}")
```

### Limpieza Automática
```python
# Limpiar datos antiguos
eliminados = bodega.limpiar_datos_antiguos(dias_antiguedad=365)
print(f"Eliminadas {eliminados} entradas antiguas")
```

## 🔧 Configuración

### Directorios de Datos
- `./bodega_datos/`: Almacenamiento de la bodega
- `./perfiles_usuario/`: Perfiles de usuario
- `./datos_personalidad/`: Datos de personalidad

### Logging
El sistema usa logging estándar de Python. Para configurar:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## 🚨 Solución de Problemas

### Error de Micrófono
Si no funciona el reconocimiento de voz:
1. Verifica que el micrófono esté conectado
2. Instala `pyaudio`: `pip install pyaudio`
3. En Windows, verifica permisos de micrófono

### Error de Importación
Si hay errores de importación:
1. Verifica que estés en el directorio correcto
2. Instala dependencias: `pip install -r requirements.txt`
3. Verifica la estructura de directorios

### Problemas de Rendimiento
Para mejorar el rendimiento:
1. Ejecuta limpieza periódica: `bodega.limpiar_datos_antiguos()`
2. Limita resultados de búsqueda con `limite`
3. Usa palabras clave específicas en búsquedas

## 🔮 Funcionalidades Futuras

- [ ] Integración con APIs externas
- [ ] Análisis de sentimientos avanzado
- [ ] Soporte para múltiples idiomas
- [ ] Interfaz web interactiva
- [ ] Sincronización en la nube
- [ ] Análisis predictivo de comportamiento

## 📝 Ejemplos de Uso

### Conversación Básica
```
👤 Usuario: Hola Aria
🤖 Aria: ¡Hola! Me alegra mucho volver a hablar contigo.

👤 Usuario: Me gusta la tecnología
🤖 Aria: ¡Qué interesante! Me recuerda a algunos temas de tecnología que hemos discutido.

👤 Usuario: ¿Qué sabes sobre IA?
🤖 Aria: ¡Fascinante! ¿Te gustaría explorar cómo se relaciona esto con tecnología?
```

### Adaptación Progresiva
El sistema aprende y se adapta:
- **Primera conversación**: Respuestas genéricas
- **Después de varias interacciones**: Respuestas personalizadas
- **Conversaciones avanzadas**: Proactividad basada en intereses

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Implementa los cambios
4. Ejecuta las pruebas
5. Envía un pull request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo LICENSE para más detalles.

---

**¡Disfruta conversando con Aria! 🤖✨**
