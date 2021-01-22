from django.shortcuts import render

from .models import Global, Countries, India


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
