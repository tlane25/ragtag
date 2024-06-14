Each file has it's own instructions/explanations along with it so dig in. Here's an overview of what's available:

File Guide:
v0:
 - v0.py          -> simple program for retrieving 'documents' that match a query (using word counts)
 - sbert_test.py  -> simple embedding test to see how sentences can be compared with each other using SBERT
 - v0.2.py        -> same goal as v0.py except using SBERT embedding/comparing in place of word counts
 - openai_test.py -> simple OpenAI query + console-printed response, requires OpenAI acc and billing info but is pretty cheap
 - v0.3.py        -> WIP; hopefully will combine the retrieval of v0.2.py with some generation (put the G in RAG) 