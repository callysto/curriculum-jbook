![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/CompareAndOrderNumbers/compare-and-order-numbers.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Compare and order numbers

## Instructions before you start
Once the notebook has loaded, click the fast forward button ">>" in the menu bar above. Click "Yes" to restart and run.

%%html

<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

## Index

<a href="#Introduction"> Introduction </a> <br/>
<a href="#Comparing_Numbers"> Comparing Numbers </a> <br />
<a href="#Comparing_Whole_Numbers"> Comparing Whole Numbers</a> <br />
- <a href="#Example1"> Practice Example </a> 

<a href="#Comparing_Positive_Decimal_Numbers"> Comparing Positive Decimal Numbers </a> <br />

- <a href="#Example2"> Practice Example </a>

<a href="#Comparing_Positive_Fractions"> Comparing Positive Fractions </a> <br />

- <a href="#Example3"> Practice Example </a>

<a href="#Comparing_Different_Number_Types"> Comparing Different Numbers Types </a> <br />

- <a href="#Whole_Numbers_to_Fractions"> Comparing Whole Numbers to Fractions </a>

- <a href="#Whole_Numbers_to_Decimals">Comparing Whole Numbers to Decimals </a>

- <a href="#Decimals_to_Fractions"> Comparing Decimals to Fractions </a>

    - <a href="#Convert_Decimal_to_Fraction"> Decimals to Fractions Method </a>

    - <a href="#Convert_Fraction_to_Decimal"> Fractions to Decimals Method </a>

    - <a href="#Hybrid_Method"> Hybrid Method </a>

- <a href="#Example4"> Practice Examples </a>

<a href="#Ordering"> Ordering: Positive Fractions, Positive Decimals and Whole Numbers </a>

- <a href="#Ordering_Mixed"> Ordering Mixed Number Types </a>

<a href="#Ordering_Examples"> Ordering Practice Examples </a> <br />
<a href="#Conclusion"> Conclusion </a>


## Compare and Order: Positive Fractions, Positive Decimals and Whole Numbers

<a name="Introduction"></a>
## Introduction

To compare and order positive fractions, positive decimals and whole numbers we need to first understand how to compare them and then we will be able to order them. We will start with showing how to compare whole numbers, fractions and decimals separately and then we will show how to compare between each of them. To be able to compare between each of them we will need  understand how to convert whole numbers to fractions, fractions to decimals, decimals to fractions and so on. Once we understand how to compare fractions, decimals and whole numbers we will then be able to order a list of them. We will show how to order them from the lowest number to the highest number.

<a name="Comparing_Numbers"></a>
## Comparing Numbers

When comparing two numbers there are 3 possible outcomes. The first number can be less than the second number, the first number can be greater than the second number or the first number can be equal to the second number. The symbols for **greater than**, **less than** and **equal to** are:

<img src="images/Greater_Than.png" alt="GreaterThan" width=300 align=middle>

Relations can be created between two quantities using these symbols, for example:

<center>$\Large 4 > 6 \hspace{3cm} 3 < 7 \hspace{3cm} \frac{22}{2} = 11$</center>

The first two examples involving greater than or less than symbols are examples of **inequalities** while the third, involving the equal sign is called an **equality** or **equation**.  Each of these are a mathematical statement which can be either true or false.  The first example is false while the second and third are true. For an inequality to be true the pointed part of the symbol should be pointing to the smaller quantity and the wider part of the symbol (the opening) should be on the side of the larger quantity.

<a name="Comparing_Whole_Numbers"></a>
## Comparing Whole Numbers

Now that we know about the symbols used in comparing numbers let us consider comparing whole numbers. Comparing single digit numbers is straight forward but when numbers have multiple digits we will need to use the number's place values.

<img src="images/placevalueWN.png" alt="PlaceValue" width=400 align=middle>

When comparing two numbers we will be comparing the digits in these place values. Suppose first that two whole numbers have the same number of digits. The farthest left digit represents the greatest value so the digits in those place values will be compared first. If one digit is greater than the other then we have determined which number is greater than the other. If the two digits are equal then we need to move right to the next place value and compare the digits in it. If these two digits differ then the larger digit determines the greater number.  If these two digits are equal we will need to keep moving to the next place value and continue the process of digit comparison. If we continue all the way to the last place value and those digits are equal then the two numbers are equal otherwise one number will be greater than the other. An example below demonstrates this process.

> The two numbers being compared are:
>
> $\Large 1578 \hspace{1cm} \text{ and } \hspace{1cm} 1523$
>
> Starting with the digit in the left most place value of our first number and comparing it to the digit in the same place value of the second number we have:
>
> $\Large \color{red}{\underline{1}}578 \hspace{1cm} \text{ and } \hspace{1cm} \color{red}{\underline{1}}523$
> 
> $\Large \hspace{2.3cm}1 = 1$
>
> The two digits in the thousand place value are equal so we need to move right to the next place value and compare those digits.
>
> $\Large 1\color{red}{\underline{5}}78 \hspace{1cm} \text{ and } \hspace{1cm} 1\color{red}{\underline{5}}23$
>
> $\Large \hspace{2.3cm}5 = 5$
>
> As above the digits are equal again so we need to move on to the next place value and compare the digits.
>
> $\Large 15\color{red}{\underline{7}}8 \hspace{1cm} \text{ and } \hspace{1cm} 15\color{red}{\underline{2}}3$
>
> $\Large \hspace{2.3cm}7 > 2$
>
> Here we have 7 being greater than 2 which means the corresponding number to the 7 digit is greater than the number corresponding to the 2 digit.  We can express our result with the true inequality
>
> $\Large \hspace{1.2cm}1578 > 1523$
>
> If we wish to express this result instead using the less than symbol we have the inequality
>
> $\Large \hspace{1.2cm}1523 < 1578$

Next consider an example of comparing two whole numbers that do not have the same number of digits. For example we could have:

> $\Large 534 \hspace{1cm} \text{ and } \hspace{1cm} 98$
>
> $\Large \color{red}{\underline{5}}34 \hspace{1cm} \text{ and } \hspace{0.65cm} \color{red}{\underline{\hspace{0.35cm}}}98$
>
> All we have to do is to add zeros in front of the number with fewer digits. Adding zero in front of a number does nothing to its value since we are not adding anything to it.
>
> $\Large \color{red}{\underline{5}}34 \hspace{1cm} \text{ and } \hspace{0.65cm} \color{red}{\underline{0}}98$
>
> Now that we have the same number of digits in each number we can compare the numbers using the process described above without an issue.
>
> $\Large \hspace{1.9cm}5 > 0$
>
> Since 5 is greater than 0 we have:
>
> $\Large \hspace{1.1cm}534 > 98$

Following the processes outlined above the reader will be able to compare two positive whole numbers and determine if one is greater than the other or if they are equal.

<a name="Example1"></a>
### Practice Examples

Here are some practice examples for the reader to become familiar with the processes described above. The first example will give two numbers with a **greater than**, **less than** or **equal sign** between them and you need to choose whether the **inequality** or **equality** is true or false. For example the inequality 4 < 6 is true but the inequality 6 < 4 is false since 6 is not less than 4. To generate a new example you only need to click on the **New Example** button. 

The second example will give two numbers with a space in between them. You will need to choose the correct symbol to go in between the two numbers. There are a **greater than** button, **less than** button and **equal sign** button below the numbers that you can click to choose your answer. To generate a new example you only need to click on the **New Example** button. 

#### 1. Whole Number Examples

#### a)

import ipywidgets as widgets
from IPython.display import display, Math, Latex
import traitlets
from IPython.display import Markdown as md
import random

#The two numbers used in the example along with what symbol is used to compare them
first_number = 8
second_number = 15
symbol_number = 0

#List of symbols that can be used in the examples
symbol_list = ['<','>','=']


#The outputs displayed in the widget
example_output = widgets.HTMLMath(
    value='<font size="5">8 < 15</font>',
)

answer_output = widgets.HTML('')

#The buttons used in the widget
true_button = widgets.ToggleButton(
    value=False,
    description='True',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or Inequality is true',
    continuous_update=True
)

false_button = widgets.ToggleButton(
    value=False,
    description='False',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or Inequality is false',
    continuous_update=True
)

new_example_button = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
false_button.layout.width = '100px'
true_button.layout.width = '100px'

new_example_button.layout.margin = '10px 0px 0px 250px'

example_output.layout.margin = '10px 0px 10px 65px'

#The layout and design of the widgets
number_widget = widgets.VBox(children=[new_example_button, example_output])

question_widget = widgets.HBox(children=[false_button, true_button])

display_widget = widgets.VBox(children=[number_widget, question_widget, answer_output])

#Generate a new example for the reader
def update_Example(change):
    global first_number
    global second_number
    global symbol_number
    
    first_number = random.randint(10,999)
    second_number = random.randint(10,999)
    symbol_number = random.randint(0,2)
    example_output.value = '<font size="5">' + str(first_number) + ' ' + symbol_list[symbol_number] + ' ' + str(second_number) + '</font>'
    true_button.value = False
    false_button.value = False

#When the false button is clicked it is checked whether the example is false
def update_false(change):
    new_update = change.new
    
    if(new_update): #if the button is clicked to the true value
        if((symbol_number == 0) and not (first_number < second_number)):
            answer_output.value = 'You are right. The inequality is false.'
        elif ((symbol_number == 1) and not (first_number > second_number)):
            answer_output.value = 'You are right. The inequality is false.'
        elif ((symbol_number == 2) and not (first_number == second_number)):
            answer_output.value = 'You are right. The equality is false.'
        else:
            if(symbol_number == 2):
                answer_output.value = 'The equality is actually true.'
            else:
                answer_output.value = 'The inequality is actually true.'
        true_button.value = False
    elif(not true_button.value): #if the button is clicked to the false value and the true button is false
        answer_output.value = '' 

#When the false button is clicked it is checked whether the example is true
def update_true(change):
    new_update1 = change.new
    if(new_update1): #if the button is clicked to the true value
        if((symbol_number == 0) and (first_number < second_number)):
            answer_output.value = 'You are right. The inequality is true.'
        elif ((symbol_number == 1) and (first_number > second_number)):
            answer_output.value = 'You are right. The inequality is true.'
        elif ((symbol_number == 2) and (first_number == second_number)):
            answer_output.value = 'You are right. The equality is true.'
        else:
            if(symbol_number == 2):
                answer_output.value = 'The equality is actually false.'
            else:
                answer_output.value = 'The inequality is actually false.'
        false_button.value = False
    elif(not false_button.value): #if the button is clicked to the false value and the true button is false
        answer_output.value = '' 
    
#Observe when the buttons true/false value has changed and call the function
false_button.observe(update_false, names='value')

true_button.observe(update_true, names='value')        

#Call the function when the button has been clicked
new_example_button.on_click(update_Example)

#display the example widget
display_widget

#### b)

#The two numbers used in the example
left_number = 8
right_number = 15

#The outputs displayed in the widget
left_number_output = widgets.HTMLMath(
    value='<font size="5">8</font>',
)
right_number_output = widgets.HTMLMath(
    value='<font size="5">15</font>',
)
symbol_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)

example2_answer_output = widgets.HTML('')

