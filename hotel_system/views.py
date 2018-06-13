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
