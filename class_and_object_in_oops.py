class insturctorinfo:
    pass
instructor_1=insturctorinfo()   
print(type(instructor_1))
 
class Car_desgin:
    pass
Thar=Car_desgin()
print(type(Thar))

#instructor_1.name="payal"
#instructor_1.address="Delhi"
#print(instructor_1.name)


class department:
    
    def __init__(self,name,address,roll_no):
        self.name=name
        self.address=address
        self.follower=0 ##default value
        self.roll_no=roll_no


department_1=department("jenny","gurgaon",21619151)
print(department_1.name)
print(department_1.roll_no)
    
    
