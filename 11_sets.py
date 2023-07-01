my_set={1,2,3,4,5}
#everything has to be unique it has no duplicates.
my_set.add(100)
my_set.add(2)
print(my_set)
#to convert list into set or vice versa 
#we can use it to remove duplicates.
list=[1,2,3,4,5,65,56,65,56,2,3,5]
print(set(list))
#set does not support indexing
#alternate way 
print(1 in my_set)
print(len(my_set))# it only count unique things
# .copy()  .clear()
oldset={1,2,3,4,5}
new_set=oldset.copy()
oldset.clear()
print(new_set)
print(oldset)
#other methods of sets
mera_set={100,200,300,400,500}
tera_set={400,500,600,700,800,900,1000}
print(mera_set.difference(tera_set))
#.difference() finds the difference between mera_set and tera_set which is {100,200,300}.
mera_set.discard(500)
#.discard() removes an element from a set if it is a member.
print(mera_set)
mera_set.add(500) 
#.difference_update()
mera_set.difference_update(tera_set)
#it basically removes the difference between the two sets.
#In this case 400 and 500 are removed and only 100 200 300 will remain in the mera_set
print(mera_set) #o/p---> {100,200,300}
#.intersection()
uska_set={100,200,300,400,500}
print(uska_set.intersection(tera_set))#o/p of commom things between two sets. (&) also we can use
qwerty={10000,20000,30000}

#.isdisjoint() means the sets have nothing in commom.
print(uska_set.isdisjoint(qwerty)) #o/p--> True
#.isdisjoint() means do sets have anything in commom between them.
#.union() IT JUST UNITES THE TWO SETS
print(mera_set.union(tera_set))
#alternate way
print(mera_set | tera_set)#thats work as well for union.
#.issubset() and .issuperset()
set1={1,2,3,4,5,6}
set2={1,2,3,4,5}
print(set1.issubset(set2))
print(set1.issuperset(set2))

#subset is inside the circle and super set means outside the circle of set.
# you dont have to memorize all this just google it when you need.