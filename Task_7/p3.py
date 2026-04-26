class Flight:
    def __init__(self):
        self.passengers = []

    def add_passenger(self,passenger_obj):
        self.passengers.append(passenger_obj)

    def passengers_info(self):
        for p in self.passengers:
            print(f"Name : {p.name}, Age : {p.age}, Country : {p.country}")
        

class Passenger:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

p1 = Passenger("Khalid",25,"Egypt")
p2 = Passenger("Mai",23,"Brazil")
f1 = Flight()
f1.add_passenger(p1)
f1.add_passenger(p2)
print("The passengers information for f1 flight is : ")
f1.passengers_info()