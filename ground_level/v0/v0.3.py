'''
Aim here is to combine the Retreival part of v0.2.py and the Generation part
of openai_test.py. See both of those files for background/comments/explanations;
I've removed most of them here for brevity


Previous outputs from my testing:

  What topic do you want advice on? should i confide in my friend?
  your document retrieval results are:

  When trying to improve a relationship, communicate openly and honestly with your partner.
  When facing a difficult decision, consult trusted friends or mentors for advice.
  When facing criticism, consider the source and whether it's constructive.

  your AI generated results are:

  When considering confiding in your friend, ensure that you communicate openly and honestly 
  with them about your feelings and concerns. Seek advice from trusted friends or mentors 
  to gain different perspectives on the situation before making a decision. Evaluate the 
  source of the criticism from your friend to determine if it is constructive and coming 
  from a place of care. Ultimately, sharing your thoughts with your friend can strengthen 
  your relationship, as long as there is open and honest communication.

  ~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~
  
  What topic do you want advice on? i'm nervous about my first day on the job. will my coworkers like me?
  your document retrieval results are:

  When starting a new job, take time to learn the company culture.
  When attending a job interview, research the company beforehand to show interest.
  When facing a challenge, remind yourself of past successes to boost confidence.

  your AI generated results are:

  On your first day on the job, focus on learning about the company culture to 
  better understand your coworkers. Remember to be yourself and show genuine 
  interest in getting to know your new colleagues. Research the company beforehand 
  to have talking points ready and demonstrate your enthusiasm for the role. If 
  you feel nervous, remind yourself of past successes to boost your confidence in 
  making a positive impression.

  ~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~=~-~
  
  What topic do you want advice on? sometimes i feel down, how could i be happier
  your document retrieval results are:

  When facing adversity, focus on solutions rather than dwelling on problems.
  When feeling overwhelmed, prioritize tasks and tackle them one at a time.
  When facing a challenge, remind yourself of past successes to boost confidence.

  your AI generated results are:

  When feeling down, focus on solutions instead of dwelling on problems to shift 
  your mindset. Prioritize tasks that will bring you joy and tackle them one at a 
  time to regain a sense of accomplishment. Remind yourself of past successes to boost 
  your confidence and build a positive outlook for the future. By taking proactive 
  steps and maintaining a positive mindset, you can navigate through tough times and 
  find happiness within yourself.





'''

# https://sbert.net/
from sentence_transformers import SentenceTransformer
from openai import OpenAI

model = SentenceTransformer("all-MiniLM-L6-v2") # embedding model
client = OpenAI() # openai client

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
  query_embed = model.encode(query) # [[12, 13, 13, ...]]
  doc_embed = model.encode(document_sentence) # [[12, 13, 13, ...]]
  tensor = model.similarity(query_embed, doc_embed) # tensor[[.034]] # `type(tensor))` => <class 'torch.Tensor'> (https://pytorch.org/docs/stable/torch.html)
  return tensor.item() # apparently `.item()` returns the inner value of a torch.Tensor (only if tensor has one value)

# sorts the documents by similarity_score
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

# results is [[similarity_score1, sentence1], ...]
# returns top three sentences joined with `\n`
def top_n_documents(results, n):
  top_n_results = results[:n] # results is [[similarity_score1, sentence1], ...]
  top_n_sentences_only = list(map(lambda pair: pair[1], top_n_results))
  return '\n'.join(top_n_sentences_only)

# loop until ^C
while True:
  print()
  user_query = input('What topic do you want advice on? ')
  results = sorted_results(user_query, advice_list)
  top_three_documents = top_n_documents(results, 3)
  print('\nyour document retrieval results are:\n')
  print(top_three_documents)

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a concise author of a small advice column in a newspaper."},
      {"role": "system", "content": f'The advice you should use is {top_three_documents}'},
      {"role": "user", "content": f'Extrapolate on but only use the given information to write four sentences worth of advice to answer this question: {user_query}'}
    ]
  )
  
  print('\nyour AI generated results are:\n')
  print(completion.choices[0].message.content)
  print('-~=~'*40)
  


