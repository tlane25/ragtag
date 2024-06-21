"""

note: you will need to create a .env file in the root project folder (e.g., same folder with main.py)
it will contain: OPENAI_API_KEY=yourKeyHere

"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def process_prompt(context):
    messages = create_messages(context)
    response = send_prompt(messages)
    return response


def create_messages(context):
    """
    format of messages to submit to OpenAI:
    messages=[
        {"role": "system", "content": "You are a concise author of a small advice column in a newspaper."},
        {"role": "system", "content": f'The advice you should use is {top_three_documents}'},
        {"role": "user", "content": f'Extrapolate on but only use the given information to write four sentences worth of advice to answer this question: {user_query}'}
    ]
    """
    preamble = 'Extrapolate on but only use the given information to respond to this question:'
    messages = []

    # add system role entries
    for chunk in context['matches']:
        messages.append({
            'role': 'system',
            'content': chunk
        })

    # add user role
    messages.append({
        'role': 'user',
        'content': f'{preamble} {context['query']}'
    })

    return messages



def send_prompt(returned_messages):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=returned_messages
    )

    return completion.choices[0].message.content



# test code
test_context = {
    'query': 'what colour is the sky?',
    'matches': ['the sky is blue', 'sunsets are sometimes glorious hues of orange and red', 'as the sun rises shades of pink and orange are sometimes visible against the clouds']
}
# print(create_messages(test_context));
# process_prompt(test_context)
