import json

import requests
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from datetime import datetime

from .models import Global, Countries, CountriesHistory,India
from .forms import IndiaForm

# Create your views here.
def fetchCovidData():
    r = requests.get('https://api.covid19api.com/summary')
    r = r.json()

    return r


def home(request):
    r = fetchCovidData()

    # summary=dict(summary)
    global_data = r['Global']
    c = r['Countries']

    summary1 = json.dumps(c, indent=4)
    print(global_data)
    global_datanew = None
    countries_data_new = None
    for i in range(len(c)):
        countries_data = r['Countries'][i]
        print("country",countries_data['Date'],type(countries_data['Date']))
        if Countries.objects.filter(slugId=countries_data['Slug']).exists():
            if Countries.objects.filter(date=countries_data['Date'], slugId=countries_data['Slug']).exists():
                countries_data_new = Countries.objects.all()
                # india_data=Countries.objects.get(country="india")
            else:
                CountriesHistory.objects.create(cid=countries_data['ID'],
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
                countries_data_new = Countries.objects.get(slugId=countries_data['Slug'])
                countries_data_new.cid = countries_data['ID']
                countries_data_new.newConfirmed = int(countries_data['NewConfirmed'])
                countries_data_new.totalConfirmed = int(countries_data['TotalConfirmed'])
                countries_data_new.newDeaths = int(countries_data['NewDeaths'])
                countries_data_new.totalDeaths = int(countries_data['TotalDeaths'])
                countries_data_new.newRecovered = int(countries_data['NewRecovered'])
                countries_data_new.totalRecoverd = int(countries_data['TotalRecovered'])
                countries_data_new.date = countries_data['Date']
                countries_data_new.save()
                # return HttpResponseRedirect('/')
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
        global_datanew = Global.objects.get(gid=global_data['ID'])
    else:
        Global.objects.create(gid=global_data['ID'],
                              newConfirmed=int(global_data['NewConfirmed']),
                              totalConfirmed=int(global_data['TotalConfirmed']),
                              newDeaths=int(global_data['NewDeaths']),
                              totalDeaths=int(global_data['TotalDeaths']),
                              newRecovered=int(global_data['NewRecovered']),
                              totalRecoverd=int(global_data['TotalRecovered']),
                              )

    print("range of dist is : ", len(c))
    # print(r)
    context = {"global_data": global_data,
               "summary": r,
               "global_data_new": global_datanew,
               "countries_data_new": countries_data_new,
               }
    return render(request, 'covid/home.html', context)


def india(request):

    India_json = requests.get("https://api.covid19india.org/data.json")
    r=India_json.json()
    statewise=r['statewise']
    datenew=statewise[0]['lastupdatedtime']
    for i in range(len(statewise)):
        statewise = r['statewise'][i]
        date = statewise['lastupdatedtime']
        date = date.replace('/', '-')
        datesplit = date.split(" ")
        date = datetime.strptime(datesplit[0], '%d-%m-%Y')
        date = date.strftime('%Y-%m-%d ')
        date += datesplit[1]
        indiadata=None

        if India.objects.filter(state_code=statewise['statecode']).exists():
            indiadata=India.objects.all()
            for x in indiadata:
                if x.state_code == "UT":
                    x.state_code = "UK"
                    # x.save()
                elif x.state_code == "LA":
                    x.state_code = "LD"
                    # x.save()
                elif x.state_code == "TG":
                    x.state_code = "TS"
                    # x.save()
                elif x.state_code == "OR":
                    x.state_code = "OD"
                x.save()
            # indiadata.update()
            # UK=UT LD=LA TS=TG OD=OR
            indiadata=India.objects.exclude(state_code="TT").exclude(state_code="UN")
            # India.objects.create(active=statewise['active'],
            #                      confirmed=statewise['confirmed'],
            #                      deaths=statewise['deaths'],
            #                      new_confirmed=statewise['deltaconfirmed'],
            #                      new_deaths=statewise['deltadeaths'],
            #                      new_recovered=statewise['deltarecovered'],
            #                      recovered=statewise['recovered'],
            #                      last_update_time=date,
            #                      )
        else:

            India.objects.create(state=statewise['state'],
                                 state_code=statewise['statecode'],
                                 active=statewise['active'],
                                 confirmed=statewise['confirmed'],
                                 deaths=statewise['deaths'],
                                 new_confirmed=statewise['deltaconfirmed'],
                                 new_deaths=statewise['deltadeaths'],
                                 new_recovered=statewise['deltarecovered'],
                                 recovered=statewise['recovered'],
                                 last_update_time=date,
                                 )
            # print(statewise['state'])
    return render(request, 'covid/IndiaData.html',{"indiadata":indiadata})
