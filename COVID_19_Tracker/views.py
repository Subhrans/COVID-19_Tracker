import requests
from django.shortcuts import render
from .models import Global,Countries
import json


# Create your views here.
def fetchCovidData():
    r = requests.get('https://api.covid19api.com/summary')
    r= r.json()
    return r
def home(request):
    r=fetchCovidData()

    # summary=dict(summary)
    global_data = r['Global']
    c = r['Countries']

    summary1 = json.dumps(c, indent=4)
    print(global_data)
    global_datanew=None
    countries_data_new=None
    for i in range(len(c)):
        countries_data = r['Countries'][i]
        if Countries.objects.filter(cid=countries_data['ID']).exists():
            countries_data_new=Countries.objects.all()
        else:
            Countries.objects.create(cid=countries_data['ID'],
                                    country=countries_data['Country'],
                                    countryCode=countries_data['CountryCode'],
                                    slugId=countries_data['Slug'],
                                    newConfirmed=int(countries_data['NewConfirmed']),
                                    totalConfirmed=int(countries_data['TotalConfirmed']),
                                    newDeaths=int(countries_data['NewDeaths']),
                                    totalDeaths=int(countries_data['TotalDeaths']),
                                    newRecovered=int(countries_data['NewRecovered']),
                                    totalRecoverd=int(countries_data['TotalRecovered']),
                                    date=countries_data['Date'],
                                  )

    if Global.objects.filter(gid=global_data['ID']).exists():
        global_datanew=Global.objects.get(gid=global_data['ID'])
    else:
        Global.objects.create(gid=global_data['ID'],
                              newConfirmed=int(global_data['NewConfirmed']),
                              totalConfirmed=int(global_data['TotalConfirmed']),
                              newDeaths=int(global_data['NewDeaths']),
                              totalDeaths=int(global_data['TotalDeaths']),
                              newRecovered=int(global_data['NewRecovered']),
                              totalRecoverd=int(global_data['TotalRecovered']),
                              )
    print(type(global_data))
    print(global_datanew)
    print(summary1)
    print("range of dist is : ",len(c))
    # print(r)
    context = {"global_data": global_data,
               "summary": r,
               "global_data_new":global_datanew,
               "countries_data_new":countries_data_new,
               }
    return render(request, 'covid/home.html', context)
