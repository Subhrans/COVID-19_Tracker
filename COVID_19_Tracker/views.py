from django.shortcuts import render
import requests
from .models import Global, Countries, India,CountryCode
from geopy.geocoders import Nominatim
import folium
from math import sqrt
from .forms import SearchLocation

# Create your views here.
def search_country(request):
    geolocators = Nominatim(user_agent="COVID_19_Tracker")
    # global_datanew = Global.objects.last()
    country=indiadata=total=country_all=tooltip_text=data=None
    rad=10
    if request.method=="POST":
        searchform=SearchLocation(request.POST)
        if searchform.is_valid():
            pk=searchform.cleaned_data['location_name']

            if pk=="India":
                indiadata = India.objects.exclude(state_code="TT")  # context
                total = India.objects.get(state_code="TT")  # context
                indialoc=geolocators.geocode(pk)
                map = folium.Map(location=(indialoc.latitude,indialoc.longitude))
                for i in indiadata:
                    statelocation=(i.lat,i.lon)
                    tooltip_text = f"{i.state.capitalize()}<br>" \
                                   f"Confirmed: {i.confirmed}<br>" \
                                   f"Recovered: {i.recovered}"
                    rad = sqrt(i.confirmed) / 20

                    folium.CircleMarker(location=statelocation, radius=rad, tooltip=tooltip_text, fill=True,
                                        fill_color="#428bca").add_to(map)
            else:
                country = Countries.objects.get(country__contains=pk)  # context
                location = (country.lat, country.lon)

                map = folium.Map(location=location,)
                country_all = Countries.objects.all()  # context

                for i in country_all:
                    pk = i.slugId
                    if i.lat == None:
                        print(pk)

                    else:
                        location = (i.lat   , i.lon)
                        rad = sqrt(i.totalConfirmed) / 100 + 3
                        tooltip_text = f"{str(pk).capitalize()}<br>" \
                                       f"Confirmed: {i.totalConfirmed}<br>" \
                                       f"Recovered: {i.totalRecoverd}"
                        folium.CircleMarker(location=location, radius=rad, tooltip=tooltip_text, fill=True,
                                            fill_color="#428bca").add_to(map)



    else:                       # Get request when page loaded Global
        searchform=SearchLocation()             #context


        map = folium.Map()  # fetch live location   #context
        country_all = Countries.objects.all()       #context
        data=Global.objects.last()                  #context

        for i in country_all:
            pk=i.slugId
            if i.lat == None:
                print(pk)
            else:
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
               }
    if data:
        context.update({'country':data})
        context.update({'global':True})

    return render(request,'covid/CountryDetails.html',context)
