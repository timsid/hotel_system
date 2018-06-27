# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Hotel
from .models import Reservation
# Create your views here.

def DefaultView(request, addon = ''):
    return render(request, 'welcome.html',
        {
            'page_class': 'index',
            'page_title': 'Welcome to hotel system'
        })

def AllHotels(request):
    """ Return list of all saved hotels """

    return render(request, "reservation/hotels.html", 
    {
        'hotels': Hotel.objects.all().order_by('hotel_city'),
        'page_class': 'hotels',
        'page_title': 'All Hotels'
        })

def HotelInCity(request):
    """ Return list of all hotels in a given city """

    random_city = "Abu Dhabi"
    hotels_in_city = Hotel.objects.filter(hotel_city = random_city)
    output = "<ul>"
    for h in hotels_in_city:
        output += "<li>" + h.hotel_name + "</li>"
    output += "</ul>"

    return HttpResponse(output)

def ReservationList(request):
    """ Return all reservations for a hotel """

    reserv_list = Reservation.objects.filter(hotel_id= 1)
    out = "<ul>"
    for r in reserv_list:
        out += "<li>{} for: {} ({} - {})".format(r.hotel, r.customer, r.start_time.strftime("%d/%b/%Y %H:%I"), r.end_time.strftime("%d/%b/%Y %H:%I"))
    out += "</ul>"

    return HttpResponse(out)