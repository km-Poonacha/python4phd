# -*- coding: utf-8 -*-
"""
This section covers some of the most important datatypes and how we can assign values and read values from them

we need to cover datetime and csv libraries

main objective is to input a sentence and figure out if the sentiment in the sentence is positive or negative 
AFINN is a list 2000 + of English words rated for valence with an integer
between minus five (negative) and plus five (positive) 
"""
from datetime import date

""" to initialize or not to initialize ? """
matrix_2by2 = []

# these are data types
integer = 99
string = 'poonacha'

print('This is an integer: ',integer )
print('This is a string: ',string )
# these are data structures - it is a combination of the the basic data types into more complex ways 
# note tupe and strings are immutable while lists mutable.. that is you can add and delete elements to a list
i_list = [1,2,3,4]
c_list = ['day','month','year']
print('This is an integer list: ',i_list )
print('This is a char list: ',c_list )

dict_date = {'day' : 29 , 'month' : 1, 'year' : 2017}
print('This is a dictionary: ',dict_date)
print('Today in dictionary is: day - ',dict_date['day'],' month - ',dict_date['month'],' year - ', dict_date['year'] )

date_today = date.today()
print('This is today: ', date_today)


""" lets play with these data types """
""" First we will see how the output looks. Remeber that integer, string bool are data types while lists dict are data structures
 also there are data structures called tuples that can be assigned using () rather than []. tuples however are immutable as in you 
can not add or delete elemets into them """


""" Editing these data types"""

#concatinating a string 
print( string + 'km' )
#data type conversion str() and int ()
print(type(date))
print(str(date).split('-'))

# using split()
string2 = input('Enter a string pls: ')
print (string2)
print (string2.split( ))

# create a matrix using append() and insert()

# functions .. lets create a function to input a sentence and splits the sentence into words
# understand local variables 
# enter arguments into the functions and return from the function 


""" EX 1: Lets create a dictionary with keys "day, month and year" and assign values """
def splitwords():
    string2 = input('Enter a string pls: ')
    words = string2.split( )
    return words
    
def main():
    l_words = splitwords()
    


    
    
main()
