from app import app
import pandas as pd
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    csv = pd.read_csv('data/ufo.csv')
    return jsonify(csv.T.to_dict().values())
