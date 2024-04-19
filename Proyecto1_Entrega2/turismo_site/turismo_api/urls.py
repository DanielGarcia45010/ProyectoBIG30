from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_classification, name='predict_classification'),
    path('classification/', views.get_hotel_classification, name='get_hotel_classification'),
    path('reviews/<str:username>', views.get_reviews_by_username, name='get_reviews_by_username'),
    path('reviews/', views.get_all_reviews, name='get_reviews'),
    path('reviews/create/', views.create_review, name='create_review'),
    
]