class A:
    def display(self):
        print("display from A class")
class B(A):
    def display(slef):
        print(F"dispaly from B class")
class C:
    def show(self):
        print("Hi from C class")
class D(B,C):
    def display(self):
        A.display(self)
        super().display()
        print("display from D class")
d=D()
d.display()
d.show()
print(D.mro())
help(help)

class University(Obj):
    def __init__(self,Name):
        self.Name=Name

    def showDetails(self,Details):
        self.Details=Details
    def display(self):
        print(F"{self.__class__.__name__} name is: {self.Name} and Unveristy details: {self.Details}")

class Course(University):
    pass

class Branch(University):
    pass 
    
class student(University):
    pass
   
class Faculty(University):
    pass
   
uni=University("vels")
uni.showDetails("pallavaram")
uni.display()
cou=Course("python")
cou.showDetails("dsa")
cou.display()
bra=Branch("engineering")
bra.showDetails("3Floor class")
bra.display()
stu=student("avi")
stu.showDetails("trichy")
stu.display()
fac = Faculty("Thuirga")
fac.showDetails("chennai")
fac.display()

