from fastapi import FastAPI, File, UploadFile
# cors middleware tutorial https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware
import pymupdf as pym
import spacy
import io

nlp = spacy.load("en_core_web_sm")
app = FastAPI()


# .add_middleware: 
app.add_middleware(
    CORSMiddleware,
    # allow_origins val should be string array of allowed crossorigin requests
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/path/{id}")
async def toot(id):
    return {"message": id,
            "type": type(id)}

@app.post("/api/upload")
async def uploadFile(file: UploadFile = File(...)):
    file_bytes = await file.read()
    file_buffer = io.BytesIO(file_bytes)

    pdf = pym.open(stream=file_buffer, filetype="pdf")
    text = ""

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text += page.get_text()

    print(text[1000:2000])

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    print(sentences[50])

    return {"filename": file.filename}