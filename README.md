# NEURIA Backend (FastAPI)

Ce projet est le backend API de NEURIA, un moteur de recherche assisté par IA.

## Installation locale

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Déploiement Render

**Build Command:**  
```bash
pip install -r requirements.txt
```

**Start Command:**  
```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

**Environment Variable:**

| Key | Value |
|-----|-------|
| OPENAI_API_KEY | ta clé OpenAI |

## Route principale

POST /search  
Payload : `{ "query": "ta question" }`