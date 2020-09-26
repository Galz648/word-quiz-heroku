from flask import Flask, request, jsonify, abort
from config import wordnikApiKey
from os import environ
from flask_cors import CORS


from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
client = swagger.ApiClient(wordnikApiKey, apiUrl)
wordApi = WordApi.WordApi(client)
environ["FLASK_APP"] = __name__
environ["FLASK_DEBUG"] = "1"
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def home():
    return "<p> /api/word/define?word='{word}' <br> /api/word/related?word='{word}' <br> /api/word/sentences?word='{word}' </p>"

# Example : /api/word/define?word='{word}'
@app.route('/api/word/define')
def define():
    try:
        limit = 1
        word = request.args['word']
        print('started')
        definition = wordApi.getDefinitions(word=word, limit=limit)[0].text
        return jsonify({'data':definition})

    except Exception as e:
        jsonify({'error':e})
        abort(404)

       
# Example : /api/word/related?word='{word}'
@app.route('/api/word/related')
def related():
    try:
        limit = 4
        word = request.args['word']
        related = wordApi.getRelatedWords(word=word, limit=limit)[0].words
        print(dir(related))
        return jsonify({'data':related})
    except Exception as e:
        jsonify({'error':e})
        abort(404)
    
# Example : /api/word/sentences?word='{word}'
@app.route('/api/word/sentences')
def sentences():
    try:
        limit = 3
        word = request.args['word']
        examples_list = [example.text for example in wordApi.getExamples(word=word, limit=limit).examples]
        print(f'examples_list: {examples_list}')
        return jsonify({'data':examples_list})
    except Exception as e:
        jsonify({'error':e})
        abort(404)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
