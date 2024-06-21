from fastapi import FastAPI, File, UploadFile
# cors middleware tutorial https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware
from services import process

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

@app.post("/api/upload")
async def process_file(file: UploadFile = File(...)):
    sentences = await process.pdf(file)
    print(sentences[30])
    return {"filename": file.filename}

