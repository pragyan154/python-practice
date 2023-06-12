class Animal:
    def __init__(self, name) :
        self.name =name
    def eat (self):
        print(f"{self .name} is eating")

class CanFly:
    def fly(self):
        print (f"{self.name} is flying")

class CanSwim:
    def swim(self):
        print (f"{self.name} is swimming")

#mutiple inheritance
class Duck(Animal, CanSwim, CanFly) :
    def __init__(self, name):
        super().__init__(name)

class Penquin(Animal, CanSwim) :
    def init (self, name):
        super().__init__(name)


donald =Duck("Donald") 
pingu =Penquin("penq")
donald.eat()
donald.fly()
donald.swim()
pingu.eat()
pingu.swim()




#--------------------------------------------------------



#  class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def accelerate (self):
#         print(f"The {self.color} {self.brand} is acceelrating")
#     def brake(self):
#         print(f"The {self.color} {self.brand} is braking")


# #parent of Car is vehicle 
# class Car (Vehicle):
#     def __init__(self, brand, color, doors) :
#         super().__init__(brand, color) 
#         self.doors=doors

#     def honk(self):
#         print(f"The ${self.color} ${self .brand} is honking horn")

# class Motorcycle(Vehicle):
#     def __init__(self, brand, color):
#         super().__init__(brand, color)
#     def wheelie(self):
#         print(f"The ${self.color} ${self .brand} is popping a wheelie")

# mycar = Car("Toyota", "red", 4)
# mymotorcycle = Motorcycle("Harley", "black")
# #these would call base calass methods 
# mycar. accelerate()
# mycar.brake()
# #derived class method would be called 
# mycar.honk()
# mymotorcycle.wheelie()



#--------------------------------------------------------









# class book:
#     def __init__(self,title):
#         self.title = title

# class news:
#     def __init__(self, news):
#         self.news = news

# b1 = book("xx")
# b2 = book("yy")

# n1 = news("khabar")
# n2 = news("kkoko")

# print(type(b1))
# print(type(b2))

# print(type(n1)== type(n2))
# print(isinstance(n2,object))