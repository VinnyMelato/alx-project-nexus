from django.db import models
from django.contrib.auth.models import User

class TaxiRank(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Taxi(models.Model):
    rank = models.ForeignKey(TaxiRank, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Taxi to {self.destination} from {self.rank.name}"

class Review(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.taxi.destination} by {self.user.username}"