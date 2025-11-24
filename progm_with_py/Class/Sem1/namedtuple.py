from collections import namedtuple
car = namedtuple('Car', ['Make', 'Model'])
my_car = car("Ford", "Figo")
print(my_car)
print(my_car.Make)
print(my_car.Model)
print(my_car[1])
print(my_car[0])



