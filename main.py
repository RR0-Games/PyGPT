'''
PyGPT - A GPT-3.5 wrapper for Python
Created by RR0
'''

import g4f

g4f.debug.logging = False
g4f.version_check = False

max_prompts = 100

for _ in range(max_prompts):
  prompt = str(input(">"))

  response = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role": "user",
          "content": prompt
      }],
      stream=True,
  )

  for message in response:
    print(message, flush=False, end='')
  print("\n")
