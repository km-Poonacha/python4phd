
# coding: utf-8

# ## Lesson 1: Data and Types

# In this lesson we learn about the basic data types and data structures and play with them a little. 
# Lets start by initializing integer, string, list and dictionary 
# ### 1. Data Types
# Let us create an integer and string variable and see its output. 

# In[3]:

integer = 99
string = 'poonacha'

print('This is an integer: ',integer )
print('This is a string: ',string )


# ### 2. Data Structures
# Data structures combine the basic datatypes (integer, float, string, boolean) to create more complex types. There are several types of data structures but the most commonly used ones are "lists" and "dictionaries"
# 
# #### Lists
# We start with a list. A list is a sequence of integer / character data types.
# Let us now create two list's one with only integer data "i_list" and the other with only character data "c_list". 

# In[2]:

i_list = [1,2,3,4]
c_list = ['day','month','year']

print('This is an integer list: ',i_list )
print('This is a char list: ',c_list )


# The elements in the lists are numbered upwards from 0. Hence, we can access each element in the list using its index number. The following code prints the first element of c_list.

# In[5]:

print('The first element is: ', c_list[0])


# #### Dictionaries
# A dictionary is similar to a list but rather than an index which represents each element, the dictionary uses a unique user defined key. The following code creates a dictionary by the name "dict_date" with three elements representing the current day, month and year.

# In[6]:

dict_date = {'day' : 29 , 'month' : 1, 'year' : 2017}
print('This is a dictionary: ',dict_date)
print('Today in dictionary is: day - ',dict_date['day'],' month - ',dict_date['month'],' year - ', dict_date['year'] )


# ### 3. Some Simple Data Operations 
# 
# #### Integer / floating point
# Most integer/floating point operators that you use in stata or other languages work in python as well - eg (+,-,*,/).

# Let us write a code to find the quotient and reminder of a number given a divisor. The operator '//' can be used to find the quotient and '%' can be used to find the reminder. 

# In[1]:

number = 199
divisor = 10
rem = 199 % 10
quotient = 199 // 10
print('reminder = ', rem,'quotient = ', quotient)


# #### String
# Strings are used to input and read sentences and words. There are several operations that can be done on a string. 
# 1. Concatinating - We can use either "+" operator combine two strings. Join() can be used to combine a list of strings into a single string.

# In[15]:

string = 'poonacha'
string = string + ' medappa' 
print(string)


# 2. split('*seperator*') - We can use the split() command to split a string into a list of smaller strings depending on a specified seperator. Conversely, join('*seperator*') can be used to combine a list of strings into a single string using the seperator. If no seperator is specified, it assumes the seperator is a space or a tab. The input('*input message*') function is used to enter data from the consol. 
# 
# Let us write a code to enter a sentence and split it into a list of words. 

# In[3]:

s_input = input('Enter the sentence to be split: ')
items = s_input.split()
print(items)


# #### Lists
# Lists are mutable i.e. we can append, insert and delete elements from the list. append(*data to be entered*), insert(*index*, *data*), del(*index*)

# In[7]:

i_list = [1,2,3,4]

# Append the number 5 at the end
i_list.append(5)
print(i_list)

# Insert the 1.5 between 1 and 2
i_list.insert(1,1.5)
print(i_list)

#delete the number 2
del i_list[2]
print(i_list)

#delete the entire list
del i_list[:]
print(i_list)


# ### Excercise 1:
# Write a small code to enter a date in "dd/mm/yyyy" format. Use the split() command to split the entered date into day, month and year. Hint. you need to specify the seperater as '/'.

# In[6]:

# Enter Code




#

