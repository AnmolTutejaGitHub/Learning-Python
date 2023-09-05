def swap_case(s):
    swapped=''
    for i in s:
        if i==i.upper():
            swapped=swapped+i.lower()
            
        elif i==i.lower():
             swapped=swapped+i.upper()
    return swapped
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
