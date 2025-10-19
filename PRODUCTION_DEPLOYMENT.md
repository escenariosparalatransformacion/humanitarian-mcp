# Despliegue en Producción - Disponible 24/7

Opciones para tener tu MCP disponible permanentemente sin tu computadora abierta.

---

## 🎯 OBJETIVO

Un servidor que:
- ✅ Esté **siempre disponible** (24/7)
- ✅ No dependa de tu computadora
- ✅ Sea **accesible desde cualquier lugar**
- ✅ Sea **fácil de mantener**
- ✅ Sea **asequible** (o gratis)

---

## 📊 OPCIONES COMPARADAS

| Opción | Costo | Facilidad | Uptime | Escala |
|--------|-------|-----------|--------|--------|
| AWS Lambda | $$$$ | Difícil | 99.99% | Ilimitada |
| Google Cloud Run | $$ | Fácil | 99.95% | Auto |
| Azure Container | $$ | Medio | 99.95% | Auto |
| Heroku | $$$ | Muy fácil | 99.9% | Media |
| Railway | $$ | Muy fácil | 99.9% | Media |
| Render | $$ | Muy fácil | 99.9% | Media |
| DigitalOcean | $ | Fácil | 99.9% | Manual |
| Replit | GRATIS | Muy fácil | 85% | Baja |

---

## 🥇 OPCIÓN 1: GOOGLE CLOUD RUN (RECOMENDADO)

**Mejor relación facilidad/precio/rendimiento**

### Ventajas:
- ✅ Gratis hasta 2 millones de solicitudes/mes
- ✅ Super fácil de desplegar
- ✅ Escala automática
- ✅ HTTPS automático
- ✅ Sin tarjeta de crédito para probar

### Paso 1: Crear cuenta Google Cloud

1. Ve a: https://cloud.google.com
2. Haz clic en "Comenzar gratis"
3. Crea tu cuenta (te dan $300 gratis)

### Paso 2: Crear proyecto

1. Ve a: https://console.cloud.google.com
2. En la parte superior, haz clic en "Crear proyecto"
3. Nombre: `humanitarian-mcp`
4. Clic en "Crear"

### Paso 3: Desplegar contenedor Docker

**Opción A: Usar Cloud Console (Visual)**

1. En la barra de búsqueda, escribe: `Cloud Run`
2. Haz clic en "Cloud Run"
3. Haz clic en "Crear servicio"
4. Selecciona "Desplegar desde un repositorio de código existente"
5. Conecta tu GitHub (o carga los archivos manualmente)
6. Selecciona:
   - Repositorio: Tu carpeta MCP
   - Rama: main
   - Dockerfile: Selecciona el Dockerfile
7. Haz clic en "Crear"

**Opción B: Usar CLI (Recomendado)**