#The buttons used in the widget
greater_than_button = widgets.ToggleButton(
    value=False,
    description='Greater Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

less_than_button = widgets.ToggleButton(
    value=False,
    description='Less Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

equal_to_button = widgets.ToggleButton(
    value=False,
    description='Equal To',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

example2_new_example_button = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
greater_than_button.layout.width = '100px'
less_than_button.layout.width = '100px'
equal_to_button.layout.width = '100px'

example2_new_example_button.layout.margin = '10px 0px 0px 250px'

left_number_output.layout.margin = '10px 0px 10px 100px'
symbol_output.layout.margin = '10px 15px 10px 15px'
right_number_output.layout.margin = '10px 0px 10px 0px'

#The layout and design of the widgets
example2_output_widget = widgets.HBox(children=[left_number_output, symbol_output, right_number_output])

example2_number_widget = widgets.VBox(children=[example2_new_example_button, example2_output_widget])

example2_question_widget = widgets.HBox(children=[greater_than_button, less_than_button, equal_to_button])

example2_display_widget = widgets.VBox(children=[example2_number_widget, example2_question_widget, example2_answer_output])

#Generate a new example for the reader
def update_example2_Example(change):
    global left_number
    global right_number
    
    left_number = random.randint(10,999)
    right_number = random.randint(10,999)
    left_number_output.value = '<font size="5">' + str(left_number) + '</font>'
    right_number_output.value = '<font size="5">' + str(right_number) + '</font>'
    symbol_output.value = '<font size="5"></font>'
    greater_than_button.value = False
    less_than_button.value = False
    equal_to_button.value = False

#When the greater than button is clicked it is checked if greater than is the correct answer
def update_greater(change):
    new_update = change.new
    
    if(new_update): #if the button is clicked to the true value
        if(left_number > right_number):
            example2_answer_output.value = 'You are correct. ' + str(left_number) + ' is greater than ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> > </font>'
        else:
            example2_answer_output.value = 'That is not correct. ' + str(left_number) + ' is not greater than ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> > </font>'
        less_than_button.value = False
        equal_to_button.value = False
    elif(not less_than_button.value and not equal_to_button.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output.value = ''

#When the less than button is clicked it is checked if less than is the correct answer
def update_less(change):
    new_update1 = change.new
    if(new_update1): #if the button is clicked to the true value
        if(left_number < right_number):
            example2_answer_output.value = 'You are correct. ' + str(left_number) + ' is less than ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> < </font>'
        else:
            example2_answer_output.value = 'That is not correct. ' + str(left_number) + ' is not less than ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> < </font>'
        greater_than_button.value = False
        equal_to_button.value = False
    elif(not greater_than_button.value and not equal_to_button.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output.value = '' 

#When the equal to button is clicked it is checked if equal to is the correct answer
def update_equal(change):
    new_update2 = change.new
    if(new_update2): #if the button is clicked to the true value
        if(left_number == right_number):
            example2_answer_output.value = 'You are correct. ' + str(left_number) + ' is equal to ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> = </font>'
        else:
            example2_answer_output.value = 'That is not correct. ' + str(left_number) + ' is not equal to ' + str(right_number) + '.'
            symbol_output.value = '<font size="5"> = </font>'
        greater_than_button.value = False
        less_than_button.value = False
    elif(not greater_than_button.value and not less_than_button.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output.value = ''
        
#Observe when the buttons values have changed and call the function
greater_than_button.observe(update_greater, names='value')

less_than_button.observe(update_less, names='value')    

equal_to_button.observe(update_equal, names='value')

#Call the function when the button has been clicked
example2_new_example_button.on_click(update_example2_Example)

#display the example widget
example2_display_widget

<a name="Comparing_Positive_Decimal_Numbers"></a>
## Comparing Positive Decimal Numbers

To compare positive decimal numbers we are going to follow the same process using place values as in the <a href="#Comparing_Whole_Numbers">*Comparing Whole Numbers*</a> section above. 

<img src="images/placevalue.png" alt="PlaceValue" width=500 align=middle>

The first three decimal place values are tenths, hundredths and thousandths. We will only consider decimals to the thousandths place value since that is enough to show the procedure. As in the whole number case we compare the place values of two numbers from left to right to determine whether one number is greater than the other. When moving from the ones place value to the tenths value we follow the same process and compare the digits in the tenths place value of the two numbers and then the hundredth's digits and so on. The following example will give a general idea of this.

> The two numbers being compared are:
>
> $\Large 1.845 \hspace{1cm} \text{ and } \hspace{1cm} 1.839$
>
> Starting with the digit in the left most place value of our first number and comparing it to the digit in the same place value of the second number we have:
>
> $\Large \color{red}{\underline{1}}.845 \hspace{1cm} \text{ and } \hspace{1cm} \color{red}{\underline{1}}.839$
> 
> $\Large \hspace{2.5cm}1 = 1$
>
> The two digits in the ones place value are equal so we need to move right to the next place value and compare those digits.
>
> $\Large 1.\color{red}{\underline{8}}45 \hspace{1cm} \text{ and } \hspace{1cm} 1.\color{red}{\underline{8}}39$
>
> $\Large \hspace{2.5cm}8 = 8$
>
> As above the digits are equal again so we need to move on to the next place value and compare the digits.
>
> $\Large 1.8\color{red}{\underline{4}}5 \hspace{1cm} \text{ and } \hspace{1cm} 1.8\color{red}{\underline{3}}9$
>
> $\Large \hspace{2.5cm}4 > 3$
>
> Here we have 4 being greater than 3 which means the corresponding number to the 4 digit is greater than the number corresponding to the 3 digit.
>
> $\Large \hspace{1.2cm}1.845 > 1.839$

The example above demonstrates the concept of comparing positive decimal numbers but as in the <a href="#Comparing_Whole_Numbers">*Comparing Whole Numbers*</a> section we could have two decimal numbers with a different number of digits. If the number of digits to the left of the decimal place differ then we only need to add zeros to the left of the number with fewer digits as before. If we have a differing number of digits to the right of the decimal place then we need to add zeros to the right of the number with fewer digits. Consider the following example:

> $\Large 5.38 \hspace{1cm} \text{ and } \hspace{1cm} 5.3$
>
> Comparing the digits in the left most place value.
>
> $\Large \color{red}{\underline{5}}.38 \hspace{1cm} \text{ and } \hspace{1cm} \color{red}{\underline{5}}.3$
>
> $\Large \hspace{2.1cm}5 = 5$
>
> The two digits in the ones place value are equal so we need to move right to the next place value and compare those digits.
>
> $\Large 5.\color{red}{\underline{3}}8 \hspace{1cm} \text{ and } \hspace{1cm} 5.\color{red}{\underline{3}}$
>
> $\Large \hspace{2.1cm}3 = 3$
>
> As above the digits are equal again so we need to move on to the next place value and compare the digits. Here we have a problem since one of our numbers does not have a digit in the hundredth place. This is solved by placing a zero into the hundredth place. Adding a zero here to the end of the decimal number does not change the value since zero times one hundredth is just zero.  (Note that we are not shifting the digits to the left! We cannot add a zero to the end of a whole number since it moves up every digit by one place value.) Adding zero to the number and then comparing the digits we get:
>
> $\Large 5.3\color{red}{\underline{8}} \hspace{1cm} \text{ and } \hspace{1cm} 5.3\color{red}{\underline{\hspace{0.35cm}}}$
>
> $\Large 5.3\color{red}{\underline{8}} \hspace{1cm} \text{ and } \hspace{1cm} 5.3\color{red}{\underline{0}}$
>
> $\Large \hspace{2.1cm} 8 > 0$
>
> 8 is clearly greater than 0 so we have
>
> $\Large \hspace{1.2cm}5.38 > 5.3$

Following the processes outlined above the reader will be able to compare two positive decimal numbers and determine if one is greater than the other or if they are equal.

<a name="Example2"></a>
### Practice Examples

Here are some practice examples for you to become familiar with using the processes described above. The examples are similar to those in the <a href="#Example1">*Comparing Whole Numbers*</a> section.

#### 2. Decimal Examples

#### a)

#The two numbers used in the example along with what symbol is used to compare them
first_number2 = 0.345
second_number2 = 0.329
symbol_number2 = 0
random_int = 8

#List of symbols that can be used in the examples
symbol_list2 = ['<','>','=']

#The outputs displayed in the widget
example_output2 = widgets.HTMLMath(
    value='<font size="5">8.345 < 8.329</font>',
)

answer_output2 = widgets.HTML('')

#The buttons used in the widget
true_button2 = widgets.ToggleButton(
    value=False,
    description='True',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is true',
    continuous_update=True
)

false_button2 = widgets.ToggleButton(
    value=False,
    description='False',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is false',
    continuous_update=True
)

new_example_button2 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
false_button2.layout.width = '100px'
true_button2.layout.width = '100px'

new_example_button2.layout.margin = '10px 0px 0px 250px'

example_output2.layout.margin = '10px 0px 10px 35px'

#The layout and design of the widgets
number_widget2 = widgets.VBox(children=[new_example_button2, example_output2])

question_widget2 = widgets.HBox(children=[false_button2, true_button2])

display_widget2 = widgets.VBox(children=[number_widget2, question_widget2, answer_output2])

#Generate a new example for the reader
def update_Example2(change):
    global first_number2
    global second_number2
    global symbol_number2
    
    random_int = random.randint(1,9)
    first_number2 = round(random.random(), 3) + random_int
    first_number2 = round(first_number2, 3)
    second_number2 = round(random.random(), 3) + random_int
    second_number2 = round(second_number2, 3)
    symbol_number2 = random.randint(0,2)
    example_output2.value = '<font size="5">' + str(first_number2) + ' ' + symbol_list2[symbol_number2] + ' ' + str(second_number2) + '</font>'
    true_button2.value = False
    false_button2.value = False
    
#When the false button is clicked it is checked whether the example is false
def update_false2(change):
    new_update2 = change.new
    
    if(new_update2): #if the button is clicked to the true value
        if((symbol_number2 == 0) and not (first_number2 < second_number2)):
            answer_output2.value = 'You are right. The inequality is false.'
        elif ((symbol_number2 == 1) and not (first_number2 > second_number2)):
            answer_output2.value = 'You are right. The inequality is false.'
        elif ((symbol_number2 == 2) and not (first_number2 == second_number2)):
            answer_output2.value = 'You are right. The equality is false.'
        else:
            if (symbol_number2 == 2):
                answer_output2.value = 'The equality is actually true.'
            else:
                answer_output2.value = 'The inequality is actually true.'
        true_button2.value = False
    elif(not true_button2.value): #if the button is clicked to the false value and the true button is false
        answer_output2.value = '' 

#When the false button is clicked it is checked whether the example is true
def update_true2(change):
    new_update3 = change.new
    if(new_update3): #if the button is clicked to the true value
        if((symbol_number2 == 0) and (first_number2 < second_number2)):
            answer_output2.value = 'You are right. The inequality is true.'
        elif ((symbol_number2 == 1) and (first_number2 > second_number2)):
            answer_output2.value = 'You are right. The inequality is true.'
        elif ((symbol_number2 == 2) and (first_number2 == second_number2)):
            answer_output2.value = 'You are right. The equality is true.'
        else:
            if (symbol_number2 == 2):
                answer_output2.value = 'The equality is actually false.'
            else:
                answer_output2.value = 'The inequality is actually false.'
        false_button2.value = False
    elif(not false_button2.value): #if the button is clicked to the false value and the true button is false
        answer_output2.value = '' 
    
#Observe when the buttons true/false value has changed and call the function
false_button2.observe(update_false2, names='value')

true_button2.observe(update_true2, names='value')        

#Call the function when the button has been clicked
new_example_button2.on_click(update_Example2)

#display the example widget
display_widget2

#### b)

#The two numbers used in the example
left_number2 = 8.435
right_number2 = 8.421

#The outputs displayed in the widget
left_number_output2 = widgets.HTMLMath(
    value='<font size="5">8.435</font>',
)
right_number_output2 = widgets.HTMLMath(
    value='<font size="5">8.421</font>',
)
symbol_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)

example2_answer_output2 = widgets.HTML('')

#The buttons used in the widget
greater_than_button2 = widgets.ToggleButton(
    value=False,
    description='Greater Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

less_than_button2 = widgets.ToggleButton(
    value=False,
    description='Less Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

equal_to_button2 = widgets.ToggleButton(
    value=False,
    description='Equal To',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

example2_new_example_button2 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
greater_than_button2.layout.width = '100px'
less_than_button2.layout.width = '100px'
equal_to_button2.layout.width = '100px'

example2_new_example_button2.layout.margin = '10px 0px 0px 250px'

left_number_output2.layout.margin = '10px 0px 10px 80px'
symbol_output2.layout.margin = '10px 15px 10px 15px'
right_number_output2.layout.margin = '10px 0px 10px 0px'

#The layout and design of the widgets
example2_output_widget2 = widgets.HBox(children=[left_number_output2, symbol_output2, right_number_output2])

example2_number_widget2 = widgets.VBox(children=[example2_new_example_button2, example2_output_widget2])

example2_question_widget2 = widgets.HBox(children=[greater_than_button2, less_than_button2, equal_to_button2])

example2_display_widget2 = widgets.VBox(children=[example2_number_widget2, example2_question_widget2, example2_answer_output2])

#Generate a new example for the reader
def update_example2_Example2(change):
    global left_number2
    global right_number2
    
    random_int = random.randint(1,9)
    left_number2 = round(random.random(), 3) + random_int
    left_number2 = round(left_number2, 3)
    right_number2 = round(random.random(), 3) + random_int
    right_number2 = round(right_number2, 3)
    left_number_output2.value = '<font size="5">' + str(left_number2) + '</font>'
    right_number_output2.value = '<font size="5">' + str(right_number2) + '</font>'
    symbol_output2.value = '<font size="5"></font>'
    greater_than_button2.value = False
    less_than_button2.value = False
    equal_to_button2.value = False

#When the greater than button is clicked it is checked if greater than is the correct answer
def update_greater2(change):
    new_update = change.new
    
    if(new_update): #if the button is clicked to the true value
        if(left_number2 > right_number2):
            example2_answer_output2.value = 'You are correct. ' + str(left_number2) + ' is greater than ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> > </font>'
        else:
            example2_answer_output2.value = 'That is not correct. ' + str(left_number2) + ' is not greater than ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> > </font>'
        less_than_button2.value = False
        equal_to_button2.value = False
    elif(not less_than_button2.value and not equal_to_button2.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output2.value = ''

#When the less than button is clicked it is checked if less than is the correct answer
def update_less2(change):
    new_update1 = change.new
    if(new_update1): #if the button is clicked to the true value
        if(left_number2 < right_number2):
            example2_answer_output2.value = 'You are correct. ' + str(left_number2) + ' is less than ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> < </font>'
        else:
            example2_answer_output2.value = 'That is not correct. ' + str(left_number2) + ' is not less than ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> < </font>'
        greater_than_button2.value = False
        equal_to_button2.value = False
    elif(not greater_than_button2.value and not equal_to_button2.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output2.value = '' 

#When the equal to button is clicked it is checked if equal to is the correct answer
def update_equal2(change):
    new_update2 = change.new
    if(new_update2): #if the button is clicked to the true value
        if(left_number2 == right_number2):
            example2_answer_output2.value = 'You are correct. ' + str(left_number2) + ' is equal to ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> = </font>'
        else:
            example2_answer_output2.value = 'That is not correct. ' + str(left_number2) + ' is not equal to ' + str(right_number2) + '.'
            symbol_output2.value = '<font size="5"> = </font>'
        greater_than_button2.value = False
        less_than_button2.value = False
    elif(not greater_than_button2.value and not less_than_button2.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output2.value = ''
        
#Observe when the buttons values have changed and call the function
greater_than_button2.observe(update_greater2, names='value')

less_than_button2.observe(update_less2, names='value')    

equal_to_button2.observe(update_equal2, names='value')

#Call the function when the button has been clicked
example2_new_example_button2.on_click(update_example2_Example2)

#display the example widget
example2_display_widget2

<a name="Comparing_Positive_Fractions"></a>
## Comparing Positive Fractions

Comparing fractions will use the same processes defined in the <a href="#Comparing_Whole_Numbers">*Comparing Whole Numbers*</a> section along with a few more. When comparing fractions we have to consider both the **numerators** and the **denominators** of the fractions. When we add or subtract fractions we need the denominators to be the same and when we compare fractions we also need them to be the same. Once the denominators of the numbers are the same we only need to compare the numerators to determine whether one number is greater than the other or if they are equal.

Typically two fractions will not have the same denominator which means we will need to modify them to ensure they have the same denominator. To modify the fractions to have the same denominator we need to find a **common denominator** between them. The simplist way to find a common denominator is to multiply the two denominators together and use the result as the new denominator for both fractions. We need to remember that when we modify the denominator of a fraction we need to modify the numerator the same way. Consider the two fractions below.

> $\Large \frac{3}{8} \hspace{0.5cm},\hspace{0.5cm} \frac{2}{3}$
>
> To find a common denominator we can multiply the two denominators together
>
> $\large 8 \times 3 = 24$
> 
> The new denominator will be 24. We must remember that when we multiply the denominator of a fraction by a value we must do the same to the numerator to generate an equivalent fraction.  We are really just multiplying the original fraction by one to get equivalent fractions with common denominators.  For our example: 
>
> $\Large \frac{3}{8} \times \frac{3}{3} = \frac{9}{24} \hspace{0.5cm},\hspace{0.5cm} \frac{2}{3} \times \frac{8}{8} = \frac{16}{24}$
>
> Now we can compare the numerators of the two fractions since the denominators are the same. Comparing the numerators as we did with whole numbers we have:
>
> $\large 9 < 16$
>
> Which means:
>
> 
> $\Large \frac{9}{24} < \frac{16}{24} \hspace{3cm} \frac{3}{8} < \frac{2}{3}$

It should be noted that by multiplying the two denominators together to find a common denominator does not always give the lowest common denominator. If you have a calculator handy then it is not that much of a problem but if you do not then it may be useful to find the lowest common denominator between the two denominators and then proceed with modifying the numerators. 

In the fraction examples below there will be both proper and improper fractions. In case the reader has forgotten **proper fractions** are fractions where the numerator is less than the denominator and **improper fractions** are where the numerator is greater than or equal to the denominator.

<a name="Example3"></a>
### Practice Examples

Here are some practice examples for you to become familiar with using the processes described above. The examples are similar to those in the <a href="#Example1">*Comparing Whole Numbers*</a> section.

#### 3. Fraction Examples

#### a)

#The two fractions used in the example along with what symbol is used to compare them
first_number_numerator3 = 5
first_number_denominator3 = 12
second_number_numerator3 = 7
second_number_denominator3 = 10
symbol_number3 = 0

#The modified fractions where they have the same denominator
new_first_numerator = first_number_numerator3*second_number_denominator3
new_second_numerator = second_number_numerator3*first_number_denominator3
new_denominator = first_number_denominator3*second_number_denominator3

#List of symbols that can be used in the examples
symbol_list3 = ['<','>','=']

#The outputs displayed in the widget
example_output3 = widgets.HTMLMath(
    value=r"<font size='6'><sup>5</sup>&frasl;<sub>12</sub>  <  <sup>7</sup>&frasl;<sub>10</sub></font>",
)

answer_output3 = widgets.HTML('')
equality_answer_output = widgets.HTMLMath(
    value=''
)

#The buttons used in the widget
true_button3 = widgets.ToggleButton(
    value=False,
    description='True',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is true',
    continuous_update=True
)

false_button3 = widgets.ToggleButton(
    value=False,
    description='False',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is false',
    continuous_update=True
)

new_example_button3 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
false_button3.layout.width = '100px'
true_button3.layout.width = '100px'

new_example_button3.layout.margin = '10px 0px 0px 250px'

example_output3.layout.margin = '10px 0px 10px 40px'

equality_answer_output.layout.margin = '20px 0px 10px 20px'

#The layout and design of the widgets
number_widget3 = widgets.VBox(children=[new_example_button3, example_output3])

question_widget3 = widgets.HBox(children=[false_button3, true_button3])

display_widget3 = widgets.VBox(children=[number_widget3, question_widget3, answer_output3, equality_answer_output])

#Generate a new example for the reader
def update_Example3(change):
    global first_number_numerator3
    global first_number_denominator3
    global second_number_numerator3
    global second_number_denominator3
    global symbol_number3
    global new_first_numerator
    global new_second_numerator
    global new_denominator
    
    first_number_numerator3 = random.randint(1,20)
    first_number_denominator3 = random.randint(1,20)
    second_number_numerator3 = random.randint(1,20)
    second_number_denominator3 = random.randint(1,20)
    symbol_number3 = random.randint(0,2)
    example_output3.value = r"<font size='6'><sup>" + str(first_number_numerator3) + "</sup>&frasl;<sub>" + str(first_number_denominator3) + "</sub> " +  symbol_list3[symbol_number3] + " <sup>" + str(second_number_numerator3) + "</sup>&frasl;<sub>" + str(second_number_denominator3) + "</sub></font>"
    true_button3.value = False
    false_button3.value = False
    
    new_denominator = first_number_denominator3*second_number_denominator3
    new_first_numerator = first_number_numerator3*second_number_denominator3
    new_second_numerator = second_number_numerator3*first_number_denominator3
    
#When the false button is clicked it is checked whether the example is false   
def update_false3(change):
    new_update3 = change.new
    
    if(new_update3): #if the button is clicked to the true value
        if((symbol_number3 == 0) and not (new_first_numerator < new_second_numerator)):
            answer_output3.value = 'You are right. The inequality is false.'
        elif ((symbol_number3 == 1) and not (new_first_numerator > new_second_numerator)):
            answer_output3.value = 'You are right. The inequality is false.'
        elif ((symbol_number3 == 2) and not (new_first_numerator == new_second_numerator)):
            answer_output3.value = 'You are right. The equality is false.'
        else:
            if(symbol_number3 == 2):
                answer_output3.value = 'The equality is actually true.'
            else:
                answer_output3.value = 'The inequality is actually true.'
        true_button3.value = False
        equality_answer_output.value = r"<font size='6'><sup>" + str(new_first_numerator) + "</sup>&frasl;<sub>" + str(new_denominator) + "</sub> " +  symbol_list3[symbol_number3] + " <sup>" + str(new_second_numerator) + "</sup>&frasl;<sub>" + str(new_denominator) + "</sub></font>"
    elif(not true_button3.value): #if the button is clicked to the false value and the true button is false
        answer_output3.value = ''
        equality_answer_output.value = ''

#When the false button is clicked it is checked whether the example is true
def update_true3(change):
    new_update4 = change.new
    if(new_update4): #if the button is clicked to the true value
        if((symbol_number3 == 0) and (new_first_numerator < new_second_numerator)):
            answer_output3.value = 'You are right. The inequality is true.'
        elif ((symbol_number3 == 1) and (new_first_numerator > new_second_numerator)):
            answer_output3.value = 'You are right. The inequality is true.'
        elif ((symbol_number3 == 2) and (new_first_numerator == new_second_numerator)):
            answer_output3.value = 'You are right. The equality is true.'
        else:
            if(symbol_number3 == 2):
                answer_output3.value = 'The equality is actually false.'
            else:
                answer_output3.value = 'The inequality is actually false.'
        false_button3.value = False
        equality_answer_output.value = r"<font size='6'><sup>" + str(new_first_numerator) + "</sup>&frasl;<sub>" + str(new_denominator) + "</sub> " +  symbol_list3[symbol_number3] + " <sup>" + str(new_second_numerator) + "</sup>&frasl;<sub>" + str(new_denominator) + "</sub></font>"
    elif(not false_button3.value): #if the button is clicked to the false value and the true button is false
        answer_output3.value = ''
        equality_answer_output.value = ''
    
#Observe when the buttons true/false value has changed and call the function
false_button3.observe(update_false3, names='value')

true_button3.observe(update_true3, names='value')        

#Call the function when the button has been clicked
new_example_button3.on_click(update_Example3)

#display the example widget
display_widget3

#### b)

#The two numbers used in the example
left_number_numerator = 8
left_number_denominator = 12
right_number_numerator = 3
right_number_denominator = 4

#The modified fractions where they have the same denominator
new_left_numerator = left_number_numerator*right_number_denominator
new_right_numerator = right_number_numerator*left_number_denominator
new_denominator3 = left_number_denominator*right_number_denominator

#The outputs displayed in the widget
left_number_output3 = widgets.HTMLMath(
    value=r"<font size='6'><sup>8</sup>&frasl;<sub>12</sub></font>",
)
right_number_output3 = widgets.HTMLMath(
    value=r"<font size='6'><sup>3</sup>&frasl;<sub>4</sub></font>",
)
symbol_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)

example2_answer_output3 = widgets.HTML('')
equality_answer_output3 = widgets.HTMLMath(
    value=''
)

#The buttons used in the widget
greater_than_button3 = widgets.ToggleButton(
    value=False,
    description='Greater Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

less_than_button3 = widgets.ToggleButton(
    value=False,
    description='Less Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

equal_to_button3 = widgets.ToggleButton(
    value=False,
    description='Equal To',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

example2_new_example_button3 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
greater_than_button3.layout.width = '100px'
less_than_button3.layout.width = '100px'
equal_to_button3.layout.width = '100px'

example2_new_example_button3.layout.margin = '10px 0px 0px 250px'

left_number_output3.layout.margin = '10px 0px 10px 80px'
symbol_output3.layout.margin = '10px 15px 10px 15px'
right_number_output3.layout.margin = '10px 0px 10px 0px'
equality_answer_output3.layout.margin = '10px 0px 10px 40px'

#The layout and design of the widgets
example2_output_widget3 = widgets.HBox(children=[left_number_output3, symbol_output3, right_number_output3])

example2_number_widget3 = widgets.VBox(children=[example2_new_example_button3, example2_output_widget3])

example2_question_widget3 = widgets.HBox(children=[greater_than_button3, less_than_button3, equal_to_button3])

example2_display_widget3 = widgets.VBox(children=[example2_number_widget3, example2_question_widget3, example2_answer_output3, equality_answer_output3])

#Generate a new example for the reader
def update_example2_Example3(change):
    global left_number_numerator
    global left_number_denominator
    global right_number_numerator
    global right_number_denominator
    global new_left_numerator
    global new_right_numerator
    global new_denominator3
    
    
    left_number_numerator = random.randint(1,20)
    left_number_denominator = random.randint(1,20)
    right_number_numerator = random.randint(1,20)
    right_number_denominator = random.randint(1,20)
    left_number_output3.value = r"<font size='6'><sup>" + str(left_number_numerator) + "</sup>&frasl;<sub>" + str(left_number_denominator) + "</sub></font>"
    right_number_output3.value = r"<font size='6'><sup>" + str(right_number_numerator) + "</sup>&frasl;<sub>" + str(right_number_denominator) + "</sub></font>"
    symbol_output3.value = '<font size="5"></font>'
    equality_answer_output3.value = ''
    greater_than_button3.value = False
    less_than_button3.value = False
    equal_to_button3.value = False
    
    new_left_numerator = left_number_numerator*right_number_denominator
    new_right_numerator = right_number_numerator*left_number_denominator
    new_denominator3 = left_number_denominator*right_number_denominator

#When the greater than button is clicked it is checked if greater than is the correct answer
def update_greater3(change):
    new_update = change.new
    
    if(new_update): #if the button is clicked to the true value
        if(new_left_numerator > new_right_numerator):
            example2_answer_output3.value = 'You are correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is greater than ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> > </font>'
        else:
            example2_answer_output3.value = 'That is not correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is not greater than ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> > </font>'
        less_than_button3.value = False
        equal_to_button3.value = False
        equality_answer_output3.value = r"<font size='6'><sup>" + str(new_left_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub> > <sup>" + str(new_right_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub></font>"
    elif(not less_than_button3.value and not equal_to_button3.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output3.value = ''
        equality_answer_output3.value = ''

#When the less than button is clicked it is checked if less than is the correct answer
def update_less3(change):
    new_update1 = change.new
    if(new_update1): #if the button is clicked to the true value
        if(new_left_numerator < new_right_numerator):
            example2_answer_output3.value = 'You are correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is less than ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> < </font>'
        else:
            example2_answer_output3.value = 'That is not correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is not less than ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> < </font>'
        greater_than_button3.value = False
        equal_to_button3.value = False
        equality_answer_output3.value = r"<font size='6'><sup>" + str(new_left_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub> < <sup>" + str(new_right_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub></font>"
    elif(not greater_than_button3.value and not equal_to_button3.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output3.value = '' 
        equality_answer_output3.value = ''

#When the equal to button is clicked it is checked if equal to is the correct answer
def update_equal3(change):
    new_update2 = change.new
    if(new_update2): #if the button is clicked to the true value
        if(new_left_numerator == new_right_numerator):
            example2_answer_output3.value = 'You are correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is equal to than ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> = </font>'
        else:
            example2_answer_output3.value = 'That is not correct. ' + str(left_number_numerator) + '/' + str(left_number_denominator) + ' is not equal to ' + str(right_number_numerator) + '/' + str(right_number_denominator) + '.'
            symbol_output3.value = '<font size="6"> = </font>'
        greater_than_button3.value = False
        less_than_button3.value = False
        equality_answer_output3.value = r"<font size='6'><sup>" + str(new_left_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub> = <sup>" + str(new_right_numerator) + "</sup>&frasl;<sub>" + str(new_denominator3) + "</sub></font>"
    elif(not greater_than_button3.value and not less_than_button3.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output3.value = ''
        equality_answer_output3.value = ''
        
#Observe when the buttons values have changed and call the function
greater_than_button3.observe(update_greater3, names='value')

less_than_button3.observe(update_less3, names='value')    

equal_to_button3.observe(update_equal3, names='value')

#Call the function when the button has been clicked
example2_new_example_button3.on_click(update_example2_Example3)

#display the example widget
example2_display_widget3

<a name="Comparing_Different_Number_Types"></a>
## Comparing Different Types of Numbers

So far we have discussed comparing whole numbers to whole numbers, decimals to decimals and fractions to fractions. We have not discussed how to compare whole numbers to decimals, whole numbers to fractions and decimals to fractions. In this section we will discuss how to compare two different types of numbers.

<a name="Whole_Numbers_to_Fractions"></a>
### Comparing Whole Numbers to Fractions

To be able to compare two different types of numbers we will need to convert them to the same number type. When comparing whole numbers to fractions we will convert the whole number to a fraction since a fraction cannot usually be converted to a whole number. 

To compare a whole number to a fraction convert the whole number to a fraction with the same denominator. A whole number can be looked upon as a fraction with the numerator being the whole number and the denominator having a value of 1. To convert the whole number to a fraction with the same denominator we then only need to multiply the whole number by the fraction whose numerator and denominator are the same as the denominator of the original fraction. The example below shows this method.

> The two numbers being compared are:
>
> $\Large 4 \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{7}$
> 
> We start off by looking at the whole number as a fraction with the denominator of 1.
> 
> $\Large \frac{4}{1} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{7}$
>
> To get a common denominator we then multiply the whole number by $\frac{7}{7}$ since $7$ is the denominator of the fraction.
>
> $\Large \frac{4}{1} \times \frac{7}{7} = \frac{28}{7} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{7}$
>
> Now we can compare the two fractions.
>
> $\Large \frac{28}{7} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{7}$
>
> It is clear that
>
> $\Large 28 > 9$
>
> So we determine
>
> $\Large 4 > \frac{9}{7}$

Using the method described above and shown in the example we can compare whole numbers to fractions.

<a name="Whole_Numbers_to_Decimals"></a>
### Comparing Whole Numbers to Decimals

When we compare whole numbers to decimals we will convert the whole number to a decimal since we cannot convert a decimal to a whole number. As mentioned above in the <a href="#Comparing_Positive_Decimal_Numbers">*Comparing Decimal Numbers*</a> section, when we have two decimals with a different number of digits to the right we can add zeros to the right of the number until it has the same number of digits. This is exactly what we will do with our whole number until it has the same number of digits to the right of the decimal as the decimal number has. The example below demonstrates this.

> The two numbers being compared are:
>
> $\Large 3 \hspace{1cm} \text{ and } \hspace{1cm} 2.185$
> 
> To convert the whole number to a decimal we just need to add zeros to the right of the decimal until it has the same number of digits after the decimal as the decimal number.
>
> $\Large 3.\color{red}{\underline{\hspace{1.05cm}}} \hspace{1cm} \text{ and } \hspace{1cm} 2.\color{red}{\underline{185}}$
>
> $\Large 3.\color{red}{\underline{000}} \hspace{1cm} \text{ and } \hspace{1cm} 2.\color{red}{\underline{185}}$
>
> Now we can compare the two decimals.
> 
> $\Large 3.000 \hspace{1cm} \text{ and } \hspace{1cm} 2.185$
>
> Comparing them we determine:
>
> $\Large 3.000 > 2.185$
>
> Which means that:
>
> $\Large 3 > 2.185$

Using the method in the example that was described we can compare whole numbers to decimals.

<a name="Decimals_to_Fractions"></a>
### Comparing Decimals to Fractions

When we compare decimals to fractions we can either convert the decimals to fractions, fractions to decimals or use a hybrid method of both. We will go through all three methods and it will be up to the readers to choose which method they want to use. If the reader is using a calculator the easiest method to use will be converting fractions to decimals.
<a name="Convert_Decimal_to_Fraction"></a>
#### Convert Decimals to Fractions

To convert decimals to fractions we use the decimal's lowest place value. For example if we have a decimal to the hundredth place value we would multiply the number by 100 and it would turn the decimal into a whole number. Since a decimal can be thought of as a fraction with denominator of 1 we must multiply the denominator by 100 as well and this would turn the decimal into an equivalent fraction. The example below will show this method with a decimal number to the tenth place.

> The two numbers being compared are:
>
> $\Large 3.4 \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
> 
> First we convert the decimal number to a fraction. We see the decimal's lowest place value is the tenth place value which means we want to multiply the decimal by 10 to turn it into a whole number. Considering the decimal as a fraction over denominator of one, we preserve the value by multiplying by $1=\frac{10}{10}$ .
>
> $\Large \frac{3.4}{1} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
>
> $\Large \frac{3.4}{1} \times \frac{10}{10} = \frac{34}{10} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
>
> So we end up with the two fractions below.
>
> $\Large \frac{34}{10} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
>
> Using the method described in Comparing Fractions section we have:
>
> $\Large \frac{68}{20} \hspace{1cm} \text{ and } \hspace{1cm} \frac{90}{20}$
>
> $\Large 68 < 90$
>
> Which means:
>
> $\Large 3.4 < \frac{9}{2}$

<a name="Convert_Fraction_to_Decimal"></a>
#### Convert Fractions to Decimals

To convert fractions to decimals we will need a calculator or need to use long division to turn the fraction into a decimal. It is assumed that the reader knows how to do long division and can turn the fraction into a decimal so that will not be covered. The example below shows this.

> The two numbers being compared are:
>
> $\Large \frac{7}{4} \hspace{1cm} \text{ and } \hspace{1cm} 1.34$
>
> Dividing 7 by 4 we get the decimal:
>
> $\Large \frac{7}{4} = 1.75 \hspace{1cm} \text{ and } \hspace{1cm} 1.34$
>
> The two decimal numbers are then:
> 
> $\Large 1.75 \hspace{1cm} \text{ and } \hspace{1cm} 1.34$
>
> Comparing them we determine:
>
> $\Large 1.75 > 1.34$
>
> Which means:
>
> $\Large \frac{7}{4} > 1.34$

Using this method can become difficult since some fractions can be decimal numbers that have many digits to the right of the decimal place. This could make using long division difficult. If the reader has a calculator then this method would be the fastest since one can get the decimal answer right away.

<a name="Hybrid_Method"></a>
#### Hybrid Method

In this method we will be converting the decimal number to a hybrid fraction with a decimal number in the numerator. We will first use the method discussed in the <a href="#Whole_Numbers_to_Fractions">*Comparing Whole Numbers to Fractions*</a> section and then use the method in the <a href="#Whole_Numbers_to_Decimals">*Comparing Whole Numbers to Decimals*</a> section. 

We will start off by thinking of the decimal as a fraction with denominator of 1. Then we will multiply the decimal by the denominator of the fraction. The 1 denominator of the fraction will also be multiplied by the fraction denominator so the value of the number does not change. Now that the two fractions have the same denominator we only need to compare the numerators. The numerators of the fractions are a decimal number and a whole number so we will need to convert the whole number to a decimal and then they can be compared. The example below will show this method. 

> The two numbers being compared are:
>
> $\Large 3.4 \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
> 
> First we convert the decimal number to a fraction with denominator 1.
>
> $\Large \frac{3.4}{1} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
>
> We then find an equivalent fraction to the new fraction using the denominator of the original fraction
>
> $\Large \frac{3.4}{1} \times \frac{2}{2} = \frac{6.8}{2} \hspace{1cm} \text{ and } \hspace{1cm} \frac{9}{2}$
>
> Now that the denominators of the fractions are the same we can compare the numerators.
>
> $\Large 6.8 \hspace{1cm} \text{ and } \hspace{1cm} 9$
>
> The numerators are not the same type of number so we need to convert the whole number to a decimal.
>
> $\Large 6.8 \hspace{1cm} \text{ and } \hspace{1cm} 9.0$
>
> Now we can compare the numbers and determine:
>
> $\Large 6.8 < 9.0$
>
> Which means:
>
> $\Large 3.4 < \frac{9}{2}$


The three methods discussed above each have there own advantages and disadvantages so it will be up to the reader to decide which method they prefer to use. 

<a name="Example4"></a>
### Practice Examples

Here are some practice examples for you to become familiar with using the processes described above. The examples are similar to those in the <a href="#Example1">*Comparing Whole Numbers*</a> section.

#### 4. Random Number Type Examples

#### a)

#The numbers used in the example, the symbol is used to compare them and the type of example
fraction_numerator = 5
fraction_denominator = 12
whole_number = 7
decimal_number = 5.5
symbol_number4 = 0
example_type = 0

#Common denominators depending on what example is being displayed
whole_number_numerator = whole_number*fraction_denominator
decimal_number_numerator = decimal_number*fraction_denominator   

#List of symbols that can be used in the examples
symbol_list4 = ['<','>','=']

#The outputs displayed in the widget
example_output4 = widgets.HTMLMath(
    value=r"<font size='6'> 3  <  <sup>7</sup>&frasl;<sub>10</sub></font>",
)

answer_output4 = widgets.HTML('')

#The buttons used in the widget
true_button4 = widgets.ToggleButton(
    value=False,
    description='True',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is true',
    continuous_update=True
)

false_button4 = widgets.ToggleButton(
    value=False,
    description='False',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Equality or inequality is false',
    continuous_update=True
)

new_example_button4 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
false_button4.layout.width = '100px'
true_button4.layout.width = '100px'

new_example_button4.layout.margin = '10px 0px 0px 300px'

example_output4.layout.margin = '10px 0px 10px 40px'

#The layout and design of the widgets
number_widget4 = widgets.VBox(children=[new_example_button4, example_output4])

question_widget4 = widgets.HBox(children=[false_button4, true_button4])

display_widget4 = widgets.VBox(children=[number_widget4, question_widget4, answer_output4])

#Generate a new example for the reader
def update_Example4(change):
    global fraction_numerator
    global fraction_denominator
    global whole_number
    global decimal_number
    global symbol_number4
    global example_type
    global whole_number
    global whole_number_numerator
    global decimal_number_numerator
    
    fraction_numerator = random.randint(1,20)
    fraction_denominator = random.randint(1,20)
    whole_number = random.randint(1,20)
    decimal_number = round(random.uniform(0,15), 3)
    decimal_number = round(decimal_number, 3)
    symbol_number4 = random.randint(0,2)
    example_type = random.randint(0,2)
    if(example_type == 0):
        example_output4.value = r"<font size='6'>" + str(whole_number) + " " +  symbol_list4[symbol_number4] + " <sup>" + str(fraction_numerator) + "</sup>&frasl;<sub>" + str(fraction_denominator) + "</sub></font>"
    elif(example_type == 1):
        example_output4.value = r"<font size='6'>" + str(whole_number) + " " +  symbol_list4[symbol_number4] + " " + str(decimal_number) + "</font>"
    elif(example_type == 2):
        example_output4.value = r"<font size='6'>" + str(decimal_number) + " " + symbol_list4[symbol_number4] + " <sup>" + str(fraction_numerator) + "</sup>&frasl;<sub>" + str(fraction_denominator) + "</sub></font>" 
    true_button4.value = False
    false_button4.value = False
    
    whole_number_numerator = whole_number*fraction_denominator
    decimal_number_numerator = decimal_number*float(fraction_denominator)    
    
#When the false button is clicked it is checked whether the example is false
def update_false4(change):
    new_update4 = change.new
    
    if(new_update4): #if the button is clicked to the true value
        if(example_type == 0):
            if((symbol_number4 == 0) and not (whole_number_numerator < fraction_numerator)):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 1) and not (whole_number_numerator > fraction_numerator)):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 2) and not (whole_number_numerator == fraction_numerator)):
                answer_output4.value = 'You are right. The equality is false.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually true.'
                else:
                    answer_output4.value = 'The inequality is actually true.'
        elif(example_type == 1):
            if((symbol_number4 == 0) and not (float(whole_number) < decimal_number)):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 1) and not (float(whole_number) > decimal_number)):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 2) and not (float(whole_number) == decimal_number)):
                answer_output4.value = 'You are right. The equality is false.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually true.'
                else:
                    answer_output4.value = 'The inequality is actually true.'
        elif(example_type == 2):             
            if((symbol_number4 == 0) and not (decimal_number_numerator < float(fraction_numerator))):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 1) and not (decimal_number_numerator > float(fraction_numerator))):
                answer_output4.value = 'You are right. The inequality is false.'
            elif ((symbol_number4 == 2) and not (decimal_number_numerator == float(fraction_numerator))):
                answer_output4.value = 'You are right. The equality is false.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually true.'
                else:
                    answer_output4.value = 'The inequality is actually true.'
        true_button4.value = False
    elif(not true_button4.value): #if the button is clicked to the false value and the true button is false
        answer_output4.value = '' 

#When the false button is clicked it is checked whether the example is true
def update_true4(change):
    new_update5 = change.new
    if(new_update5): #if the button is clicked to the true value
        if(example_type == 0):
            if((symbol_number4 == 0) and (whole_number_numerator < fraction_numerator)):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 1) and (whole_number_numerator > fraction_numerator)):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 2) and (whole_number_numerator == fraction_numerator)):
                answer_output4.value = 'You are right. The equality is true.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually false.'
                else:
                    answer_output4.value = 'The inequality is actually false.'
        elif(example_type == 1):
            if((symbol_number4 == 0) and (float(whole_number) < decimal_number)):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 1) and (float(whole_number) > decimal_number)):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 2) and (float(whole_number) == decimal_number)):
                answer_output4.value = 'You are right. The equality is true.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually false.'
                else:
                    answer_output4.value = 'The inequality is actually false.'
        elif(example_type == 2):             
            if((symbol_number4 == 0) and (decimal_number_numerator < float(fraction_numerator))):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 1) and (decimal_number_numerator > float(fraction_numerator))):
                answer_output4.value = 'You are right. The inequality is true.'
            elif ((symbol_number4 == 2) and (decimal_number_numerator == float(fraction_numerator))):
                answer_output4.value = 'You are right. The equality is true.'
            else:
                if(symbol_number4 == 2):
                    answer_output4.value = 'The equality is actually false.'
                else:
                    answer_output4.value = 'The inequality is actually false.'        
        
        false_button4.value = False
    elif(not false_button4.value): #if the button is clicked to the false value and the true button is false
        answer_output4.value = '' 
    
