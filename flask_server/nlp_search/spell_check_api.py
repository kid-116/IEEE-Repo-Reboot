import requests
import json


def spellCheck(query):
    api_key = "d1b5e17acff24b10b5da9cfccf039aee"
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

# print(spellCheck("helo worl"))
