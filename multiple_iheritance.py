class human:
    def __init__(self,num_heart):
        print ("valling init from Human")
        self.num_eyes=2
        self.num_heart=num_heart
        
    def eat(self):
        print("i can eat")
    #def work(self):
        #print("i can cook")#

class Male:
    def __init__(self,name):
        print("calling init from male")
        self.name=name
    def flirt(self):
        print("i can flrit")
    def work(self):
        print("i can code")#each class has same name

class female(human,Male):# user call frist human so human.work object run
    def __init__(self,name,num_heart,laptop):
        self.laptop=laptop
        human.__init__(self,num_heart)
        Male.__init__(self,name)
    def sleep(self):
        print("i can sleep")
    def display(self):
        print(F"Hi,iam {self.name} the version of laptop is{self.laptop}")
    #def work(self):
        #print("i can test")#mro method resolution order

girls = female("sviash",5,"lenov")
print(girls.num_heart)
print(girls.laptop)
girls.display()
#print(female.mro())
#girls.eat()

#print(girls.num_eyes)
#girls.work()# here is frist inlizated human class so it print the i can cook frist
#Male.work(girls)#inhertiance of same method naming 
#girls.flirt()
