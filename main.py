#run command: conda activate
#run command: fastapi dev main.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, World!'}