import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def spellCheck(query):
    api_key = os.getenv('AZURE_SPELL_KEY')
    endpoint = "https://api.bing.microsoft.com/v7.0/SpellCheck"

    data = {'text': query}

    params = {
        'mkt': 'en-us',
        'mode': 'proof'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
    }

    response = requests.post(endpoint, headers=headers,
                             params=params, data=data)

    json_response = response.json()
    response_suggestions_list = json.loads(
        json.dumps(json_response))['flaggedTokens']
    for word in response_suggestions_list:
        query = query.replace(
            word['token'], word['suggestions'][0]['suggestion'])

    return query