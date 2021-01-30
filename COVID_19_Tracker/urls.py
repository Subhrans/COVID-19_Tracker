from django.urls import path

from . import views

app_name = "COVID-19"
urlpatterns = [
    path('',views.search_country,name="search_country"),
]
