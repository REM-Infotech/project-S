from flask import Flask
import pandas as pd

app = Flask (__name__)

# construir funcionalidades

@app.route('/')
def homepage():
    return 'Hello World'

# start api

app.run(host='0.0.0.0', port=80, debug=True)