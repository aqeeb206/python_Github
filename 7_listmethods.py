#list methods
basket=[1,2,3,4,5]
print(len(basket))
#adding ones methods
# longlist='''
# basketl.append('g')
# basketl.insert(5,'90')
# basketl.extend(['100','gjg'])
# '''
# newlist=basket.append(100)
# print(newlist)#newlist will be completely none bcoz append cganges the list in place.
# #in place means it doesnt produce a value .all it does is to append 100 to the basket that you give it
# #so in order for our newlist to have 100 at the end .
# basket.insert(4,100)
# basket.extend([200])#add or extend the objects in the last of the list depending upon the how many you do
# print(basket)
# new_list=basket
# print(basket)
# print(new_list)

#removing
'''
basket.pop()
print(basket)
l1=basket.pop(0)#it will return the value of the index that is removed .here 1 will be removed.
print(l1)
print(basket)
print('\n')
basket.remove(3)
print(basket)
newbasket=basket[:]
print(newbasket)
newbasket.clear()#clear removes what ever is in the list
print(newbasket)

'''

#important ones
basketl=['a','b','x','c','d','e','a']
print(basketl.index('c'))# it will return the  index of char 'c' which is 2.
print(basketl.index('b',0,2))# it will start looking for char 'b' from index 0 to 2.
print(len(basketl))
#len()..it starts counting from one like humans
#in is a keyword used to check value is present in a list ,tuple,etc.
print('c' in basketl)
print('d'in basketl)
print(basketl.count('c'))#we can check how many times an item occur.
#basketl.sort()# it sorts the list
#print(basketl)
print(sorted(basketl))#sorted is a function . it does not modify the basket it creates a new one.
newbasket=basketl.copy()#copy the list for us and returns a new list
print(newbasket)
basketl.reverse()#it reverses the list
print(basketl)
#learn more from google if you need it.