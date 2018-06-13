from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
#from controllers.notification import *
#from controllers.main import *
#from controllers.tester import *

from django.http import HttpResponse

def InitializeData(request):
    """ Add Hotels, Customers, Reservations """
    hotel = Hotel()
    rotana_hotel = hotel.add_hotel(20, "Rotana", "Abu Dhabi", 200, 40)
    sheraton_hotel = hotel.add_hotel(21,"Sheraton", "Abu Dhabi", 300, 100)
    five_hotel = hotel.add_hotel(22, "Five", "Cairo", 200, 1)
    return HttpResponse("<h2>Data Initialized<h2>")

def HotelList(request):
    """ show list of all saved hotels """
    hotel = Hotel()

    # hotel.get_all_hotels()
    # you told me to use instance directly not an function
    hotel_list = hotel.hotels_list
    
    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h['name'] + "</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    """ Show list of all hotels in an city """

    hotel = Hotel()
    
    # select any city
    hotels_in_city = hotel.get_hotels_in_city('Abu Dhabi')

    output_list = '<ul>'
    for h in hotels_in_city:
        output_list += "<li>" + h + "</li>"
    output_list += "</ul>"
    return HttpResponse(output_list)