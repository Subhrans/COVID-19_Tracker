import requests
from django.shortcuts import render


# Create your views here.

def home(request):
    r = requests.get('https://api.covid19api.com/summary')
    summary = r.json()
    # summary=json.dumps(summary,indent=4, separators=('. ','= '))
    # summary=dict(summary)
    global_data = summary['Global']
    print(summary)
    print(type(global_data))
    print(global_data)
    context = {"global_data": global_data,
               "summary": summary,
               }
    return render(request, 'covid/home.html', context)
