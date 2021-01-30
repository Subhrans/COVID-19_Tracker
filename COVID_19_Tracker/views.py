from django.shortcuts import render
import requests
from .models import Global, Countries, India,CountryCode
from geopy.geocoders import Nominatim
import folium
from math import sqrt
from .forms import SearchLocation

# Create your views here.
def home(request):

    countries_data_new = Countries.objects.all()
    global_datanew = Global.objects.last()
    context = {
        "global_data_new": global_datanew,
        "countries_data_new": countries_data_new,
    }
    return render(request, 'covid/home.html', context)


def india(request):
    indiadata=India.objects.all()
    indiadata=India.objects.exclude(state_code="TT")
    total=India.objects.get(state_code="TT")
    return render(request, 'covid/IndiaData.html',{"indiadata":indiadata,"total":total})

def country_data(country_name):
    url = "https://covid-19-statistics.p.rapidapi.com/provinces"

    querystring = {"iso": "CHN"}

    headers = {
        'x-rapidapi-key': "63eb16e94fmsh86f425f3554a1c0p1ede21jsn7d2edf6fb6c4",
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r=response.json()['data']
    # print(response.json()['data'][1])
    # for i in range(len(r)):
    #     print(r[i])
    return response.json()

# this function will execute only one time
def country_code():

    url = "https://covid-19-statistics.p.rapidapi.com/regions"

    headers = {
        'x-rapidapi-key': "63eb16e94fmsh86f425f3554a1c0p1ede21jsn7d2edf6fb6c4",
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    r=response.json()['data']
    print(len(r))

    for i in range(1):
        pass
        # print(r[i])
        courtywisedata=country_data(r[i]['iso'])
        # CountryCode.objects.create(iso=r[i]['iso'],name=r[i]['name'])

    print("try")
    # print(r['iso'])

# country_code()

def search_country(request):
    geolocators = Nominatim(user_agent="COVID_19_Tracker")
    # global_datanew = Global.objects.last()
    country=indiadata=total=country_all=None
    if request.method=="POST":
        searchform=SearchLocation(request.POST)
        if searchform.is_valid():
            pk=searchform.cleaned_data['location_name']

            if pk=="India":
                indiadata = India.objects.exclude(state_code="TT")  # context
                total = India.objects.get(state_code="TT")  # context
            else:
                country = Countries.objects.get(country=pk)  # context

            countryloc = geolocators.geocode(pk)
            lat = countryloc.latitude
            lon = countryloc.longitude
            location = (lat, lon)
            # rad = sqrt(i.totalConfirmed) / 100 + 3
            map = folium.Map(location=location,)
            folium.CircleMarker(location=location, radius=15, tooltip="none", fill=True,
                                fill_color="#428bca").add_to(map)

    else:                       # Get request when page loaded Global
        searchform=SearchLocation()             #context
        map = folium.Map()  # fetch live location   #context
        country_all = Countries.objects.all()       #context
        data=Global.objects.last()                  #context

        for i in country_all:
            pk=i.slugId
            # countryloc = geolocators.geocode(pk)
            if i.lat == None:
                print(pk)

            else:
                # print("country_name:", pk, "lat: ", i.lat, "lon:", i.lon)
                # getcountry=Countries.objects.get(slugId=pk)
                # getcountry.lat=countryloc.latitude
                # getcountry.lon=countryloc.longitude
                # getcountry.save()
                location = (i.lat, i.lon)
                rad=sqrt(i.totalConfirmed) / 100+3
                tooltip_text=f"{pk}<br>" \
                             f"Confirmed: {i.totalConfirmed}<br>" \
                             f"Recovered: {i.totalRecoverd}"
                folium.CircleMarker(location=location, radius=rad, tooltip=tooltip_text,fill=True,fill_color="#428bca").add_to(map)

    map=map._repr_html_()
    context = {'country': country,
               'indiadata':indiadata,
               'total':total,
               'map':map,
               'searchform':searchform,
               'country_all':country_all,
               # "global_data_new": global_datanew,
               }

    return render(request,'covid/CountryDetails.html',context)
def countryview(request,pk):
    pass