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
        definition = wordApi.getDefinitions(word=word, limit=1)[0]
        
    except Exception as e:
        abort(404)
    else:
        return f'hello heroku! this is my word: {word} - definition: {definition.text}' 
    

@app.route('/api/word/related')
def related():
    word = request.args['word']
    related = wordApi.getRelatedWords(word=word)
    print(related)
    print(dir(related))
    return related
    
    
    
@app.route('/api/word/sentences')
def sentences():
    word = request.args['word']
    return 'sentences'


if __name__ == "__main__":
    app.run()