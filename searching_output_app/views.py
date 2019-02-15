from django.shortcuts import render
import csv
from .models import Restaurant
import datetime

def home(request):
    day = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
    time = day.time()
    week_day = day.weekday()
    if week_day==6:
        week_day = 0
    else:
        week_day +=1

    return render(request, 'searching_output_app/base.html', {'time':time,
                                                              'week_day':week_day})

def valid_places(request):
    day = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
    time = day.time()
    week_day = day.weekday()
    if week_day==6:
        week_day = 0
    else:
        week_day +=1

    valid_places = list(Restaurant.objects.filter(day=week_day))

    for el in valid_places:
        if (el.w_to < time < el.w_from) == False:
            valid_places.remove(el)
    return render(request, 'searching_output_app/valid_places.html', {'time':time,'week_day':week_day,
                                                                      'valid_places':valid_places,})
