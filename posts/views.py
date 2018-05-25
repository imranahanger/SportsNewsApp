from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from posts.models import News, Key
from posts import api, form


def news(request):
    # api.get_data(request)
    context = {
        'news': News.objects.order_by('-date_added')[:10]
    }
    return render(request,'posts/index.html',context)

def key(request):
    if request.method=="POST":
        KeyForms = form.KeyForm(request.POST)
        if KeyForms.is_valid():
            new_key = Key(key=request.POST['key'])
            new_key.save()
            print("yes")
            return redirect('key')
    else:
        print("no")
        KeyForms = form.KeyForm()
    context = {'form':KeyForms}    
    return render(request,'posts/key.html',context)
