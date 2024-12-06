
#alphabets="abcdefghijklmnopqrstuvwxyz"
#for i in range (0,len(alphabets),4):
    #print(alphabets[i:i+4])

#import textwrap

#string="abcdefghijklmnopqrstuwxyz"
#wrap = textwrap.fill(string,width=4)
#print(wrap)   
#wrap
#string="abcdefghijklmnopqrstuwxyz"
#wrap = textwrap.wrap(string,width=4)
#print(wrap)
#input[[1,4,5],[1,3,4],[2,6]]
abc=[[1,4,5],[1,3,4],[2,6]]
abc.sort(key=lambda x:x[0])
interval = []
for i in abc:
    interval.extend(i)
print(sorted(interval))
