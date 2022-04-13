# model
# flask
from flask import Response, request
from flask_restful import Resource
from wordcloud import WordCloud
import json

class AnalyticsApi(Resource):
    
    def post(self):
        body = request.get_json()
        reader_contents = list(body) 
        
        cloud = WordCloud().generate(body['texto'].lower())
        print(cloud.words_)
        words = []
        freqs = []

        for word in cloud.words_:
            words.append(word)
            freqs.append(int(cloud.words_[word]*4716))

        print(words)

        return {"message": "El usuario no tiene permisos para realizar esta operación.",
                    "status": 403}, 403
        