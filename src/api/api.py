
from fastapi import FastAPI
import uvicorn
import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from src.api.pre_processing import *

app = FastAPI()

@app.get("/api/v1/pre-processing")
async def api_preprocess_text(text: str,
                            clean_html: bool = True,
                            clean_special_char: bool = True,
                            clean_extra_whitespace: bool = True,
                            chuan_hoa_unicode_action: bool = True,
                            chuan_hoa_chu_thuong: bool = True,
                            chuan_hoa_dau_thanh: bool = True,
                            chuan_hoa_dau_cau:bool = True,
                              split_word: bool = True,
                              split_sent: bool = True,
                              remove_sw: bool=True
                              ):
    text = preprocess_text(text=text,
                           clean_html=clean_html,
                           clean_special_char=clean_special_char,
                           clean_extra_whitespace=clean_extra_whitespace,
                           chuan_hoa_unicode_action=chuan_hoa_unicode_action,
                           chuan_hoa_chu_thuong=chuan_hoa_chu_thuong,
                           chuan_hoa_dau_thanh=chuan_hoa_dau_thanh,
                           chuan_hoa_dau_cau=chuan_hoa_dau_cau,
                           split_word=split_word,
                           split_sent=split_sent,
                           remove_sw =remove_sw
                           )
    return {"data": text}


def API():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    API()
