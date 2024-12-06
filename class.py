class studentDetails:
    follower=0#class object variable=default class attribute
    def __init__(self,name,department):
        self.student_name=name
        self.student_department=department
    def display(self,subject):
        print(f"hi am {self.student_name} and teach {subject}")
    def update_follower(self,character):
        self.follower+=1
student_1=studentDetails("jenny","B.Tech cse")
student_2=studentDetails("abilash","B.Tech cse")
student_1.display("python")
student_1.update_follower("payal")
print(instructor_1.followers)

print(f"he is {student_2.student_name} from {student_2.student_department} department")


