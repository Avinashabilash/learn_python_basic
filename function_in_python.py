import math

#def greet():
    #print(f"hi {name}")
    #print(f"hello we are fan of u")



def calculation(height,widht,coverage=7):#7 square meter 
    area=height*widht
    no_of_cans=math.ceil(area / coverage)
    print(f"you need {no_of_cans} buy a cans")
    #return no_of_cans 

height=float(input("enter a height: "))
widht=float(input("enter a widht of wall: "))
#print(calculation(height,widht))
calculation(height,widht)

def function(total_mark):#this total_mark is parameter
   avrg=total_mark/5#basically parameter def function varible using define a fuciton expect
   print(avrg)#genally its palce holder
function(10)#argument its a function call actual value used to pass data type 
function(35)#the value inside the function
