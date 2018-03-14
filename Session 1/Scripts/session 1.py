# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 06:49:37 2018

@author: kmpoo
"""

#int_variable = 99
#str_variable = "poonacha"
#
#print(int_variable,str_variable)

#i_list = [1,2,3,4]
#c_list = ['p','po','poo']
#
#print('this is the first element of the integer list :',i_list[0])
#print('this is the first element of the string list :',c_list[0])

#dict_date = {'day':14, 'month': 3, 'year':2018}
#
#print('today is  :',dict_date.keys())
#
#for key in dict_date.keys():
#    print(key)

#number = 199
#divisor = 10
#rem = number % divisor
#quotient = number // divisor
#print('reminder = ', rem, 'quotient = ', quotient)



#string = 'poonacha'
#print(hex(id(string)))
#string = string + ' medappa'
#print(hex(id(string)))
#
#words = string.split()
#print(words[1])

def check_if_5(number):
    if number == 5:
        return 1
    else:
        return 0


return_val = check_if_5(5)

if return_val == 1:
    print('entered number is 5')
else:
    print('not five')
    
