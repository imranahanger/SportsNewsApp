from django.urls import path
from posts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('v1', views.test, name='test'),
    path('news', views.news1, name='news'),
    path('key', views.key, name='key')
]