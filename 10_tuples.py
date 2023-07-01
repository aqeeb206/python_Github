my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)
#Also it is a valid key in pyhton for dictionary
new_tuple = my_tuple[1:2]
print(new_tuple)
x,y,z, *other =(23,56,98,96,45,23)
print(x,y,z)
print(other)
#Tuple has only two methods
#.count() .index()
print(my_tuple.count(5))#it counts how many times a value is present in tuple
print(my_tuple.index(5))#it gives index of that value
