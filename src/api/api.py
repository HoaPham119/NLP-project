from fastapi import FastAPI
import uvicorn
import asyncio
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from src.api.pre_processing import *

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


@app.get("/api/v1/pre-processing")
async def api_preprocess_text(text: str,
                    clean: bool = True,
                    standardized: bool = True,
                    split_word: bool = True,
                    split_sent: bool = True,
                        ):
    text = preprocess_text(text=text,
                           clean = clean,
                        standardized = standardized,
                        split_word = split_word,
                        split_sent = split_sent
                        )
    return {"data": text}

# @app.get("/normalize/{text}")
# async def api_normalize_text(text):
#     text = normalize_text(text=text)
#     return {"data": text}

def API():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    API()

