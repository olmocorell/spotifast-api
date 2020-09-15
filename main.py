from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello word"}


@app.get("/callback")
def errorapi():
    return {"message":"Callback Spotify Api"}
