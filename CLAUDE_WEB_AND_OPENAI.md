# Usar tu MCP con Claude Web y OpenAI

Tu MCP está corriendo en Docker en `http://localhost:8000`. Aquí hay varias formas de usarlo sin Claude Desktop.

---

## 📌 IMPORTANTE: ACCESO A TU LOCALHOST

**Problema:** Claude Web y OpenAI están en internet. Tu MCP está en `localhost:8000` (solo tu computadora).

**Soluciones:**

### Opción A: Exponer a Internet (RECOMENDADO para Claude Web)
Necesitas un servicio que haga que tu localhost sea accesible desde internet.

**Herramientas gratuitas:**
- **ngrok** (más popular)
- **Cloudflare Tunnel** (más seguro)
- **localtunnel** (simple)

---

## 🚀 SOLUCIÓN 1: USAR NGROK (Más Fácil)

### Paso 1: Descargar ngrok

1. Ve a: https://ngrok.com/download
2. Descarga para Windows
3. Descomprime el archivo `ngrok.exe`

### Paso 2: Abrir Terminal en la carpeta de ngrok

```powershell
cd "C:\ruta\donde\descargaste\ngrok"
```

### Paso 3: Ejecutar ngrok

```powershell
./ngrok http 8000
```

**Verás algo como:**
```
ngrok
Session Status                online
Account                       tu-email@example.com
Connection                    stable
Version                        3.3.0
Region                         United States (us)
Latency                        25ms
Web Interface                  http://127.0.0.1:4040
Forwarding                     https://abc123def.ngrok.io -> http://localhost:8000
```

**COPIA ESTA URL:** `https://abc123def.ngrok.io`

### Paso 4: Verifica que funciona

Abre en tu navegador:
```
https://abc123def.ngrok.io/docs
```

Deberías ver tu API con todos los 5 tools. ✅

---

## 🔗 USANDO NGROK URL CON CLAUDE WEB

Desafortunadamente, **Claude Web NO soporta directamente URLs personalizadas** para MCPs (por ahora).

**Lo que SÍ puedes hacer:**

### Opción 1: Usar REST API directamente en Claude

En Claude Web, puedes hacer esto:

```
Yo: "Necesito que hagas una llamada HTTP a mi API para analizar una negociación.

La URL es: https://abc123def.ngrok.io/api/v1/island-of-agreement

Los parámetros son:
- situation_description: [descripción]
- organization_name: [tu org]
- counterpart_name: [contraparte]

Por favor, haz la llamada y muéstrame el resultado."
```

Claude puede hacer llamadas HTTP si le das el URL exacto.

---

## 🤖 SOLUCIÓN 2: INTEGRACIÓN CON OPENAI

Esta es la mejor opción para OpenAI. OpenAI soporta "Custom Actions" o "Tools" que usan URLs externas.

### Paso 1: Exponer tu MCP con ngrok

```powershell
./ngrok http 8000
```

Copia la URL que genera (ej: `https://abc123def.ngrok.io`)

### Paso 2: Obtener el OpenAPI schema de tu MCP

Accede a:
```
https://abc123def.ngrok.io/openapi.json
```

Cópialo completo (es un JSON grande).

### Paso 3: Crear Custom Action en OpenAI

**En OpenAI (ChatGPT Plus o API):**

1. Ve a: https://chat.openai.com
2. Abre una conversación
3. Haz clic en **"+"** o accede a **GPT Builder**
4. Selecciona **"Create new action"** o **"Configure"**
5. En la sección de Actions, haz clic en **"Create new action"**

**Llena los datos:**

- **Schema:** Pega el JSON de `openapi.json`
- **Authentication:** None (o API Key si lo necesitas)
- **URL Base:** `https://abc123def.ngrok.io`

### Paso 4: Prueba en OpenAI

```
Yo: "Analiza esta negociación usando el Island of Agreement tool"

[ChatGPT usará automáticamente tu MCP a través de la API]
```

---

## 📄 EJEMPLO: CONFIGURACIÓN OPENAI CON CURL

Si prefieres hacerlo por código:

```python
import requests
import json
from openai import OpenAI

# Tu URL de ngrok
BASE_URL = "https://abc123def.ngrok.io"

# Cliente OpenAI
client = OpenAI(api_key="tu-api-key")

# Definir el schema de tu API
tools = [
    {
        "type": "function",
        "function": {
            "name": "humanitarian_island_of_agreement",
            "description": "Crea un análisis Island of Agreement",
            "parameters": {
                "type": "object",
                "properties": {
                    "situation_description": {
                        "type": "string",
                        "description": "Descripción de la situación"
                    },
                    "organization_name": {
                        "type": "string",
                        "description": "Nombre de tu organización"
                    },
                    "counterpart_name": {
                        "type": "string",
                        "description": "Nombre de la contraparte"
                    },
                    "response_format": {
                        "type": "string",
                        "enum": ["markdown", "json"],
                        "description": "Formato de respuesta"
                    },
                    "detail_level": {
                        "type": "string",
                        "enum": ["concise", "detailed"],
                        "description": "Nivel de detalle"
                    }
                },
                "required": ["situation_description", "organization_name", "counterpart_name"]
            }
        }
    }
]

# Mensaje inicial
messages = [
    {
        "role": "user",
        "content": "Analiza esta negociación: UN negotiating with regional government for IDP camp access"
    }
]

# Llamar a OpenAI con tools
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Procesar respuesta
if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call.function.name == "humanitarian_island_of_agreement":
            # Llamar a tu API
            api_response = requests.post(
                f"{BASE_URL}/api/v1/island-of-agreement",
                json=json.loads(tool_call.function.arguments)
            )

            print(api_response.json())
```

