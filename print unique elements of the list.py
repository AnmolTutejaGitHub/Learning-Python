#write a python function that takes a list and returns a new list with unique elements of the first list 

def unique_list(st):
    return list(set(st))

print(unique_list([1,1,1,1,2,2,2,3,3,3,4,4,5,5,5,66,6,7,6,7,5,6,4,6,4,6,4,56,7,90,0,97,5,6,8,9,6,78]))
#OR can do this (logical method)

def uniquee_list(a):
    seen_numbers=[]
    for number in a:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers

print(uniquee_list([1,1,1,2,3,45,6,6,6,12,2,2,2,6,8,8,8])

