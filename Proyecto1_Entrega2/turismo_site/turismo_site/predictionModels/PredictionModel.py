from joblib import load
import pickle as pkl
from .TextPreprocessor import * # Ensures that all the modules have been loaded in their new locations *first*.
from . import TextPreprocessor  # imports WrapperPackage/packageA
import sys
sys.modules['TextPreprocessor'] = TextPreprocessor

class PredictionModel:

    def __init__(self):
        self.model = pkl.load( open('pipeline/pipeline.pkl', 'rb'), )

    def make_prediction(self, data):
        result = self.model.predict(data)
        return result