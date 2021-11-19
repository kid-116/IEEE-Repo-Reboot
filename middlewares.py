import os
from flask import redirect, request
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

def auth():
    def _auth(f):
        @wraps(f)
        def __auth(*args, **kwargs):
            key = request.args.get('key')
            # print(key)
            # print(os.getenv('API_KEY'))
            if key:
                if key == os.getenv('API_KEY'):
                    print("Authentification successful")
                    return f()
                else:
                    return "Inavlid API key"
                    # return redirect('/')
            else:
                return "Try again with an API key"
                # return redirect('/')
        return __auth
    return _auth