```bash
# Instalar Google Cloud CLI
# Descarga desde: https://cloud.google.com/sdk/docs/install

# Luego:
gcloud auth login

gcloud config set project humanitarian-mcp

cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"

gcloud run deploy humanitarian-mcp \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

### Paso 4: ¡Listo!

Google te da una URL pública:
```
https://humanitarian-mcp-xyz123.a.run.app
```

Accede a:
```
https://humanitarian-mcp-xyz123.a.run.app/docs
```

---

## 🥈 OPCIÓN 2: RAILWAY (MÁS FÁCIL)

**La más fácil de todas. Literal: 3 clics.**

### Ventajas:
- ✅ Super intuitivo
- ✅ Integración con GitHub
- ✅ Despliegues automáticos
- ✅ $5/mes gratis

### Paso 1: Crear cuenta

1. Ve a: https://railway.app
2. Haz clic en "Sign up"
3. Conecta con GitHub

### Paso 2: Nuevo proyecto

1. Haz clic en "Create New Project"
2. Selecciona "Deploy from GitHub repo"
3. Conecta tu repositorio
4. Selecciona la rama

### Paso 3: Configurar

1. En "Service", haz clic en "Settings"
2. Selecciona "Dockerfile"
3. Haz clic en "Deploy"

¡**Listo!** Railway automáticamente:
- Construye tu imagen
- La despliega
- Te da una URL pública

---

## 🥉 OPCIÓN 3: RENDER

**También muy fácil, gratis con limitaciones**

### Paso 1: Crear cuenta

Ve a: https://render.com y regístrate

### Paso 2: Crear nuevo servicio

1. Dashboard → "New +"
2. Selecciona "Web Service"
3. Conecta GitHub
4. Selecciona tu repo

### Paso 3: Configurar

- Name: `humanitarian-mcp`
- Environment: Docker
- Plan: Free (o Starter $7/mes)

### Paso 4: Deploy

Haz clic en "Create Web Service"

¡Desplegado! Te da una URL como:
```
https://humanitarian-mcp.onrender.com
```

---

## 💪 OPCIÓN 4: DIGITALOCEAN (MÁS CONTROL)

**Si quieres más control sobre la infraestructura**

### Ventajas:
- ✅ Muy confiable
- ✅ Buena documentación
- ✅ Preciso: $5/mes
- ✅ Buen soporte

### Paso 1: Crear cuenta DigitalOcean

Ve a: https://www.digitalocean.com

### Paso 2: Crear App

1. Dashboard → "Apps"
2. "Create Apps"
3. Conecta GitHub
4. Selecciona repo

### Paso 3: Configurar

```yaml
name: humanitarian-mcp
services:
- name: api
  dockerfile: ./Dockerfile
  http_port: 8000
```

### Paso 4: Deploy

DigitalOcean despliega automáticamente.

URL:
```
https://humanitarian-mcp-xxxxx.ondigitalocean.app
```

---

## ☁️ OPCIÓN 5: AWS LAMBDA (SERVERLESS)

**Si quieres pay-per-use (solo pagas por lo que usas)**

### Ventajas:
- ✅ Muy barato (casi gratis si uso bajo)
- ✅ Escala infinita
- ✅ Muy confiable

### Desventaja:
- ❌ Más complejo de configurar

### Paso 1: Crear cuenta AWS

Ve a: https://aws.amazon.com

### Paso 2: Crear Function

```bash
# Instalar AWS CLI
pip install awscli

# Configurar credenciales
aws configure

# Empaquetar
zip -r function.zip . -x ".git/*" ".gitignore" "node_modules/*"

# Subir a Lambda
aws lambda create-function \
    --function-name humanitarian-mcp \
    --runtime python3.10 \
    --role arn:aws:iam::ACCOUNT-ID:role/lambda-role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip

# Crear API Gateway
aws apigateway create-rest-api \
    --name humanitarian-mcp-api
```

**Más fácil:** Usa AWS Console

---

## 🎯 OPCIÓN 6: GITHUB PAGES + WORKERS (GRATUITO)

**Para máximo ahorro (completamente gratis)**

### Usar Cloudflare Workers

```bash
# Instalar Wrangler
npm install -g wrangler

# Crear proyecto
wrangler init humanitarian-mcp

# Desplegar
wrangler publish
```

Te da URL:
```
https://humanitarian-mcp.workers.dev
```

---

## 🚀 MÍ RECOMENDACIÓN FINAL

### Para comenzar (GRATIS):
**Google Cloud Run**
- Gratis hasta 2M requests/mes
- Muy fácil
- Profesional
- Sin tarjeta de crédito

### Para producción (BARATO):
**Railway** ($5/mes) o **Render** ($7/mes)
- Super fácil
- Automático
- Muy confiable
- Despliegues automáticos en cada push a GitHub

### Para empresa (ROBUSTO):
**DigitalOcean** ($5/mes) o **AWS**
- Más control
- Mejor documentación
- Soporte 24/7
- Infraestructura profesional

---

## 📋 GUÍA RÁPIDA: GOOGLE CLOUD RUN (RECOMENDADO)

### Requisitos:
- Cuenta Google
- Git/GitHub

### Paso 1: Sube a GitHub

```bash
git init
git add .
git commit -m "Humanitarian MCP"
git remote add origin https://github.com/tuusuario/humanitarian-mcp
git push -u origin main
```

### Paso 2: Crea proyecto en Google Cloud

1. Ve a: https://console.cloud.google.com
2. Crea proyecto: `humanitarian-mcp`
3. Activa Cloud Run

### Paso 3: Deploy

```bash
# Instalar Google Cloud CLI
# https://cloud.google.com/sdk/docs/install

