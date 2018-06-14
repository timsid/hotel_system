class Hotel:
    hotels_list = []

    def __init__(self):
        pass

    def add_hotel(self, number, hotel_name, city, total_rooms, empty_rooms):
        self.hotel_id = number
        self.name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        # add new hotel to hotels list
        self.hotels_list.append({
            "id" : self.hotel_id,
            "name" : self.name,
            "city" : self.city,
            "total_rooms" : self.total_rooms,
            "empty_rooms" : self.empty_rooms
        })
    
    def get_hotels_in_city(self, city):
        """search for city in hotels list and print hotel name, total number of rooms if found """
        hotels_in_city = []
        for hotel in self.hotels_list:
            if hotel['city'] == city:
                hotels_in_city.append(hotel['name'])
        return hotels_in_city
    
    def get_empty_rooms_in_hotel(self, hotel_id):
        for hotel in self.hotels_list:
            if hotel['id'] == hotel_id:
                return hotel['empty_rooms']
            