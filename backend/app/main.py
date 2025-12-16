from fastapi import FastAPI

app = FastAPI(title='MediaLog API')

@app.get('/')
def root():
    return {"status": "ok", "app": "media-log"}