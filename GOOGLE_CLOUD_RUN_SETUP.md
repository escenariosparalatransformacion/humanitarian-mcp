# Desplegar en Google Cloud Run - Guía Paso a Paso

Tu MCP disponible 24/7, gratis. Tarda 10 minutos.

---

## 🎯 QUÉ VAMOS A LOGRAR

```
Tu computadora local → GitHub → Google Cloud Run
                                    ↓
                        URL pública: https://mi-mcp.a.run.app
                        Disponible 24/7, sin tener nada abierto
```

---

## 📋 REQUISITOS

- ✅ GitHub (gratis)
- ✅ Google Cloud (gratis con $300)
- ✅ Tu carpeta del MCP en GitHub

---

## 🚀 PASO 1: CREAR REPOSITORIO EN GITHUB

### 1.1 Ve a GitHub

https://github.com/new

### 1.2 Crea un nuevo repositorio

**Nombre:** `humanitarian-mcp`

**Descripción:** `Humanitarian Negotiation MCP Server`

**Visibilidad:** Public (para que funcione el deploy automático)

**Haz clic en:** "Create repository"

### 1.3 Copia del repositorio

Verás una URL como:
```
https://github.com/tu-usuario/humanitarian-mcp
```

Cópiala.

---

## 💻 PASO 2: SUBE TU CÓDIGO A GITHUB

### 2.1 Abre PowerShell en tu carpeta MCP

```powershell
cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"
```

### 2.2 Inicializa Git

```powershell
git init
```

### 2.3 Agrega tu repositorio remoto

```powershell
git remote add origin https://github.com/tu-usuario/humanitarian-mcp
```

(Reemplaza `tu-usuario` con tu usuario de GitHub)

### 2.4 Agrega todos los archivos

```powershell
git add .
```

### 2.5 Haz el primer commit

```powershell
git commit -m "Initial commit: Humanitarian Negotiation MCP"
```

### 2.6 Push a GitHub

```powershell
git branch -M main
git push -u origin main
```

**Te pedirá autenticación.** Sigue las instrucciones de GitHub.

---

## ☁️ PASO 3: CONFIGURAR GOOGLE CLOUD

### 3.1 Crear cuenta Google Cloud

1. Ve a: https://cloud.google.com/free
2. Haz clic en "Get started for free"
3. Crea tu cuenta con tu Gmail
4. Acepta los términos

Te dan **$300 de crédito gratis** para probar.

### 3.2 Crear un proyecto

1. Ve a: https://console.cloud.google.com
2. En la parte superior izquierda, haz clic en "Select a Project"
3. Haz clic en "NEW PROJECT"
4. **Nombre del proyecto:** `humanitarian-mcp`
5. Haz clic en "CREATE"

**Espera unos segundos a que se cree.**

### 3.3 Habilitar Cloud Run API

1. En la barra de búsqueda (arriba), escribe: `Cloud Run`
2. Haz clic en "Cloud Run"
3. Si sale un mensaje de "Enable API", haz clic en "ENABLE"
4. Espera a que se habilite (1-2 minutos)

---

## 🚢 PASO 4: DESPLEGAR TU MCP

### Opción A: Usando Google Cloud Console (Visual - RECOMENDADO)

#### 4.1 Ve a Cloud Run

En Google Cloud Console, busca y abre "Cloud Run"

#### 4.2 Crea un nuevo servicio

Haz clic en "Create Service"

#### 4.3 Configura la fuente

- Selecciona: "Deploy from a Git repository"
- Haz clic en "Set up with Cloud Build"

#### 4.4 Conecta GitHub

- Haz clic en "Connect to a repository"
- Selecciona "GitHub" (necesitará permisos)
- Autoriza a Google Cloud para acceder a GitHub
- Selecciona tu repositorio: `humanitarian-mcp`

#### 4.5 Configura el deployment

**Settings:**
- **Source:** GitHub
- **Repository:** humanitarian-mcp
- **Branch:** main
- **Build type:** Dockerfile

#### 4.6 Configura el servicio

- **Service name:** `humanitarian-mcp`
- **Region:** `us-central1` (recomendado)
- **Memory:** `512 MB` (suficiente)
- **CPU:** `1 CPU` (suficiente)
- **Timeout:** `300` segundos

#### 4.7 Deployment settings

- **CPU is only allocated during request processing:** Sí (para ahorrar)
- **Authentication:** Require authentication → **NO** (para que todos accedan)

#### 4.8 ¡Desplega!

Haz clic en "Create"

**Espera 3-5 minutos.** Google:
- Descarga tu código de GitHub
- Construye la imagen Docker
- La despliega
- Te da una URL pública

---

### Opción B: Usando CLI (Terminal - MÁS RÁPIDO)

#### 4.1 Instala Google Cloud CLI

Ve a: https://cloud.google.com/sdk/docs/install

Para Windows:
1. Descarga el instalador
2. Ejecuta
3. Sigue las instrucciones

#### 4.2 Configura Google Cloud CLI

```powershell
gcloud init
```

Te pedirá:
1. Elige tu cuenta Google
2. Selecciona el proyecto: `humanitarian-mcp`
3. Selecciona región: `us-central1`

#### 4.3 Deploy

