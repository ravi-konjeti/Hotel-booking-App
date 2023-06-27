import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id":str})

# In classes while instanciating them we have to give the parameters which
# must be given in __init__ as parameters while intanciating them
class Hotel:
    watermark ="The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id # self.anything in a class is instance variable
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
#
    def available(self):
        """Check if a hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

class ReservationTicket:
    reserved = "asf"
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        a = customer_name
        print(a) # a is not recognized in the methods in this class, as a is just a


    def generate(self):
        content = f"""
            Thank you for your reservation!
            Here is your booking data:
            Name: {self.the_customer_name}
            Hotel name: {self.hotel.name}
            
            """
        return content


    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="john wick ", hotel_object=hotel1)
print(ticket.the_customer_name, ticket.customer_name)
print(ticket.generate())




