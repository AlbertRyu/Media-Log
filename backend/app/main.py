from fastapi import FastAPI

app = FastAPI(title='MediaLog API')

@app.get('/')
def root():
    return {"status": "ok", "app": "media-log"}

@app.get('/api/hello')
def root():
    return {"message": "Hello from FastAPI", "source": "backend"}