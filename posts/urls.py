from django.urls import path
from posts import views


urlpatterns = [
    path('', views.news, name='news'),
    path('key', views.key, name='key')
]