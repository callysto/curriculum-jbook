![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/IntroductionToDataStructures/introduction-to-data-structures.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Python - Lists and Dictionaries


Hello! Today, we will be introducing powerful tools we can use when coding in Python: lists, dictionaries, and tuples. We will show you how to perform basic operations on these types, as well as explore their functions and methods. 

To run all the cells, find the Cell tab at the top of the page, and then select Run All. To run individual cells, click the cell you want to run, and then find the Run button at the top of the page.

### Chapter Goals:

[Introduction to Lists](#Lists) <br />
[List Basics](#List_Basics) <br />
[List Slices](#List_Slicing) <br />
[List Functions](#List_Functions) <br />
[List Methods](#List_Methods) <br />
[String Splitting](#String_Splitting) <br />
[Introduction to Dictionaries](#Dictionaries) <br />
[Dictionary Functions](#Dictionary_Functions) <br />
[Dictionary Methods](#Dictionary_Methods) <br />
[Introduction to Python Tuples](#Python_Tuples) <br />
[Tuple Methods](#Tuple_Methods) <br />
[Dictionaries with Tuples](#Dictionaries_with_Tuples) <br />
[Tuple Unpacking](#Tuple_Unpacking)

<a id='Lists'></a>
## Lists

A **list** is a data type in Python. More specifically, a list is what is known as a **linear data structure**. That is, all elements in the list are orginized in a linear order. 

Much like a string, you can access individual elements, add elements, remove elements, copy a list, etc. However, the crucial difference between a string and a list is that lists can hold multiple data types at once, whereas strings can only hold characters. Items inside a list are called **elements** and each element has an **index** starting from 0 to the length of the list. 

<a id='List_Basics'></a>
### List Basics:

To declare a list in Python, we simply enclose our items in square brackets. For example, if we type:

[1,2,3,4,5,6,7,8,9,10]

we will have created a list of elements numbered 1 to 10. Here is a list with multiple data types:

[True, False, "Hello", 1, 2, 3, 4, 5, 'a','b','c']

Like strings, we can pass lists to the print function as a whole list, or we can specify what elements to print by providing index locations.

# Declaring and Printing Lists

# List Declarations
list1 = ["physics", "chemistry", 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

print(list1[0]) # This print function prints the first element in list1
print(list2[1:5]) # This will print elements starting at index 1, that is the second element, up to index 5
print(list3) # This will print the entire list

### Creating new lists from old lists:

Like strings, we can create new lists by using the + operator and the * operator.

# Example

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2 # This will create a new list consisting of list1 and list2
print(list3)

list4 = ["Hello World! "] * 5 # This will create a new list, consitsing of Hello World! repeated 5 times
print(list4)


We can also easily check for an element in a list by using the "in" keyword, just like we did when we were checking for characters in a string.

# Checking if a given element is in a list

list1 = [1, 2, 3]

# We would like to check that 3 is in this list, to do this, we say:

print(3 in list1) # This will be true
print(4 in list1) # This will be false

#### For Loops:

On many occasions, we would like to traverse through a list or a string and perform an operation on each element. For loops allow us to manipulate each element in a list in a compact way, without us having to type out every individual index. 

# Example
list1 = [1, 2, 3, 4, 5, 6]

# We can say this
print(list1)

# Or we can use a for loop

# The loop starts at index 0 and goes to the end of the list,
# changing the value of x is taken care of by the for loop
for x in list1:
    print(x)
    
# Notice how the outputs differ. If we want to print in a line instead of vertical column inside the for loop,
# we have to specify what the print function puts after each x
for x in list1:
    print(x, end = " ")

<a id='List_Slicing'></a>
### Introduction to List Slicing:

**List slicing** is a method we can use to get subsets of elements from a list without using a for loop. Slicing can be applied to lists, strings, dictionaries or any other user defined data structure. This makes list slicing a very versatile tool that we can use. 

# Example
# We want to get the first 5 numbers from this list without using a for loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7]

# How do we do this? Well, we can use the syntax we used above:
print(list2[1:5])

# That print function is actually an example of a list slice
# The colon tells python that we want to preform a list slice
# The 1 is the start index, and is included, the 5 is the end index and is not included

# So we can now say:
print(list1[0:5])

# Another Example
# We can reverse a list quite easily with list slicing, without using a for loop:

# Here, we used the fact that if there is no start and end position given, the slice starts at index 0,
# and goes to the last index by default. This is nice, because we don't need to worry about the length.
# The -1 tells Python to traverse the list backwards

list1 = list1[::-1]

print(list1)


#### Practice:

Make three lists of length five, with names L1, L2, and L3. Compose L1 out of numbers, L2 out of strings, and L3 out of any types you choose, and do the following:

> Print the element at index 1 in L1 <br />
> Print the elements at indices 1 to 3 in L2 <br />
> Multiply L2 by 4 <br />
> Reverse L1 using list slicing <br />
> Create a new List, L4, by appending L2 and L3 <br />
> Check if 4 is in L2 <br />
> Check if "Hello" is in L2 <br />
> Print L4 on one line <br />
> Print L4 on seperate lines <br />


# Code Goes Here

<a id='List_Functions'></a>

### List Functions:

Python lists have a wide variety of useful methods and functions: 

# Length Function: This function returns the length of a list
list1 = [1, 2, 4, 11, 3, 6, 13, 5, 0, -1]
list2 = [1, 4, 4]
list3 =  ["Hi", "Hey", "Howdy"]

print(len(list1))

# Max Function: This function returns the maximum value in a list
print(max(list1))

# Min Function: This function returns the minumum value in a list
print(min(list1))

# Sorted Function: This function sorts the list in ascending order (or alphebetical order)
print(sorted(list1))

<a id='List_Methods'></a>
### List Methods:

# Append Method: This is the method we use to add items to a list, and since it is a method, we use the . operator
list2.append(7)
print(list2)

# Count Method: This method will return the number of times an item shows up in a list
print(list2.count(4))

# Extend Method: This method acts like the + operator, it appends the contents of one list to the other,
# then returns nothing
list2.extend(list3)
print(list2)

# Index Method: This method returns the first occurence of the specified element
print(list2.index(4))

# Insert Method: This method will insert an object at the specified index
list2.insert(0,5)
print(list2)

# Remove Method: This method will remove a specified object from a list
list2.remove(4)
print(list2)

# Reverse Method: Reverses the elements in a given list
list1.reverse()
print(list1)

# Sort Method: This method will sort the elements in a given list
list1.sort()
print(list1)

### Practice:

Create three lists, each as long as you wish, with names L5, L6, L7. Compose L5 out of numbers, L6 out of strings, and L7 out of any types you choose, and do the following:

> Find the lengths of all three and print the lengths <br />
> Find the largest and smallest number in L5 and print them <br />
> Alphabetize L6, and print the result <br />
> Sort L5 from largest to smallest and print the result <br />


# Code Goes Here

<a id='String_Splitting'></a>
## String Splitting:

Suppose we want to create a list from a string. We can use a string method called split. Split takes a string, and returns a list of all the words in a string.

The function is defined by: str.split(sep = " ", maxsplit = -1)

Where: sep is the character you want your words to be separated by. By default, it is a whitespace. Maxsplit is the number of splits to do. By default, the function will split every word in the string apart.

# Example #
string1 = "Hello World"
new_list = string1.split() # Default split function
print(new_list)

# More Complicated Example
string2 = "This is a string example...wow!!!"
print(string2.split())
print(string2.split("i", 1)) # This will find the i in the string, and split once, i will be the seperator
print(string2.split("w")) # This will use w as a seperator, and split the string multiple times
print(string2.split(" ", 2)) # This will split the string twice, and use whitespace as a seperator

# Application
# We can determine how many words a string has by counting the number of whitespaces
# To do this, we use split on a given string, and then use the list function len()

words = string2.split()
print(len(words))

# Another Application
# Suppose we want to sort a list of numbers in ascending order but the input is grabbed from input()
# We cannot apply the sorted method, because sorted requires integers or strings. So we need to convert our
# input to integers. However, we cannot say L = int(input()).split(). However, we can use a for loop!

input_string = "8 3 5 1 9 2" # Pretend input from input()
numbers = [int(x) for x in input_string.split()] # This is a compact way of writing a for loop when doing operations on a list
print(sorted(numbers))

### Extra Resources:

[Introduction to lists with methods and functions](https://www.w3schools.com/python/python_lists.asp)<br />
[A more in-depth look at lists with applications](https://www.geeksforgeeks.org/python-list/)

<a id='Dictionaries'></a>
## Dictionaries

We now turn to **dictionaries**. A Python **dictionary**, like a list, is a very powerful tool in Python, which we can apply in many situations and algorithms.

Dictionaries are composed of **indices**, which are called **keys**, and a collection of values, where each valued is associated with one key. We call this relationship a **Key-Value Pair**. A couple of things to note:

> 1. Keys must be an unchanging data type such as strings or numbers (later, we will see that Tuples also work)
> 2. The values can be of any type
> 3. Keys must be unique in a dictionary, however, values do not need to be unique
> 4. When naming dictionaries, do not use "dict", that is reserved for the function dict()

# Examples of Dictionaries
# A dictionary is declared using the following syntax
# Each Key-Value Pair is seperated by a comma
d1 = {"Name": "Zara", "Age": 7, "Class": "First"}
d2 = {"one": "uno", "two": "dos", "three": "tres"}
d3 = {} # Empty Dictionary

# Accessing Values
# We can use square brackets to access elements like lists
# The difference is that we need to specify a key to access a value

print(d1["Name"]) # Prints the value associated with Name
print(d1["Age"]) # Prints the value associated with Age

# Updating Dictionaries
# To update individual values for a key-value pair, we do the following:

d1["Age"] = 8 # This updates the value for the key "Age"
print(d1)

# Adding a new entry

d1["School"] = "St. Peter's" # This will append a key-value pair to the current dictionary
print(d1)

# Changing Key Names
# To change a key name, we have to do two things:
# 1. Swap the newkey for the old key: dictionary[oldkey] = dictionary[newkey]
# 2. Delete the old key: del dictionary[oldkey]

d1["Category"] = d1["Class"] # updates "Class" to "Category"
del d1["Class"]
print(d1)

# Deleting individual elements
# We can remove individual key-value pairs from dictionaries
# Suppose we wish to delete the pair with key Name:

del d1["Name"] # This deletes the key-value pair Name: Zara
print(d1)

# Removing all Key-Value Pairs
# To remove all Key-Value pairs without deleting the dictionary itself we use the dictionary method clear():

d1.clear()
print(d1)

# Deleting an entire dictionary

del d1 # Removes the dictionary from memory

### Practice

Make a dictionary D1 with four key-value pairs, then output the following:

> Find the values at the first and second key-value pairs and print them <br />
> Update the value at the first key-value pair <br />
> Add two new key-value pairs and print D1 <br />
> Delete the last key-value pair <br />
> Clear D1 and print <br />

# Code Goes Here

<a id='Dictionary_Functions'></a>
### Dictionary Functions:

Like lists, dictionaries have a variety of functions that we can use:

# Finding the length of a dictonary

dict1 = {"Name": "Zara", "Age": 7, "Class": "First"}
print(len(dict1))

# Printing a string representation of a dictionary

print(str(dict1))

# This function determines the type of object you give it, works with dictionaries

print(type(dict1))

<a id='Dictionary_Methods'></a>
### Dictionary Methods:

Dictionaries also have many methods that we can use:

# Clear Method: Removes all elements in a dictionary, returns None

dict1.clear()
print(dict1)

# From Keys Method: This method will create a new dictionary from a list of keys, and a set of values

list1 = ["Age", "Height", "Weight"]
dict2 = dict.fromkeys(list1, 10)
print(dict2)

# Items Method: Method will return a list of the key-value pairs in a dictionary

dict1 = {"Name": "Zara", "Age": 7, "Class": "First"}
key_value_list = dict1.items()
print(key_value_list)

# Keys Method: Produces a list of a given dictionaries keys

key_list = dict1.keys()
print(key_list)

# Values Method: Produces a list of the values in a given dictionary

value_list = dict1.values()
print(value_list)

# Set Default Method: This will create a default value for a given key

dict1.setdefault("Age", 2) # already in dict1
dict1.setdefault("Gender", None) # new to dict1

print(dict1)

# Update Method: This takes the key-value pairs from one dictionary and adds them to another

dict2 = {"Gender": "female"}
dict1.update(dict2)
print(dict1)

# Dict and Zip Functions
# Suppose we want to accept a dictionary as user input, one way we can do this is to have the user enter values
# for two lists. One list is a keys list, the other is a values list.

keys = ["a", "b", "c"]
values = [1, 2, 3]

# We can then apply the function zip, which takes two lists and creates key-value pairs out of them
# and pass the result to the dict function, which turns these pairs into dictionary pairs

new_dict = dict(zip(keys,values))
print(new_dict)

### Practice:

Create a new dictionary D2, composed of five key-value pairs, and output the following: 

> Print D2 <br />
> Print all values in D2 <br />
> Print all keys in D2 <br />
> Add a key-value pair using any method you wish, and print D2 <br />


# Code Goes Here

### Extra Resources:

[Tutorial on Dictionaries](https://www.tutorialspoint.com/python/python_dictionary.htm) <br />
[Introduction to Dictionaries with applications](https://www.geeksforgeeks.org/python-dictionary/) <br />


<a id='Python_Tuples'></a>
## Introduction to Python Tuples:

A **Tuple** is another data type in Python. Tuples are similar to lists, as they can hold a sequence of values. However Tuples differ from lists in the following ways: 

> 1. Tuples are defined using round brackets (), and not square brackets. <br />
> 2. Elements inside a tuple cannot be changed <br />
> 3. Elements inside a tuple cannot be removed <br />
> 4. Tuples can be used as elements inside a dictionary <br />

Operations such as concatenation and slicing can still be performed.

# Basic Tuple Syntax and Operations
# Declare an empty tuple

tuple1 = ()

# Initialize a tuple

tuple2 = (1,2,3,4,5,6)

# Tuple with one element, requires a comma

tuple3 = (1,)

# Printing tuples

print(tuple2)

# Concatanating tuples

tuple4 = tuple3 + tuple2
print(tuple4)

# Getting elements from a tuple

print(tuple4[4])

<a id='Tuple_Methods'></a>
### Tuple Methods:

Because Python tuples cannot be changed once declared, there are only two methods it can call.

# Count Method: Returns the number of occurences of a given element

print(tuple4.count(1))

# Index Method: Finds the first occurence of a given element, and returns its position

print(tuple4.index(3))

<a id='Dictionaries_with_Tuples'></a>
### Dictionaries with Tuples:

As we have seen above, tuples cannot be changed. Therefore, we can use tuples as keys in a dictionary. 

# Example of a dictionary with tuples #

dict_with_tuples = {('a', 'b'): 1, (1, 2, 3, 4): 2, ("Hello", 6, 7, 8): 3}

key_list = dict_with_tuples.keys()
print(key_list)

value_list = dict_with_tuples.values()
print(value_list)

<a id='Tuple_Unpacking'></a>
### Tuple Unpacking:

**Tuple Unpacking** is a way of assigning individual elements inside a tuple to their own unique variables. We will illustrate with an example:

# Tuple unpacking
person = ("James", 23, 1995)

# We can take all three elements, and assign them to unique variables like this:

(name, age, birth_year) = person

print(name, '\n')
print(age, '\n')
print(birth_year, '\n')

### Practice: 

> 1. Create two tuples of length four called T1 and T2, with whatever types you want, and combine them to create a third tuple T3. <br />
> 2. Print all three tuples <br />
> 3. Create a dictionary with the tuples you created. Then create a key list and a value list. <br />
> 4. Unpack tuples T1 and T2 using the method we saw above, and print the results. <br />

# Code Goes Here

### Extra Resources:

[Basic Introduction with some neat applications](http://openbookproject.net/thinkcs/python/english3e/tuples.html) <br />
[Another introduction with tuple functions](https://www.geeksforgeeks.org/tuples-in-python/)

## Conclusion

To end this notebook, we will recap what we have seen:

> 1. Basic list operations, methods and functions
> 2. Basic dictionary operations, methods and functions
> 3. A brief introduction to tuples

Now that we have these tools at our disposal, we are now able to create more powerful and robust programs. Our expectation is that you are comfortable with the basics of lists, dictionaries, and to some extent, tuples.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)