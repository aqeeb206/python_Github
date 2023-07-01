basketl=['a','b','x','c','d','e','a']
basketl.sort()
print(basketl)
basketl.reverse()
print(basketl)
print(len(basketl))
print(basketl[::-1])#it creates a new version of list.
print(basketl)
print(list(range(1,10))) #from 0 to 9. for 0 to 10 use range(1,11)
#print(list(range(10)))alternate way.
#.join()  method its work on strings  its a string method.
sentence='!'
new_sentence=sentence.join(['hi','my','name','is','Golu'])
#alternate way is--> new_sentence=" ".join(['hi','my','name','is','Golu'])
print(new_sentence) 
#LIST UNPACKING
a,b,c,*other,d=[1,2,3,4,5,6,7,8,9]
#to remain other items packed use (*  followed by a variable . here variable is (other)).
print(a)
print(b)
print(c)
print(other)
print(d)#d will be the very last item. here it will be 9.