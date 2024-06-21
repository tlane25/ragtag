from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
# cors middleware tutorial https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware

import process
import vector as vdb
from process_prompt import process_prompt




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
    print("processing file...")
    sentences = await process.pdf(file)
    print("file processed. embedding and inserting into db...")
    result = vdb.embed_and_insert(sentences)
    return {"message": f"{result['insert_count']} entries added to database"}

class UserQuery(BaseModel):
    query: str

@app.post("/api/query")
async def post_query(query: UserQuery):
    print('user query: ', query)
    matches = await vdb.process_query(query)
    print('matches: ', matches)
    response = await process_prompt(query, matches)
    return { "type": "response", "body": response }


