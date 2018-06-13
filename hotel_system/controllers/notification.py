from twilio.rest import Client

class Notification:
    def __init__(self):
        pass
    
    def send_sms(self, phone_number, message):
        account_sid = 'AC6e7b0d0844ba50561a68df234c859ef6'
        auth_token = '93b86d9b8fc999ff6c1dcb2007a0458e'
        twilio_number = '+16673031716'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = message,
            from_ = twilio_number,
            to = phone_number
        )
        #if not message.account_sid:
        #    return "Error: SMS Send Failed"
    
    def success_opr(self, customer_name, phone_number, str_date, end_date):
        mes = 'Successfully reserved room to: {name} From: {start} To {end}'.format(name= customer_name, start= str_date, end= end_date)
        return mes
        
        #self.send_sms(phone_number, mes)
        

    