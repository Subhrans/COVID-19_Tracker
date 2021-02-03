from math import sqrt

import folium
from django.shortcuts import render
from geopy.geocoders import Nominatim

from .forms import SearchLocation
from .models import Global, Countries, India


# App View
def search_country(request):
    geolocators = Nominatim(user_agent="COVID_19_Tracker")      # Initialize App folder to get latitude and longitude
    country = indiadata = total = country_all = tooltip_text = data = map = None    # Initialize context variables
    country_name_list = Countries.objects.values_list('country', flat=True)     # Fetched all country name as a list
    if request.method == "POST":            # When user search country or state or district
        searchform = SearchLocation(request.POST)
        if searchform.is_valid():       # Checking the user input value is empty or not
            pk = searchform.cleaned_data['location_name']       # Getting user input and store in a variable

            if pk.upper() == "INDIA":
                indiadata = India.objects.exclude(state_code="TT")  # Getting all rows of India table except (Total) row
                total = India.objects.get(state_code="TT")  # Getting (Total Cases) row
                indialoc = geolocators.geocode(pk)      # Getting India's Latitude Longitude
                map = folium.Map(location=(indialoc.latitude, indialoc.longitude), zoom_start=4.5)  # Creating a Map to specific loation
                for i in indiadata:
                    statelocation = (i.lat, i.lon)      # Getting each state location's latitude longitude
                    tooltip_text = f"{i.state.capitalize()}<br>" \
                                   f"Confirmed: {i.confirmed}<br>" \
                                   f"Recovered: {i.recovered}"
                    rad = sqrt(i.confirmed) / 20        # Fixed radius of India view on Map

                    folium.CircleMarker(location=statelocation, radius=rad, tooltip=tooltip_text, fill=True,
                                        fill_color="#428bca").add_to(map)   # Draw circle's of each location's, added to Map object
            else:
                country = Countries.objects.get(country__iexact=pk)  # Different Country Details
                location = (country.lat, country.lon)

                map = folium.Map(location=location, min_zoom=2, zoom_start=5)
                country_all = Countries.objects.all()  # context

                for i in country_all:
                    pk = i.slugId
                    if i.lat is None:
                        continue

                    else:
                        location = (i.lat, i.lon)
                        rad = sqrt(i.totalConfirmed) / 100 + 3
                        tooltip_text = f"{str(pk).capitalize()}<br>" \
                                       f"Confirmed: {i.totalConfirmed}<br>" \
                                       f"Recovered: {i.totalRecoverd}"
                        folium.CircleMarker(location=location, radius=rad, tooltip=tooltip_text, fill=True,
                                            fill_color="#428bca").add_to(map)

    else:  # Get request when page loaded Global
        searchform = SearchLocation()  # context

        map = folium.Map(min_zoom=1.5)  # fetch live location  context
        country_all = Countries.objects.all()  # context
        data = Global.objects.last()  # context

        for i in country_all:
            pk = i.slugId
            if i.lat is None:
                continue
            else:
                location = (i.lat, i.lon)
                rad = sqrt(i.totalConfirmed) / 100 + 3
                tooltip_text = f"{pk}<br>" \
                               f"Confirmed: {i.totalConfirmed}<br>" \
                               f"Recovered: {i.totalRecoverd}"
                folium.CircleMarker(location=location, radius=rad, tooltip=tooltip_text, color="#428bca", fill=True,
                                    fill_color="#428bca").add_to(map)

    map = map._repr_html_()
    context = {'country': country,
               'indiadata': indiadata,
               'total': total,
               'map': map,
               'searchform': searchform,
               'country_all': country_all,
               'country_name_list': country_name_list,
               }
    if data:
        context.update({'country': data})
        context.update({'global': True})

    return render(request, 'covid/CountryDetails.html', context)


def search_state(request):
    pass
