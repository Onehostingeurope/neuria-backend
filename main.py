from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# Autoriser tous les domaines (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clé OpenAI depuis les variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

class SearchRequest(BaseModel):
    query: str

@app.post("/search")
async def search_ai(request: SearchRequest):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Tu es un moteur de recherche intelligent qui résume les meilleurs résultats web."},
                {"role": "user", "content": f"Résume les 3 meilleurs résultats web pour : {request.query}"}
            ]
        )
        return {"summary": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}