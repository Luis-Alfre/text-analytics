# model
# flask
from flask import Response, request
from flask_restful import Resource
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import OrderedDict
from PDFminer.high_level import extract_text


def wordcloud (body):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(body['texto'].lower())
 
        # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig("cloud.png")
    
def graphBarr(x,y):
    plt.bar(x, y)
    plt.savefig("Plot generated using Matplotlib.png")

    
        
class AnalyticsApi(Resource):
    
    def post(self):
        body = request.get_json()
        
        #cloud = WordCloud().generate(body['texto'].lower())
        freqs = []
     
        #words = list(cloud.words_.keys())
        reader_contents = (body['texto'].lower()).split()
        words = list(OrderedDict.fromkeys(reader_contents))
                
        for word in words:
            freqs.append(reader_contents.count(word))
            
        
        print(words)
        
        graphBarr(words,freqs)    
        
        wordcloud(body)
        

    

        return {"message": "Las graficas se han realizado",
                    "status": 200}, 200
        
class AnalyticsApiPdf(Resource):
    
    def post(self):
        body = request.files['file']
        PDF_read = extract_text(body)
        print(PDF_read) 
        
        # cloud = WordCloud().generate(body['texto'].lower())
        # print(cloud.words_)
        # words = []
        # freqs = []

        # for word in cloud.words_:
        #     words.append(word)
        #     freqs.append(int(cloud.words_[word]*4716))

        # print(words)

        return {"message": "El usuario no tiene permisos para realizar esta operación.",
                    "status": 403}, 403
        