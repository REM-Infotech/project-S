from flask import Flask, make_response, jsonify
import mysql.connector

app = Flask (__name__)

# construir funcionalidades
@app.route('/')
def homepage():
    return render_template('index.html')

app.run(host='0.0.0.0', port='80', debug=True)
