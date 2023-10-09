# Write a program with a function that accepts a string from keyboard and create a new string after converting character
# of each word capitalized. For instance, if the sentence is “stop and smell the roses”
# the output should be “Stop And Smell The Roses”

s = input("Enter a string:")
mylist = s.split()

for i in range(len(mylist)):
    mylist[i] = mylist[i][0].upper() + mylist[i][1:]

output_string = ' '.join(mylist)
print(output_string)
