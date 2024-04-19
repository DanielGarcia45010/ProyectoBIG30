from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from unidecode import unidecode
import pandas as pd

class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        print("TextPreprocessor initialized")
        self.stop_words = set(stopwords.words('english'))

    def fit(self, X, y=None):
        print("Fitting TextPreprocessor...")
        return self

    def transform(self, X, y=None):
        print("Transforming text...")
        return self.preprocess(X)
    
    def cleanText(self, text):
        stop_words = set(stopwords.words('spanish'))
        stemmer = SnowballStemmer('spanish')
        # Convertir el texto a minúsculas
        text = text.lower()
        # Tokenizar el texto
        words = word_tokenize(text, language='spanish')
        # Eliminar stopwords y palabras no alfabéticas, y aplicar stemming
        cleanWords = [stemmer.stem(word) for word in words if word.isalpha() and word not in stop_words]
        # Unir de nuevo las palabras en una cadena
        cleanText = ' '.join(cleanWords)
        return cleanText

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(df)
        print("Preprocessing text...")
        print("Step 1/4", end="\r")
        df['Review'] = df['Review'].apply(unidecode)
        print("Step 2/4", end="\r")
        df['Review'] = df['Review'].str.encode(
            'ascii', 'ignore').str.decode('ascii')
        print("Step 3/4", end="\r")
        df['Review'] = df['Review'].str.lower()
        print("Step 4/4", end="\r")
        df['clean_review'] = df['Review'].apply(self.cleanText)
        df_clean = df['clean_review']
        # rename tokenized_str to text
        print("Finished preprocessing text...")
        return df_clean
        