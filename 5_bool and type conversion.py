# #a boolean is just a false or true nothing else
# name='Aqeeb'
# is_cool=True

# is_cool=False
# print(bool(1))#--> True
# print(bool(0))#--> False
# print(bool('True'))

#Exercise 1
#Type Conversion
# birthyear=input('when or what year were you born?')
# currentyear=2022
# age=currentyear-int(birthyear)
# print(f'You are {age} years old')
#Exercise 2
username =input('enter your username\n')
password =input('enter your password\n')
confidential= len(password) * '*'
print(f'{username} and your password {confidential} is {len(confidential)} characters long  ')
