from django.contrib import admin
from .models import Catagories, Article, User_model
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'publication_date']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'article']


admin.site.register(Catagories, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(User_model, UserAdmin)
