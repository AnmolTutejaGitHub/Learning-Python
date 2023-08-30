#Master Yoda:Given a sentence , return a sentence with words reversed

def func(sentence):
   mylist= sentence.split()  #Makes list 
   anotherlist=[]
   i=0
   for item in mylist:
      #i=0  #sets i=0 each time in lopp put it outside the loop
      n=len(mylist) #To find number of elements in mylist
      anotherlist.append(mylist[n-1-i]) #-1 for indexing strats from 0 but length doesn't
      i=i+1

   print(anotherlist)
   #convert another list into string 
   #Taken help from chatgpt to form below logic
   revsentence=' '.join(map(str,anotherlist))  #' ' for spaces between words of string
   print(revsentence)


func("My name is Anmol")

