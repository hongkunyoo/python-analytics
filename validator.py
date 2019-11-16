import requests
import pickle
import base64


def request(df):
    pickled = pickle.dumps(df)
    pickled_b64 = base64.b64encode(pickled)
    url = 'http://54.180.167.184:5000'
    response = requests.post(url, json={'data': pickled_b64})
    return response.text

