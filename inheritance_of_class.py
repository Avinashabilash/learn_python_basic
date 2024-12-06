class Human:
    def __init__(self,no_laptop):
        self.num_of_eye=34
        self.num_of_nose=45
        self.laptop=no_laptop
    def ability(self):
        print("i can eat,sleep,walk,run,think,jump,work,farming,etc....")
    def power(self):
        print("one lion power, two hourse power, three elephates power")
    def work(self):
        print("hard worker")
class Male(Human):
    def __init__(self,name,top):
        super().__init__(top)
        self.name=name
    
    def flirt(self):
        print(" male also human but they have sex organ or differnt")
    def work(self):
        super().work()
        print("i can work relax")
#human=Human("avinash",32)
#human.work()

human_1=Male("avinash",32)
#human_1.ability()
#human_1.power()
#human_1.flirt()
human_1.work()
print(human_1.num_of_eye)
print(human_1.name)
print(human_1.laptop)
