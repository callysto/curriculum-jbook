![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/MultiplesAndFactors/multiples-and-factors.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Multiples and Factors

## Multiples

Multiples are what you get when you multiply a number by integers.

For example, the first five multiples of 3 are 3, 6, 9, 12, and 15.

Let's write some Python code to find multiples of a number. `Run` the next cell to see what happens. `Run` the next cell to see what happens.

number = 3
howManyMultiples = 5
for n in range(1, howManyMultiples + 1): # we need the +1 because range doesn't include the last integer
    print(number * n)

That code printed the first five multiples of three, let's add a statement about that.

number = 3
howManyMultiples = 5

print('The first',howManyMultiples,'of',number,'are:')
for n in range(1, howManyMultiples+1):
    print(number * n)

### Multiples Practice Problem
If every 9th caller to a radio station wins a prize, how many of the first 30 callers will win a prize?

### Lowest Common Multiple

We can also write some code to find the **lowest common multiple** of two numbers.  Feel free to change the values of the variables `number1` and `number2`.

number1 = 7
number2 = 9

# figure out which of the two numbers is larger and store it in the variable lcm
if number2 > number1:
    lcm = number2
else:
    lcm = number1

while(True): # start an infinite loop
    if lcm % number1 == 0 and lcm % number2 == 0: # if the remainder of dividing lcm by number1 and number2 is 0
        print('The lowest common multiple of', number1, 'and', number2, 'is', lcm)
        break # stop the loop
    else:
        lcm += 1 # add one to the lcm and try again

### LCM Practice Problem 1
If hamburger buns are sold in packages (multiples) of 12 and hamburger patties are sold in packages of 8, how many hamburgers would you need to make in order to not have any buns or patties left over?

### LCM Practice Problem 2
Starting at the beginning of a month, if I go to the grocery store every seven days and my sister goes every four days, on which day of the month will we both go to the grocery store on the same day?

## Factors

**Factors** of a number can be multiplied to form that number.

For example, the factors of 6 are 1, 2, 3, and 6 ($1 \times 6 = 6$ and $ 2 \times 3 = 6$).

A number is **prime** if it has just two factors (1 and itself). A number with more than two factors is a **composite** number.

Let's write some code to find the factors of the number 6.

To design our algorithm, we'll divide 6 by each number from 1 to 6, **if** the remainder is 0 **then** 6 is divisible by that number.

number = 6
factors = []                              # create an empty list where we will store the factors
for factor in range(1, number):           # start a loop at 1 and go until we reach the number we stored at the beginning
    if number % factor == 0:              # if the remainder of that division is 0 then...
        factors.append(factor)            # append the factor we just found to our list of factors
factors.append(number)                    # we know that a number is always divisible by itself, so append that
print('The factors of ',number,'are',factors) # print the list of factors

If we want to see each factor as it is found, which might be useful for numbers with a lot of factors, we can add a print statement inside the loop.

number = 1000
factors = []
for factor in range(1, number):
    if number % factor == 0:
        print(factor)
        factors.append(factor)
factors.append(number)
print('The factors of ',number,'are',factors)

Of course we wanted to find factors of really large numbers then we could use some shortcuts to make it easier, but this should be good enough for now. If you find your program is running too long (It says `In[*]:` but doesn't seem to be doing anything), you can cancel it by clicking the stop button (■) or holding the ctrl key and pressing c.

Let's add a little more code to check if the number is prime or composite (remember that a prime number only has two factors).

number = 1000
factors = []
for factor in range(1, number):
    if number % factor == 0:
        #print(factor)
        factors.append(factor)
factors.append(number)
print('The factors of ',number,'are',factors)

if len(factors) == 2: # if there are only two factors in the list
    print(number, 'is a prime number because it has only two factors.')
else:
    print(number, 'is a composite number with', len(factors), 'factors.')

### Factors Practice Problem 1
Which two single-digit numbers have four factors?

### Factors Practice Problem 2
What is the smallest number that has more than four factors?

### Factors Practice Problem 3
Is 93 a prime or composite number?

### Greatest Common Factor

Also known as "greatest common divisor", this is the largest factor that two numbers have in common. For example, the factors of 6 are (1, 2, 3, 6) and the factors of 9 are (1, 3, 9) so the greatest common factor of 6 and 9 is 3.

There is a module in the [Python math library](https://docs.python.org/3/library/math.html) called `gcd` that can calculate the greatest common factor of two numbers.

from math import gcd
number1 = 6
number2 = 9
greatest_common_factor = gcd(number1, number2)
print('The greatest common factor of', number1, 'and', number2, 'is', greatest_common_factor)

### GCF Practice Problem

You are making treat bags for a birthday party, and need to be sure everyone gets the same number of treats. If you have 28 hard candies and 21 chocolates, how many candy bags can you make up?

## Summary

In this notebook you learned that multiples are what you get when you multiply a number by integers, and factors of a number can be multiplied to form that number. You also learned about greatest common factors and lowest common multiples.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)