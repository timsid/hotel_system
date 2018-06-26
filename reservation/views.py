# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Hotel
from .models import Reservation
# Create your views here.

def DefaultView(request, addon = ''):
    """ Show all urls in default page like a navigation """

    out = "<h1>Welcome to Hotel Reservation App</h1>"
    out += """
    <h3>Here List of all urls:</h3>
    <h4>
        <ul>
            <li><a href='allhotels'>Get all saved hotels</a></li>
            <li><a href='hotelincity'>Get all hotels In (Abu Dhabi)</a></li>
            <li><a href='reservationlist'>Get all reservations for hotel Shelton (hotel_id = 1)
        </ul>
    </h4>
    """
    return HttpResponse(out)
    #return render(request, "reservation/index.html")

def AllHotels(request):
    """ Return list of all saved hotels """

    # hotels_list = "<ul>"
    # for h in Hotel.objects.all():
    #     hotels_list += "<li>" + h.hotel_name + "</li>"
    # hotels_list += "</li>"

    #return HttpResponse(hotels_list)

    return render(request, "reservation/index.html", {'hotels': Hotel.objects.all()})

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