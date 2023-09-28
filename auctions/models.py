from django.contrib.auth.models import AbstractUser
from django.db import models

category_choices = [
    ("ET", "Entertainment"),
    ("GV", "Gebruiksvoorwerpen"),
    ("IT", " IT"),
    ("AU", "Auto's"),
    ("DI", "Divers")
]

active_choices = [
    ("Y", "Yes"),
    ("N", "No"),
]

class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Auction(models.Model):

    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    category = models.CharField(max_length=2, choices=category_choices, default="DI")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=1024, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    opening_bid = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.CharField(max_length=1, choices=active_choices, default="Y")
    
    def __str__(self):
        return f"{self.title}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watched_items")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auction}"

class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)

    def __str__(self):
        return f"{self.id}"

