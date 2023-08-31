#Displaying information

print([1,2,3])
print([4,5,6])
print([7,8,9])

#instead do this: create a display function
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

example_row=[1,2,3]
#calling
display(example_row,example_row,example_row)

#flexibility of doing this is:
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

display(row1,row2,row3)

#reassignment 
row2[1]='X'
display(row1,row2,row3)


##Accepting user input

position_index=int(input("Choose an index position:"))
row1[position_index] #defined in displaying information

#Validating user input
#checking for correct data type
def user_choice():
    #variables
    #inital
    choice='wrong' #initialising with a string so it will enter loop for 1st time 
    acceptable_range=range(0,10)
    within_range=False

    #Two condition to check
    #digit or within_range==False
    while choice.isdigit()==False or within_range==False:

        choice=input("Please enter a number(0,10):")
        #digit check
        if choice.isdigit()==False:
            print("Sorry that is not a digit!")

        #range check
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print("Sorry you are out of range(0,10):")
                within_range=False
        
    return int(choice)
