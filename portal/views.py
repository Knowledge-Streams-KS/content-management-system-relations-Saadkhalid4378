from django.shortcuts import render, HttpResponse
from .models import Catagories, Article, User_model
from .forms import Category_form, Article_form, User_form
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('category')
        category = Catagories(name=name)
        print(category)
        category.save()
        # return HttpResponse(f'{category} category')
        return render(request, "portal/categorycreation.html", {'category': category } )
    else:
        request.method == 'GET'
        return render(request, 'portal/categorycreation.html')


def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        publication_date = request.POST.get('date')
        catagories = request.POST.get('ctgrt')
        catagorie_obj = Catagories.objects.filter(name=catagories)
        # print(catagorie_obj)
        article = Article(title=title, content=content, publication_date=publication_date, )
        # print(article)
        article.save()
        categories = []
        for category in catagorie_obj:
            categories.append(category.id)
        
        article.catagories.set(categories)


        
        # for ctry in ctgry:
        #     article.catagories.add(ctry)
        return HttpResponse(f'{article} article')
    else:
        request.method == 'GET'
        return render(request, 'portal/articlecreation.html')


def article_list(request):
    lst = Article.objects.all()
    print(lst)
    return render(request, 'portal/homepage.html', {'lst': lst})


def category_modelform(request):
    if request.method == 'POST':
        form = Category_form(request.POST)
        form.save()
        return HttpResponse(f'{form} Caterory form')
    else:
        form = Category_form()
        return render(request, 'portal/categorycreation.html', {'form': form})


class Class_category(CreateView):
    model = Catagories
    fields = ['name']
    template_name = 'portal/Create-Category.html'
    success_url = '/portal/homepage.html/'


class Class_Article(CreateView):
    model = Article
    # fields = "__all__"
    fields = ['title', 'content', 'publication_date', 'catagories']
    template_name = 'portal/Create-Article.html'
    success_url = '/portal/category/'
