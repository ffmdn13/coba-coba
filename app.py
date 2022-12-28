import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get('MONGODB_URI')
DB_NAME = os.environ.get('DB_NAME')


client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

web = Flask(__name__)

@web.route('/')
def home():
    return render_template('index.html')

@web.route('/bucket', methods = ['POST'])
def web_post():
    name_receive = request.form['name_data']
    comment_receive = request.form['comment_data']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.testquery.insert_one(doc)
    return jsonify({'msg': 'Message posted'})

if __name__ == '__main__':
    web.run('0.0.0.0', port = 5000, debug = True)