# server.py

import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ufo')
def ufo():
    csv = pd.read_csv('../data/ufo.csv')
    return jsonify(csv.T.to_dict().values())

if __name__ == "__main__":
    app.run()
