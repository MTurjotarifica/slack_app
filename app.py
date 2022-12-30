from flask import Flask, request, render_template
import requests, os, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) #debug = True, makes sure if we modify this file we don't need to rerun the python script
    
    




