import urllib.request
from dotenv import load_dotenv
import json
import os
import ssl

load_dotenv()

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

def getCategories(query):
    data = {
        "Inputs": {
            "input1":
            [
                {
                    'title': query,
                    'main_cat': "All Beauty", #Garbage value; should be the name of any one 
                },
            ],
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'http://eae21c18-c61a-4325-916f-95023e554c25.centralindia.azurecontainer.io/score'
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ os.getenv('AZURE_NLP_KEY'))}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        main_result = json.loads(str(result)[2:-1])['Results']['WebServiceOutput0'][0]
        main_result.pop('Scored Labels')
        l = list(main_result.items())
        probableCats = []
        l.sort(key = lambda cat: cat[1], reverse=True)
        for cat in l[:3]:
            probableCats.append(cat[0][21:])  
        return probableCats
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return None