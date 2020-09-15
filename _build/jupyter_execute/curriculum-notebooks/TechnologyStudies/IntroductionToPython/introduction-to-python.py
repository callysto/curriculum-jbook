![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/IntroductionToPython/introduction-to-python.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Python - introduction

Programming is a process that instructs the computer to perform a task. Let's think you have a task to write 1 to 1000. It will take a lot of time if you want to write this using pen and paper. But you can easily do it by writing a few lines of a program. Programming will make your life simple in complex work. There are so many programming languages have been demonstrated so far. Python is one of them, which is widely used and the most popular one. In fact, Python becomes the No. 1 programming language in 2017 based on [IEEE Spectrum](https://spectrum.ieee.org/computing/software/the-2017-top-programming-languages), and is used to build many popular websites like Youtube and Instagram. In this notebook, we will learn this python language to solve simple real-life sequential algorithm-based problems using the input-process-output (IPO) approach. The sequential algorithm performs it's each part of task sequentially, which is easy to implement in Python programming language. Each part of IPO approach will help us to learn the introductory Python programming knowledge. Thus, this notebook will give the user introductory level Python programming knowledge.

from IPython.display import HTML
import io
import base64

hide_me = ''
HTML('''<script>
code_show=true; 
function code_toggle() {
  if (code_show) {
    $('div.input').each(function(id) {
      el = $(this).find('.cm-variable:first');
      if (id == 0 || el.text() == 'hide_me') {
        $(this).hide();
      }
    });
    $('div.output_prompt').css('opacity', 0);
  } else {
    $('div.input').each(function(id) {
      $(this).show();
    });
    $('div.output_prompt').css('opacity', 1);
  }
  code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input style="opacity:0" type="submit" value="Click here to toggle on/off the raw code."></form>''')

## Basic: Python Programming

A tradition in computer science for your first program is to write a program which outputs a simple phrase: `Hello World!`. To complete this tradition, input the following into the cell below:

```python
print("Hello World!")
 ```



You can run the above cell with either pressing `Ctrl + Enter` or by selecting the cell and clicking `Run` at the top”, which will give the output: `Hello World!`. Here we have used the `print` statement, which can output a sentence enclosed within quotations to the screen.

### Variables and Input Reading

#### Variables

Let's think, you have a pen and a pencil. Now, you want to find the total of these two items. You can do this thing like `print(1 + 1)`. This line of the program will execute $2$. Let's see this by running the following section: 

print(1+1)

Instead of using `print(1 + 1)`, you can give them a proper name such as `pen` and `pencil`. These `pen` and `pencil` are known as **variables**. This is Python’s way of “remembering” a value. Variables can be numbers like integers or decimals  (for a computer, decimals are known as “floating point numbers”), or even words and characters, which are known as “strings”. Let's write a program to find the total amount of your pen and pencil using variable concept.

pen =1

pencil = 1

total = pen + pencil

print(total)

#### Reading Input from the Keyboard

Almost in all programs, we need to read some values from the user as the **input**, and store them in some variables, so that we can use them later. The input function always returns '*string*' which is a sequence of characters or words. Let's see the following example of taking an input variable as string type:

```python
variable = input("Prompt message")

color = input("Your favourite color:" )
```
From the above expression, `color` input variable can be any string such as `Red`.

Let's try the above input function in the cell below, you can run it with either pressing `Ctrl + Enter` or by selecting the cell and clicking `Run` at the top”.

#NBVAL_SKIP

color = input("your favourite color: ")

wish = input("Wish message of your friend's birthday: ")

In the below cell, you can create your own input function based on the above example.



We can also take any '*numerical*' input from the **input** function. But we have to initialize it before the input function. There are various types of numerical input. Here we will familiar with `integer` and `float` numbers. Integer is a whole number, and it can be positive, negative and zero. But integer can not be the fractional number. Float defines the number which has decimal point. We can take an integer and float input number by writing '`int`' and '`float`' just before the `input` function respectively. Float number will also work in case of the whole number, but integer number will not take float number. Let's see a couple of example of taking input using integer and float:

```python
price = int(input("Price of your pen: "))
```

From the above expression, `price` input variable can be any whole number such as $4$. But it can not be any decimal point number such as $4.5$.

```python
price = float(input("Price of your pen: "))
```
From the above expression. `price` variable will be decimal point number such as $4.5$. But, it will also work in case of whole number such as $4$.

We have to decide the type of numerical input type based on our goal. Let's run the cell below as we did earlier to check the above examples:

#NBVAL_SKIP

price = int(input("Price of your pen: "))

price = float(input("Price of your pen: "))

## Creating Your First Algorithm
An algorithm is a set of operations or steps to be performed to solve a problem or a task. Everything can be written as an algorithm, for example, let's write a simple algorithm of our daily morning life:

1. Wake up from sleep
2. Brush your teeth
3. Take a shower
4. Take the breakfast
5. Get into the car or bus for school

Let's write another simple algorithm to call to your friend:

1. Take your mobile phone
2. Go to your contact list
3. Search your friend's name
4. Call your friend

These two algorithms are the simple examples that we follow in our real life. In computing, programmers write the set of instructions of an algorithm that instructs computer to perform that task.

A sequential algorithm performs the set of operations sequentially from start to finish. Sequential algorithm is easy to understand and implement. We will familiar with the basic level of python programming from this notebook using this sequential algorithm.

The input/process/output (IPO) approach is widely used to solve a computing problem. We will also use this approach to solve the sequential algorithm computing problem using the python programming. This IPO approach will also help us to learn the introductory Python knowledge. Let's see the following points and it will give you the clear idea:

* Input part will teach us how to take input for a problem.
* Process part will teach us to perform any arithmetic operations.
* Output part will help to display the output on the computer screen. 

Let's try to understand each part of a IPO approach.

1. **Input** is pre-existing data of the algorithm, which has been provided by an external system. In this notebook, pre-existing data will be variable and external system will be you or reader. 

2. **Process** is the most important in this IPO approach. In another way, we can say that it is the heart of the algorithm. It takes the input and performs some logical operations based on the goal of the algorithm to transform it to the next output stage. Here, logical operation will be arithmetic operations based on the output of the algorithm. 

3. **Output** is the result of the algorithm which has been obtained by processing the input.

In a sequential algorithm, operations have been performed sequentially. So, processing occurs only when all input required data are available and output occurs only after appropriate processing has occurred. Let's see the following example that will give you a clear idea of input, process, and output (IPO) approach of a sequential algorithm:

### Example 1

***Write an algorithm or program that will take numbers from you/user, and show the average of these three number.***

### Solution

To solve this algorithm or program, we first have to define the input, process and output. Let's see the following points to define them for this computing problem:

* The goal of this algorithm is to compute the average of three numbers. So, we have to take these three numbers, which will act as **input** of the algorithm. 

* Now, we have to find the process part of the algorithm. To find that we have to think how you will get the average from these three numbers. We have to perform following arithmetic operation to get the output, which will act as **process** part of the algorithm. 

    \begin{equation}
    \text{avg} = \frac{\text{num1} + \text{num2} + \text{num3}}{3}
    \end{equation}

* Finally, we will get the average of these three numbers at the **output** stage from the process part.

From the above explanation we can say that to define the input and process we can ask the following questions:

* *Input*: **What do we need to obtain the output?**

* *Process*: **How will we obtain the output from the input?**

#### Algorithm

Let's see the algorithm and IPO part of this problem by running the following cell: 

# This Part is not related to reader. But reader will run this part by select this cell and press "ctrl + enter" to watch the video

hide_me

video = io.open('avg-flowchart.mp4', 'rb').read()
encoded = base64.b64encode(video)
HTML(data='''<video alt="test" controls>
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
             </video>'''.format(encoded.decode('ascii')))

#NBVAL_SKIP

#
# Compute the average
#

# Read the input value from user : 3 numbers
num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))
num3 = int(input("Enter your number 3: "))

