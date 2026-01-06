from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend live, stable, minimal"}

@app.get("/health")
def health():
    return {"ok": True}
