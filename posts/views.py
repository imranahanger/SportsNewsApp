from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from posts.models import News, Key
from posts import api


def news(request):
    testtt = api.get_data(request)
    context = {
        'news': News.objects.order_by('-date_added')[:10]
    }
    return render(request,'posts/index.html',context)

def key(request):
    return render(request,'posts/key.html')
