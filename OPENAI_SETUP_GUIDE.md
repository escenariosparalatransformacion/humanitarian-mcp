# Guía Completa: Integrar tu MCP con OpenAI

Paso a paso para usar tu Humanitarian Negotiation MCP con OpenAI (ChatGPT).

---

## 🎯 OBJETIVO

Que OpenAI pueda acceder a tus 5 tools a través de tu URL expuesta.

---

## 📋 REQUISITOS

- ✅ MCP corriendo en Docker (http://localhost:8000)
- ✅ ngrok instalado
- ✅ Cuenta OpenAI (ChatGPT Plus o API)

---

## 🚀 PASO 1: EXPONER TU API CON NGROK

### 1.1 Descargar ngrok

Ve a: https://ngrok.com/download

Descarga para Windows y descomprime en una carpeta (ej: `C:\ngrok`)

### 1.2 Abre PowerShell en la carpeta de ngrok

```powershell
cd C:\ngrok
```

### 1.3 Ejecuta ngrok

```powershell
.\ngrok http 8000
```

### 1.4 Verás algo así

```
ngrok                                                             (Ctrl+C to quit)

Session Status                online
Account                       your-email@gmail.com
Connection                    stable
Version                        3.3.5
Region                         United States (us)
Latency                        23ms
Web Interface                  http://127.0.0.1:4040
Forwarding                     https://1a23b456c789.ngrok.io -> http://localhost:8000

Connections                    ttl     opn     dl      in      out
                               0       1       0       0B      0B
```

**COPIA ESTA URL:** `https://1a23b456c789.ngrok.io` (la tuya será diferente)

### 1.5 IMPORTANTE: Deja ngrok corriendo

**NO cierres esta terminal.** ngrok debe seguir ejecutándose para que funcione.

---

## 🧪 PASO 2: VERIFICA QUE FUNCIONA

### Opción A: En el navegador

Abre en tu navegador:
```
https://1a23b456c789.ngrok.io/docs
```

(Reemplaza con tu URL)

Deberías ver una página con todos tus 5 tools. ✅

### Opción B: Con cURL

```powershell
curl https://1a23b456c789.ngrok.io/health
```

Deberías ver:
```json
{"status":"operational",...}
```

---

## 🤖 PASO 3: CONFIGURAR EN OPENAI

### Opción A: Usar GPT Actions (ChatGPT Plus)

**3.1 Ve a ChatGPT:**
https://chat.openai.com

**3.2 En un chat, haz clic en los 3 puntos (⋯)**

**3.3 Selecciona "Configurar"**

**3.4 Ve a la pestaña "Actions"**

**3.5 Haz clic en "Create new action"**

**3.6 Llena el formulario:**

**Schema Name:** `Humanitarian Negotiation MCP`

**Description:** `Tools for humanitarian negotiation analysis`

**Action Auth:** None (por ahora)

**3.7 En "Import from URL" o "Paste Schema":**

Obtén el schema de tu API ejecutando en otra terminal:

```powershell
curl https://1a23b456c789.ngrok.io/openapi.json
```

Copia TODO ese JSON.

Luego en OpenAI, en el campo "Schema", pega todo ese JSON.

**3.8 Haz clic en "Save"**

---

### Opción B: Usar API (Más flexible)

Si prefieres código Python:

```python
import openai
import requests
import json

openai.api_key = "sk-your-api-key"

# URL de tu MCP
BASE_URL = "https://1a23b456c789.ngrok.io"

# Obtén el schema
schema_response = requests.get(f"{BASE_URL}/openapi.json")
openai_schema = schema_response.json()

# Define tools para OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "humanitarian_create_island_of_agreement",
            "description": "Creates Island of Agreement analysis",
            "parameters": {
                "type": "object",
                "properties": {
                    "situation_description": {"type": "string"},
                    "organization_name": {"type": "string"},
                    "counterpart_name": {"type": "string"},
                    "response_format": {"type": "string", "enum": ["markdown", "json"]},
                    "detail_level": {"type": "string", "enum": ["concise", "detailed"]}
                },
                "required": ["situation_description", "organization_name", "counterpart_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "humanitarian_analyze_icebergs",
            "description": "Analyzes positions, reasoning, and motives",
            "parameters": {
                "type": "object",
                "properties": {
                    "organization_name": {"type": "string"},
                    "counterpart_name": {"type": "string"},
                    "organization_positions": {"type": "array", "items": {"type": "string"}},
                    "organization_reasoning": {"type": "array", "items": {"type": "string"}},
                    "organization_motives": {"type": "array", "items": {"type": "string"}},
                    "counterpart_positions": {"type": "array", "items": {"type": "string"}},
                    "response_format": {"type": "string", "enum": ["markdown", "json"]},
                    "detail_level": {"type": "string", "enum": ["concise", "detailed"]}
                },
                "required": ["organization_name", "counterpart_name", "organization_positions",
                            "organization_reasoning", "organization_motives", "counterpart_positions"]
            }
        }
    }
]

# Hacer una conversación con tools
messages = [
    {
        "role": "user",
        "content": "Analiza esta negociación humanitaria: UN agency negotiating with regional government for IDP camp access. Use Island of Agreement methodology."
    }
]

response = openai.ChatCompletion.create(
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

        # Llamar a tu API
        if tool_name == "humanitarian_create_island_of_agreement":
            api_response = requests.post(
                f"{BASE_URL}/api/v1/island-of-agreement",
                json=tool_args
            )
            print(api_response.json())
```

---

## ✅ PASO 4: PRUEBA EN OPENAI

### En ChatGPT:

**Escribe algo como:**

```
Soy trabajador humanitario. Necesito ayuda analizando una negociación.

Situación: Una agencia de la ONU necesita acceso a campamentos de desplazados en una región.
El gobierno requiere que todas las operaciones sean coordinadas a través del Ministerio del Interior.
Hay preocupaciones de seguridad en la zona.

Organización: World Food Programme (WFP)
Contraparte: Ministerio del Interior

Por favor, usa el método Island of Agreement para analizar esto.
```

OpenAI debería:
1. Reconocer que necesita tu tool
2. Llamar a tu API en `https://1a23b456c789.ngrok.io`
3. Recibir el análisis
4. Mostrártelo en un formato bonito

---

## 🔄 SI QUIERES MÁS TOOLS

La guía arriba solo incluye 2 tools. Si quieres agregar los otros 3:

3. `humanitarian_analyze_stakeholders`
4. `humanitarian_leverage_stakeholder_influence`
5. `humanitarian_negotiation_guide`

Copia el mismo patrón en la lista `tools` de Python.

---

## ⚠️ PROBLEMAS COMUNES

### Error: "403 Forbidden"
**Solución:** Revisa que ngrok esté corriendo en Terminal 1

### Error: "Connection timeout"
**Solución:** Reinicia ngrok con `Ctrl+C` y ejecuta de nuevo: `./ngrok http 8000`

### Error: "Invalid schema"
**Solución:** Copia TODO el JSON de `/openapi.json`, no solo parte

### La URL cambió
**Solución:** Cada vez que reinicies ngrok, cambia. Actualiza en OpenAI con la nueva URL.

---

## 🔐 SEGURIDAD (OPCIONAL)

Si expones tu API, es buena idea protegerla:

### Agregar autenticación en http_server.py:

```python
from fastapi import Header, HTTPException

API_KEY = "tu-clave-secreta-aqui"

@app.post("/api/v1/island-of-agreement")
async def api_island_of_agreement(
    request: IslandOfAgreementRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # ... resto del código
```

Luego desde OpenAI/Python:

```python
headers = {"X-API-Key": "tu-clave-secreta-aqui"}
response = requests.post(url, json=data, headers=headers)
```

---

## 📱 TAMBIÉN FUNCIONA EN MOBILE

Si tienes la URL de ngrok, puedes acceder desde cualquier dispositivo:

```
https://1a23b456c789.ngrok.io/docs
```

Funciona en iPhone, Android, etc.

---

## 💡 TIPS AVANZADOS

### URL Permanente (Cuenta ngrok paga)

```powershell
.\ngrok http 8000 --domain=humanitariomcp.ngrok.io
```

Luego SIEMPRE es la misma URL, sin cambios.

### Usar Cloudflare (Mejor para producción)

```powershell
# Descarga cloudflared
.\cloudflared.exe tunnel --url http://localhost:8000

# Te da una URL tipo:
# https://algun-random-string.trycloudflare.com
```

---

## 🎯 CHECKLIST FINAL

- ✅ Docker corriendo: `docker ps` muestra el contenedor
- ✅ ngrok corriendo: Terminal abierta con ngrok active
- ✅ URL funciona: `https://tu-url.ngrok.io/docs` muestra la API
- ✅ OpenAI configurado: Actions añadidas en ChatGPT
- ✅ Prueba exitosa: ChatGPT puede llamar a tu API

---

## 🚀 ESTÁS LISTO

Ahora puedes usar tu MCP con OpenAI desde cualquier lugar, sin Claude Desktop.

¿Tienes preguntas? 👇