#Observe when the buttons true/false value has changed and call the function
false_button4.observe(update_false4, names='value')

true_button4.observe(update_true4, names='value')        

#Call the function when the button has been clicked
new_example_button4.on_click(update_Example4)

#display the example widget
display_widget4

#### b)

#The numbers used in the example
fraction_numerator2 = 2
fraction_denominator2 = 7
whole_number2 = 4
decimal_number2 = 5.5
example_type2 = 0

#Common denominators depending on what example is being displayed
whole_number_numerator2 = whole_number2*fraction_denominator2
decimal_number_numerator2 = decimal_number2*fraction_denominator2  

#The outputs displayed in the widget
left_number_output4 = widgets.HTMLMath(
    value=r"<font size='6'> 4 </font>",
)
right_number_output4 = widgets.HTMLMath(
    value=r"<font size='6'><sup>2</sup>&frasl;<sub>7</sub></font>",
)
symbol_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)

example2_answer_output4 = widgets.HTML('')

#The buttons used in the widget
greater_than_button4 = widgets.ToggleButton(
    value=False,
    description='Greater Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

less_than_button4 = widgets.ToggleButton(
    value=False,
    description='Less Than',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

equal_to_button4 = widgets.ToggleButton(
    value=False,
    description='Equal To',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    continuous_update=True
)

example2_new_example_button4 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
greater_than_button4.layout.width = '100px'
less_than_button4.layout.width = '100px'
equal_to_button4.layout.width = '100px'

example2_new_example_button4.layout.margin = '10px 0px 0px 250px'

left_number_output4.layout.margin = '10px 0px 10px 80px'
symbol_output4.layout.margin = '10px 15px 10px 15px'
right_number_output4.layout.margin = '10px 0px 10px 0px'

#The layout and design of the widgets
example2_output_widget4 = widgets.HBox(children=[left_number_output4, symbol_output4, right_number_output4])

example2_number_widget4 = widgets.VBox(children=[example2_new_example_button4, example2_output_widget4])

example2_question_widget4 = widgets.HBox(children=[greater_than_button4, less_than_button4, equal_to_button4])

example2_display_widget4 = widgets.VBox(children=[example2_number_widget4, example2_question_widget4, example2_answer_output4])

#Generate a new example for the reader
def update_example2_Example4(change):
    global fraction_numerator2
    global fraction_denominator2
    global whole_number2
    global decimal_number2
    global example_type2
    global whole_number_numerator2
    global decimal_number_numerator2
    
    fraction_numerator2 = random.randint(1,20)
    fraction_denominator2 = random.randint(1,20)
    whole_number2 = random.randint(1,20)
    decimal_number2 = round(random.uniform(0,15), 3)
    decimal_number2 = round(decimal_number2, 3)
    example_type2 = random.randint(0,2)
    if(example_type2 == 0):
        left_number_output4.value = r"<font size='6'>" + str(whole_number2) + "</font>"
        right_number_output4.value = r"<font size='6'><sup>" + str(fraction_numerator2) + "</sup>&frasl;<sub>" + str(fraction_denominator2) + "</sub></font>"
    elif(example_type2 == 1):
        left_number_output4.value = r"<font size='6'>" + str(whole_number2) + "</font>"
        right_number_output4.value = r"<font size='6'>" + str(decimal_number2) + "</font>"
    elif(example_type2 == 2):
        left_number_output4.value = r"<font size='6'> "+ str(decimal_number2) + "</font>"
        right_number_output4.value = r"<font size='6'><sup>" + str(fraction_numerator2) + "</sup>&frasl;<sub>" + str(fraction_denominator2) + "</sub></font>"
    
    symbol_output4.value = '<font size="5"></font>'
    greater_than_button4.value = False
    less_than_button4.value = False
    equal_to_button4.value = False
    
    whole_number_numerator2 = whole_number2*fraction_denominator2
    decimal_number_numerator2 = decimal_number2*float(fraction_denominator2) 
    
    
#When the greater than button is clicked it is checked if greater than is the correct answer
def update_greater4(change):
    new_update = change.new
    
    if(new_update): #if the button is clicked to the true value
        if((example_type2 == 0) and (whole_number_numerator2 > fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is greater than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> > </font>'
        elif ((example_type2 == 1) and (whole_number2 > decimal_number2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is greater than ' + str(decimal_number2) + '.'
            symbol_output4.value = '<font size="6"> > </font>'
        elif ((example_type2 == 2) and (decimal_number_numerator2 > fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(decimal_number2) + ' is greater than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> > </font>'
        else:
            if (example_type2 == 0):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not greater than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            elif (example_type2 == 1):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not greater than ' + str(decimal_number2) + '.'
            elif (example_type2 == 2):
                example2_answer_output4.value = 'That is not correct. ' + str(decimal_number2) + ' is not greater than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> > </font>'
            
        less_than_button4.value = False
        equal_to_button4.value = False
    elif(not less_than_button4.value and not equal_to_button4.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output4.value = ''

#When the less than button is clicked it is checked if less than is the correct answer
def update_less4(change):
    new_update1 = change.new
    if(new_update1): #if the button is clicked to the true value
        if((example_type2 == 0) and (whole_number_numerator2 < fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is less than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> < </font>'
        elif ((example_type2 == 1) and (whole_number2 < decimal_number2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is less than ' + str(decimal_number2) + '.'
            symbol_output4.value = '<font size="6"> < </font>'
        elif ((example_type2 == 2) and (decimal_number_numerator2 < fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(decimal_number2) + ' is less than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> < </font>'
        else:
            if (example_type2 == 0):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not less than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            elif (example_type2 == 1):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not less than ' + str(decimal_number2) + '.'
            elif (example_type2 == 2):
                example2_answer_output4.value = 'That is not correct. ' + str(decimal_number2) + ' is not less than ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> < </font>'
        greater_than_button4.value = False
        equal_to_button4.value = False
    elif(not greater_than_button4.value and not equal_to_button4.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output4.value = '' 

#When the equal to button is clicked it is checked if equal to is the correct answer
def update_equal4(change):
    new_update2 = change.new
    if(new_update2): #if the button is clicked to the true value
        if((example_type2 == 0) and (whole_number_numerator2 == fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is equal to ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> = </font>'
        elif ((example_type2 == 1) and (whole_number2 == decimal_number2)):
            example2_answer_output4.value = 'You are correct. ' + str(whole_number2) + ' is equal to ' + str(decimal_number2) + '.'
            symbol_output4.value = '<font size="6"> = </font>'
        elif ((example_type2 == 2) and (decimal_number_numerator2 == fraction_numerator2)):
            example2_answer_output4.value = 'You are correct. ' + str(decimal_number2) + ' is equal to ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> = </font>'
        else:
            if (example_type2 == 0):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not equal to ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            elif (example_type2 == 1):
                example2_answer_output4.value = 'That is not correct. ' + str(whole_number2) + ' is not equal to ' + str(decimal_number2) + '.'
            elif (example_type2 == 2):
                example2_answer_output4.value = 'That is not correct. ' + str(decimal_number2) + ' is not equal to ' + str(fraction_numerator2) + '/' + str(fraction_denominator2) + '.'
            symbol_output4.value = '<font size="6"> = </font>'
        
        greater_than_button4.value = False
        less_than_button4.value = False
    elif(not greater_than_button4.value and not less_than_button4.value): #if the button is clicked to the false value and the other buttons are false
        example2_answer_output4.value = ''
        
#Observe when the buttons values have changed and call the function
greater_than_button4.observe(update_greater4, names='value')

less_than_button4.observe(update_less4, names='value')    

equal_to_button4.observe(update_equal4, names='value')

#Call the function when the button has been clicked
example2_new_example_button4.on_click(update_example2_Example4)

#display the example widget
example2_display_widget4

<a name="Ordering"></a>
## Ordering: Positive Fractions, Positive Decimals and Whole Numbers

When we order numbers there are two ways that they can be ordered. We will only focus on ordering numbers from lowest to highest. If you want highest to lowest you can just reverse that ordering.

To order numbers from lowest to highest we will use a looping method that can be used to order fractions, decimals or whole numbers. The method we use starts by finding the highest number, then the second highest, and so on until only the lowest number is left. For example if we have a list of 5 numbers the method starts off by picking the first number in the list and putting it as the highest number. We then compare the current highest number to the next number in the list and if the next number is greater than it we pick that number as the new highest number. Now we move on to the next number in the list and compare the new highest number to it and as before if the next number is greater than it we pick that number as the new highest number. This process continues until we reach the end of the list. The number that is currently the highest number will be the highest number in the list. We then remove the current highest number from the list and start the process again to find the highest number of the reduced list. This will then find the second highest number and we remove that number from the list and then find the next highest number in the list again. We repeat this process until we only have one number left in the list which will be the lowest number. The example below will show this method.

> We have a list of 5 whole numbers below:
>
> $\large 9, 4, 7, 2, 5$
>
> We start off setting the first number as the highest number.
>
> $\large \text{HN} = 9$
>
> We then compare it to the next number.
>
> $\large 9, \color{red}{\underline{4}}, 7, 2, 5$
>
> $\large 9 > 4$
>
> 9 is greater than 4 so 9 stays as the highest number.
>
> $\large \text{HN} = 9$
>
> We then move on to the next number.
>
> $\large 9, 4, \color{red}{\underline{7}}, 2, 5$
>
> $\large 9 > 7$
>
> $\large \text{HN} = 9$
>
> 9 is still the highest number so we move to the next number.
>
> $\large 9, 4, 7, \color{red}{\underline{2}}, 5$
>
> $\large 9 > 2$
>
> $\large \text{HN} = 9$
>
> It is still greater so we move to the next number.
>
> $\large 9, 4, 7, 2,\color{red}{\underline{5}}$
>
> $\large 9 > 5$
>
> $\large \text{HN} = 9$
>
> We have reached the end of the list and 9 is still the highest number. 9 will be removed from the list and put as the highest number in a new list. We now start the search again in the list to find the next highest number. The first number in the list will again be set as the highest number.
>
> $\large 4, 7, 2, 5 \hspace{10cm} 9$
> 
> $\large \text{HN} = 4$
>
> The highest number will be compared to the next number in the list.
>
> $\large 4,\color{red}{\underline{7}}, 2, 5 \hspace{10cm} 9$
>
> $\large 4 < 7$
>
> Our current highest number is less then 7 so 7 becomes the new highest number.
>
> $\large \text{HN} = 7$
>
> We then move on to the next number and compare it again the highest number.
>
> $\large 4, 7,\color{red}{\underline{2}}, 5 \hspace{10cm} 9$
>
> $\large 7 > 2$
>
> $\large \text{HN} = 7$
>
> $\large 4, 7, 2,\color{red}{\underline{5}} \hspace{10cm} 9$
>
> $\large 7 > 5$
>
> $\large \text{HN} = 7$
>
> We have reached the end of the list and 7 remained the highest number. Now we remove 7 from the list and add it to the left of 9 in our new list.
>
> $\large 4, 2, 5 \hspace{10cm} 7,9$
>
> Following the same process shown above our next highest number from the first list is 5 and it will be added to the second list.
>
> $\large 4, 2 \hspace{10cm} 5,7,9$
> 
> The next highest is 4.
>
> $\large 2 \hspace{10cm} 4,5,7,9$
>
> We now only have one number left in the list and it will be the lowest number. This number will get added to the left of the second list.
>
>  $\large  \hspace{9.7cm} 2,4,5,7,9$
>
> Our second list is sorted from lowest to highest and gives us the ordered list.

By following this procedure we will be able to sort lists of whole numbers, decimals and fractions from lowest to highest. To sort a list of fractions the reader will need to convert the fractions in the list to all have the same denominator and then they can be compared and ordered. 

<a name="Ordering_Mixed"></a>
### Ordering Mixed Number Types

To order a list of mixed number types the same process outlined above in comparing and ordering the list will be done. The difference will be the reader will need to first go through the list and convert all the numbers to the same number type before it can be sorted. An example will not be done here since examples have already been down showing how to convert between number types and how to sort a list.

<a name="Ordering_Examples"></a>
## Practice Examples

The examples below asks the reader to sort lists of whole numbers, fractions, decimals and mixed number type lists.

In the examples a list of 5 numbers will be generated and the reader needs to pick in the drop down box whether the number should be in the 1st, 2nd, 3rd, 4th or 5th position. The **Show Selected List** button will show the reader the list of numbers in the order they have selected. Once the reader has selected the order of the list they can click on the **Submit Answer** button and it will tell the reader whether the list has been sorted correctly. The **Submit Answer** button also shows the currently selected list and displays the numbers in <span style="color:red"> red </span> if it is in the wrong position and <span style="color:lime"> green </span> if it is in the correct position.

#### 1. Sort the Whole Number List

#Random list of numbers and a list that will be used for the sorted numbers
number_list = [4,9,1,3,6]

current_list = [0,0,0,0,0]

sorted_list = []

#output for the number list displayed in the widget
first_number_output = widgets.HTMLMath(
    value='<font size="5"> 4 </font>',
)
second_number_output = widgets.HTMLMath(
    value='<font size="5"> 9 </font>',
)
third_number_output = widgets.HTMLMath(
    value='<font size="5"> 1 </font>',
)
fourth_number_output = widgets.HTMLMath(
    value='<font size="5"> 3 </font>',
)
fifth_number_output = widgets.HTMLMath(
    value='<font size="5"> 6 </font>',
)

number_output_list = [first_number_output, second_number_output, third_number_output, fourth_number_output, fifth_number_output]

#output for the list picked by the reader
first_choice_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
second_choice_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
third_choice_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
fourth_choice_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
fifth_choice_output = widgets.HTMLMath(
    value='<font size="5">  </font>',
)

output_choice_list = [first_choice_output, second_choice_output, third_choice_output, fourth_choice_output, fifth_choice_output]

error_output = widgets.HTML('') #output for whether a user has entered two numbers in the same position of the list

list_answer_output = widgets.HTML('') #output for whether the list was sorted correctly

#drop down position choices for the numbers the reader picks
first_choice = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
second_choice = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
third_choice = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fourth_choice = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fifth_choice = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)

choice_list = [first_choice, second_choice, third_choice, fourth_choice, fifth_choice]

#buttons shown in the widget
new_list_button = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

submit_button = widgets.Button(
    value=False,
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Submit the answer',
    continuous_update=True
)

show_list_button = widgets.Button(
    value=False,
    description='Show Selected List',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show the current selected list the reader has selected',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
for i in range(len(choice_list)):
    choice_list[i].layout.width = '150px'

for i in range(len(output_choice_list)):
    output_choice_list[i].layout.width = '150px'

for i in range(len(number_output_list)):
    number_output_list[i].layout.margin = '10px 0px 10px 0px'

new_list_button.layout.margin = '10px 0px 0px 800px'
show_list_button.layout.margin = '10px 0px 0px 800px'

#The layout and design of the widgets
position_one_widget = widgets.VBox(children=[first_number_output, first_choice])
position_two_widget = widgets.VBox(children=[second_number_output, second_choice])
position_three_widget = widgets.VBox(children=[third_number_output, third_choice])
position_four_widget = widgets.VBox(children=[fourth_number_output, fourth_choice])
position_five_widget = widgets.VBox(children=[fifth_number_output, fifth_choice])

position_widget = widgets.HBox(children=[position_one_widget, position_two_widget, position_three_widget, position_four_widget, position_five_widget])
choice_widget = widgets.HBox(children=[first_choice_output, second_choice_output, third_choice_output, fourth_choice_output, fifth_choice_output])

display_list_widget = widgets.VBox(children=[new_list_button, position_widget, submit_button , list_answer_output, error_output, show_list_button, choice_widget])

#Generate a new example list for the reader
def update_Example(change):
    global number_list
    
    #Generate a random list of whole numbers
    for i in range(len(number_list)):
        number_list[i] = random.randint(10,999)
    
    #Set the output value based on the random list
    for i in range(len(number_output_list)):
        number_output_list[i].value = '<font size="5"> ' + str(number_list[i]) + ' </font>'
    
    #Set the list choices to null
    for i in range(len(choice_list)):
        choice_list[i].value = 0
    
    display_List(True) #display the current selected list by the reader
    
    #Set the current selected list to null
    for i in range(len(number_list)):
        current_list[i] = 0
    
    sort_list() #call the function to sort the list

#Display the current selected list by the reader
def display_List(change):
    list_answer_output.value = ''
    
    #Erase the current displayed list
    for i in range(len(output_choice_list)):
        output_choice_list[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list)):
        for j in range(len(output_choice_list)):
            if(choice_list[i].value == (j+1)):
                output_choice_list[j].value = number_output_list[i].value

#Sorts the random list by looping through pulling out the highest number each time
def sort_list():
    global number_list
    global sorted_list
    
    del sorted_list[:]
    temp_list = number_list[:]
    
    for j in range(len(temp_list)):
        highest_number = temp_list[0]
        position = 0
    
        for i in range(len(temp_list)):
            if (highest_number < temp_list[i]):
                highest_number = temp_list[i]
        
        sorted_list.insert(0, highest_number)
        
        temp_list.remove(highest_number)

#Compares the current list selected by the reader to the sorted list
def check_Answer(change):
    global number_list
    global current_list
    global sorted_list
    
    sort_list()
    
    #empty the current list before setting it
    for i in range(len(number_list)):
        current_list[i] = 0
    
    #set the list selected by the reader to the current list
    for i in range(len(choice_list)):
        if (not(choice_list[i].value == 0)):
            current_list[(choice_list[i].value-1)] = number_list[i]
    
    #compare the two lists
    if (current_list == sorted_list):
        list_answer_output.value = 'Correct! You have sorted the list correctly.'
    else:
        list_answer_output.value = 'Incorrect. The list is not sorted.'

    #Erase the current displayed list
    for i in range(len(output_choice_list)):
        output_choice_list[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list)):
        for j in range(len(output_choice_list)):
            if(choice_list[i].value == (j+1)):
                output_choice_list[j].value = number_output_list[i].value
    
    for i in range(len(current_list)):
        if(current_list[i] == sorted_list[i]):
            output_choice_list[i].value = '<font size="5" color="lime">' + output_choice_list[i].value +  '</font>'
        else:
            output_choice_list[i].value = '<font size="5" color="red">' + output_choice_list[i].value +  '</font>'
        
    
    
#checks to see if the user has enter two or more numbers in the same position
def check_Error(change):
    error = False
    
    for i in range(len(choice_list)):
        if(not(choice_list[i].value == 0)):
            for j in range(len(choice_list)-(i+1)):
                if(choice_list[i].value == choice_list[j+i+1].value):
                    error_output.value = 'ERROR: You have two or more numbers in the same position!'
                    error = True
                    break
        if(error):
            break
    
    if(not(error)):
        error_output.value = ''

    
#Call the function when the button has been clicked     
new_list_button.on_click(update_Example)

show_list_button.on_click(display_List)

submit_button.on_click(check_Answer)

first_choice.observe(check_Error, names='value')
second_choice.observe(check_Error, names='value')
third_choice.observe(check_Error, names='value')
fourth_choice.observe(check_Error, names='value')
fifth_choice.observe(check_Error, names='value')

#display the example widget
display_list_widget

#### 2. Sort the Decimal List

#Random list of numbers and a list that will be used for the sorted numbers
decimal_list = [4.56,7.45,3.231,4.23,7.011]

current_decimal_list = [0.0,0.0,0.0,0.0,0.0]

sorted_decimal_list = []

#output for the number list displayed in the widget
first_decimal_output = widgets.HTMLMath(
    value='<font size="5"> 4.56 </font>',
)
second_decimal_output = widgets.HTMLMath(
    value='<font size="5"> 7.45 </font>',
)
third_decimal_output = widgets.HTMLMath(
    value='<font size="5"> 3.231 </font>',
)
fourth_decimal_output = widgets.HTMLMath(
    value='<font size="5"> 4.23 </font>',
)
fifth_decimal_output = widgets.HTMLMath(
    value='<font size="5"> 7.011 </font>',
)

decimal_output_list = [first_decimal_output, second_decimal_output, third_decimal_output, fourth_decimal_output, fifth_decimal_output]

#output for the list picked by the reader
first_choice_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
second_choice_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
third_choice_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
fourth_choice_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)
fifth_choice_output2 = widgets.HTMLMath(
    value='<font size="5">  </font>',
)

output_choice_list2 = [first_choice_output2, second_choice_output2, third_choice_output2, fourth_choice_output2, fifth_choice_output2]

error_output2 = widgets.HTML('') #output for whether a user has entered two numbers in the same position of the list

list_answer_output2 = widgets.HTML('') #output for whether the list was sorted correctly

#drop down position choices for the numbers the reader picks
first_choice2 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
second_choice2 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
third_choice2 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fourth_choice2 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fifth_choice2 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)

choice_list2 = [first_choice2, second_choice2, third_choice2, fourth_choice2, fifth_choice2]

#buttons shown in the widget
new_list_button2 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

submit_button2 = widgets.Button(
    value=False,
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Submit the answer',
    continuous_update=True
)

show_list_button2 = widgets.Button(
    value=False,
    description='Show Selected List',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show the current selected list the reader has selected',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
for i in range(len(choice_list2)):
    choice_list2[i].layout.width = '150px'

for i in range(len(output_choice_list2)):
    output_choice_list2[i].layout.width = '150px'

for i in range(len(decimal_output_list)):
    decimal_output_list[i].layout.margin = '10px 0px 10px 0px'

new_list_button2.layout.margin = '10px 0px 0px 800px'
show_list_button2.layout.margin = '10px 0px 0px 800px'

#The layout and design of the widgets
position_one_widget2 = widgets.VBox(children=[first_decimal_output, first_choice2])
position_two_widget2 = widgets.VBox(children=[second_decimal_output, second_choice2])
position_three_widget2 = widgets.VBox(children=[third_decimal_output, third_choice2])
position_four_widget2 = widgets.VBox(children=[fourth_decimal_output, fourth_choice2])
position_five_widget2 = widgets.VBox(children=[fifth_decimal_output, fifth_choice2])

position_widget2 = widgets.HBox(children=[position_one_widget2, position_two_widget2, position_three_widget2, position_four_widget2, position_five_widget2])
choice_widget2 = widgets.HBox(children=[first_choice_output2, second_choice_output2, third_choice_output2, fourth_choice_output2, fifth_choice_output2])

display_list_widget2 = widgets.VBox(children=[new_list_button2, position_widget2, submit_button2, list_answer_output2, error_output2, show_list_button2, choice_widget2])

#Generate a new example list for the reader
def update_Example2(change):
    global decimal_list
    
    #Generate a random list of decimal numbers
    for i in range(len(decimal_list)):
        decimal_list[i] = round(random.uniform(0,15), 3)
        decimal_list[i] = round(decimal_list[i], 3)
    
    #Set the output value based on the random list
    for i in range(len(decimal_output_list)):
        decimal_output_list[i].value = '<font size="5"> ' + str(decimal_list[i]) + ' </font>'
    
    #Set the list choices to null
    for i in range(len(choice_list2)):
        choice_list2[i].value = 0
    
    display_List2(True) #display the current selected list by the reader
    
    #Set the current selected list to null
    for i in range(len(decimal_list)):
        current_decimal_list[i] = 0.0

#Display the current selected list by the reader
def display_List2(change):
    list_answer_output2.value = ''
    
    #Erase the current displayed list
    for i in range(len(output_choice_list2)):
        output_choice_list2[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list2)):
        for j in range(len(output_choice_list2)):
            if(choice_list2[i].value == (j+1)):
                output_choice_list2[j].value = decimal_output_list[i].value

#Sorts the random list by looping through pulling out the highest number each time
def sort_list2():
    global decimal_list
    global sorted_decimal_list
    
    del sorted_decimal_list[:]
    temp_list = decimal_list[:]
    
    for j in range(len(temp_list)):
        highest_number = temp_list[0]
    
        for i in range(len(temp_list)):
            if (highest_number < temp_list[i]):
                highest_number = temp_list[i]
        
        sorted_decimal_list.insert(0, highest_number)
        
        temp_list.remove(highest_number)

#Compares the current list selected by the reader to the sorted list
def check_Answer2(change):
    global decimal_list
    global current_decimal_list
    global sorted_decimal_list
    
    sort_list2()
    
    #empty the current list before setting it
    for i in range(len(decimal_list)):
        current_decimal_list[i] = 0.0
    
    #set the list selected by the reader to the current list
    for i in range(len(choice_list2)):
        if (not(choice_list2[i].value == 0.0)):
            current_decimal_list[(choice_list2[i].value-1)] = decimal_list[i]
    
    #compare the two lists
    if (current_decimal_list == sorted_decimal_list):
        list_answer_output2.value = 'Correct! You have sorted the list correctly.'
    else:
        list_answer_output2.value = 'Incorrect. The list is not sorted.'

    #Erase the current displayed list
    for i in range(len(output_choice_list2)):
        output_choice_list2[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list2)):
        for j in range(len(output_choice_list2)):
            if(choice_list2[i].value == (j+1)):
                output_choice_list2[j].value = decimal_output_list[i].value
    
    for i in range(len(current_decimal_list)):
        if(current_decimal_list[i] == sorted_decimal_list[i]):
            output_choice_list2[i].value = '<font size="5" color="lime">' + output_choice_list2[i].value +  '</font>'
        else:
            output_choice_list2[i].value = '<font size="5" color="red">' + output_choice_list2[i].value +  '</font>'
        
#checks to see if the user has enter two or more numbers in the same position
def check_Error2(change):
    error = False
    
    for i in range(len(choice_list2)):
        if(not(choice_list2[i].value == 0)):
            for j in range(len(choice_list2)-(i+1)):
                if(choice_list2[i].value == choice_list2[j+i+1].value):
                    error_output2.value = 'ERROR: You have two or more numbers in the same position!'
                    error = True
                    break
        if(error):
            break
    
    if(not(error)):
        error_output2.value = ''        

        
#Call the function when the button has been clicked 
new_list_button2.on_click(update_Example2)

show_list_button2.on_click(display_List2)

submit_button2.on_click(check_Answer2)

first_choice2.observe(check_Error2, names='value')
second_choice2.observe(check_Error2, names='value')
third_choice2.observe(check_Error2, names='value')
fourth_choice2.observe(check_Error2, names='value')
fifth_choice2.observe(check_Error2, names='value')

#display the example widget
display_list_widget2

#### 3. Sort the Fraction List

#Random list of numbers and a list that will be used for the sorted numbers
fraction_numerator_list = [3,9,2,5,7]
fraction_denominator_list = [5,14,8,9,11]

converted_fraction_list=[]

#Convert the fractions into a list of decimals
for i in range(len(fraction_numerator_list)):
    converted_fraction_list.append(float(fraction_numerator_list[i])/float(fraction_denominator_list[i]))

current_fraction_list = [0.0,0.0,0.0,0.0,0.0]

sorted_fraction_list = []

#output for the number list
first_fraction_output = widgets.HTMLMath(
    value=r"<font size='6'><sup>3</sup>&frasl;<sub>5</sub></font>",
)
second_fraction_output = widgets.HTMLMath(
    value=r"<font size='6'><sup>9</sup>&frasl;<sub>14</sub></font>",
)
third_fraction_output = widgets.HTMLMath(
    value=r"<font size='6'><sup>2</sup>&frasl;<sub>8</sub></font>",
)
fourth_fraction_output = widgets.HTMLMath(
    value=r"<font size='6'><sup>5</sup>&frasl;<sub>9</sub></font>",
)
fifth_fraction_output = widgets.HTMLMath(
    value=r"<font size='6'><sup>7</sup>&frasl;<sub>11</sub></font>",
)

fraction_output_list = [first_fraction_output, second_fraction_output, third_fraction_output, fourth_fraction_output, fifth_fraction_output]

#output for the list picked by the reader
first_choice_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
second_choice_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
third_choice_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
fourth_choice_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
fifth_choice_output3 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)

output_choice_list3 = [first_choice_output3, second_choice_output3, third_choice_output3, fourth_choice_output3, fifth_choice_output3]

error_output3 = widgets.HTML('') #output for whether a user has entered two numbers in the same position of the list

list_answer_output3 = widgets.HTML('') #output for whether the list was sorted correctly

#drop down position choices for the numbers the reader picks
first_choice3 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
second_choice3 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
third_choice3 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fourth_choice3 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fifth_choice3 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)

choice_list3 = [first_choice3, second_choice3, third_choice3, fourth_choice3, fifth_choice3]

#buttons shown in the widget
new_list_button3 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

submit_button3 = widgets.Button(
    value=False,
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Submit the answer',
    continuous_update=True
)

show_list_button3 = widgets.Button(
    value=False,
    description='Show Current List',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show the current list the reader has selected',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
for i in range(len(choice_list3)):
    choice_list3[i].layout.width = '150px'

for i in range(len(output_choice_list3)):
    output_choice_list3[i].layout.width = '155px'
    output_choice_list3[i].layout.margin = '10px 0px 10px 0px'
    
for i in range(len(fraction_output_list)):
    fraction_output_list[i].layout.margin = '10px 0px 10px 0px'


new_list_button3.layout.margin = '10px 0px 0px 800px'
show_list_button3.layout.margin = '10px 0px 0px 800px'

#The layout and design of the widgets
position_one_widget3 = widgets.VBox(children=[first_fraction_output, first_choice3])
position_two_widget3 = widgets.VBox(children=[second_fraction_output, second_choice3])
position_three_widget3 = widgets.VBox(children=[third_fraction_output, third_choice3])
position_four_widget3 = widgets.VBox(children=[fourth_fraction_output, fourth_choice3])
position_five_widget3 = widgets.VBox(children=[fifth_fraction_output, fifth_choice3])

position_widget3 = widgets.HBox(children=[position_one_widget3, position_two_widget3, position_three_widget3, position_four_widget3, position_five_widget3])
choice_widget3 = widgets.HBox(children=[first_choice_output3, second_choice_output3, third_choice_output3, fourth_choice_output3, fifth_choice_output3])

display_list_widget3 = widgets.VBox(children=[new_list_button3, position_widget3, submit_button3, list_answer_output3, error_output3, show_list_button3, choice_widget3])

#Generate a new example list for the reader
def update_Example3(change):
    global fraction_numerator_list
    global fraction_denominator_list
    global converted_fraction_list
    global current_fraction_list
    
    #Generate a random list of fractions
    for i in range(len(fraction_numerator_list)):
        fraction_numerator_list[i] = random.randint(1,20)
        fraction_denominator_list[i] = random.randint(1,20)
    
    #Convert the fraction list to a decimal list
    for i in range(len(fraction_numerator_list)):
        converted_fraction_list[i] = float(fraction_numerator_list[i])/float(fraction_denominator_list[i])
    
    #Set the output value based on the random list
    for i in range(len(fraction_output_list)):
        fraction_output_list[i].value = r"<font size='6'><sup>" + str(fraction_numerator_list[i]) + "</sup>&frasl;<sub>" + str(fraction_denominator_list[i]) + "</sub></font>"
    
    #Set the list choices to null
    for i in range(len(choice_list3)):
        choice_list3[i].value = 0
    
    display_List3(True) #display the current selected list by the reader
    
    #Set the current selected list to null
    for i in range(len(fraction_numerator_list)):
        current_fraction_list[i] = 0.0

#Display the current selected list by the reader
def display_List3(change):
    list_answer_output3.value = ''
    
    #Erase the current displayed list
    for i in range(len(output_choice_list3)):
        output_choice_list3[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list3)):
        for j in range(len(output_choice_list3)):
            if(choice_list3[i].value == (j+1)):
                output_choice_list3[j].value = fraction_output_list[i].value

#Sorts the random list by looping through pulling out the highest number each time
def sort_list3():
    global converted_fraction_list
    global sorted_fraction_list
    
    del sorted_fraction_list[:]
    temp_list = converted_fraction_list[:]
    
    for j in range(len(temp_list)):
        highest_number = temp_list[0]
    
        for i in range(len(temp_list)):
            if (highest_number < temp_list[i]):
                highest_number = temp_list[i]
        
        sorted_fraction_list.insert(0, highest_number)
        
        temp_list.remove(highest_number)

#Compares the current list selected by the reader to the sorted list
def check_Answer3(change):
    global converted_fraction_list
    global current_fraction_list
    global sorted_fraction_list
    
    sort_list3()
    
    #empty the current list before setting it
    for i in range(len(converted_fraction_list)):
        current_fraction_list[i] = 0.0
    
    #set the list selected by the reader to the current list
    for i in range(len(choice_list3)):
        if (not(choice_list3[i].value == 0.0)):
            current_fraction_list[(choice_list3[i].value-1)] = converted_fraction_list[i]
    
    #compare the two lists
    if (current_fraction_list == sorted_fraction_list):
        list_answer_output3.value = 'Correct! You have sorted the list.'
    else:
        list_answer_output3.value = 'Incorrect. The list is not sorted.'

    #Erase the current displayed list
    for i in range(len(output_choice_list3)):
        output_choice_list3[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list3)):
        for j in range(len(output_choice_list3)):
            if(choice_list3[i].value == (j+1)):
                output_choice_list3[j].value = fraction_output_list[i].value
    
    for i in range(len(current_fraction_list)):
        if(current_fraction_list[i] == sorted_fraction_list[i]):
            output_choice_list3[i].value = '<font size="5" color="lime">' + output_choice_list3[i].value +  '</font>'
        else:
            output_choice_list3[i].value = '<font size="5" color="red">' + output_choice_list3[i].value +  '</font>'    

    
#checks to see if the user has enter two or more numbers in the same position
def check_Error3(change):
    error = False
    
    for i in range(len(choice_list3)):
        if(not(choice_list3[i].value == 0)):
            for j in range(len(choice_list3)-(i+1)):
                if(choice_list3[i].value == choice_list3[j+i+1].value):
                    error_output3.value = 'ERROR: You have two or more numbers in the same position!'
                    error = True
                    break
        if(error):
            break
    
    if(not(error)):
        error_output3.value = ''
        

#Call the function when the button has been clicked 
new_list_button3.on_click(update_Example3)

show_list_button3.on_click(display_List3)

submit_button3.on_click(check_Answer3)

first_choice3.observe(check_Error3, names='value')
second_choice3.observe(check_Error3, names='value')
third_choice3.observe(check_Error3, names='value')
fourth_choice3.observe(check_Error3, names='value')
fifth_choice3.observe(check_Error3, names='value')

#display the example widget
display_list_widget3

#### 4. Mixed List

#Random list of numbers and a list that will be used for the sorted numbers
mixed_list = [3.23,9,2,5.392,7]
mixed_denominator_list = [1,1,7,1,1]
number_type_list = [2,1,3,2,1] #

converted_mixed_list = []

#Convert the fractions into a list of decimals
for i in range(len(mixed_list)):
    converted_mixed_list.append(float(mixed_list[i])/float(mixed_denominator_list[i]))

current_mixed_list = [0.0,0.0,0.0,0.0,0.0]

sorted_mixed_list = []

#output for the number list
first_output = widgets.HTMLMath(
    value=r"<font size='5'>3.23</font>",
)
second_output = widgets.HTMLMath(
    value=r"<font size='5'>9</font>",
)
third_output = widgets.HTMLMath(
    value=r"<font size='5'><sup>2</sup>&frasl;<sub>7</sub></font>",
)
fourth_output = widgets.HTMLMath(
    value=r"<font size='5'>5.392</font>",
)
fifth_output = widgets.HTMLMath(
    value=r"<font size='5'>7</font>",
)

output_list = [first_output, second_output, third_output, fourth_output, fifth_output]

#output for the list picked by the reader
first_choice_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
second_choice_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
third_choice_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
fourth_choice_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)
fifth_choice_output4 = widgets.HTMLMath(
    value='<font size="6">  </font>',
)

output_choice_list4 = [first_choice_output4, second_choice_output4, third_choice_output4, fourth_choice_output4, fifth_choice_output4]

error_output4 = widgets.HTML('') #output for whether a user has entered two numbers in the same position of the list

list_answer_output4 = widgets.HTML('') #output for whether the list was sorted correctly

#drop down position choices for the numbers the reader picks
first_choice4 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
second_choice4 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
third_choice4 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fourth_choice4 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)
fifth_choice4 = widgets.Dropdown(
    options={' ':0,'Position One': 1, 'Position Two': 2, 'Position Three': 3, 'Position Four': 4, 'Position Five': 5},
    value=0,
    description='',
)

choice_list4 = [first_choice4, second_choice4, third_choice4, fourth_choice4, fifth_choice4]

#buttons shown in the widget
new_list_button4 = widgets.Button(
    value=False,
    description='New Example',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Generate a new exmaple',
    continuous_update=True
)

submit_button4 = widgets.Button(
    value=False,
    description='Submit Answer',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Submit the answer',
    continuous_update=True
)

show_list_button4 = widgets.Button(
    value=False,
    description='Show Current List',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show the current list the reader has selected',
    continuous_update=True
)

#Layout and styling for the objects used in the widget
for i in range(len(choice_list4)):
    choice_list4[i].layout.width = '150px'

for i in range(len(output_choice_list4)):
    output_choice_list4[i].layout.width = '155px'
    output_choice_list4[i].layout.margin = '10px 0px 10px 0px'
    
for i in range(len(output_list)):
    output_list[i].layout.margin = '10px 0px 10px 0px'

new_list_button4.layout.margin = '10px 0px 0px 800px'
show_list_button4.layout.margin = '10px 0px 0px 800px'

#The layout and design of the widgets
position_one_widget4 = widgets.VBox(children=[first_output, first_choice4])
position_two_widget4 = widgets.VBox(children=[second_output, second_choice4])
position_three_widget4 = widgets.VBox(children=[third_output, third_choice4])
position_four_widget4 = widgets.VBox(children=[fourth_output, fourth_choice4])
position_five_widget4 = widgets.VBox(children=[fifth_output, fifth_choice4])

position_widget4 = widgets.HBox(children=[position_one_widget4, position_two_widget4, position_three_widget4, position_four_widget4, position_five_widget4])
choice_widget4 = widgets.HBox(children=[first_choice_output4, second_choice_output4, third_choice_output4, fourth_choice_output4, fifth_choice_output4])

display_list_widget4 = widgets.VBox(children=[new_list_button4, position_widget4, submit_button4, list_answer_output4, error_output4, show_list_button4, choice_widget4])

#Generate a new example list for the reader
def update_Example4(change):
    global mixed_list
    global mixed_denominator_list
    global converted_mixed_list
    global current_mixed_list
    global number_type_list
    
    #Generate a random list of number types
    for i in range(len(mixed_list)):
        number_type_list[i] = random.randint(1,3)
        mixed_denominator_list[i] = 1
    
    #Generate a random list of numbers based on the corresponding number type 
    for i in range(len(mixed_list)):
        if (number_type_list[i] == 1):
            mixed_list[i] = random.randint(1,20)
        elif (number_type_list[i] == 2):
            mixed_list[i] = round(random.uniform(0,15), 3)
            mixed_list[i] = round(mixed_list[i], 3)
        elif (number_type_list[i] == 3):
            mixed_list[i] = random.randint(1,20)
            mixed_denominator_list[i] = random.randint(1,20)
    
    #Convert the random list to a decimal list
    for i in range(len(mixed_list)):
        converted_mixed_list[i] = float(mixed_list[i])/float(mixed_denominator_list[i])
    
    #Set the output value based on the random list and corresponding number type 
    for i in range(len(output_list)):
        if (number_type_list[i] == 1):
            output_list[i].value = '<font size="5"> ' + str(mixed_list[i]) + ' </font>'
        elif (number_type_list[i] == 2):
            output_list[i].value = '<font size="5"> ' + str(mixed_list[i]) + ' </font>'
        elif (number_type_list[i] == 3):
            output_list[i].value = r"<font size='5'><sup>" + str(mixed_list[i]) + "</sup>&frasl;<sub>" + str(mixed_denominator_list[i]) + "</sub></font>"
    
    #Set the list choices to null
    for i in range(len(choice_list4)):
        choice_list4[i].value = 0
    
    display_List4(True) #display the current selected list by the reader
    
    #Set the current selected list to null
    for i in range(len(mixed_list)):
        current_mixed_list[i] = 0.0

#Display the current selected list by the reader
def display_List4(change):
    list_answer_output4.value = ''
    
    #Erase the current displayed list
    for i in range(len(output_choice_list4)):
        output_choice_list4[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list4)):
        for j in range(len(output_choice_list4)):
            if(choice_list4[i].value == (j+1)):
                output_choice_list4[j].value = output_list[i].value

#Sorts the random list by looping through pulling out the highest number each time
def sort_list4():
    global converted_mixed_list
    global sorted_mixed_list
    
    del sorted_mixed_list[:]
    temp_list = converted_mixed_list[:]
    
    for j in range(len(temp_list)):
        highest_number = temp_list[0]
    
        for i in range(len(temp_list)):
            if (highest_number < temp_list[i]):
                highest_number = temp_list[i]
        
        sorted_mixed_list.insert(0, highest_number)
        
        temp_list.remove(highest_number)

#Compares the current list selected by the reader to the sorted list
def check_Answer4(change):
    global converted_mixed_list
    global current_mixed_list
    global sorted_mixed_list
    
    sort_list4()
    
    #empty the current list before setting it
    for i in range(len(converted_mixed_list)):
        current_mixed_list[i] = 0.0
    
    #set the list selected by the reader to the current list
    for i in range(len(choice_list4)):
        if (not(choice_list4[i].value == 0.0)):
            current_mixed_list[(choice_list4[i].value-1)] = converted_mixed_list[i]
    
    #compare the two lists
    if (current_mixed_list == sorted_mixed_list):
        list_answer_output4.value = 'Correct! You have sorted the list.'
    else:
        list_answer_output4.value = 'Incorrect. The list is not sorted.'

    #Erase the current displayed list
    for i in range(len(output_choice_list4)):
        output_choice_list4[i].value = ''
    
    #displayed the list selected by the reader
    for i in range(len(choice_list4)):
        for j in range(len(output_choice_list4)):
            if(choice_list4[i].value == (j+1)):
                output_choice_list4[j].value = output_list[i].value
    
    for i in range(len(current_mixed_list)):
        if(current_mixed_list[i] == sorted_mixed_list[i]):
            output_choice_list4[i].value = '<font size="5" color="lime">' + output_choice_list4[i].value +  '</font>'
        else:
            output_choice_list4[i].value = '<font size="5" color="red">' + output_choice_list4[i].value +  '</font>'
        
#checks to see if the user has enter two or more numbers in the same position
def check_Error4(change):
    error = False
    
    for i in range(len(choice_list4)):
        if(not(choice_list4[i].value == 0)):
            for j in range(len(choice_list4)-(i+1)):
                if(choice_list4[i].value == choice_list4[j+i+1].value):
                    error_output4.value = 'ERROR: You have two or more numbers in the same position!'
                    error = True
                    break
        if(error):
            break
    
    if(not(error)):
        error_output4.value = ''
        
        
#Call the function when the button has been clicked 
new_list_button4.on_click(update_Example4)

show_list_button4.on_click(display_List4)

submit_button4.on_click(check_Answer4)

first_choice4.observe(check_Error4, names='value')
second_choice4.observe(check_Error4, names='value')
third_choice4.observe(check_Error4, names='value')
fourth_choice4.observe(check_Error4, names='value')
fifth_choice4.observe(check_Error4, names='value')

#display the example widget
display_list_widget4

<a name="Conclusion"></a>
## Conclusion

In this notebook the reader will have gained sufficient knowledge to be able to compare whole numbers, decimals and fractions to themselves and each other. The reader will have also learnt how to sort a list of whole numbers, decimal numbers, or fractions as well as sorting a mixed list of those number types. There are interactive examples for comparing two numbers as well as examples for sorting a list of 5 numbers. The reader has the option to generate as many examples as they want to ensure a complete understanding of the subject matter by them. If the reader has gone through this notebook and completed multiple examples they should obtain a sufficient understanding of comparing and order whole numbers, decimals and fractions.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)