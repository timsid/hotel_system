from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
from controllers.notification import *
#from controllers.main import *
#from controllers.tester import *

from django.http import HttpResponse

def InitializeData(request):
    """ Add Hotels, Customers, Reservations """
    # add hotels
    hotel = Hotel()
    rotana_hotel = hotel.add_hotel(20, "Rotana", "Abu Dhabi", 200, 40)
    sheraton_hotel = hotel.add_hotel(21,"Sheraton", "Abu Dhabi", 300, 100)
    five_hotel = hotel.add_hotel(22, "Five", "Cairo", 200, 3)

    # add customers
    customer1 = Customer('SomeOne Alive', '+2001143647417')
    customer2 = Customer('SomeOne Dead', "+2001143647417")

    # init reservation
    reserv = Reservation()
    # init notification
    notify = Notification()

    # add new reservation
    # check if hotel has empty rooms
    if hotel.get_empty_rooms_in_hotel(22) > 0: # five_hotel id ==> 22
        customer_id = customer1.customers_list.index({'name': customer2.name, "phone_number": customer2.phone_number})
        start_date = "22-5-2012"
        end_date = "20-3-2015"

        if(reserv.add_new_reservation(22, hotel.hotels_list, customer_id, start_date, end_date)):
            mes = "<h3 style='color: green'>"
            mes += notify.success_opr(customer1.name, customer1.phone_number, start_date, end_date)
            # bonus message
            mes += "</h3><h4>Refresh page to add more reservations</h4>"
    else:
        mes = "<h1 style='color: red'>sorry no rooms available</h1>"
    
    return HttpResponse(mes)

def HotelList(request):
    """ Return list of all saved hotels """
    hotel = Hotel()

    # hotel.get_all_hotels()
    # you told me to use instance directly not an function
    hotel_list = hotel.hotels_list
    
    hotel_list_output = "<h4><ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h['name'] + "</li>"
    hotel_list_output += "</ul></h4>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    """ Return list of all hotels in an city """

    hotel = Hotel()

    # select any city
    hotels_in_city = hotel.get_hotels_in_city('Abu Dhabi')

    output_list = '<h4><ul>'
    for h in hotels_in_city:
        output_list += "<li>" + h + "</li>"
    output_list += "</ul></h4>"
    return HttpResponse(output_list)

def ReservationList(request):
    """ Return all reservations for a hotel """
    reserv = Reservation()
    # this will add an empty customer
    # but the function will return the right customer
    customer = Customer('', '')

    # any hotel
    reservation_list = reserv.get_resevrations_for_hotel(22, customer.customers_list)

    output_list = "<h4><ul>"
    for r in reservation_list:
        output_list += "<li>" + r + "</li>"
    output_list += '</ul></h4>'

    return HttpResponse(output_list)

