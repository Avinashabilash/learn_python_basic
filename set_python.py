set1={1,2,3,4,5,10,11,23 }
set2={1,2,3,4,5,10}
#print(set1.isdisjoint(["mohan","jenny","ram"]))
# it used to find element set1 is in set2
#print(set1.issubset(set2))
#its symbol of issubset operator here check set2 is in set1 
#print(set1<=set2) 

se={"eat","tan","nat","bat"}
se1={"ate","tea","bat"}
##superset it use to compare the se2 in se1 in same of (reverse)vice versa
## version using superset
print(se1.issuperset(se))
#symbol of .issuperset operator is >= reerse of subset

print(set1<=set2)
#clear set
var={1,2,3,4,5}
var.clear()
print(var)
var.add(5)
print(var)
# clear all the varabile hole set 
del var

