class House:
   def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

   def go_to(self, new_floors):
       if new_floors > self.number_of_floors:
           print('Taкого этажа не существует')

       if new_floors < self.number_of_floors:
           for i in range(1, new_floors + 1):
               print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
