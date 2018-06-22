# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Hotel

# Create your views here.

def AllHotels(request):
    """ Return list of all saved hotels """

    hotels_list = "<ul>"
    for h in Hotel.objects.all():
        hotels_list += "<li>" + h.hotel_name + "</li>"
    hotels_list += "</li>"

    return HttpResponse(hotels_list)

def HotelInCity(request):
    """ Return list of all hotels in a given city """

    random_city = "Abu Dhabi"
    hotels_in_city = Hotel.objects.filter(hotel_city = random_city)
    output = "<ul>"
    for h in hotels_in_city:
        output += "<li>" + h.hotel_name + "</li>"
    output += "</ul>"

    return HttpResponse(output)