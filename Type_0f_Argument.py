#def greet(name,dept,department):
    #print(f"hi {name}")
    #print(f"are from {dept} department")
    #if department.lower() == "yes":
       # print("welcome to college!")
    #elif department.lower() == "no":
        #print("check once again")
        #print("check in consule office")
    #else:
        #print("invalid syntax.")
        

#department=input("enter yes or no: ")
#greet("avinash",dept="cse",department=department)#keyword argument

##positonal will be alway before the keyword argument
##postional variable argument value will be in the segement


#user_input = "  hello world  "
#cleaned_input = user_input.strip()

#print(f"Original: '{user_input}'")  # Output: '  hello world  '
#print(f"Cleaned: '{cleaned_input}'")  # Output: 'hello world'

##defualt argument
#def student( name,mark=40,subject="math"):#here mark and subject are the defualt argument
    #print (f"hi {name},your mark {mark}in this {subject} subject")
#student("avi")


##Arbitary argumnet #positional
#def add(*number):
    #c=0
    #for i in number:
        #c+=i
    #print(f"sum of value: {c}")
#add(5,6,7)

#arg positional arbitary
#def add(name,*number):
    #c=0
    #for i in number:
        #c+=i
    #print(f"sum of value: {c}")
    ##print(" my name {name}")
#add("yogesh",5,6,7)

##kwgs keyword arbitary
#def student_detail(*args,**detail):
    #for key,value in detail.items():
       # print(key,value)
    #print(args)

#student_detail(1,2,name="ram",age=30,dept="cse")
#student_detail("over",name="shyam",dept="cse")




















