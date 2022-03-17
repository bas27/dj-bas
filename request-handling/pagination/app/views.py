from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from app import settings
import csv
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    # current_page = 1
    current_page = request.GET.get('page', 1)
    data = [i for i in get_data()]
    paginator = Paginator(data, 10)
    data_page = paginator.get_page(current_page)

    if data_page.has_next():
        param_next_p = {
            'page': data_page.next_page_number()
        }
        # next_page_url = f'/bus_stations?page={data_page.next_page_number()}'
        next_page_url = "/bus_stations?"+urlencode(param_next_p)
    else:
        next_page_url = None
    if data_page.has_previous():
        param_prev_p = {
            'page': data_page.previous_page_number()
        }
        # prev_page_url = f'/bus_stations?page={data_page.previous_page_number()}'
        prev_page_url = "/bus_stations?"+urlencode(param_prev_p)
    else:
        prev_page_url = None
    return render(request, 'index.html', context={
        'bus_stations': data_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def get_data():
    data_bus_st = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            tmp_dict = {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            data_bus_st.append(tmp_dict)
    return data_bus_st