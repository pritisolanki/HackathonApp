from flask import Flask, flash, request, redirect, render_template , jsonify
import requests
import os  
from model import predict

app = Flask(__name__)
app.config["DEBUG"] = True

AUTH_TOKEN = ['5f404f73-fae1-4c94-bcd2-ba49d6afdea4', 'ABC12345']

app.secret_key = "12345secret&865" # for encrypting the session

@app.route('/', methods=['GET'])
def home():
    return "hello world"

@app.route('/api/predict' , methods=['GET' , 'POST'])
def get_predication():

    res = {}
    #print(header , "Header printing")
    
    data = request.get_json()
    name,age,lat,lng,disable,outdoor,preparation=data['name'],data['age'],data['lat'],data['lng'],data['disable'],data['outdoor'],data['preparation']
    community,local_support,environment,asset_protection=data['community'],data['local_support'],data['environment'],data['asset_protection']
    res['response'] = 'OK'
    res['output'] =  predict(name,age,lat,lng,disable,outdoor,preparation,community,local_support,environment,asset_protection)
    return jsonify(res)

if __name__ == '__main__':
    app.run()