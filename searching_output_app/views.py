from django.shortcuts import render, get_object_or_404
import csv
from .models import Restaurant
import datetime

WEEK_DAYS = {1:'Monday',
             2:'Tuesday',
             3:'Wednesday',
             4:'Thursday',
             5:'Friday',
             6:'Saturday',
             0:'Sunday'}

def home(request):
    now_dt = datetime.datetime.now()
    week_day = now_dt.weekday()
    now_time = now_dt.time()

#    day = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
#    time = day.time()
#    week_day = day.weekday()
    if week_day==6:
        week_day = 0
    else:
        week_day +=1

    week_day_str = WEEK_DAYS[week_day]

    return render(request, 'searching_output_app/base.html', {'now_time':now_time,
                                                              'week_day_str':week_day_str, 'week_day':week_day ,} )

def valid_places(request):

    now_dt = datetime.datetime.now()
    week_day = now_dt.weekday()
    now_time = now_dt.time()
    if week_day==6:
        week_day = 0
    else:
        week_day +=1

    week_day_str = WEEK_DAYS[week_day]

    places_for_day= list(Restaurant.objects.filter(day=week_day))

    valid_places = []
    for el in places_for_day:
        print(el.w_to, now_time, el.w_from)
        if el.w_to == el.w_from:
            print('24 hours')
            valid_places.append(el)
            print('yes')
        elif el.w_to < el.w_from:
            if now_time >= el.w_to and now_time <= el.w_from:
                valid_places.append(el)
                print('yes')
        else:
            if now_time >= el.w_to or now_time <= el.w_from:
                valid_places.append(el)
                print('yes')

    return render(request, 'searching_output_app/valid_places.html', {'now_time':now_time,'week_day_str':week_day_str,'week_day':week_day,
                                                                      'valid_places':valid_places, })

def place_details(request, pk):
    place = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'searching_output_app/place_details.html', {'place': place})

