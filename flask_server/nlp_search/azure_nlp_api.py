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

def getCategories(query, ptr):
    print('getting categories')
    data = {
        "Inputs": {
            "WebServiceInput1":
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
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ os.getenv('AZURE_NLP_KEY'))}

    req = urllib.request.Request(os.getenv('AZURE_NLP_ENDPOINT'), body, headers)

    try:
        print('before req')
        response = urllib.request.urlopen(req)
        result = response.read()
        print('after req')
        main_result = json.loads(str(result)[2:-1])['Results']['WebServiceOutput0'][0]
        main_result.pop('Scored Labels')
        l = list(main_result.items())
        l.sort(key = lambda cat: cat[1], reverse=True)
        for i, cat in enumerate(l[:3]):
            ptr[i] = cat[0][21:]  
        # return probableCats
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return None