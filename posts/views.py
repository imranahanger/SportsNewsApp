from django.shortcuts import render
from django.http import HttpResponse

from .models import news

def index(request):
    return HttpResponse('Hello World')

def test(request):
    return HttpResponse('<h1><i>this  is test</i></h1>')

def news1(request):
    print("*****************************************")
    print(news.objects.all())
    print("*****************************************")
    context = {
        'news': news.objects.all()
    }
    return render(request,'posts/index.html',context)

def key(request):
    return render(request,'posts/key.html')
