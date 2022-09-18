

from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


with open('data-398-2018-08-30.csv', "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stops_list = [row for row in reader]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stops_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)