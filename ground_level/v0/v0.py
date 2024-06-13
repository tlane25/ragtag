'''
Here we will implement a simple search engine that will return a meditation that
is most similar to the query by chunking both the query and the documents into words
and then calculating the jaccard similarity between the two.
'''

# SBERT sentence embedding model from https://sbert.net/
# installed w/pip: `pip install -U sentence-transformers`
# note: had to run VSCode as administrator to get install to work
from sentence_transformers import SentenceTransformer

meditations = [
    "Reflect each day on the brevity of life. Remember that you are mortal, and let this realization sharpen your focus and humility in all your endeavors.",
    "Consider the nature of things. All that exists does so for a reason, and in understanding this, you find peace and acceptance of the universe's order.",
    "When faced with adversity, remember that it is not the event itself that troubles you, but your perception of it. Adjust your thoughts and the world will seem more bearable.",
    "Cultivate a spirit of gratitude. Every moment is a gift, and every challenge an opportunity for growth. Embrace life with an open heart and a willing mind.",
    "Do not be swayed by the opinions of others. Your path is your own, and true wisdom lies in knowing oneself and remaining steadfast in one's principles.",
    "The pursuit of virtue is the highest good. In all things, strive to act with justice, temperance, courage, and wisdom. These are the pillars of a noble life.",
    "Contemplate the vastness of time and the insignificance of your own existence. In this perspective, find liberation from the trivial concerns that plague daily life.",
    "Understand that all is transient. Just as the seasons change, so too do fortunes and sorrows. Embrace the flow of life with serenity and equanimity.",
    "Practice mindfulness in every action. Whether great or small, let each deed be done with full attention and a clear conscience, for this is the essence of living well.",
    "Remember that your mind is sovereign. External circumstances may be beyond your control, but your thoughts and attitudes are always within your command.",
    "Seek harmony with nature. Recognize that you are a part of a larger whole, and in aligning your will with the natural order, you will find true peace.",
    "Cherish your connections with others, but do not become dependent on them for your happiness. True contentment comes from within, and not from external sources.",
    "Reflect on the impermanence of all things. Every beginning has an end, and in this cyclical nature, find the wisdom to live fully in the present moment.",
    "Pursue knowledge and understanding, for ignorance is the root of many ills. Through learning, we cultivate the mind and better our capacity to contribute to the world.",
    "Cultivate a spirit of humility. No one is infallible, and recognizing your own limitations allows for growth and the true appreciation of the strengths of others.",
    "Embrace simplicity in all things. Extravagance and excess often lead to distraction and dissatisfaction. True contentment is found in appreciating the simple and essential.",
    "Let your actions be guided by reason and virtue, rather than by impulse or desire. This is the path to a life of purpose and integrity.",
    "Recognize the interconnectedness of all beings. Your actions have repercussions beyond your own life. Act with compassion and consider the broader impact of your choices.",
    "Maintain a spirit of resilience. Life's trials are opportunities to cultivate strength and perseverance. Face each challenge with dignity and resolve.",
    "Accept that some things are beyond your control. Focus on what you can change, and let go of the rest. This is the essence of inner tranquility and wisdom."
]

def jaccard_similarity(query, document):
  query = query.lower().split(' ')
  document = document.lower().split(' ')
  intersection = set(query).intersection(set(document))
  union = set(query).union(set(document))
  return len(intersection)/len(union)

def return_response(query, corpus):
  similarities = []
  for doc in corpus:
    similarity = jaccard_similarity(query, doc)
    similarities.append(similarity)
  
  return meditations[similarities.index(max(similarities))]

# pretrained Sentence Transformer model copied from exmple found at:
# https://sbert.net/docs/quickstart.html#sentence-transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# seeing what happens when you model.encode a whole array of sentences
def sbert_encode_all_sentences(sentences):
  print('embedding an array of sentences:')
  embeddings = model.encode(sentences)
  print('embeddings', embeddings)
  print('embedding shape', embeddings.shape)

# seeing what happens when you model.encode just one sentence string
def sbert_encode_individual_sentence(sentence):
  print('embedding just one sentence:')
  embeddings = model.encode(sentence)
  print('embeddings', embeddings)
  print('embedding shape', embeddings.shape)

sbert_encode_all_sentences(meditations)
sbert_encode_individual_sentence(meditations[0])


# keep_going = True

# while keep_going:
#   user_query = input('What topic do you want your meditation to be?')
#   best_match = return_response(user_query, meditations)
#   print(best_match)
#   keep_going = False
#   again = input('Would you like to go again?(y/n)')
#   keep_going = True if again == 'y' else False


'''
The trouble with this is that if the input prompt and the related strings have no
common words, then there is no similarity and the first meditation will be returned
Another issue is that the token invovled is a whole word and one word may have a 
variety of meaning. Here when I type "nature" looking for qoutes related to the natural world, 
I get a qoute about the nature of things. more about the characteristics. 

You could also query "Anything but nature" 
This is another issue of semantics
'''