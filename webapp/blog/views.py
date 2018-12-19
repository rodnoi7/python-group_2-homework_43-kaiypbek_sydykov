from django.shortcuts import render, redirect, get_object_or_404
from blog.models import User, Article, Comment, Mark
from django.http import Http404


def index_view(request):
    article = Article.objects.all()
    contex = {
        'articles': article,
    }
    return render(request, 'index.html', contex)

def create_blog_view(request):
    if request.method == 'GET':
        return render(request, 'create_view.html')
    elif request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        text = request.POST.get('text')
        article = Article.objects.create(author=author, title=title, text=text)
        article.save()
        article = Article.objects.all()
        context = {
            'article': article
        }
        return redirect('index')


def create_user_view(request):
    if request.method == 'GET':
        return render(request, 'create_user_view.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        login = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')
        about_yourself = request.POST.get('text')
        user = User.objects.create(name=name, surname=surname, login=login, password=password, email=email, about_yourself=text)
        user.save()
        user.objects.all()
        context = {
            'users': user
        }
        return redirect('index')


def user_view(request, user_pk):
    try:
        user = User.objects.all()
    except User.DoesNotExist:
        raise Http404

    context = {
        'users': user
    }
    return render(request, 'users_view.html', context)


def article_view(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist: Http404
        
    context = {
        'article': article
    }
    return render(request, 'view.html', context)
