## private class##
class Student:
    def __init__(self, name, roll):
        self.name=name
        self.__roll = roll
    def display(self):
        print(f"hi i am {self.name} from student rollno is {self._Student__roll}")
class Teacher(Student):
    def __init__(self,name,rollno):
        super().__init__(name,rollno)
s=Student("rahul",21619151)
print(s.name)
print(s._Student__roll)
s.display()
t=Teacher("eat",21619150)
print(t.name)

## proctect class##
#class university :
#    def __init__(self,name,place):
    #    self.name=name
    #    self._place=place
 #   def department(self,departementname,class_name):
  #      self._departemnt_name=departementname
   #     self._class_name=class_name
#
#class School(university):
#    def __init__(self,name,_place):
#        super().__init__(name,_place)
 #       print(f"{self.__class__.__name__}name:{self.name}, place:{self._place}")

#s=School("vles","pallavram")
#s.department("CSE","A")
#print(f"department : {s._departemnt_name}")
#print(f"class name: {s._class_name}")
