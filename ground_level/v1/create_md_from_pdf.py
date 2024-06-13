'''
V1 to improve on the previous one in the following ways:
[X] Create a markdown file from a pdf
[] Chunk the markdown file into sentences
[] We will embed the sentences using a pre-trained model
[] We will store the embeddings in a database
[] We will embed the user query and perform vector search
[] We will return the top 3 most similar sentences and combine them into a 
   prompt along with the user query and send to open ai for a response

Looming Questions:
PDF Chunking:
  - Is it possible to extract text from the pdf into markdown? YES!
  - If the pdf has a table of contents, is it possible to extract and use for text
  - How large should the chunks be? Should we chunk by sentence or paragraph?

Document Storage:
  - Should we store a copy of the raw text in a database? Thinking there could be 
    a benefit to having the embeddings link to the raw text. This way, if the

'''
# standard libraries
import os as oz # the great and powerful
import pathlib as pl # for path manipulation

# non-standard libraries
import pymupdf as pym # PyMuPDF for pdf extraction
import pymupdf4llm as pmll # for markdown extraction

pdf = pym.open('./AsyncJS.pdf')
markdown = pmll.to_markdown(pdf)

pl.Path('./AsyncJS.md').write_bytes(markdown.encode())