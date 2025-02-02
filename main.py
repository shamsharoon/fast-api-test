from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Heroku!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
