#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
#exercise 1 list and list slicing
new_list = ['a', 'b', 'c']
print(new_list[1])# 'b'
print(new_list[-2])# 'b
print(new_list[1:3])# 'b','c'
new_list[0] = 'z'
print(new_list)# 'z','b','c'

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) # 'z',2,3
print(bonus) # 'z',2,3,5

#exercise list 
# using this list: 
# basket = ["Banana", 
#           ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!
# print(basket[1][1][0])

#exercise list methods

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
print(basket)

# 2. Remove "Blueberries" from the list.
basket.pop()
print(basket)
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket)
# 4. Add "Apples" at the beginning of the list
basket.insert(0,"Apples")
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))

# 6. empty the basket
basket.clear()

print(basket)

# exercise common list patterns
#fix this code so that it prints a sorted list of all of our friends 
# (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends+=new_friend
print(friends.sort())
print(friends)
