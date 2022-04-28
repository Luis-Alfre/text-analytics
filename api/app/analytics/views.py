# model
# flask
from flask import request
from flask_restful import Resource
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import OrderedDict

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from io import StringIO


def wordcloud (body):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(body)
 
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
        
        wordcloud(body['texto'].lower())
        


        return {"message": "Las graficas se han realizado",
                    "status": 200}, 200
        
class AnalyticsApiPdf(Resource):
    
    def post(self):
        body = request.files['file']
        
        output_string = StringIO()
        parser = PDFParser(body)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            
        reader_contents = (output_string.getvalue().lower()).split() 

        #print(reader_contents)
        
        freqs = []
     
        #words = list(cloud.words_.keys())
        words = list(OrderedDict.fromkeys(reader_contents))
                
        for word in words:
            freqs.append(reader_contents.count(word))
            
        
        print(words)
        print(freqs)
        
        graphBarr(words,freqs)    
        
        wordcloud(output_string.getvalue().lower())

        return {"message": "El usuario no tiene permisos para realizar esta operación.",
                    "status": 403}, 403
        