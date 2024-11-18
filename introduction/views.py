from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request,"index.html")

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from numpy import arange,random
from io import BytesIO
from django.http import HttpResponse
from introduction.models import Visit
from datetime import datetime

def graph(request):
    x=arange(24)
    instance=Visit.objects.get(id=1)
    hour=datetime.now().hour
    instance.data[hour]=instance.data[hour]+1
    instance.save()
    y=Visit.objects.get(id=1).data
    pyplot.bar(x,y)
    pyplot.xlim(0,24)
    pyplot.xlabel("Time(hour)")
    pyplot.ylabel("The number of visiting this URL")
    buf=BytesIO()
    pyplot.savefig(buf,format='jpeg')
    pyplot.close()
    buf.seek(0)
    return HttpResponse(buf.getvalue(),content_type='image/jpeg')