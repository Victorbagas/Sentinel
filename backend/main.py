
from fastapi import FastAPI

app = FastAPI(title="Backend Platform")

@app.get("/")
def root():
    return {"message": "Project running successfully"}
