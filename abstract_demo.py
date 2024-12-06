from abstract_class import vehicle
class Bike(vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("self with kick ")
class Scooty(vehicle):
    def __init__(self,n):
        super().__init__(n)
        self.no_of__tyres=n

    def start(self):
        print("self start")
        
class Car(vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.no_of__tyres=n
        self.no_of_gears=6

    def start(self):
        print("self with key")
        
        