# Compute the avaerage of the numbers : Processing
avg = (num1 + num2 + num3)/3

# Display the result : Output
print("The average of the numbers:", avg)

#### Testing

Testing is an important part of programming. Testing is performed to check whether the program is running expectedly or not. Let's test the above program using the following test cases:

1. Case 1: **Input** = (0, 5, 7) -----> **Output** = 4

2. Case 2: **Input** = (0, -2, 5)-----> **Output** = 1

Input = (1.5,  , ) -----> Error will be shown after taking the first number as input. It will be shown as **`ValueError: invalid literal for int() with base 10: '1.5'`**. It will also indicate the line of the program that we are getting this error by showing an arrow in that line. In that line, we take integer as input and which is a whole number. But we are giving input $1.5$ which is a decimal point float number, not a whole number. That's why this value error is showing. 

#### Revised Program

We can protect ourselves from this **`"ValueError"`** by building in some protection into the input statements. So, we will take the input as a float number. This will allow us to take both whole, decimal point, and negative numbers. Now let's see the revised program of this algorithm below:

#NBVAL_SKIP

#
# Compute the average
#

# Read the input value from user : 3 number
num1 = float(input("Enter your number 1: "))  #Change occurs
num2 = float(input("Enter your number 2: "))  #Change occurs
num3 = float(input("Enter your number 3: "))  #Change occurs

