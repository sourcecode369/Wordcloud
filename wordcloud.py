import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

currendir = os.path.dirname('__file__')
currendir

def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currendir,"cloud.jpg")))
    stopwords = set(STOPWORDS)
    wc=WordCloud(background_color="white",mask=mask,max_words=200,stopwords=stopwords,)
    wc.generate(text)
    wc.to_file(os.path.join(currendir,"deep.png"))

create_wordcloud(get_wiki("Deep_learning"))
