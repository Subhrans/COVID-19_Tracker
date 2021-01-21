import json

import requests
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from datetime import datetime

from .models import Global, Countries, CountriesHistory,India
from .utils import indiaData,globalData,fetchCovidGlobalData
from .forms import IndiaForm

# Create your views here.
def home(request):
    globalData()
    r = fetchCovidGlobalData()
    global_data = r['Global']
    countries_data_new = Countries.objects.all()
    global_datanew = Global.objects.get(gid=global_data['ID'])
    context = {"global_data": global_data,
               "summary": r,
               "global_data_new": global_datanew,
               "countries_data_new": countries_data_new,
               }
    return render(request, 'covid/home.html', context)


def india(request):
    indiaData()
    indiadata=India.objects.all()
    indiadata=India.objects.exclude(state_code="TT")
    # India.objects.create(active=statewise['active'],
    #                      confirmed=statewise['confirmed'],
    #                      deaths=statewise['deaths'],
    #                      new_confirmed=statewise['deltaconfirmed'],
    #                      new_deaths=statewise['deltadeaths'],
    #                      new_recovered=statewise['deltarecovered'],
    #                      recovered=statewise['recovered'],
    #                      last_update_time=date,
    #                      )
    total=India.objects.get(state_code="TT")
    return render(request, 'covid/IndiaData.html',{"indiadata":indiadata,"total":total})
