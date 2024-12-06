def gcd(a,b):
    if a==0:
         return b
    return gcd(b%a,a)
a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
print("gcd of",a,"&",b,"is =",gcd(a,b))
