from django import forms
from django.forms import ModelForm
from .models import Article, Catagories, User_model


class Category_form(forms.ModelForm):
    class Meta:
        model = Catagories
        fields = ['name']


class Article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class User_form(forms.ModelForm):
    class Meta:
        model = User_model
        fields = ['username', 'email', 'password', 'article']
