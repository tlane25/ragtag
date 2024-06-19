Welcome!

__Research Questions__
What type of files should we focus on?
How should we best chunk according to file size?
How should we best chunk according to embedded model?
How should we best embed according to size and number of chunks?





6/13/23: Notes with James

Python/ JS backend microservices communicate with gRPC

hard to find tools to test gRPC, potential project in there

config details of RAG may be varied enough over a wide array of documents (chunking/embedding/query match) that we may be better suited solving a very specific RAG problem(maybe product makes more sense)

Embedding models have an upper limit, maybe could use that upper limit as a "max" chunk size, then provide goldilocks options for chunk size/ overlap/ embedding model. (maybe RAGaaS is feasible )

