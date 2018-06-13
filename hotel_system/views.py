from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
#from controllers.notification import *
#from controllers.main import *
#from controllers.tester import *

from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse('Hello Django')

def WelcomePage(request):
    return HttpResponse('Welcome Page')

"""def HotelList(request):
    # call the function to get all hotels
    hotel = Hotel()
    # hotel.get_all_hotels()
    # you told me to use instance directly not an function
    hotel_list = hotel.hotels_list
    
    hotel_list_output = "<ul>"
    for h in hotel_list"""