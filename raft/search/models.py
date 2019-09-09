from django.db import models

class ViewedRafts(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()
    num_reviews = models.IntegerField()
    price = models.IntegerField()

    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()

    time_viewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DefaultLocation(models.Model):
    city = models.CharField(max_length=20)