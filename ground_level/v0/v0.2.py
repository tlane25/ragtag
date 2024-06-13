'''
Here we will implement a simple search engine that will return advice that
is most similar to the query by:

    using SBERT's default embedding model.

example good request: when should i confide in my friend
example bad request: my toupee keeps sliding off and i can never find it once it hits the ground

got a little carried away with the fluff stuff; this is just basic proof of concept for embedding
'''

# SBERT sentence embedding model from https://sbert.net/
# installed w/pip: `pip install -U sentence-transformers`
# note: had to run VSCode as administrator to get install to work
from sentence_transformers import SentenceTransformer

# pretrained Sentence Transformer model copied from exmple found at:
# https://sbert.net/docs/quickstart.html#sentence-transformer
model = SentenceTransformer("all-MiniLM-L6-v2")


advice_list = [
    "Always save a portion of your income for emergencies.",
    "Remember to floss daily for good dental hygiene.",
    "When hiking, let someone know your plans and expected return time.",
    "Rotate your passwords regularly to enhance online security.",
    "When cooking, taste your food as you go and adjust seasoning accordingly.",
    "Check your car's tire pressure regularly to improve fuel efficiency.",
    "When giving a presentation, make eye contact with your audience.",
    "Before signing a contract, read it thoroughly and understand all terms.",
    "When traveling, keep copies of important documents in a separate location.",
    "When meeting someone new, repeat their name to help remember it.",
    "When trying to solve a problem, break it down into smaller, manageable tasks.",
    "Invest in a comfortable mattress for better sleep quality.",
    "Practice deep breathing exercises to reduce stress and anxiety.",
    "When starting a new job, take time to learn the company culture.",
    "When shopping for groceries, make a list to avoid impulse purchases.",
    "Regularly back up important files and documents to prevent data loss.",
    "When exercising, focus on form to prevent injury.",
    "Take breaks during long periods of screen time to rest your eyes.",
    "When painting a room, use painter's tape to achieve clean lines.",
    "When trying a new hobby, be patient with yourself and embrace the learning process.",
    "When giving feedback, focus on specific actions rather than generalizations.",
    "When studying, find a quiet and comfortable space to minimize distractions.",
    "When facing criticism, consider the source and whether it's constructive.",
    "When trying to make a decision, weigh the pros and cons before acting.",
    "When feeling overwhelmed, prioritize tasks and tackle them one at a time.",
    "When traveling abroad, research local customs and etiquette beforehand.",
    "When sending an important email, proofread it carefully before hitting send.",
    "When investing in stocks, diversify your portfolio to spread risk.",
    "When facing adversity, focus on solutions rather than dwelling on problems.",
    "When cooking with spices, start with a small amount and add more to taste.",
    "When learning a new language, practice speaking with native speakers whenever possible.",
    "When budgeting, allocate funds for both needs and wants.",
    "When giving a gift, consider the recipient's interests and preferences.",
    "When attending a job interview, research the company beforehand to show interest.",
    "When cleaning, start from the top of the room and work your way down.",
    "When driving in unfamiliar areas, use GPS or maps to avoid getting lost.",
    "When practicing a musical instrument, focus on mastering one technique at a time.",
    "When writing, vary your sentence structure to keep readers engaged.",
    "When facing a difficult decision, consult trusted friends or mentors for advice.",
    "When participating in a debate, listen to opposing viewpoints with an open mind.",
    "When cooking pasta, reserve some pasta water to add to sauces for extra flavor.",
    "When exercising outdoors, wear sunscreen to protect your skin from UV rays.",
    "When planting a garden, choose plants that are well-suited to your climate.",
    "When learning a new skill, break it down into smaller, achievable milestones.",
    "When attending a social event, be present and engage with others rather than checking your phone.",
    "When trying to improve a relationship, communicate openly and honestly with your partner.",
    "When practicing meditation, focus on your breath to center your mind.",
    "When facing a challenge, remind yourself of past successes to boost confidence.",
    "When volunteering, choose causes that align with your values and interests."
]

# gets similarity tensor from query sentence + 'document' sentence
def sbert_embed_similarity_score(query, document_sentence):
  query_embed = model.encode(query)
  doc_embed = model.encode(document_sentence)
  tensor = model.similarity(query_embed, doc_embed) # `type(tensor))` => <class 'torch.Tensor'> (https://pytorch.org/docs/stable/torch.html)
  return tensor.item() # apparently `.item()` returns the inner value of a torch.Tensor (only if tensor has one value)

def sorted_results(query, document_sentences):
  # using `document_sentences`
  #   [ 'sentence 1...', 'sentence 2...', etc. ] 
  # 
  # to get `results`:
  #   [
  #     [similarity_score_for_sentence_1, 'sentence 1...'], 
  #     [similarity_score_for_sentence_2, 'sentence 2...'], 
  #     etc.
  #   ] 
  results = []
  for sentence in document_sentences:
    results.append([sbert_embed_similarity_score(query, sentence), sentence])

  # return results sorted by their similarity_score
  return sorted(results, key=lambda arr: arr[0], reverse=True)

# fluff UX/display method
def match_strength(results):
  if results[0][0] > 0.25:
    return 'good'
  elif results[0][0] > 0.22:
    return 'ok'
  else:
    return 'bad'

# fluff UX/display method
def describe_match_strength(strength_of_match):
  match strength_of_match:
    case 'good':
      print("I have some advice for you!")
    case 'ok':
      print("I might have something that could help you... how's this?")
    case 'bad':
      print("Unfortunately I don't think I can help. Just in case, how's this advice?")
    case _:
      print('check match_strength string! should be `good`, `ok`, or `bad`')

# fluff UX/display method
def number_of_results_to_display(strength_of_match):
  match strength_of_match:
    case 'good':
      return 3
    case 'ok':
      return 2
    case 'bad':
      return 1
    case _:
      print('check match_strength string! should be `good`, `ok`, or `bad`')
    
def display_results(query, document_sentences):
  print()
  
  # (important) gets list of sentences and their similarity_score (compared to the query)
  results = sorted_results(query, document_sentences)

  # (just fluff) returns `good`, `ok`, or `bad` based on a rough comparison of the similarity_score
  strength_of_match = match_strength(results)

  # (just fluff) prints a conversational statement to set the stage for how good/bad the highest similarity_score is
  describe_match_strength(strength_of_match)

  # (just fluff) returns the number of matching sentences that'd make sense to show given the top sentence match,
  # ie 3 sentences for a good match but 1 'hail mary' sentences for a bad match
  number_of_results = number_of_results_to_display(strength_of_match)

  # (important) prints the top n = number_of_results matching sentences
  for i in range(0, number_of_results):
    rounded_similarity = round(results[i][0], 2)
    print(f'Result #{i + 1} - Similarity [{rounded_similarity}]: ', results[i][1])

  # (just fluff) bottom border
  print('\n', '-' * 130)

# loop until ^C
while True:
  print()
  user_query = input('What topic do you want advice on? ')
  display_results(user_query, advice_list)
  

