l1=['a','b','c']
l2=[1,2,3,4,5]
l3=[1,'a',True ,12.5]
#print(l1)
amazon_cart=[
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0::2])
amazon_cart[0]='laptop'
new_cart=amazon_cart
new_cart[0]='gum'
#if we change in new cart something it will also get change in amazon_cart.bcoz new_cart is pointing to the amazon_cart.
print('\n')
#to avoid this use this (amazon_cart[:])<---it will copy the amazon_cart list in new cart
new_cart=amazon_cart[:]#so you will see this type of code in many code bases

print(amazon_cart[0:3])
print(new_cart)

#matrix
matrix=[
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
print(matrix[0][1])


list=["go","java","python","c"]
list1=list[:]
list[0]="rust"
print(list)
print(list1)