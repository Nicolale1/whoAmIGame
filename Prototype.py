import openai
import random
import character
from key import secret_key #importing secrect_key from file

client = openai.OpenAI(api_key=secret_key) #making a client

def send_message(user_message, character_string):
    response = client.chat.completions.create(
        model="gpt-4",  # eller "gpt-4"
        messages=[
            {"role": "system", "content": "Du er en karakter, men du kan ikke si hvem du er. Dersom du manger infomrasjon fra karakteren kan du bruke det du vet om karakteren. Hvis jeg gjetter rigtig må du si det, når jeg skriver du mener jeg karakteren du spiller. Ikke gi ut for mye informasjon"
            
            + character_string},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content