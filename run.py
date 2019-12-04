from flask import Flask, request, jsonify, abort
from config import wordnikApiKey
from os import environ

from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
client = swagger.ApiClient(wordnikApiKey, apiUrl)
wordApi = WordApi.WordApi(client)
environ["FLASK_APP"] = __name__
environ["FLASK_DEBUG"] = "1"
app = Flask(__name__)

@app.route('/api/word/define')
def define():
    try:
        word = request.args['word']
        print('started')
        definition = wordApi.getDefinitions(word=word, limit=1)[0].text
        
    except Exception as e:
        abort(404)
    else:
        return jsonify({'data':definition})
    

@app.route('/api/word/related')
def related():
    word = request.args['word']
    related = wordApi.getRelatedWords(word=word)[0].words
    print(dir(related))
    return jsonify({'data':related})
    
    
    
@app.route('/api/word/sentences')
def sentences():
    limit = 3
    word = request.args['word']
    examples_list = [example.text for example in wordApi.getExamples(word=word, limit=limit).examples]
    print(f'examples_list: {examples_list}')
    return jsonify({'data':examples_list})


if __name__ == "__main__":
    app.run()
