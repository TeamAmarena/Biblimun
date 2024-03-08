from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subscription_date = models.DateTimeField(auto_now_add=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author)
    isbn = models.CharField(max_length=13)
