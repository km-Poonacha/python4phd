# -*- coding: utf-8 -*-
"""
This section covers some of the most important datatypes and how we can assign values and read values from them
"""
from datetime import date
""" to initialize or not to initialize ? """
matrix_2by2 = []


integer = 99
string = 'poonacha'
i_list = [1,2,3,4]
c_list = ['p','po','poo','poon']
dictionary = {'p' : 1 , 'po' : 2, 'poo' : 3, 'poon' : 4}
date = date.today()

""" lets play with these data types """
""" First we will see how the output looks """

print('This is an integer: ',integer )
print('This is a string: ',string )
print('This is an integer list: ',i_list )
print('This is a char list: ',c_list )
print('This is a dictionary: ',dictionary)
print('This is today: ', date)

""" Finding the data types """
print(type(date))

""" Editing these data types"""

#concatinating a string 
print( string + 'km' )
#can you repeat the same with date ?
print(str(date) * 4)

# using spli()

string2 = input('Enter a string pls: ')
print (string2)
print (string2.split( ))

