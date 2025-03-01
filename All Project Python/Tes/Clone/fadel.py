import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
response = bard.get_answer("What is a LLM?")['content']
print(response)

import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
prompt='''
What is a LLM?
The answer format should be the following.

answer: {
[
  id: 1,
  content: draft1
],
 id: 2,
  content: draft2
]
}
'''
response = bard.get_answer(prompt)['content']
print(response)

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