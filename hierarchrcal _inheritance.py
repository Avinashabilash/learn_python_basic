class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showDetails(self):
        print(F"name: {self.name},age: {self.age}")
        
    def eat(self):
        print("i can eat")
class Male(human):
    def __init__(self,m_name,age,location):
        human.__init__(self,m_name,age)
        self.location=location()
    def sleep(self):
        print("i can sleep whole day.")
class female(human):
    def work(self):
        print("i can code")
#female_1=female("avinas",20)
#female_1
#female_1.eat()
#female_1.work()
male_1=Male("avi",40,"Dehli")
#male_1.showDetails()
#male_1.eat()
#male_1.sleep()
