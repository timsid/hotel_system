from hotel import Hotel
from customer import Customer
from reservation import Reservation
from notification import Notification

def start_app():
    rotana_hotel = Hotel(20, "Rotana", "Abu Dhabi", 200, 40)
    sheraton_hotel = Hotel(21,"Sheraton", "Abu Dhabi", 300, 100)
    five_hotel = Hotel(22, "Five", "Cairo", 200, 1)

    customer1 = Customer('SomeOne Alive', '+2001143647417')
    customer2 = Customer('SomeOne Dead', "+2001143647417")
    
    new_reserv = Reservation(22, 'Five', customer1.name)
    notify = Notification()

    print rotana_hotel.get_hotels_in_city()
    if five_hotel.get_empty_rooms_in_hotel()  == 0: # 1
        print "sorry no rooms available"
        return
    else:
        print new_reserv.get_resevrations_for_hotel()
        customer_id = customer1.customers_list.index({'name': customer2.name, "phone_number": customer2.phone_number})
        start_date = "22-5-2012"
        end_date = "20-3-2015"
        if(new_reserv.add_new_reservation(five_hotel.hotel_id, five_hotel.hotels_list, customer_id, start_date, end_date)):
            notify.success_opr(customer1.name, customer1.phone_number, start_date, end_date)
    
        print five_hotel.get_empty_rooms_in_hotel() # 0
        print new_reserv.get_resevrations_for_hotel()

start_app()