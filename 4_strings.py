#formatted strings
name="Jhonny"
age= 55
subject="Maths"
print('hi '+ name + ' .You are  '+ str(age) + '  years old\n')
#new feature of python 3.
#by adding f to the beginning .we can say it is a formatted strings . 
print(f'hi {name}.you are  {age} years old')
print('\n')
#another way of doing it..
print('MC is a theroetical subject {good} {x}'.format(good='learn',x='it'))
print('MC is a theroetical subject {0} {1}'.format('learn','it'))
print('\n')
print('i love and hate studying {} '.format(subject))
print('\n')
print('hi {0}.you are  {1} years old'.format('jhonny','55'))
print('\n')
print('hi {new_name}.you are  {age} years old'.format(new_name='sally',age='100'))
#string indexes
selfish,number= 'me me me','01234567'
print(selfish[3])
#[start:stop:stepover] by default stepover is 1
print(number[::2])
print(number[::-3])
#immutability # refer notes also
number+='8'
print(number)



