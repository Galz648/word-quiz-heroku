from flask import Flask, request, jsonify
from config import wordnikApiKey
from os import environ

environ["FLASK_APP"] = __name__
environ["FLASK_DEBUG"] = "1"
app = Flask(__name__)


@app.route('/api/word/define')
def define():
    return 'hello heroku!'
if __name__ == "__main__":
    app.run()