from fastapi import FastAPI

app = FastAPI(
    title="API Investissements",
    description="API pour informer sur différents types d'investissements.",
    version="1.0.0",
    servers=[
        {
            "url": "https://api-investissements.onrender.com",
            "description": "Serveur Render"
        }
    ]
)

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API d'investissements !"}

@app.get("/investissements")
def liste_investissements():
    return ["Actions", "Obligations", "Immobilier", "Crowdfunding"]
