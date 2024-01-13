from django.db import models
from  django.contrib.auth.models import User
# Create your models here.


class Catagories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f' {self.name} The category'


class Article(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = models.CharField(max_length=64)
    publication_date = models.DateField()
    catagories = models.ManyToManyField(Catagories, max_length=64)

    def __str__(self):
        return f' {self.title}  The Article'


class User_model(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    article = models.ForeignKey(Article, max_length=64, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.username} {self.email} {self.article} The user'

