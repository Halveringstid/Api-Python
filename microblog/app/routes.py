from app import app
from flask import render_template, request, jsonify
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import requests
import json
import os
import re
import operator
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
        return jsonify(data)
            # render_template('assets.html', data = data)

