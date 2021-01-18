from django.urls import path
from . import views

app_name = "COVID-19"
urlpatterns = [
    path('', views.home, name="home"),
]
