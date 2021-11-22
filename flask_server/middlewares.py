import os
from flask import redirect, request
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

def auth():
    def _auth(f):
        @wraps(f)
        def __auth(*args, **kwargs):
            key = request.headers.get('key')
            if key:
                if key == os.getenv('API_KEY'):
                    print("Authentification successful")
                    if kwargs.get('pid'):
                        return f(pid=kwargs.get('pid'))
                    else:
                        return f()
                else:
                    return "Inavlid API key"
                    # return redirect('/')
            else:
                return "Try again with an API key"
                # return redirect('/')
        return __auth
    return _auth