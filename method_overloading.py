#class demo:
#    def add(set,a,b):
 #       return a+b
 #   def add (self,a,b,c):
  #      return a+b+c

#d= demo()
#print(d.add(5,6,7))
#print(d.add(2,3))

##how to achive method overloading       
#using default parameter
#class demo:
#    def add(set,a,b):
 #       return a+b
 #   def add (self,a,b,c=0):## basically we add default as for c value it indicate 
  #      return a+b+c

#d= demo()
#print(d.add(5,6,7))
#print(d.add(2,3))
# using arbitary arugment
class demo:
    def add(self,*args):
        total=0
        i=0
        while i < len(args):
            total+=args[i]
            i+=1
        return total

d=demo()
print(d.add(3, 4, 5, 6))
print(d.add(3,4,87,90))
        
            
        

