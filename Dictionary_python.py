###----++dictionary+++---###
detail={
    'name':'avinash',
    'reg_no':21619151,
    'phone':8072268801
}
print(detail)
####or####

string=f"name:%s ,reg_no:%d ,phone:%d"%(detail['name'] , detail['reg_no'], detail['phone'])
#print(string)

####0R###
deital=dict[('name','avinash'),
    ('reg_no',21619151),
    ('phone',8072268801)]

#print(detail)

detail['borther']={123,456,789}
detail['name']={'avinash':21619151,'abilash':456}
#print(detail['name']['avinash'])
#print(detail)


print(detail.get('borther'))

data={
    1:'mohan',
    2:'ram',
    0:'jenny',
    3:'avi'
}
#print(data[0])
#del(data[0])
#print(data.pop(1))
#print(data.popitem())
#data.clear()
#print(data.keys())
#print(data.values())
#print(data.items())

#for i in data:
    #s=data[i]
    #print(s)
    #print(data[i])
