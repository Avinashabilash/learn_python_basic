#n=1,2,3,4,5
#print(type(n))

#a=10,
#print(type(a))
#y=(7)
#print(type(y))
#c = [1, 2, 3],
#print(type(c))
#def display():
    #for i in range(1,11):
        #if i==10:
           # print("Bye!!")
#display()
#import random
#dic_no=["one","two","three","four","five","six"]
#dic=random.randint(0,5)
#print(dic_no[dic])

#year=int(input("in which year you were born? "))
#if year>1980 and year <= 1996:
 #   print("millenial")
#elif year>1996:
#    print("you are genZ")
#age = int(input("enter a age: "))
#if age >= 18:
 #   print(f"you can vote at {age}.")
#else:
 #    print(f"you can't vote at {age}.")
#a,b=0,0
#a= int(input("enter a:"))
#b= int(input("enter b:"))
#multiplcation=a*b
#print(multiplcation)

def fizzbuzz():
    for i in range (1,16):
        if i % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    # Example usage:
n = 15  # Replace with any number you want to test
fizzbuzz()
