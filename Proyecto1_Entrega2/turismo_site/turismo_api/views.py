from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .logic import reviews_logic as rl
from django.core import serializers
from django.http import HttpResponse

import json

# Create your views here.
@csrf_exempt
def get_reviews_by_username(request, username):
    if request.method == 'GET':
        reviews = rl.get_reviews_by_username(username)
        reviews_dto = serializers.serialize('json', reviews)
        return HttpResponse(reviews_dto, content_type='application/json')
    
@csrf_exempt
def get_hotel_classification(request):
    if request.method == 'GET':
        classification = rl.get_hotel_classification()
        json_object = json.dumps({"classification": classification}, ensure_ascii=False) 
        return HttpResponse(json_object, content_type='application/json')
    
@csrf_exempt
def get_all_reviews(request):
    if request.method == 'GET':
        reviews = rl.get_all_reviews()
        json_object = json.dumps(reviews, ensure_ascii=False) 
        return HttpResponse(json_object, content_type='application/json')
    
@csrf_exempt
def create_review(request):
    if request.method == 'POST':
        review = rl.create_review(json.loads(request.body))
        if review is None:
            return HttpResponse(status=400)
        review_dto = serializers.serialize('json', [review])
        return HttpResponse(review_dto, content_type='application/json')

@csrf_exempt
def predict_classification(request):
    if request.method == 'POST':
        review = rl.predict(json.loads(request.body))
        if review is None:
            return HttpResponse(status=400)
        json_object = json.dumps(review, ensure_ascii=False) 
        return HttpResponse(json_object, content_type='application/json')
    

