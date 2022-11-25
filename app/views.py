from django.shortcuts import render
from django.core.paginator import Paginator
import csv


DATA = []
with open('data-398-2018-08-30.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        DATA.append((row['Name'], row['Street'], row['District']))
 
content = [data for data in DATA]

def bus_stations(request):
    page_numbers = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_numbers)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)
