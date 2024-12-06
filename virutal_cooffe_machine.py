product={
    "water":"250ml",
    "milk":"50ml",
    "cofee":"58g",
    "money":0
}

type_coffee={
    "latte":150,
    "espresso":100,
    "cappuccino":200
}
condition=True
while condition:
    choice=input("what do u like to have? (latte/espresso/cappuccno): ")
    if choice in type_coffee:
        while True:
            coin1=int(input("how many 5rs.coins: "))
            coin2=int(input("how many 10 rs.coins: "))
            coin3=int(input("how many 20 rs.coins: "))
            coins=(coin1*5)+(coin2*10)+(coin3*20)
            coffee_price=int(type_coffee[choice])
            print(coffee_price)
            if coins>=coffee_price:
                product["money"]+=coffee_price
                change=coins-coffee_price
                print(f"perparing your {choice}.ur change is {change}rs have change.")
                break
            else:
                print("Sorry, you don't have enough money. Kindly add more coins.")
                continue
    while True:
        wanna_again = input("What do you like to have? (latte/espresso/cappuccino/report/off): ")
        if wanna_again == "report"or "r":
            print(product)
        elif wanna_again == "off":
            condition=False
            break
        elif wanna_again in Type_coffee:
            break
        else:
            print(f"Preparing your {wanna_again}")
            continue
        if not condition:
            break
