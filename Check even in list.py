#Check even in list 
def check_even_in_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass
            
    return False
        

print(check_even_in_list([1,2,5]))