gcloud auth login
gcloud config set project humanitarian-mcp

cd "C:\Users\Jhozman Camacho\Downloads\FACT Negotiator MCP"

gcloud run deploy humanitarian-mcp \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

### Paso 4: ¡Listo!

Google te da tu URL:
```
https://humanitarian-mcp-abc123.a.run.app
```

**Disponible 24/7 sin hacer nada más.**

---

## 🔗 USAR TU MCP PRODUCTIVO

Una vez desplegado, simplemente cambia URLs:

**Antes (con ngrok):**
```
https://abc123.ngrok.io/api/v1/island-of-agreement
```

**Ahora (en producción):**
```
https://humanitarian-mcp-abc123.a.run.app/api/v1/island-of-agreement
```

**Funciona con:**
- ✅ OpenAI
- ✅ Claude Web
- ✅ Cualquier aplicación
- ✅ Integraciones (Zapier, IFTTT)

---

## 📊 COSTOS ESTIMADOS/MES

| Servicio | Costo Mínimo | Incluye |
|----------|------------|---------|
| Google Cloud Run | GRATIS | 2M requests |
| Railway | $5 | Almacenamiento + Requests |
| Render | $7 | Todo ilimitado |
| DigitalOcean | $5 | App + Database |
| AWS Lambda | $0-$5 | Según uso |
| Heroku | $0 (deprecado) | Obsoleto |

---

## 🔒 SEGURIDAD EN PRODUCCIÓN

### Agregar Autenticación

En tu `http_server.py`:

```python
from fastapi import Header, HTTPException

API_KEY = "tu-clave-super-secreta"

@app.post("/api/v1/island-of-agreement")
async def api_island_of_agreement(
    request: IslandOfAgreementRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # ... resto del código
```

### Usar como variable de entorno

En Google Cloud Run, DigitalOcean, etc.:

```bash
# Deployment
gcloud run deploy humanitarian-mcp \
    --set-env-vars API_KEY=tu-clave-secreta \
    ...
```

En el código:

```python
import os
API_KEY = os.getenv("API_KEY")
```

---

## 📈 MONITOREO

### Google Cloud:
```bash
gcloud run services describe humanitarian-mcp
```

### Railway/Render:
Dashboard visual en web

### Alertas:
Configura notificaciones si el servicio cae

---

## 🎯 PRÓXIMOS PASOS

### Opción A: Google Cloud Run (RECOMENDADO)

1. Crea cuenta: https://cloud.google.com
2. Sigue la guía rápida arriba
3. ¡Listo en 5 minutos!

### Opción B: Railway (MÁS FÁCIL)

1. Ve a: https://railway.app
2. Conecta GitHub
3. 3 clics y listo

### Opción C: Render

1. Ve a: https://render.com
2. Conecta GitHub
3. Deploy automático

---

## ✨ VENTAJAS DE PRODUCCIÓN

Una vez desplegado:

✅ **Tu MCP está siempre disponible**
✅ **No necesitas ngrok abierto**
✅ **No necesitas tu computadora encendida**
✅ **URL permanente y profesional**
✅ **Pueden acceder desde cualquier lugar**
✅ **Escala automáticamente**
✅ **HTTPS automático**
✅ **Monitoreo incluido**

---

## 🚀 CONCLUSIÓN

**Para desarrollo/pruebas:** ngrok + local
**Para pequeña empresa:** Railway o Render
**Para producción real:** Google Cloud Run o DigitalOcean
**Para gran escala:** AWS o Google Cloud Platform

¿Cuál prefieres? Te ayudo a configurarla. 👇
