import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


stop_words=stopwords.words('english')
stemmer=PorterStemmer()

def clean_function(string):
    clean = re.sub('[^a-zA-Z]',' ',string.lower())
    clean = clean.split()
    clean= [stemmer.stem(word) for word in clean if (word not in stop_words)]
    clean = ' '.join(clean)
    return clean