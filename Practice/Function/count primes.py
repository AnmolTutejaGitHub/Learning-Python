#Count prime : write a fumction that returns the number of prime numbers that exist up to and including a given number.
#(by convention we'll treat 0 and 1 as not prime)
#example : count_prime(100) --> 25

def count_prime(num):
    #check for 0 and 1 input
    if num<2:
        return 0
    
    # 2 or greater
    prime=[2] #list to store prime nos. (2 in prime no.), I will append prime nos. here

    #counter going up to the input num
    x=3 

    #x is going upto every number upto input number
    while x<=num:
        for y in range(3,x,2): #step jump of 2 as we can skip even numbers as they are not prime 
            if x%y==0:
                x+=2  #update condition of x as jump is of 2 .... notice x in range picture qill become clearn we are increasing range for increase in x 
                break
        else:               #for else use 
                prime.append(x)
                x+=2
    print(prime)
    return len(prime)  #length of list prime is count 

print(count_prime(100))
