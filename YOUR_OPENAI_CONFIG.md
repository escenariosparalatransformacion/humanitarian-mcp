# Tu Configuración OpenAI - PASO A PASO

Tu URL de ngrok: `https://3953334c0179.ngrok-free.app`

Sigue estos pasos exactos para conectar tu MCP con OpenAI.

---

## 🔗 PASO 1: OBTÉN EL SCHEMA DE TU API

En PowerShell (o curl), ejecuta:

```powershell
curl https://3953334c0179.ngrok-free.app/openapi.json
```

**O simplemente abre en el navegador:**
```
https://3953334c0179.ngrok-free.app/openapi.json
```

Verás un JSON gigante. **Cópialo todo** (Ctrl+A, Ctrl+C).

---

## 🤖 PASO 2: ABRE CHATGPT

Ve a: https://chat.openai.com

---

## ⚙️ PASO 3: CREA UNA ACCIÓN EN CHATGPT

### 3.1 En un chat, haz clic en los 3 puntos (⋯)

![Menú de ChatGPT]

### 3.2 Selecciona "Configurar"

### 3.3 Ve a la pestaña "ACCIONES"

### 3.4 Haz clic en "Crear nueva acción"

### 3.5 Llena el formulario:

**En la sección "Schema":**

Pega TODO el JSON que copiaste de: `https://3953334c0179.ngrok-free.app/openapi.json`

**Configuración rápida:**
- **Nombre:** Humanitarian Negotiation MCP
- **Descripción:** Tools for humanitarian negotiation analysis
- **URL base:** `https://3953334c0179.ngrok-free.app`
- **Autenticación:** None

### 3.6 Haz clic en "Guardar"

---

## ✅ PASO 4: PRUEBA EN CHATGPT

En el chat de ChatGPT, escribe algo como:

```
Necesito analizar una negociación humanitaria.

Situación: Una agencia de la ONU necesita acceso a campamentos de desplazados.
El gobierno requiere coordinación a través del Ministerio del Interior.

Usa el método Island of Agreement para analizar esto.

Organización: World Food Programme
Contraparte: Ministerio del Interior
```

---

## 🎯 PASO 5: ChatGPT Automáticamente:

1. Reconoce que necesita tu herramienta
2. Llama a tu API en `https://3953334c0179.ngrok-free.app`
3. Recibe el resultado
4. Te lo muestra formateado

---

## 📋 ALTERNATIVA: USAR CÓDIGO PYTHON

Si prefieres más control, aquí está el código:

```python
from openai import OpenAI
import requests
import json

# Tu API
BASE_URL = "https://3953334c0179.ngrok-free.app"
API_KEY = "sk-your-openai-api-key"

# Cliente OpenAI
client = OpenAI(api_key=API_KEY)

# Obtén el schema de tu API
schema_response = requests.get(f"{BASE_URL}/openapi.json")
api_schema = schema_response.json()

# Define tools basado en tu schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "humanitarian_create_island_of_agreement",
            "description": "Creates Island of Agreement analysis for humanitarian negotiations",
            "parameters": {
                "type": "object",
                "properties": {
                    "situation_description": {
                        "type": "string",
                        "description": "Comprehensive description of the negotiation situation"
                    },
                    "organization_name": {
                        "type": "string",
                        "description": "Name of your organization"
                    },
                    "counterpart_name": {
                        "type": "string",
                        "description": "Name of the counterpart"
                    },
                    "response_format": {
                        "type": "string",
                        "enum": ["markdown", "json"],
                        "description": "Response format"
                    },
                    "detail_level": {
                        "type": "string",
                        "enum": ["concise", "detailed"],
                        "description": "Level of detail"
                    }
                },
                "required": ["situation_description", "organization_name", "counterpart_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "humanitarian_analyze_icebergs",
            "description": "Analyzes positions, reasoning, and underlying motives",
            "parameters": {
                "type": "object",
                "properties": {
                    "organization_name": {"type": "string"},
                    "counterpart_name": {"type": "string"},
                    "organization_positions": {"type": "array", "items": {"type": "string"}},
                    "organization_reasoning": {"type": "array", "items": {"type": "string"}},
                    "organization_motives": {"type": "array", "items": {"type": "string"}},
                    "counterpart_positions": {"type": "array", "items": {"type": "string"}},
                    "counterpart_reasoning": {"type": "array", "items": {"type": "string"}},
                    "counterpart_motives": {"type": "array", "items": {"type": "string"}},
                    "response_format": {"type": "string", "enum": ["markdown", "json"]}
                },
                "required": ["organization_name", "counterpart_name", "organization_positions",
                            "organization_reasoning", "organization_motives", "counterpart_positions"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "humanitarian_analyze_stakeholders",
            "description": "Analyzes and prioritizes stakeholders",
            "parameters": {
                "type": "object",
                "properties": {
                    "context": {"type": "string"},
                    "stakeholders": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "power": {"type": "number"},
                                "urgency": {"type": "number"},
                                "legitimacy": {"type": "number"},
                                "position": {"type": "number"}
                            }
                        }
                    },
                    "response_format": {"type": "string", "enum": ["markdown", "json"]}
                },
                "required": ["context", "stakeholders"]
            }
        }
    }
]

# Conversación
messages = [
    {
        "role": "user",
        "content": "Analiza esta negociación humanitaria usando Island of Agreement: UN agency with regional government for IDP camp access"
    }
]

# Llamar a OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Procesar respuesta
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)

        print(f"\n📞 Llamando a: {tool_name}")
        print(f"📊 Con argumentos: {json.dumps(tool_args, indent=2)}")

        # Llamar a tu API
        api_endpoint = f"{BASE_URL}/api/v1/{tool_name.replace('humanitarian_', '').replace('_', '-')}"
        api_response = requests.post(api_endpoint, json=tool_args)

        print(f"\n✅ Respuesta de tu API:")
        print(json.dumps(api_response.json(), indent=2))
else:
    print(response.choices[0].message.content)
```

---

## 🌐 URL IMPORTANTE

Tu API está disponible en:

```
https://3953334c0179.ngrok-free.app
```

Endpoints:
- **Documentación:** `https://3953334c0179.ngrok-free.app/docs`
- **Health check:** `https://3953334c0179.ngrok-free.app/health`
- **Tools list:** `https://3953334c0179.ngrok-free.app/tools`
- **Schema:** `https://3953334c0179.ngrok-free.app/openapi.json`

---

## ⚠️ IMPORTANTE

**Tu URL de ngrok cambia cada vez que reinicies ngrok.**

Cuando reinicies:
1. Ejecuta: `ngrok http 8000`
2. Obtén la nueva URL
3. Actualiza en OpenAI

Para URL PERMANENTE, usa Google Cloud Run (ver `GOOGLE_CLOUD_RUN_SETUP.md`)

---

## 🧪 PRUEBAS

### Prueba 1: Docs interactivo
```
https://3953334c0179.ngrok-free.app/docs
```
Abre en navegador. Verás todos los tools.

### Prueba 2: Health check
```powershell
curl https://3953334c0179.ngrok-free.app/health
```

### Prueba 3: En OpenAI
Sigue los pasos de arriba.

---

## ✨ ¡LISTO!

Ya puedes usar tu MCP con OpenAI. 🎉

Si necesitas ayuda en cualquier paso, dime cuál. 👇
