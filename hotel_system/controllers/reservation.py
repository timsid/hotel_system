class Reservation():
    resevration_list = []
    def __init__(self):
        pass
    
    def get_resevrations_for_hotel(self, hotel_id, customer_list):
        """ search for hotel_name in reservation list and print customer name """
        reserv_list = []
        for hotel in self.resevration_list:
            if hotel['hotel_id'] == hotel_id:
                customer_name = customer_list[hotel['customer_id']]['name']
                mes = "%s From %s To %s"%(customer_name, hotel['start_date'], hotel['end_date'])
                reserv_list.append(mes)
        return reserv_list
    
    def add_new_reservation(self, hotel_id, hotels_list, customer_id, start_date, end_date):
        """ check if there is empty rooms in hotel name """
        for hotel in hotels_list:
            if hotel['id'] == hotel_id:
                hotel['empty_rooms'] -= 1
                new_reservation = {
                    "hotel_id": hotel_id,
                    "customer_id": customer_id,
                    "start_date": start_date,
                    "end_date": end_date
                }
                self.resevration_list.append(new_reservation)
                return True
        return False