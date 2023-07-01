# fname='Aqeeb'
# lname='Ansari'
# full_name=fname +'  ' + lname
# print(full_name)
# print('\n')
# #String Concatenation .
# #It only works with strings
# print('ANSARI ' + 'AQEEB')
# #Type Conversion
# str(100)
# print(str(100))
# print(type(int(str(100))))
# #refer Notes
# #Escape Sequences(\)
# weather=" \t It'\s \"kind of\" a sunny weather \n hows the day   going!"
# print(weather)
# print('\n')
# print('\n')
# long_string= '''
# WW
# 00
# --
# '''
# print(long_string)

#BUILT IN FUNCTIONS + METHODS
print(len('hellooooo'))
quote='to be or not to be'
print(quote.upper())#everything gets capitalized
print(quote.capitalize())#capitalizes first letter and rest are lower
print(quote.lower())#it lowercase everything
print(quote.find('be'))#search in the code if ots exist or no 
#return its occurrence or index
#replace('old','new')
print(quote.replace('be','me'))#it replaces 'be' by 'me'
#we are creating a new str we never modify the original one
#bcoz strings are immutable(means we cannot change once it is created).
print(quote.strip())

