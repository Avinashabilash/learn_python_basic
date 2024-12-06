## pizza order program
pizza = input("which size of pizza do u want to have small,medium,large: ")
bill = 0

if pizza.lower() =='s':
    bill = 100
    print("pay 100")
elif pizza.lower() == 'm':
    bill = 200
    print("pay 200")
elif pizza.upper() == 'L':
    bill = 300
    print("pay 300")
else:
    print(" invaild selection size pizzza")
    bill = 0

if bill != 0:
    pepperoni=input("do u wanna add pepproni in pizza which type (y/n): ")
    if pepperoni.lower()== 'y'or  pepperoni.upper()== 'Y' :
        size_pepperoni=input("how do u like small or lager: ")
        if size_pepperoni == 's' or size_pepperoni == 'S':
            bill += 30
        elif size_pepperoni.lower()== 'l'or size_pepperoni == 'L':
            bill += 50
    else:
        print("Invalid pepperoni size selection")
    
    extra_cheese= input(" do u have extra cheese (y/n): ")
    if extra_cheese.lower() == 'y' or extra_cheese.upper() == 'Y':
        bill += 20
    else:
        print("Invalid selection of cheese")  

    
    print(f" your total bill is {bill} rupees")
