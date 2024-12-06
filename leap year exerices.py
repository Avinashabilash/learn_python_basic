year = int(input("Enter a year: "))
print(f"Year: {year}")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("It's not a leap year.")
    else:      
        print("It's a leap year.")
else:
    print("It's not a leap year.")
