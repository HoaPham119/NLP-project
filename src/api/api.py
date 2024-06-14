from fastapi import FastAPI
import uvicorn
import asyncio


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

def API():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    API()

