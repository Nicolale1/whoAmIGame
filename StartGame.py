from OpenAiCalls import send_message
from character import getCharacter
import random

caracter_string = getCharacter(random.randint(0,9))

print('''
      this is a prototype of the guess who i am game.
      You are chatting with a chatbot that has a secret caracter, real or fictional")
      you have 10 messages to guess
      Good luck
      ''')
for i in range(9):
    print(send_message(input("\n"),caracter_string))