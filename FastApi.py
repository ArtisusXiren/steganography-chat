#!/usr/bin/env python
# coding: utf-8

from Steganography import encode , decode
import io
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI,File,Form,UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.mount("/", StaticFiles(directory="build", html=True), name="static")
@app.get("/")
def read_index():
    html_file = os.path.join(os.path.dirname(__file__), "build", "index.html")
    return HTMLResponse(content=open(html_file, "r").read(), media_type="text/html")
@app.post('/send')
async def send(message: str= Form(...),image:UploadFile=File(...)):
    encoded_image=encode(image,message)
    byte_arr=io.BytesIO()
    encoded_image.save(byte_arr,format='PNG')
    byte_arr.seek(0)
    return StreamingResponse(byte_arr,media_type="image/png")
@app.post('/receive')
async def receive(image:UploadFile=File(...)):
    message=decode(image)
    return{"message":message}







