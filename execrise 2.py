height = int(input("Enter a height: "))
Bill = 0

if height >= 3:
    print("Enjoy the ride")
    age = int(input("Enter your age: "))
    
    if age < 12:
        Bill = 150
        print("Pay amount: 150 Rupees")
    elif age <= 18:
        Bill = 250
        print("Pay amount: 250 Rupees")
    else:
        Bill = 500
        print("Pay amount: 500 Rupees")
        
    want_photo = input("Do you want to take a photo (Y/N)? ")
    if want_photo.lower() == 'y':
        Bill += 50
    elif want_photo.lower() == 'N':
        print(" have a good day")
    else:
        print(f"Your total Bill is {Bill} Rupees")

else:
    print("Sorry, you can't ride")
print("fucky you... enjoy the ride")
