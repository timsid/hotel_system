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