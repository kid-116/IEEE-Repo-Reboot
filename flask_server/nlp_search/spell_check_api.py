import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def spellCheck(query):
    data = {'text': query}

    params = {
        'mkt': 'en-us',
        'mode': 'proof'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': os.getenv('AZURE_SPELL_KEY'),
    }

    response = requests.post(os.getenv('AZURE_SPELL_ENDPOINT'), headers=headers,
                             params=params, data=data)
    print(response)

    json_response = response.json()
    response_suggestions_list = json.loads(
        json.dumps(json_response))['flaggedTokens']
    for word in response_suggestions_list:
        query = query.replace(
            word['token'], word['suggestions'][0]['suggestion'])

    return query