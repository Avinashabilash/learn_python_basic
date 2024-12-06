import random
student_mark={
    'jenny':92,
    'harry':78,
    'Dimpy':56,
    'rahul':54,
    'aniket':99,
    'prem':34
    }
student_grade={}

for student,mark in student_mark.items():
    if mark >= 91:
        student_grade[student]="A+"
    elif  mark > 80:
        student_grade[student]="A"
    elif  mark > 70:
        student_grade[student]="B+"
    elif  mark > 60:
        student_grade[student]="B"
    elif mark >50:
        student_grade[student]="C"
    elif  mark > 40:
        student_grade[student]="D"
    else:
        student_grade[student]=random.choices(['fail','F','RA'])



print(student_grade)


    #print(mark)
    #mark=student_mark[student]
    #if mark >= 91:
     #   print(f"{student_name}:'A+'")
    #elif 81 <= mark <= 90:
     #   print(f"{student_name}:'A'")
   # elif 71 <= mark <= 80:
   #    print(f"{student_name}: 'B+'")
   # elif 61 <= mark <= 70:
  #      print( f"{student_name}:'B'")
   # elif 51 <= mark <= 60:
        #print( f"{student_name}:'C'")
    #elif 41 <= mark <= 50:
       # print(f"{student_name}'D'")
    #else:
        #print(f"{student_name}:{random.choices(['fail','F','RA'])}")


       
