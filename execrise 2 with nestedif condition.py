weight = float(input("Enter a weight in kg: "))
height = float(input("Enter a height in meters: "))

BMI = weight /height ** 2
print(f"BMI: {BMI:.2f}")

if BMI <18.5:
    print("underwieght")
elif 18.5 <= BMI < 25:
    print("Congratulations, you have a normal weight.")
elif 25 <= BMI < 30:
    print("You are overweight.")
elif 30 <= BMI < 35:
    print("You are obese (Class 1).")
elif 35 <= BMI < 40:
    print("You are severely obese (Class 2).")
else: #BMI >= 40
    print("You are very severely obese (Class 3).") 
