#sliding window 
def count_substring(string, sub_string):
        i=0
        j=len(sub_string)-1
        count=0
        # for _ in range(len(string)):
        while j<len(string):
            if string[i:j+1] == sub_string:
                count+=1
            i+=1
            j+=1
        return count
                
            

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
