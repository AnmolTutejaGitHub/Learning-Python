#Loops Basic

name='Anmol'
for i in name:
    print(i)    #i is character for string

colors=['red','yellow','blue','orange','pink']
for color in colors:  #name is element of list
    print(color)

#can do indexing for list
for color in colors:
    print(color[0])

#can do this too
for color in colors:
    print(color)
for x in color:
    print(x)


#range in for loop
for k in range(0,9,2):
    print(k)

st="Ronaldo is the best"
for i in st:
    print(i)   #prints character by character

#if want word by word
for i in st.split():
    print(i)