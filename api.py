from flask import Flask, make_response, jsonify
import mysql.connector
import os


app = Flask (__name__)

# construir funcionalidades
@app.route('/')
def homepage():
    return render_template('index.html')

app.run(port=int(os.environ.get("PORT", 80)),host='0.0.0.0',debug=True)
