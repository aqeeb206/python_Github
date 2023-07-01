#dictionary methods
user={
    'basket':[1,2,3],
    'greet' : 'hello',
    'age'   : 20
}
print(user.get('age'))
#print(user.get('age',90))
# the line no 8 will add a default value if 'age' does not exist in the dictionary.
#other wise it will not add if there is 'age' in the dictionary.
 
#Another way to create a dictionary by a built in function (dict).
user2 = dict (name='aqeeb aqeeb')#here name is key and 'aqeeb aqeeb' is a value.
print(user2)
#To check item in dictionary 
print('basket' in user)
#TO Access Keys use .keys() method
print('age' in user.keys())
#TO ACCESS VALUES USE .values() method
print('hello' in user.values())
#.items() method
print(user.items())
#to clear dictionary 
#print(user)
user3=user.copy()
#user.clear()
print(user3)
#.pop()--> IT REMOVE THE KEY AND VALUE ALSO IT RETURNS THE VALUE  OF WHATEVER GOT REMOVED.
#FOR EXAMPLE IF WE POP 'age' VALUE OF AGE WILL BE RETURN.
print(user3.pop('age'))
#.popitem() --->TO REMOVE LAST KEY : VALUE PAIR THAT WAS INSERTED INTO THE DICTIONARY .
print(user.popitem())
print(user)
print(user3)
#update()
user.update({'age':55})
print(user)
#AGE GOT UPDATED .IF THERE IS NO KEY LIKE AGE IT WILL CREATE A NEW KEY.