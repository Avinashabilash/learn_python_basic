word1="abc"
word2="pqrst"
A=len(word1)
B=len(word2)
a,b=0,0
word=1
s=[]
while a < A and b < B:
    if word==1:
        s.append(word1[a])
        a+=1
        word=2
    else:
        s.append(word2[b])
        b+=1
        word=1

while a<A:
    s.append(word1[a])
    a+=1
while b<B:
    s.append(word2[b])
    b+=1
    
str_s=''.join([ char for char in s])
print(str_s)
