from django.shortcuts import render
import datetime
# Create your views here.
def filter(request):
    t=datetime.datetime.now()
    d={'data':'hi filteR how RE u','t':t,'c':1}
    return render(request,'filter.html',d)