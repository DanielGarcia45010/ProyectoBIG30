from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=100)
    classification = models.IntegerField()
    review = models.TextField()

class HotelClassification(models.Model):
    guests = models.IntegerField()
    classificationSum = models.IntegerField()
# Create your models here.
