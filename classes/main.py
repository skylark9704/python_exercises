from Dealer import Car,Truck, Motorcycle
from Living import *

car = Car(4000,'Honda','Accord','2005',None)
motorcycle = Motorcycle(1200,'Honda','CBR','2006',None)

print(car.vehicle_type())
print(car.sale_price())

print(motorcycle.vehicle_type())
print(motorcycle.sale_price())

person = Human()
pet = Dog()

print(person.type())
print(person.can_speak())
print(person.num_legs())

print(pet.type())
print(pet.can_speak())
print(pet.num_legs())