# Compute the avaerage of the numbers : Processing
avg = (num1 + num2 + num3)/3

# Display the result : Output
print("The average of the numbers:", avg)

Let's think another problem as read the three numbers and display these numbers in the output. 

**Is the above problem can be solved using the IPO approach?** 

Let's use the technique that we set earlier to obtain the input and process part. 

*Input*: *What do we need to obtain the output?*  

We need three numbers from user to obtain the output. So, these three numbers will act as input.

*Process*: *How will we obtain the output from the input?* 

Our goal is to display the three numbers that you get from the input. But we do not have to perform any operation from input to get the output. So, this problem does not have any process part. 

The above problem can not be solved using IPO approach as it does not have any process part. But this is a sequential algorithm. So, we have to decide by yourself that it can be solved using the IPO approach or not based on the problem. Let’s take a look at a more practical real-world example of a sequential algorithm that can be solved using the IPO approach.

### Example 2

***Write an algorithm or program that will read seconds and then displays the equivalent hours, minutes remaining seconds.***

### Solution

Let's compute the input and process part using the technique that we used earlier for this problem:

* Input: Number of seconds.

* Process: Arithmetic operations.

* Output: Equivalent hour, minute and remaining seconds.


#### Algorithm

Let's run the below cell to see the input, process and output of this problem: 


# This Part is not related to reader. But reader will run this part by select this cell and press "ctrl + enter" to watch the video

hide_me

video = io.open('time-flowchart.mp4', 'rb').read()
encoded = base64.b64encode(video)
HTML(data='''<video alt="test" controls>
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
             </video>'''.format(encoded.decode('ascii')))

#NBVAL_SKIP

#
# Time conversion : Seconds to equivalent hours, minutes and remaining seconds
#

# Read the seconds from user : Input
second = int(input("Enter the time in seconds: "))

# Compute the hours: Processing
hour = second/3600
second = second - (hour * 3600)

# Compute the minutes and remaining seconds: Processing
minute = second/60
second = second - (minute * 60)

# Display the result of Hours, Minutes and Seconds : Output
print("Equivalent Time:", hour , "hours", minute, "minutes", second, "seconds")

### Testing

Let's test the above program using the following test cases:

1. Case 1: **Input** = (3600) -----> **Output** = 1 hours 0 minutes 0 seconds

2. case 2: **Input** = (3620) -----> **Output** = 1.005555 hours 0 minutes 0 seconds, But the output should be 1 hours 0 minutes 20 seconds

3. Case 3: **Input** = (3690) -----> **Output** = 1.025 hours 7.57912e-15 minutes 0 seconds, But the output should be 1 hours 1 minutes 30 seconds

Case 1 and 2 are not giving the expected outcomes. But no error is showing on the screen. As the goal of the program is to convert the seconds into hours, minutes and seconds. So, hour and minute cannot be decimal point float number. Let's see the following lines of the program:

```python
hour = second/3600
minute = second/60
```

In these two lines, we have not indicated the type of the hour and minute variables. So, the program will take them as a float variable by default from the division. But hour variable will be a whole number, not a decimal point number as remaining second from hour variable will go to calculate the minute. Same thing for the minute variable. So, these two variables (i.e. hour and minute) will be the integer type. We have to indicate it in the above lines of the program.

#### Revised Program

#NBVAL_SKIP

#
# Time conversion : Seconds to equivalent hours, minutes and remaining seconds
#

# Read the seconds from user : Input
second = int(input("Enter the time in seconds: "))

# Compute the hours: Processing
hour = int(second/3600)         # Change occurs
second = second - (hour * 3600)

# Compute the minutes and remaining seconds: Processing
minute = int(second/60)        # Change occur
second = second - (minute * 60)

# Display the result of Hours, Minutes and Seconds : Output
print("Equivalent Time:", hour , "hours", minute, "minutes", second, "seconds")

