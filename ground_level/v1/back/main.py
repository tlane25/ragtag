from fastapi import FastAPI, File, UploadFile
# cors middleware tutorial https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware

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
    print(file)
    return {"filename": file.filename}