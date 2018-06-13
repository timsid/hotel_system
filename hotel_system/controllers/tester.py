import unittest
from hotel import Hotel
from customer import Customer
from reservation import Reservation
from notification import Notification

class TestHotelClass(unittest.TestCase):
    
    def setUp(self):
        self.rotana_hotel = Hotel(20, "Rotana", "Abu Dhabi", 200, 40)
    
    def tearDown(self):
        Hotel.hotels_list = [] # empty hotels list
        self.rotana_hotel = None
    
    def test_instance(self):
        self.assertIsInstance(self.rotana_hotel, Hotel)
    
    def test_hotels_list(self):
        self.assertEqual(1, len(Hotel.hotels_list))
    
    def test_hotels_in_city(self):
        self.assertIn("20 ->>> Rotana", self.rotana_hotel.get_hotels_in_city())
        sheraton_hotel = Hotel(21,"Sheraton", "Abu Dhabi", 300, 100)
        self.assertIn("200 total rooms\n21 ->>> Sheraton has 300", sheraton_hotel.get_hotels_in_city())
    
    def test_empty_rooms(self):
        self.assertEqual(40, self.rotana_hotel.get_empty_rooms_in_hotel())
    
    def test_hotel_name(self):
        self.assertEqual("Rotana", self.rotana_hotel.name)
    
    def test_hotel_id(self):
        self.assertEqual(20, self.rotana_hotel.hotel_id)

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("SomeOne Alive", "+200112365425")
        self.customer2 = Customer('SomeOne Dead', "+200112365458")
    
    def tearDown(self):
        self.customer1 = None
        Customer.customers_list = []
    
    def test_instance(self):
        self.assertIsInstance(self.customer1, Customer)
    
    def test_customer_list(self):
        self.assertEqual(2, len(Customer.customers_list))
        customer3 = Customer('SomeOne something', "+200112365458")
        self.assertEqual(3, len(Customer.customers_list))
    
    def test_customer_index(self):
        customer_id = self.customer2.customers_list.index({"name": self.customer2.name, "phone_number": self.customer2.phone_number})
        self.assertEqual(1, customer_id)

class TestReservation(unittest.TestCase):

    def setUp(self):
        self.new_reserv = Reservation(20, 'Rotana', "SomeOne Alive")
    
    def test_instance(self):
        self.assertIsInstance(self.new_reserv, Reservation)
    
    def test_get_reservations_0(self):
        """
        test if the result of get_resevrations_for_hotel() function 
        is an empty list before adding new resevration
        """
        self.assertEqual([], self.new_reserv.get_resevrations_for_hotel())
    
    def test_get_reservations_1(self):
        """
        Test adding new resevration
        * False --> if the hotel is not found in hotels list
        * True --> the resevration done  
        """
        hotels_list = [{
            "id" : 20,
            "name" : 'Rotana',
            "city" : "Abu Dhabi",
            "empty_rooms" : 10,
            "total_rooms" : 200,
        }]
        self.assertFalse(self.new_reserv.add_new_reservation(40, hotels_list, 0, "", ""))
        self.assertTrue(self.new_reserv.add_new_reservation(20, hotels_list, 0, "2-4-2012", "2-5-2012"))
    
    def test_get_reservations_2(self):
        # test get_resevrations_for_hotel after adding new resevration
        self.assertEqual(['>>> SomeOne Alive From 2-4-2012 To 2-5-2012'], self.new_reserv.get_resevrations_for_hotel())
         
    
class TestNotification(unittest.TestCase):

    def setUp(self):
        self.notify = Notification()

    def tearDown(self):
        self.notify = None
    
    def test_instance(self):
        self.assertIsInstance(self.notify, Notification)

class Tester(unittest.TestCase):
    """ test running the application """
    
    def setUp(self):
        self.rotana_hotel = Hotel(20, "Rotana", "Abu Dhabi", 200, 40)
        self.sheraton_hotel = Hotel(21,"Sheraton", "Abu Dhabi", 300, 0)
        self.five_hotel = Hotel(22, "Five", "Cairo", 200, 3)
        
        self.customer1 = Customer('SomeOne Alive', '+2001143647417')
        self.customer2 = Customer('SomeOne Dead', "+2001143647417")

        self.new_reserv = Reservation(22, 'Five', self.customer1.name)
        self.notify = Notification()
    
    def tearDown(self):
        pass
    
    def test_instance(self):
        self.assertIsInstance(self.rotana_hotel, Hotel)
        self.assertIsInstance(self.sheraton_hotel, Hotel)
        self.assertIsInstance(self.customer1, Customer)
        self.assertIsInstance(self.customer2, Customer)
        self.assertIsInstance(self.new_reserv, Reservation)
        self.assertIsInstance(self.notify, Notification)
    
    def test_hotels_in_city(self):
        self.assertIn("20 ->>> Rotana", self.rotana_hotel.get_hotels_in_city())
        seven_hotel = Hotel(22, "Seven", "Abu Dhabi", 7, 15)
        self.assertIn("Seven", self.rotana_hotel.get_hotels_in_city())

    def test_empty_rooms_before(self):
        self.assertEqual(0, self.sheraton_hotel.get_empty_rooms_in_hotel())
        self.assertEqual(40, self.rotana_hotel.get_empty_rooms_in_hotel())
    
    def test__get_reservations_0(self):
        self.assertEqual([], self.new_reserv.get_resevrations_for_hotel())
    
    def test__get_reservations_1(self):
        start_date = "22-5-2013"
        end_date = "22-5-2014"
        customer_id = self.customer1.customers_list.index({'name': self.customer1.name, "phone_number": self.customer1.phone_number}) # customer1.get_index()
        self.assertTrue(self.new_reserv.add_new_reservation(self.five_hotel.hotel_id, self.five_hotel.hotels_list, customer_id, start_date, end_date))
    
    def test__get_reservations_2(self):
        self.assertEqual(['>>> SomeOne Alive From 22-5-2013 To 22-5-2014'], self.new_reserv.get_resevrations_for_hotel())
    
    def test_empty_rooms_after(self):
        self.assertEqual(2, self.five_hotel.get_empty_rooms_in_hotel())


if __name__ == '__main__':
    unittest.main()