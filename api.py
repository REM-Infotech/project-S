from flask import Flask
import pandas as pd

app = Flask (__name__)

# construir funcionalidades

@app.route('/')
def homepage():
    return 'Hello World'

# start api

app.run()