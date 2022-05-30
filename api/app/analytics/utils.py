from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO
import numpy as np



url = "/home/luis/Documentos/Wtredata/text-analytics/listText.txt"

def wordcloud (body):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(body)
    print(list(wordcloud.words_.keys()))
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig("cloud.png")
    
def graphBarr(x,y):
    plt.bar(x, y)
    plt.savefig("Plot generated using Matplotlib.png")
    
    
    
def readPDF(body):
    output_string = StringIO()
    parser = PDFParser(body)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
            
    reader_contents = (output_string.getvalue().lower()).split() 
    return reader_contents

