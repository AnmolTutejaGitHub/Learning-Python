#nested data structures exampes in python 

#grab hello #dictionaries
d={'k1':{'k2':'hello'}}
d1=d['k1']['k2']
print(d1)

d={'k1':[{'nest_key':['this is deep',['hello']]}]}
d2=d['k1'][0]['nest_key'][1][0]
print(d2)

d={'k1':[1,2,{'k2':['This is Tricky',{'tough':[1,2,['hello']]}]}]}
d3=d['k1'][2]['k2'][1]['tough'][2][0]
print(d3)

#reassign 'hello' in this nested list to say 'goodbye' instead
list1=[1,2,[3,4,'hello']]
list1[2][2]='goodbye'
print(list1)