---

## 🌐 SOLUCIÓN 3: USAR LOCALTUNNEL (MÁS SIMPLE)

```bash
# Instalar (requiere Node.js)
npm install -g localtunnel

# Ejecutar
lt --port 8000

# Verás algo como:
# your url is: https://random-string.loca.lt
```

Luego usa esa URL como tu endpoint.

---

## 🔐 SOLUCIÓN 4: CLOUDFLARE TUNNEL (MÁS SEGURO)

```bash
# Descargar cloudflared desde: https://developers.cloudflare.com/cloudflare-one/connections/connect-applications/install-and-setup/

# Ejecutar
cloudflared tunnel --url http://localhost:8000

# Verás algo como:
# https://random-string.trycloudflare.com
```

---

## 📋 COMPARATIVA: NGROK vs LOCALTUNNEL vs CLOUDFLARE

| Feature | ngrok | localtunnel | Cloudflare |
|---------|-------|-------------|-----------|
| Facilidad | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Gratuito | ✅ (limitado) | ✅ | ✅ |
| Velocidad | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Seguridad | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Estable | ✅ | ⚠️ | ✅ |

**Recomendación:** ngrok para empezar rápido, Cloudflare para producción.

---

## 🎯 INSTRUCCIONES PASO A PASO: OPENAI + NGROK

### Paso 1: Tener ngrok corriendo
```powershell
./ngrok http 8000
# Copia la URL: https://abc123def.ngrok.io
```

### Paso 2: Verifica que funciona
```
Abre en navegador: https://abc123def.ngrok.io/docs
Deberías ver tu API
```

### Paso 3: En OpenAI (ChatGPT Plus)

**Opción A: Usar GPT Actions**
1. Ve a: https://chat.openai.com
2. Abre un chat
3. Haz clic en los 3 puntos (menú)
4. Selecciona "Configure GPT"
5. Ve a "Actions"
6. "Create new action"
7. Pega el schema de: `https://abc123def.ngrok.io/openapi.json`
8. Guarda

**Opción B: Usar en código Python** (más flexible)
```python
# Ver ejemplo arriba
```

### Paso 4: Usa en Claude

```
"Usa mi API en https://abc123def.ngrok.io para analizar..."
```

---

## ⚠️ IMPORTANTE: URLS DE NGROK CAMBIAN

Cada vez que reinicies ngrok, te da una URL diferente.

**Para URL permanente (necesitas cuenta ngrok):**
```powershell
./ngrok http 8000 --domain=mi-dominio.ngrok.io
```

---

## 🔒 SEGURIDAD: PROTEGER TU API

Si expones tu API a internet, considera protegerla:

### Opción 1: Clave API en tu MCP

Edita `http_server.py`:

```python
from fastapi import Header, HTTPException

@app.post("/api/v1/island-of-agreement")
async def api_island_of_agreement(
    request: IslandOfAgreementRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != "tu-clave-secreta":
        raise HTTPException(status_code=401, detail="Invalid API key")

    # ... resto del código
```

Luego usa con:
```bash
curl -H "X-API-Key: tu-clave-secreta" https://abc123def.ngrok.io/api/v1/...
```

### Opción 2: Usar Cloudflare con autenticación

Cloudflare te permite añadir autenticación automáticamente.

---

## 🚀 GUÍA RÁPIDA: DE 0 A 100

### Si quieres usar con OpenAI AHORA:

**1. Terminal 1 - Iniciar MCP:**
```powershell
cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"
docker-compose up -d
```

**2. Terminal 2 - Ejecutar ngrok:**
```powershell
./ngrok http 8000
# Copia: https://abc123def.ngrok.io
```

**3. En OpenAI:**
```
Copiar schema de: https://abc123def.ngrok.io/openapi.json
Ir a: https://chat.openai.com
Crear Action
Pegar schema
Usar en conversación
```

**4. Listo!** Tu MCP funciona con OpenAI. ✅

---

## 📝 EJEMPLOS LISTOS PARA COPIAR

### cURL a tu API (vía ngrok):
```bash
curl -X POST https://abc123def.ngrok.io/api/v1/island-of-agreement \
  -H "Content-Type: application/json" \
  -d '{
    "situation_description": "UN negotiating with government",
    "organization_name": "WFP",
    "counterpart_name": "Ministry"
  }'
```

### Python a OpenAI con tu MCP:
```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Usa mi API para analizar..."}],
    tools=[...]  # Ver ejemplo arriba
)
```

### JavaScript/Node.js:
```javascript
const fetch = require('node-fetch');

async function callMCP(path, data) {
    const response = await fetch(`https://abc123def.ngrok.io${path}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return response.json();
}

callMCP('/api/v1/island-of-agreement', {
    situation_description: "...",
    organization_name: "...",
    counterpart_name: "..."
});
```

---

## 🎯 RESUMEN: OPCIONES DISPONIBLES

| Caso de Uso | Solución | Dificultad |
|------------|----------|-----------|
| Usar en OpenAI | ngrok + OpenAI Actions | Fácil |
| Usar en Claude Web | ngrok + URL manual | Medio |
| Compartir con equipo | ngrok o Cloudflare | Fácil |
| Producción | Cloudflare Tunnel | Medio |
| API pública | Deploy en AWS/GCP | Difícil |

---

## ✨ PRÓXIMOS PASOS

1. **Instala ngrok**: https://ngrok.com/download
2. **Ejecuta**: `./ngrok http 8000`
3. **Prueba**: Ve a la URL que te da + `/docs`
4. **Integra**: Usa la URL con OpenAI o Claude

¿Necesitas ayuda con algo específico? 👇
