from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "HELLO"

app.run(debug=True)