class House:
   def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

   def go_to(self, new_floors):
        for i in range(new_floors):
            if i < 1 or i > self.number_of_floors:
                print('Taкого этажа не существует')
            elif i < self.number_of_floors:
                 print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
