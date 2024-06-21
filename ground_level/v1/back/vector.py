from pymilvus import MilvusClient
from pymilvus import model


client = MilvusClient("vector.db")

# This should delete the collection upon each backend server restart. 
# We will want to change this to preserve our embeddings
# over time. 
if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    # I assume tweeking the dimensionality of vectors is variable we'll need to 
    # tweek. I expect it's effects reach chunksize, embedding model, similarity search accuracy
    # and speed 
    dimension=768,
)

# many embedding models to choose from with milvus
# https://milvus.io/docs/embeddings.md
embedding_fn = model.DefaultEmbeddingFunction()

def embed_and_insert(sentences):
    data = embed_sentences(sentences)
    insert_result = insert_data_into_collection(data)
    return insert_result

# embeds sentences into vectors
# creates a list of dictionaries for the vector_db
def embed_sentences(sentences):
    # here we create a list of embeddings by passing the
    # list of sentences into `embedding_fn.encode_documents`
    #
    vectors = embedding_fn.encode_documents(sentences)

    # creates an array of dictionaries via list comprehension
    # each with id, vector, text, and subject
    data = [
      {"id": i, "vector": vectors[i], "text": sentences[i], "subject":"crucial conversations" }
      for i in range(len(vectors))
    ]

    print("Data has", len(data), "entities, each with fields: ", data[0].keys())
    return data


# inserts data into the collection
def insert_data_into_collection(data):
    # collection_name should match the name of the collection you want
    # to insert into... duh
    result = client.insert(collection_name="demo_collection", data=data)

    print(result)
    return result


# for skateboard, it may be wise to limit the queries down to one sentence
# though we can likely test how longer sentences do
def process_query(query):
    query_vectors = embedding_fn.encode_queries(query)

    result = client.search(
        collection_name="demo_collection",
        data=query_vectors,
        limit=3,
        output_fields=["text"]
    )

    print(result)
    return result