```powershell
cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"

gcloud run deploy humanitarian-mcp `
    --source . `
    --platform managed `
    --region us-central1 `
    --allow-unauthenticated `
    --memory 512Mi `
    --cpu 1 `
    --timeout 300
```

**Espera 3-5 minutos.**

---

## ✅ PASO 5: OBTÉN TU URL

Google te mostrará algo como:

```
Service [humanitarian-mcp] revision [humanitarian-mcp-00001-abc] has been deployed and is serving 100% of traffic.

Service URL: https://humanitarian-mcp-abc123xyz.a.run.app
```

**COPIA ESTA URL.** Es la tuya permanente.

---

## 🧪 PASO 6: PRUEBA QUE FUNCIONA

### Prueba 1: Health check

```powershell
curl https://tu-url.a.run.app/health
```

Deberías ver:
```json
{"status":"operational",...}
```

### Prueba 2: Abre en navegador

```
https://tu-url.a.run.app/docs
```

Deberías ver la interfaz de Swagger con todos tus tools. ✅

---

## 🔄 PASO 7: ACTUALIZACIONES AUTOMÁTICAS

**Lo mejor de Google Cloud Run:** Los cambios se despliegan automáticamente.

### Cuando hagas cambios:

```powershell
cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"

# Modifica tus archivos aquí

git add .
git commit -m "Update: descripción del cambio"
git push origin main
```

**Automáticamente:**
1. GitHub recibe el push
2. Cloud Build construye la imagen
3. Cloud Run despliega
4. Tu URL se actualiza (en 2-3 minutos)

---

## 💰 COSTOS

### Plan gratuito:

- ✅ 2 millones de solicitudes/mes
- ✅ 360,000 GB-segundos/mes
- ✅ 180,000 vCPU-segundos/mes

**Para tu MCP:** Completamente **GRATIS** en el plan gratuito.

### Si usas más:

Después del límite gratuito:
- ~$0.00002400 por solicitud
- ~$0.00001667 por GB-segundo

**Incluso con uso medio, menos de $5/mes.**

---

## 📊 MONITOREAR TU MCP

### En Google Cloud Console:

1. Ve a Cloud Run
2. Haz clic en `humanitarian-mcp`
3. Verás:
   - Solicitudes/min
   - Latencia
   - Errores
   - Logs en tiempo real

### Ver logs:

```powershell
gcloud run logs read humanitarian-mcp --limit 50
```

### Si algo falla:

1. Ve a la consola
2. Haz clic en tu servicio
3. Ve a la pestaña "Logs"
4. Busca los errores

---

## 🔒 AGREGAR SEGURIDAD (OPCIONAL)

Si quieres proteger tu API con clave:

### 1. Edita `http_server.py`:

```python
from fastapi import Header, HTTPException
import os

API_KEY = os.getenv("API_KEY", "default-key")

@app.post("/api/v1/island-of-agreement")
async def api_island_of_agreement(
    request: IslandOfAgreementRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    # ... resto del código
```

### 2. En Google Cloud:

1. Ve a Cloud Run
2. Haz clic en `humanitarian-mcp`
3. Haz clic en "Edit and Deploy New Revision"
4. En "Runtime settings" → "Environment variables"
5. Agrega: `API_KEY` = `tu-clave-secreta`
6. Deploy

### 3. Usa tu API:

```bash
curl -H "X-API-Key: tu-clave-secreta" \
    https://tu-url.a.run.app/api/v1/island-of-agreement
```

---

## 🎯 RESUMEN: DESPUÉS DEL DEPLOYMENT

Tienes una URL pública como:
```
https://humanitarian-mcp-abc123.a.run.app
```

Que:
- ✅ Está disponible 24/7
- ✅ No necesita tu computadora encendida
- ✅ No necesita ngrok
- ✅ Es gratis (hasta 2M requests/mes)
- ✅ Escala automáticamente
- ✅ Se actualiza automáticamente desde GitHub

---

## 🔗 USA ESTA URL EN:

### OpenAI
Reemplaza ngrok URL por tu URL de Google Cloud Run en OpenAI Actions.

### Claude Web
Usa la URL directamente en tus prompts.

### Integraciones
Usa en Zapier, IFTTT, o cualquier aplicación.

---

## 🆘 PROBLEMAS COMUNES

### Error: "Permission denied"
**Solución:** Asegúrate que tu repositorio es **Public** en GitHub

### Error: "Build failed"
**Solución:** Revisa los logs en Cloud Build
```powershell
gcloud builds log
```

### La URL no responde
**Solución:** Espera 5 minutos después del deploy. Google puede tardar.

### "502 Bad Gateway"
**Solución:** Revisa que el puerto sea 8000 en Dockerfile

---

## 🚀 PRÓXIMOS PASOS

1. ✅ Crear repositorio GitHub
2. ✅ Subir código a GitHub
3. ✅ Crear cuenta Google Cloud
4. ✅ Desplegar en Cloud Run
5. ✅ Obtener URL pública
6. ✅ Usar en OpenAI/Claude/etc

**¡Listo! Tu MCP en producción.** 🎉

---

## 📚 RECURSOS

- Google Cloud Run Docs: https://cloud.google.com/run/docs
- Cloud Build: https://cloud.google.com/build/docs
- Dockerfile Reference: https://docs.docker.com/engine/reference/builder/

---

¿Necesitas ayuda en algún paso? 👇
