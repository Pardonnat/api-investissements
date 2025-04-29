from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API d'investissements !"}

@app.get("/investissements")
def liste_investissements():
    return ["Actions", "Obligations", "Immobilier", "Crowdfunding"]
