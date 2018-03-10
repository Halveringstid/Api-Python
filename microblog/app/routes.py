from app import app
from flask import render_template, request, jsonify
from bigchaindb_driver import BigchainDB
from math import sin, cos, sqrt, atan2, radians
from bigchaindb_driver.crypto import generate_keypair
import datetime
import requests
import json
import os
import re
import operator

def calc_distance(lat1, lon1, lat2, lon2):
    # returns in distance in kms
    R = 6373.0
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dif_lon = lon2-lon1
    dif_lat = lat2-lat1
    a = sin(dif_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c



@app.route('/')
@app.route('/index')


def index():
    user = {'username':'igorek'}
    list = [
        {
            'name': 'chuj',
            'link': 'xddx'
        },
        {
            'name': 'chuj2',
            'link': 'xd'
        }
    ]
    return render_template('index.html', title='Home', user=user, post=list)

@app.route('/api/messages/', methods=['GET', 'POST'])
def retrieve_messages():
    bdb = BigchainDB('http://80.211.240.79:59984')
    data = bdb.assets.get(search="message")
    # chuj = {item for item in data}
    if request.method == 'GET':
        if len(request.args) == 0:
            return jsonify(data)
        else:# username = request.args.get('username')
            long = float(request.args.get('lon'))
            lati = float(request.args.get('lat'))
            radius = float(request.args.get('radius'))
            near = [item for item in data if calc_distance(lati, long, item['data']['lon'], item['data']['lat']) < radius]
            return jsonify(near)
    else:
        # return jsonify(request.json)
        entry = request.json
        entry["created_at"] = datetime.datetime.now().isoformat()
        entry["type"] = "message"
        keypair = generate_keypair()
        tx = bdb.transactions.prepare(
            operation='CREATE',
            signers=keypair.public_key,
            asset={'data': entry, 'metadata': {"type": "message"}})
        signed_tx = bdb.transactions.fulfill(tx, private_keys=keypair.private_key)
        x = bdb.transactions.send(signed_tx)
        return jsonify(x['asset'])
        # for item in data:
        #     if (lati, long) == (item['data']['lat'], item['data']['lon']):
        #         if (message, auth) == (item['data']['message'], item['data']['author']):
        #             return jsonify(item)
            # render_template('assets.html', data = data)

