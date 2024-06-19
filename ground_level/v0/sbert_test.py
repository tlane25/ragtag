'''
Standalone test of SBERT sentence embedding (https://sbert.net/), simply run the file

'''

# SBERT sentence embedding model from https://sbert.net/
# installed w/pip: `pip install -U sentence-transformers`
# note: had to run VSCode as administrator to get install to work
from sentence_transformers import SentenceTransformer

# pretrained Sentence Transformer model copied from exmple found at:
# https://sbert.net/docs/quickstart.html#sentence-transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# seeing what happens when you model.encode a whole array of sentences
# not really using this here
# def sbert_encode_all_sentences(sentences):
#   # print('embedding an array of sentences:')
#   embeddings = model.encode(sentences) # this is where the embedding happens
#   return embeddings

# seeing what happens when you model.encode just one sentence string
def sbert_encode_individual_sentence(sentence):
  # print('embedding just one sentence:', sentence)
  embeddings = model.encode(sentence)
  # print('embeddings', embeddings)
  return embeddings

# random sentences to compare
sentence_a = 'cow duck dog bird iguana terrier bear'
sentence_b = 'cow duck dog bird iguana terrier ox'
sentence_c = 'none of the things i mentioned above will be mentioned here'
sentence_d = 'some animals i enjoy are dogs cats and birds but some animals i dont enjoy are chickens and lizards'

# display sentences
print()
print('Sentence A:', sentence_a)
print('Sentence B:', sentence_b)
print('Sentence C:', sentence_c)
print('Sentence D:', sentence_d)
print()

# embed each sentence using sbert's default model
embed_a = sbert_encode_individual_sentence(sentence_a)
embed_b = sbert_encode_individual_sentence(sentence_b)
embed_c = sbert_encode_individual_sentence(sentence_c)
embed_d = sbert_encode_individual_sentence(sentence_d)

# ask sbert to compare each sentence's embeddings to determine a "similarity tensor" (dunno if that's the right term)
# which returns something like `tensor([[0.30458]])` and then I use `.item()` to get just the `0.30458` (only works on
# tensors with single values like above, need to figure out something different when embedding more complex stuff i think)
should_be_similar = model.similarity(embed_a, embed_b).item() # `.item()` just extracts the value from the torch.Tensor obj
should_be_different = model.similarity(embed_a, embed_c).item()
should_be_somewhere_in_the_middle = model.similarity(embed_a, embed_d).item()

# print results
print('sentence A and B similarity (should be similar) = ', should_be_similar)
print('sentence A and C similarity (should be different) = ', should_be_different)
print('sentence A and D similarity (should be somwhere in the middle) = ', should_be_somewhere_in_the_middle)