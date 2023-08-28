#Create a list comprehension to create a list of the first letters of every word in the string below

st="Create a list comprehension to create a list of the first letters of every word in the string below"
mylist=[word[0] for word in st.split()]
print(mylist)