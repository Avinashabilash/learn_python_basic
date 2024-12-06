import math
#def prime_number():
    #digit = input("Enter a number: ")
    #number = int(digit)
    #if number < 2:
        #print("Try again. Number must be greater than 1.")
        #return
    
    #prime = False
    
    #for i in range(2,number):
        #print(i)
        #print(number)
        #if number %i == 0:
            #prime = True
            #break
    
    #if prime == False:
        #print(f"Congratulations, {number} is a prime number.")
    #else:
       # print(f"{number} is a composite number.")

#prime_number()

##math method code
#def prime_number():
    #digit = input("Enter a number: ")
    #number = int(digit)
    #if number < 2:
        #print("Try again. Number must be greater than 1.")
    
    #prime = True
    
    #for i in range(2,math.ceil(number/2)+1):
        #print(i)
        #print(number)
        #if number % i == 0:
          
            #prime = False
            #break
    
    #if prime:
        #print(f"Congratulations, {number} is a prime number.")
    #else:
       #print(f"{number} is a composite number.")

#prime_number()

## time compliexity
def prime_number():
    digit = input("Enter a number: ")
    number = int(digit)
    if number < 2:
        print("Try again. Number must be greater than 1.")
        
    prime = True
    
    for i in range(2,math.isqrt(number)+1):
        print(i)
        print(number)
        if number % i == 0:
          
            prime = False
            break
    
    if prime:
        print(f"Congratulations, {number} is a prime number.")
    else:
        print(f"{number} is a composite number.")

prime_number()
