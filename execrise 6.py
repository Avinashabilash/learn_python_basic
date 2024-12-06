crush_name=input("enter a crush_name for true love calcultor : ").lower()
your_name= input("enter a your_name for true love calcultor : ").lower()

name=str(crush_name+your_name)
print(name)
love = 0
true = 0

t= name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t + r + u + e 
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love = l + o + v + e
print(t,r,u,e,l,o,v,e)

calculator = int(str(true) + str(love)) 
print(calculator)
int(calculator)

if 10> calculator and calculator <90: #10> calculator or calculator <90:
    print(f"your score is {calculator} and you are together for tom and jerry")
elif 40<= calculator <50:
    print(f"your score is {calculator} and you both are romantic couple")
else:
    print(f"your score is {calculator}")
