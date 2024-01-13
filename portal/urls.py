"""Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')"""

from django.urls import path
from portal.views import (create_category, create_article, article_list, category_modelform, Class_category,
                          Class_Article)

urlpatterns = [
    path('create-category/', create_category, name='create-category' ),
    path('create-article/', create_article, name='create-article'),
    path('article-list/', article_list, name='article-list'),

    path('category-form/', category_modelform, name='Category-form'),

    path('category/', Class_category.as_view(), name='category'),
    path('article/', Class_Article.as_view(), name='article')





]