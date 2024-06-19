'''
https://platform.openai.com/docs/quickstart

steps:
cd into 'ragtag'

create python virtual env:
`python -m venv openai-env`

Once you’ve created the virtual environment, you need to activate it. 
On Windows, run:
`openai-env/Scripts/activate`

On Unix or MacOS, run:
`source openai-env/bin/activate`

Install the OpenAI Python library (i got an error and needed to run vscode as administrator to fix)
`pip install --upgrade openai`

good to go
'''

from openai import OpenAI
client = OpenAI()

# https://platform.openai.com/docs/api-reference/chat/create
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    # I believe the multiple 'roles' are to guide the model. 
    #   'system' roles give setup, 
    #   'user' roles give queries, 
    #   'assistant' is responses from the model itself (think about plugging 
    #     in an ai conversation back into itself so that the past responses 
    #     could be queried by the user and remembered by the model)
    #       "Typically, a conversation is formatted with a system message 
    #       first, followed by alternating user and assistant messages."
    #   https://platform.openai.com/docs/guides/text-generation/chat-completions-api
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

# see below for sample response object
print(completion.choices[0].message.content)

# Example response object:
# {
#   "id": "chatcmpl-123",
#   "object": "chat.completion",
#   "created": 1677652288,
#   "model": "gpt-3.5-turbo-0125",
#   "system_fingerprint": "fp_44709d6fcb",
#   "choices": [{
#     "index": 0,
#     "message": {
#       "role": "assistant",
#       "content": "\n\nHello there, how may I assist you today?",
#     },
#     "logprobs": null,
#     "finish_reason": "stop"
#   }],
#   "usage": {
#     "prompt_tokens": 9,
#     "completion_tokens": 12,
#     "total_tokens": 21
#   }
# }

