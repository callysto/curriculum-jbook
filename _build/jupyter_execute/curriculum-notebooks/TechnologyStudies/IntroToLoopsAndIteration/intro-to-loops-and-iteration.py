![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)
 
<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/IntroToLoopsAndIteration/intro-to-loops-and-iteration.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"></a>

# Python - Loops and Iteration

In this notebook, we will be introducing loops and iteration. They are commonly used tools in programming as they allow us to perform repetitive tasks.

To run a code cell, select the cell you wish to run, then either:
1. Click the `▶Run` button at the top of the page, or
2. Hit shift+enter.

#### Table of Contents:
[While loops](#While_Loops) <br />
[For Loops](#For_Loops) <br />
[Range Function](#Range_Function) <br />
[Range function applied to sequences](#Range_Function_on_sequence) <br />
[Break Statements](#Break_Statements) <br />
[Incrementing and Decrementing](#Increment_Decrement) <br />
[Infinite Loops](#Infinite_Loops) <br />
[Loops With If/Else statements](#Loops_with_conditions) <br />
[Nested Loops](#Nested_Loops) <br />
[Conclusion](#Conclusion) <br />

<a id='While_Loops'></a>
### While Loops:

While loops are extremely useful in programming. The idea of while loops is to execute a block of code while a boolean expression is `True`. In general, the syntax for a while loop is:

```
while something_True:
    Do some work
```

Here is an example of a basic `while` loop. This loop will print `n` as long as `n` is greater than 0. The computer will check the `n > 0` condition after it decrements `n`. If that condition still holds, then we will continue to print and decrement. If `n = 0` then the condition is no longer `True`, so the computer will not enter the `while` loop.

n = 10
while (n > 0):
    print(n)
    n = n - 1

Another example. Since `n < 0` to start, the `while` condition is not satisfied.

n = -10
while (n > 0):
    print(n)
    n = n - 1
    
print("n is less than", 0)

<a id='For_Loops'></a>
### For Loops:

`for` loops differ from `while` loops in that `for` loops will iterate a fixed number of times, whereas a `while` loop will continue until the condition is no longer satisfied. We generally use `for` loops to iterate over sequences such as lists and strings. The two keywords used in for loops are `for` and `in`.

In general, the syntax for a for loop is:

```
for Some_Variable_of_Interest in Sequence:
    Do some work
```

Note that the sequence can be a string, list, or a dictionary.

Here is an example of iterating over a string. The sequence part of this `for` loop contains a string, The computer will take the string and assign the first value in that string to the variable `letter`. Then the statement inside the `for` loop is executed. Each element in the string will then be assigned to the variable `letter` until there are no more letters left in the string.

for letter in "Dog":
    print("Current Letter:", letter)

Another example of iterating over a string. The same idea as above, but now the elements assigned to the variable are from a list.

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("Current fruit:", fruit)

<a id='Range_Function'></a>
#### The Range Function:

The `range` function is a function which generates a list of numbers, starting from `0`, and going to the number `n - 1` by default. Its function definition is given by:

`range(start, stop, step)`

`start` specifies the first number, `stop` specifies the last number, and `step` is the number by which we increment. `start` is included in the list, but `stop` is not. Each parameter has to be an integer.

for i in range(5):
    print(i)

for i in range(3, 6):
    print(i)

for i in range(4, 10, 2):
    print(i)

for i in range(0, -10, -2):
    print(i)

<a id='Range_Function_on_sequence'></a>
#### Iterating over list indices and dictionary keys:

We can apply the `range` function to iterate over the index of a list. This can be useful if we want to iterate over the list in some order that is not the default. For dictionaries, a `for` loop will loop over the keys of the dictionary.

An example of iterating through a list using `range`. What happens here is the same as what happens above when we interated through a string.

fruits = ["banana", "apple", "mango"]
for index in range(len(fruits)):
    print("Current fruit:", fruits[index])

An example of iteration on a dictionary.

d = {"x": 1, "y": 2, "z": 3}
for key in d:
    print(key, "corresponds to", d[key])

#### Application: Randomly Generated List

Suppose we wish to generate a list of numbers of size `n`.

We can use a `for` loop, the `range` function, and the `randint` function from the [random](https://docs.python.org/3/library/random.html) library to do this.

The `randint` function will generate a random integer from a specified interval.

The syntax is `randint(a,b)`. The values `a` and `b` are the endpoints, and are included as possible values.

Change the value of the `size_of_list` variable to see what happens.

size_of_list = 7

import random as rand
random_list = []

for i in range(0, size_of_list):
    # Append a random value to the list using the randint function 
    random_list.append(rand.randint(1,1000))
print(random_list)

<a id='Break_Statement'></a>
### The Break Statement:

Suppose that we wish to end a loop early if a certain condition is met. We can use what is known as a `break` statement. The `break` statement will terminate `while` and `for` loops early. Usually it is used in conjunction with `if` and `else` statements.

For example, This loop will add `1` to the variable `n`. If `n` is greater than `10` then the `if` statements will be `True`, and the `while` loop will be exited. After that the next line of code will be executed.

n = 0
while True:
    n = n + 1
    if n > 10:
        break
    print(n)
    
print("Done!")

Another example, this time iterating through the letters in a string, and breaking out if the letter is equal to `h`. Notice the `==` to check for equality.

for letter in "Python":
    if letter == "h":
        break
    print("Current Letter:", letter)

print("Done!")

### Practice:

Code the following:

1. Using a loop of your choice, output the squares of the numbers 1 to 10.
2. Find the value of $2^{16}$ using a `for` loop.
3. Using a `for` loop, print the reciprocals of the numbers from 1 to 20.

# Code goes here


<a id='Increment_Decrement'></a>
### Incrementing and Decrementing:

We can increment or decrement variables in loops using two different notations. We used one in a previous example, where we set a variable equal to itself plus `1` to increment by one each time through the loop. We can decrement in a similar way.

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

To increment or decrement we can also use the short form `n += 1` or `n -= 1`.

n = 0
while n < 10:
    n += 2 # equivalent to  n = n + 2
    print(n)

print("Done!")

n = 10
while n > 0:
    print(n)
    n -= 1

### Off by one error:

An *off by one* error occurs when a `while` loop or `for` loop executes one too many or one too few times. A common cause is using `<` or `>` when `<=` or `>=` should have been used.

Note the difference between the outputs of the following loops.

list_of_words = ['zero', 'one', 'two', 'three', 'four', 'five']
print('Loop 1:')
i = 0
while i < 5:
    print(list_of_words[i])
    i += 1
print('')
print('Loop 2:')
j = 0
while j <= 5:
    print(list_of_words[j])
    j += 1

<a id='Infinite_Loops'></a>
### Infinite Loops:

Infinite loops occur when the condition required to enter a loop never becomes `False`. This can cause undesirable behaviour or cause the computer to crash. We highly recommend avoiding these. The main culprit for these is forgetting to update a variable, or by having a loop condition that will never be `False`.

Just to illustrate the following code would continue to increment `x` and then eventually crash the kernel. The error here is that the `while` condition is always satisfied, we would need to change the condition to get the `while` loop working.

```
x = 6
while x > 5:
    print(x)
    x += 1
 ```

Sometimes infinite loops are desirable. For example computers waiting for a user input will be in an infinite loop checking for some sort of activity. This loop will continue until there is input or the device is turned off.

<a id='Loops_with_conditions'></a>
### Loops with if/else statements:

As we saw when we were using the `break` statement, we can have conditional expressions inside loops.

The following code use the `%` operator, which give the remainder after division.

For example, `9 % 4` returns `1` since `9 ÷ 4 = 2` with a remainder of `1`.

for n in range(10, 16):
    if n % 2 == 0:
        print(n, "is even.")
    else:
        print(n, "is odd.")

<a id='Nested_Loops'></a>
### Nested Loops:

It is often useful to create what are known as **nested** loops. Nested loops are simply loops contained in a main loop. Usually, we would have code that looks like:

```
while something_True:
    Do some work
        while something_else_True:
            Do some other work
```

The following code iterates over `n` from `3` to `8` (not including `8`) with a `for` loop. Each time through the `for` loop it uses a `while` loop to iterate over numbers from `1` to `n`.

for n in range(3, 8):
    print('Counting up to', n)
    i = 0
    while i < n:
        i += 1
        if i%2 == 0:
            print(i, 'is even')
        else:
            print(i, 'is odd')

### Extra Resources:

[Some basic examples](https://www.pythonforbeginners.com/loops/for-while-and-nested-loops-in-python)

[More examples of material covered in this notebook](https://www.learnpython.org/en/Loops)

[Introduction to Python loops with examples](https://www.geeksforgeeks.org/loops-in-python/)

[Different looping techniques with examples](https://www.geeksforgeeks.org/looping-techniques-python/)

[More examples of looping with control statements](https://www.geeksforgeeks.org/loops-and-loop-control-statements-continue-break-and-pass-in-python/)

<a id='Conclusion'></a>
## Conclusion:

This notebook introduced
1. `while` and `for` loops
2. The `range` function and `break` statements
3. Infinite Loops
4. Nested conditional statements and nested loops

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)