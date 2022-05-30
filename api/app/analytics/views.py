from flask import request
from flask_restful import Resource
from collections import OrderedDict
from api.app.analytics.utils import graphBarr, wordcloud, readPDF

import pandas
import numpy as np


url = "/home/luis/Documentos/Wtredata/text-analytics/listText.txt"


        
class AnalyticsApi(Resource):
    
    def post(self):
        body = request.get_json()
        limit=int(request.args.get('limit'))
        
        freqs = []
     
        reader_contents = (body['texto'].lower()).split()   
        words = list(OrderedDict.fromkeys(reader_contents))
        conecctors = list(pandas.read_csv(url))
        
        for i in conecctors:
            try:
                words.remove(i)
            except ValueError:
                pass
                        
        for word in words:
            freqs.append(reader_contents.count(word))   
            
        indices = list(reversed(np.argsort(freqs)))[:limit]
        words = ([words[i] for i in indices])
        freqs = ([freqs[i] for i in indices])
        
        graphBarr(words,freqs)    
        wordcloud(" ".join(words))
        
        return {"words": words,
                "freqs": freqs,
                    "status": 200}, 200
        
class AnalyticsApiPdf(Resource):
    
    def post(self):
        body = request.files['file']
        limit=int(request.args.get('limit'))
                    
        reader_contents = readPDF(body)
        freqs = []
     
        words = list(OrderedDict.fromkeys(reader_contents))
        conecctors = list(pandas.read_csv(url))

        for i in conecctors:
            try:
                words.remove(i)
            except ValueError:
                pass
                
        for word in words:
            freqs.append(reader_contents.count(word))
            
        indices = list(reversed(np.argsort(freqs)))[:limit]
        words = ([words[i] for i in indices])
        freqs = ([freqs[i] for i in indices])
            
        graphBarr(words,freqs)    
        wordcloud(" ".join(words))

        return {"words": words,
                "freqs": freqs,
                    "status": 200}, 200
        