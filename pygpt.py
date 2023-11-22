'''
PyGPT - A GPT-3.5 wrapper for Python
Created by RR0
'''

import g4f
import uuid

class pygpt:
  def __init__():
    g4f.debug.logging = False
    g4f.version_check = False

  def chat(max_prompts = 100):
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

      answer = ""
      for message in response:
        answer = answer + message
      return answer
  
  def prompt(prompt = ""):
    response = g4f.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [{
        "role": "user",
        "content": prompt
      }],
      stream = True
    )

    answer = ""
    for message in response:
      answer = answer + message
    return answer
  
  def save(prompt = ""):
    response = g4f.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [{
        "role": "user",
        "content": prompt
      }],
      stream = True
    )

    answer = ""
    for message in response:
      answer = answer + message

    filename = str(uuid.uuid4()) + ".txt"
    f = open(filename, "x")
    f.close()
    f = open(filename, "w")
    f.write(str(answer))
    f.close()