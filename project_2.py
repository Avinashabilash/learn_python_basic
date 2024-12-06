import random

digit= int(input("enter a digit u wanna: "))
symbol=int(input("how many symbol u wanna  : "))
alphabets=int(input("how many alphabets u wanna: "))
password=[]
s=["!","@","$","%","^","&","*","(",")","|","?","/",">","<"]
    
for i in range(symbol):
    seq=random.choice(s)
    password+=seq
    #print(seq,end=" ")


d="0123456789"
for j in range(digit):
    seq=random.choice(d)
    password+=seq
    #print(seq,end=" ")

L="abcdefghijklmnopqrstuvwxyz"

for k in range(alphabets):
    upp=L.upper()
    letter=L+upp
    seq=random.choice(letter)
    password+=seq
print(password)
random.shuffle(password)
li=" "
for i in password:
    li+=i
print(li)



