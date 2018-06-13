class Customer:
    """ add customer name and customer`s phone number to customers list """
    customers_list = []
    def __init__(self):
        pass
    
    def add_customer(self, customer_name, phone_number):
        self.name = customer_name
        self.phone_number = phone_number
        self.customers_list.append({
            'name': self.name,
            'phone_number': self.phone_number
        })