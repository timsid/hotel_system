# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Hotel
from .models import Customer
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

def AllCustomers(request):
    """ Return all customers """

    return render(request, "reservation/customers.html",
    {
        'customers': Customer.objects.all(),
        'page_class': 'customers',
        'page_title': 'All Customers'
    })

def ReservationList(request):
    """ Return all reservations for a hotel """

    reserv_list = Reservation.objects.filter(hotel_id= 1)
    out = "<ul>"
    for r in reserv_list:
        out += "<li>{} for: {} ({} - {})".format(r.hotel, r.customer, r.start_time.strftime("%d/%b/%Y %H:%I"), r.end_time.strftime("%d/%b/%Y %H:%I"))
    out += "</ul>"

    return HttpResponse(out)