from flask import Flask
from flask import request
import base64
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    data = request.get_json()
    df = pickle.loads(base64.b64decode(data['data'].encode()))

    truth = pd.read_csv('diamonds_true.csv')
    df['id'] = df.index
    merge = pd.merge(df, truth, how='inner', on='id', left_index=True, right_index=True)
    score = np.sum(np.abs(merge['price_x'] - merge['price_y']))

    return str(score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
