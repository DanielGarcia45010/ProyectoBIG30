from ..models import HotelClassification, Review
from django.conf import settings
import pandas as pd

PREDICTION_MODEL = settings.PREDICTION_MODEL

def update_hotel_classification(classificationSum):
    hc = get_hotel_classification_dict()
    hc.classificationSum += classificationSum
    hc.guests += 1
    hc.save()

def get_hotel_classification_dict():
    return HotelClassification.objects.first()

def get_hotel_classification():
    hc = get_hotel_classification_dict()
    return hc.classificationSum/hc.guests

def get_all_reviews():
    lista = []
    for objeto in Review.objects.all().values():
        lista.append(objeto)
    return lista

def get_reviews_by_username(username):
    return Review.objects.filter(username=username)

def create_review(review):
    prediction = predict(review)
    update_hotel_classification(prediction["classification"])
    review = Review(username=review["username"], classification=prediction["classification"], review=review["review"])
    review.save()
    return review

def predict(review):
    prediction =  PREDICTION_MODEL.make_prediction(pd.DataFrame([review['review']], columns=["Review"]))
    return {"classification": int(prediction[0])}
