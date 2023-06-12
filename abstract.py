from abc import ABC, abstractmethod
from enum import Enum

class traintype(Enum):
    regional = 1
    inter_city = 2

class train_driver:
    def __init__(self,age,name,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def set_salary(self,salary):
        self.salary =salary

class meansoftransport(ABC):
    def __init__(self, max_speed , efficiency, seats) -> None:
        super().__init__()
        self.max_speed = max_speed
        self.efficiency = efficiency
        self.seats = seats

    @abstractmethod
    def maintain(self):
        pass

    @abstractmethod
    def man_vehicle(self):
        pass

class train(meansoftransport):
    def __init__(self, max_speed, efficiency, seats, coaches) -> None:
        super().__init__(max_speed, efficiency, seats)
        self.coaches = coaches

    def maintain(self):
        print("doing maintainence")

    def man_vehicle(self, traindriver: train_driver):
        self.driver = traindriver

class regionaltrain(train):
    def __init__(self, max_speed, efficiency, seats, coaches) -> None:
        super().__init__(max_speed, efficiency, seats, coaches)
        self.train_type = traintype(1)

class inntercitytrain(train):
    def __init__(self, max_speed, efficiency, seats, coaches) -> None:
        super().__init__(max_speed, efficiency, seats, coaches)
        self.train_type = traintype(2)

t1 = train(200,8,29,9)
rt1 = regionaltrain(100,9,20,2)
it1 = inntercitytrain(150,8,90,10)
t1.maintain()
rt1.maintain()
it1.maintain()

def train_maintain(train: regionaltrain or inntercitytrain):
    print("start of train type: " , train.train_type)

train_maintain(rt1)
train_maintain(it1)



    