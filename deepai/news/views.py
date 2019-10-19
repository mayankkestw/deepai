from django.shortcuts import render
import requests, json
from .models import NewsAndUpdate
import calendar
from django.http import JsonResponse

# Create your views here.
def newsUpdates(request):

    API_KEY = 'bbe4894ddf204461bb1c2b4b2899aa82'

    url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey='+API_KEY

    if request.method=='GET':
        response = requests.get(url)
        print(response.status_code)
        data = json.loads(response.text)
        n = 10
        sources = []
        titles = []
        descriptions = []
        urls = []
        urls_images = []
        contents = []
        years = []
        months = []
        dates = []

        for i in range(n):
            source = data['articles'][i]['source']['name']
            title = data['articles'][i]['title']
            description = data['articles'][i]['description']
            url = data['articles'][i]['url']
            urls_image = data['articles'][i]['urlToImage']
            published = data['articles'][i]['publishedAt']
            article = data['articles'][i]['content']

            update = NewsAndUpdate(source=source, title=title, description=description, url=url, url_image=urls_image, published_time=published, content=article)
            update.save()

            info = list(NewsAndUpdate.objects.all().values())

            description = description.split('.')[0]+'.'
            date = published[:10]
            year, month, date = date.split('-')

            if month[0] == '0':
                month = int(month[1])
            else:
                month = int(month)

            month = str(calendar.month_abbr[month])

            sources.append(source)
            titles.append(title)
            descriptions.append(description)
            urls.append(url)
            urls_images.append(urls_image)
            years.append(year)
            months.append(month)
            dates.append(date)
            contents.append(article)
        

        context = zip(sources, titles, descriptions, urls, urls_images, years, months, dates, contents)
        context = {
            'context' : context
        }

    return render(request, 'news.html', context=context)