The above two examples give you the clear idea of solving algorithm using the IPO approach of python programming. Let's try to solve following exercises from the knowledge of above examples. The python programs of the exercises are also given. It will be better if you solve these exercises by hiding the python programs. You can easily hide the program by clicking the first cell of this notebook and press '`ctrl + enter`'. Finally, check the output from the test cases. If you are not getting expected output, you can check the given program by doing the same thing at the first cell that you did earlier. Try to find out program error by comparing the given program.

### Exercise 1
***Write a program that will calculate total cost of a restaurant bill. The program will read initial cost of the bill. Tax rate is $10\%$, and tip is $5\%$ of the initial cost (without tax). The program displays the output as tax, tip and overall cost of the meal.*** 

Test the program by taking the following inputs:
1. Case 1: **Input** = initial cost: 120 ----> **Output** = Tax amount: $12$, Tip amount: $6$, Overall Cost: $138$
2. Case 2: **Input** = initial cost: 150.5 ----> **Output** = Tax amount: $15.05$, Tip amount: $7.525$, Overall Cost: $173.075$

#NBVAL_SKIP

# Hide this part when you are solving the exercise
# Hide Technique: Click the first cell and press 'ctrl + enter' or Select the first cell and press 'Run' at the top

#
# Restaurant bill : Compute the overall cost, tax and tip amount
#

TAX_RATE = .1
TIP_RATE = .05

# Read the seconds from user : Input
initial_cost = float(input("Enter the initial cost: "))

# Compute the tax, tip and total: Processing
tax = initial_cost * TAX_RATE         
tip = initial_cost * TIP_RATE
overall_cost = initial_cost + tax + tip

# Display the result of tax, tip and overall cost : Output
print("Tax amount:", tax , "\nTip amount:", tip, "\nOverall Cost:", overall_cost) # \n will display the output in a new line

### Exercise 2
***Write a program that will take a two digit number and display the sum of its two digits.*** 

Test the program using the following inputs:
1. Case 1: **Input** = number: 10 -----> **Output** = Tens digit: 1, Ones digit: 0, Sum: 1
2. Case 2: **Input** = number: 15 -----> **Output** = Tens digit: 1, Ones digit: 5, Sum: 6

#NBVAL_SKIP

# Hide this part when you are solving the exercise
# Hide Technique: Click the first cell and press 'ctrl + enter' or Select the first cell and press 'Run' at the top

#
# Adding the digits of a two digit number
#

# Read the number from user : Input
num = int(input("Enter the number: "))

# Compute the tens, ones and add them: Processing
tens = int(num/10)         
ones = num - (tens * 10)
add = tens + ones

# Display the result of Hours, Minutes and Seconds : Output
print("Tens digit:", tens , "\nOnes digit:", ones, "\nSum: ", add)

If you have to see the python program to solve the above two exercises then try to solve the below real-world problem and check the result of your program with given test case result. The python program is not given for the below problem.

### Exercise 3

***Let's think you are filling an application form for a part-time job. In the application form, you have to fill the height in feet and inches. But you know your height in centimeters. Let's write a program to convert your height from centimeters to feet and inches.***

**Hint**: 1 foot = 12 inches and 1 inch = 2.54 centimetres

Test the program using the following inputs:
1. Case 1: **Input** = centimetres: 183 -----> **Output** = Feet: 6, Inches: 0.0472
2. Case 2: **Input** = centimetres: 182 -----> **Output** = Feet: 5, Inches: 11.6535

## Conclusion

This is an introductory level of python notebook. First, we introduced some fundamental knowledge of python programming as printing a statement using `print` command, familiar with various forms (i.e. string, integer, float) of variables, and how to a take various forms of variables as input from the user using `input` function. Then we familiarized with the sequential algorithm and the IPO approach to solve the algorithm. Each part of IPO approach was also discussed. Finally, we introduced two simple and real-life examples of the sequential algorithm using the IPO approach and solved them using the introductory knowledge of python programming that we learned earlier in this notebook. In those examples, we showed the technique to select the input and process unit, test cases to check the Python program, error from program, and revised program to overcome the error. We also introduced three exercises for practice purpose. The Python programs were also provided for the first two exercises for learning purposes. Various test cases are provided for each exercise to test the output. This notebook will help the user learning the introductory level python programming skill by solving sequential algorithms using the IPO approach.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)