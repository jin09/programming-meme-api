import random

from flask import Flask, jsonify

from memes import memes_db

app = Flask(__name__)


@app.route('/api/RandomMeme')
def randomise_my_meme():
    return jsonify({"meme": random.choice(memes_db)})

