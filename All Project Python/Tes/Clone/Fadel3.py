import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
prompt='What is a LLM?'

responses = bard.get_answer(prompt)['choices']

for choice in responses:
  id = choice['id']
  response = choice['content'][0]
  print(id)
  print(response)