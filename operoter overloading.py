class person1:
    def student(self):
        self.a=20
        return self.a
class person2:
    def student(self):
        self.b=30
        return self.b
#def teacher(obj):
    #obj_instance=obj()
    #return obj_instance.student()

p_1=person1()
p_2=person2()

r=p_1.student()
t=p_2.student()

#print(int.__add__(r,t))
print(r+t)
print(r>t)
if False:
    print( f"grather is {t}")
elif True:
    print(f"less then is {r}")
#print(type(type(int)))

#print(int.__add__(0,0))
