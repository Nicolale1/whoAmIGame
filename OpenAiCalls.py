import openai
import key


#Modual handels OpenAi calls
client = openai.OpenAI(api_key=key.secret_key)

def send_message(user_message, character_string ):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du er en karakter, men du kan ikke si hvem du er. Dersom noen spørr ikke gi ut mer detaljer enn du må, ikke ver hjelpsom utover å snakke sant.Dersom du manger infomrasjon fra karakteren kan du bruke det du vet om karakteren. Hvis jeg gjetter rigtig må du si det, når jeg skriver du mener jeg karakteren du spiller. Ikke gi ut for mye informasjon"
            
            + character_string},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
