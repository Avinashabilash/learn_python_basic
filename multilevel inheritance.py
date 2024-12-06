class human:
    def __init__(self,num_heart):
        self.eyes=4
        self.num_heart=num_heart
    def eat(self):
        print("i am human")
    def work(self):
        print(" i can run")
        
class Male(human):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("i can sleep")

class Boy(Male):
    def __init__ (self,num_heart,name,can_dance):
        self.know_dacning=can_dance
        human.__init__(self,num_heart)
        Male.__init__(self,name)
        #super().__init__()
    def work(self):
        #human.work(self)
        super().work()
        print("i can code")
#class programmer(Boy):
    #def work(self):
        #print("i can write programmer")

boy_1=Boy(5,"avi","jackson")
print(boy_1.know_dacning)
#person=programmer("avi")
#person.work()

#boy_1.work()
#boy_1.eat()
#boy_1.sleep()
#boy_1.boys()
#print(Boy.__mro__)
