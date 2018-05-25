import json
import requests
from posts.models import News, Key

def get_data(request):
    url = 'https://newsapi.org/v1/articles?source=breitbart-news&category=sports&sortBy=top&apiKey={0}'.format(Key.objects.get(id=1))
    data = requests.get(url)
    if data.status_code == 200:
          rate_list = data.json()
          print('**********************************')
          print(rate_list['articles'])
          print('**********************************')
          for record in rate_list['articles']:
                created = News.objects.get_or_create(
                        title=record['title'],
                        description=record['description']
                        )
                if created:
                        print("New object Created")
                else:
                        print("objects not Created")
                return rate_list['articles']