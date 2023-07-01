# dictionary={
#     'a': 2,
#     'b': 12,
#     'c': 26
# }
# print(dictionary['a'])

# my_dictionary = {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
# }
# my_list = [
#    {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
#    },
#    {
#     'a': [4,5,6],
#     'b': 'hello',
#     'x': True
#    }
# ]
# print(my_list[0]['a'][2])
# print(my_dictionary['a'][1])

# Dictionary Keys
# dictionary keys have special property it means it is mutable
my_dictionary = {
     '123'  : [1,2,3],
     True : 'hello',
    '[100]': True,
    '123' : 'hii'  #it will overwrite the previous key-->'123' on line 31.
    # so a key in dictionary has to be a unique .

 }
#   a list cannot become a key because it is mutable .it should also be unique
#  most of the times a key for a dictionary is sometimes descriptive like a string
print(my_dictionary['123'])
