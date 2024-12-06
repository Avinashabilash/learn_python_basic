name=input("enter a  letter: ").lower()
char_count={}
count=0
duplication=False
for i in range(len(name)):##i== namelenght(7) then=7
    char = name[i]## char == name"Avinash"[7]
   # print(name[i])
    for j in range(i + 1, len(name)):  # j==i+1 means==0+1,7
            if char == name[j]:
                count+=1
                duplication=True
                print(char)
print(f"Duplicate letter {name[0],name[j]}")
print(count)

if  not duplication :
    print("nomatch in word")
