![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/BudgetAndBankingAssignment/budget-and-banking-assignment.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

# Modules

import string
import numpy as np
import pandas as pd
import qgrid as q
import matplotlib.pyplot as plt

# Widgets & Display modules, etc..

from ipywidgets import widgets as w
from ipywidgets import Button, Layout
from IPython.display import display, Javascript, Markdown, HTML

# grid features for interactive grids 

grid_features = { 'fullWidthRows': True,
                  'syncColumnCellResize': True,
                  'forceFitColumns': True,
                  'rowHeight': 40,
                  'enableColumnReorder': True,
                  'enableTextSelectionOnCells': True,
                  'editable': True,
                  'filterable': False,
                  'sortable': False,
                  'highlightSelectedRow': True}

def rerun_cell( b ):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))    

def check_answers(series_input,answer_list):
    
    # convert valid answer list to string format 
    
    valid_answers = ""
    
    for item in answer_list:
        
        valid_answers = valid_answers + item + ","
        
    valid_answers = valid_answers[:len(valid_answers)-1]
    
    # compare student's answers to answer list
        
    for entry in series_input:
        
        if(entry != '' and entry not in answer_list):
            
            # display(Markdown("Some of your inputs are invalid. Please enter valid inputs from the following: ", valid_answers))
            
            return 0
        
    return 1

name_text = w.Textarea( value='', placeholder='STUDENT NAME', description='', disabled=False , layout=Layout(width='30%', height='32.5px') )
date_text = w.Textarea( value='', placeholder='DATE', description='', disabled=False , layout=Layout(width='30%', height='32.5px') )
profile_button = w.Button(button_style='info',description="Save", layout=Layout(width='15%', height='30px'))

display(name_text)
display(date_text)
display(profile_button)

profile_button.on_click( rerun_cell ) 

name = name_text.value
date = date_text.value

name_saved = False
date_saved = False

if(name != ''):
    
    name_text.close()
    display(Markdown("### Student Name: $\hspace{1.5cm}$"+ name ))
    name_saved = True
    
if(date != ''):
    
    date_text.close()
    display(Markdown("### $\hspace{2.15cm}$Date: $\hspace{1.5cm}$"+ date ))
    date_saved = True
    
if(name_saved == True and date_saved == True):
    
    profile_button.close()

# Budget and Banking

## Assignment Lesson 1

answers_recorded = 0
q1_answered = 0
q2_answered = 0
q3a_answered = 0
q3b_answered = 0
q3c_answered = 0
q3d_answered = 0

For question 1 and 2, choose the best answer.

**Question 1.** A good reason for preparing a budget

if(q1_answered == 1):
    
    q1_answered += 1
    q1_student_answer = q1_choices.value
    correct_answer = 'd.) All the above are good reasons for preparing a budget'
    
    if(q1_student_answer == correct_answer):
        
        display(Markdown("### You answered: "))
        display(Markdown(q1_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q1_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
        
else:
    
    # Question 1 Answer Choices

    choice_1 = 'a.) Running out of money each month'
    choice_2 = 'b.) To reduce debt'
    choice_3 = 'c.) To save for something special'
    choice_4 = 'd.) All the above are good reasons for preparing a budget'

    answer_choices = [ choice_1,choice_2,choice_3,choice_4 ]

    # Question 1 choices widget 

    q1_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q1_choices)

q1_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q1_choices.close()
    
if(q1_answered >= 2):
    
    q1_button.close()
    
else:
    
    q1_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q1_button.on_click( record_answer ) 
    display(q1_button)

**Question 2.** Which equation best describes gross and net pay?

if(q2_answered == 1):
    
    q2_answered += 1
    q2_student_answer = q2_choices.value
    correct_answer = 'b.) Net Pay = Gross Pay - Deductions'
    
    if(q2_student_answer == correct_answer):

        display(Markdown("### You answered: "))
        display(Markdown(q2_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q2_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
    
else:

    # Question 2 Answer Choices

    choice_1 = 'a.) Gross Pay = Net Pay - Deductions'
    choice_2 = 'b.) Net Pay = Gross Pay - Deductions'
    choice_3 = 'c.) Gross Pay = Net Pay ÷ Deductions'
    choice_4 = 'd.) Net Pay = Gross Pay ÷ Deductions'

    answer_choices = [ choice_1,choice_2,choice_3,choice_4 ]

    q2_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q2_choices)

q2_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q2_choices.close()
    
if(q2_answered >= 2):
    
    q2_button.close()
    
else:
    
    q2_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q2_button.on_click( record_answer ) 
    display(q2_button)

**Question 3.** Label the following incomes as **fixed** or **variable**. Explain reasons for each.

$\hspace{0.35cm}$**a.)** Lloyd earns $50.00 for every set of knife he sells.

if(q3a_answered == 1):
    
    q3a_answered += 1
    q3a_student_answer = q3a_choices.value
    correct_answer = 'Variable'

    if(q3a_student_answer == correct_answer):
        
        display(Markdown("### You answered: "))
        display(Markdown(q3a_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q3a_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
    
else:

    # Question 3.a Answer Choices

    choice_1 = 'Fixed'
    choice_2 = 'Variable'

    answer_choices = [ choice_1,choice_2 ]

    q3a_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q3a_choices)

q3a_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q3a_choices.close()
    
if(q3a_answered >= 2):
    
    q3a_button.close()
    
else:
    
    q3a_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q3a_button.on_click( record_answer ) 
    display(q3a_button)

$\hspace{0.35cm}$**b.)** Each month, Florence is paid 4.5% commission on her first $1,500.00 in sales. If she makes more than this, Florence is paid 6% in commission.

if(q3b_answered == 1):
    
    q3b_answered += 1
    q3b_student_answer = q3b_choices.value
    correct_answer = 'Variable'
    
    if(q3b_student_answer == correct_answer):
        
        display(Markdown("### You answered: "))
        display(Markdown(q3b_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q3b_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
    
else:

    # Question 3.b Answer Choices

    choice_1 = 'Fixed'
    choice_2 = 'Variable'

    answer_choices = [ choice_1,choice_2 ]

    q3b_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q3b_choices)

q3b_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q3b_choices.close()
    
if(q3b_answered >= 2):
    
    q3b_button.close()
    
else:
    
    q3b_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q3b_button.on_click( record_answer ) 
    display(q3b_button)

$\hspace{0.35cm}$**c.)** Corinne works 40 hours a week at $17.00 an hour. She is paid bi-weekly (every two weeks).

if(q3c_answered == 1):
    
    q3c_answered += 1
    q3c_student_answer = q3c_choices.value
    correct_answer = 'Fixed'
    
    if(q3c_student_answer == correct_answer):
        
        display(Markdown("### You answered: "))
        display(Markdown(q3c_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q3c_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
    
else:

    # Question 3.c Answer Choices

    choice_1 = 'Fixed'
    choice_2 = 'Variable'

    answer_choices = [ choice_1,choice_2 ]

    q3c_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q3c_choices)

q3c_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q3c_choices.close()
    
if(q3c_answered >= 2):
    
    q3c_button.close()
    
else:
    
    q3c_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q3c_button.on_click( record_answer ) 
    display(q3c_button)

$\hspace{0.35cm}$**d.)** Gord earns a salary of $3,000.00 each month.

if(q3d_answered == 1):
    
    q3d_answered += 1
    q3d_student_answer = q3d_choices.value
    correct_answer = 'Fixed'
    
    if(q3d_student_answer == correct_answer):
        
        display(Markdown("### You answered: "))
        display(Markdown(q3d_student_answer))
        
        display(Markdown("This is correct!"))
        
    else:
        
        display(Markdown("### You answered: "))
        display(Markdown(q3d_student_answer))

        display(Markdown("This is incorrect."))
        display(Markdown("### Correct answer: "))
        display(Markdown(correct_answer))
    
else:

    # Question 3.d Answer Choices

    choice_1 = 'Fixed'
    choice_2 = 'Variable'

    answer_choices = [ choice_1,choice_2 ]

    q3d_choices = w.RadioButtons( options=answer_choices , description="" , disabled=False , layout=Layout(width='100%'))
    display(q3d_choices)

q3d_answered += 1

def record_answer(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range( IPython.notebook.get_selected_index()-1 , IPython.notebook.get_selected_index()+1) '))    
    q3d_choices.close()
    
if(q3d_answered >= 2):
    
    q3d_button.close()
    
else:
    
    q3d_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))
    q3d_button.on_click( record_answer ) 
    display(q3d_button)

4) Lian works in a retail store $35$ hours a week. She is paid $\$12.75$ an hour bi-weekly (every two weeks). Her last paycheque had a deduction of $\$71.19$ for Income Tax, $\$35.82$ for CPP, and $\$14.85$ for EI.

$\hspace{1.5cm}$a.) Determine Lian's gross pay for two weeks.

**Write your calculations below.** 
* Valid inputs: Numbers and decimals. 
* Valid operations: `+,-,*` for addition, subtraction, and multiplication, respectively.

**Example input:** `40 * 10 * 2 + 30`

q4a_text = w.Textarea( value='', placeholder='Your calculations for Exercise 4.a.', description='', disabled=False , layout=Layout(width='100%', height='30px') )
q4a_button = w.Button(button_style='info',description="Calculate", layout=Layout(width='15%', height='30px'))

display(q4a_text)
display(q4a_button)

q4a_button.on_click( rerun_cell ) 

# Obtain user's input

q4a_input = q4a_text.value

# Define the valid character inputs for this exercise

numbers = '0123456789'
operations = '+-*'
others = ' .'
valid_inputs = numbers + operations + others

# Check if every character in user's string input is valid

user_input_valid = all( ch in valid_inputs for ch in q4a_input)

# Check for correctness of user's calculation

if(q4a_input != '' and user_input_valid == True):
    
    user_answer = eval(q4a_input)
    
    display(Markdown("### You answered: "))
    display(Markdown("$\$"+str(round(user_answer,2))+"$"))
    
    if(user_answer == 892.50):
    
        display(Markdown("Your calculation is correct!"))

        q4a_button.close()
        q4a_text.close()
        
    else:
        
        display(Markdown("Your calculation is incorrect. Try again."))
  
if(q4a_input != '' and user_input_valid == False):
    
    display(Markdown("Your answer contains invalid inputs or operations."))

$\hspace{1.5cm}$b.) Determine Lian's net pay for two weeks. 

q4b_text = w.Textarea( value='', placeholder='Your calculations for Exercise 4.b.', description='', disabled=False , layout=Layout(width='100%', height='30px') )
q4b_button = w.Button(button_style='info',description="Calculate", layout=Layout(width='15%', height='30px'))

display(q4b_text)
display(q4b_button)

q4b_button.on_click( rerun_cell ) 

# Obtain user's input

q4b_input = q4b_text.value

# Define the valid character inputs for this exercise

numbers = '0123456789'
operations = '+-*'
others = ' .'
valid_inputs = numbers + operations + others

# Check if every character in user's string input is valid

user_input_valid = all( ch in valid_inputs for ch in q4a_input)

# Check for correctness of user's calculation

if(q4b_input != '' and user_input_valid == True):
    
    user_answer = round(eval(q4b_input),2)
    correct_answer = round(eval("892.5 - 71.19 - 35.82 - 14.85"),2)
    
    display(Markdown("### You answered: "))
    display(Markdown("$\$"+str(round(user_answer,2))+"$"))
    
    if(user_answer == correct_answer):

        q4b_button.close()
        q4b_text.close()
        
        display(Markdown("Your calculation is correct!"))
        
    else:
        
        display(Markdown("Your calculation is incorrect. Try again."))    

if(q4b_input != '' and user_input_valid == False):
    
    display(Markdown("Your answer contains invalid inputs or operations."))

---

<h1 align='center'>Character Section Lesson</h1>

To conclude the Chapter 1 Assignment, you will be constructing a conservative budget and answering a "what if" question. You will be marked using a rubric that is located on the last page of the booklet.

### Character Background

Emma, a high school student working at a local grocery store as a cashier.

### Personal Background

Emma is 16 years old, in grade 11 and living at home with her parents. She plays soccer and rugby. Emma is the bass player in a band. Currently, she is using an old bass guitar that her dad played in the 1980s, and she would like to buy her own. Her goal is to buy it in five months because the band has a big gig coming up in six months. The new bass costs $828.45 including GST.


### Salary


Emma works part-time at Gobey’s Grocery. She is paid a biweekly amount of $321.13.

Emma babysits occasionally for her neighbours for $10.00 an hour. Several of Emma's babysitting client pay her by cheque, and Emma puts the money directly into her bank account.

### Expenses

Emma’s parents have encouraged her to save for post-secondary schooling. To achieve this, Emma and her parents set up a direct withdrawal from her bank account of $40.00 a paycheque into an RESP account. Emma pays for her own transit pass, which she uses to travel around the city. Emma is very thrifty and creative, so she chooses to shop for clothing at local second-hand stores. Emma’s position as the bass player in a local band requires her to maintain her instrument and provide her own sound equipment.

Emma downloads the bank record of her spending during two months (February and March).

### Notes

* The credit column contains all income (part-time job and babysitting).

* The debit column contains all expenses that Emma has paid.

* An automatic withdrawal of $40.00 each paycheque goes into an RESP account.

* In February, Emma paid rugby fees with cash, which are $180.00.

* At the end of March, Emmas’ soccer team went to an overnight tournament for which she paid $160.00 in cash as her portion of the hotel room.

<h2 align='center'>Character Section Lesson Exercises</h2>

**Question 1.** List **at least two** reasons Emma might want to prepare a budget for herself.

emma1_text = w.Textarea( value='', placeholder='Write your answer here for Question 1.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
emma1_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(emma1_text)
display(emma1_button)

emma1_button.on_click( rerun_cell ) 

emma1_input = emma1_text.value

if(emma1_input != ''):
    
    emma1_text.close()
    emma1_button.close()
    display(Markdown("### Your answer for Question 1:"))
    display(Markdown(emma1_input))

**Question 2.** Determine Emma’s net income for the month of February and March. Her bank statements are displayed below.

# Prepare dataframes for Emma's February & March Transactions

entry_types = {'Debit ($)': str , 'Credit ($)' : str}

february_transactions_df = pd.read_csv('./data/februarytransactions.csv',converters=entry_types)
february_transactions_df.set_index('Date',inplace=True)
february_transactions_df[['Debit ($)','Credit ($)']] = february_transactions_df[['Debit ($)','Credit ($)']].replace(np.nan,"0.00")

march_transactions_df = pd.read_csv('./data/marchtransactions.csv',converters=entry_types)
march_transactions_df.set_index('Date',inplace=True)
march_transactions_df[['Debit ($)','Credit ($)']] = march_transactions_df[['Debit ($)','Credit ($)']].replace(np.nan,"0.00")

# Control grid features

emma_grid_features = { 'fullWidthRows': True,
                  'syncColumnCellResize': True,
                  'forceFitColumns': True,
                  'rowHeight': 40,
                  'enableColumnReorder': True,
                  'enableTextSelectionOnCells': True,
                  'editable': False,
                  'filterable': False,
                  'sortable': False,
                  'highlightSelectedRow': True}

q_emma_feb = q.show_grid( february_transactions_df , grid_options = emma_grid_features ) 
q_emma_mar = q.show_grid( march_transactions_df , grid_options = emma_grid_features ) 

display(Markdown("<h2 align='center'>Emma's February Transactions</h2>"))

display(q_emma_feb)

**Write your calculations below.**
* Valid inputs: Numbers and decimals.
* Valid operations: `+` for addition.

**Example input:** `35 + 27.13 + 11.32`

feb_text = w.Textarea( value='', placeholder="Enter your calculation here to determine Emma's net income for the month of February. Hint: which column do Emma's income come from?", description='', disabled=False , layout=Layout(width='100%', height='30px') )
feb_button = w.Button(button_style='info',description="Calculate", layout=Layout(width='15%', height='30px'))

display(feb_text)
display(feb_button)

feb_button.on_click( rerun_cell ) 

# Obtain user's input

feb_input = feb_text.value

# Define the valid character inputs for this exercise

numbers = '0123456789'
operations = '+'
others = ' .'
valid_inputs = numbers + operations + others

# Check if every character in user's string input is valid

user_input_valid = all( ch in valid_inputs for ch in feb_input)

# Check for correctness of user's calculation

if(feb_input != '' and user_input_valid == True):
    
    user_answer = eval(feb_input)
    
    display(Markdown("### You answered: "))
    display(Markdown("$\$"+str(user_answer)+"$"))
    
    if(user_answer == 1042.26):
                
        feb_button.close()
        feb_text.close()
        
        display(Markdown("Your calculation is correct!"))
        
    else:
        
        display(Markdown("Your calculation is incorrect. Try again."))   

if(feb_input != '' and user_input_valid == False):
    
    display(Markdown("Your answer contains invalid inputs or operations."))

display(Markdown("<h2 align='center'>Emma's March Transactions</h2>"))

display(q_emma_mar)

**Write your calculations below.**
* Valid inputs: Numbers and decimals.
* Valid operations: `+` for addition.

**Example input:** `35 + 27.13 + 11.32`

mar_text = w.Textarea( value='', placeholder="Enter your calculation here to determine Emma's net income for the month of March. Hint: which column do Emma's income come from?", description='', disabled=False , layout=Layout(width='100%', height='30px') )
mar_button = w.Button(button_style='info',description="Calculate", layout=Layout(width='15%', height='30px'))

display(mar_text)
display(mar_button)

mar_button.on_click( rerun_cell ) 

# Obtain user's input

mar_input = mar_text.value

# Define the valid character inputs for this exercise

numbers = '0123456789'
operations = '+'
others = ' .'
valid_inputs = numbers + operations + others

# Check if every character in user's string input is valid

user_input_valid = all( ch in valid_inputs for ch in mar_input)

# Check for correctness of user's calculation

if(mar_input != '' and user_input_valid == True):
    
    user_answer = eval(mar_input)
    
    display(Markdown("### You answered: "))
    display(Markdown("$\$"+str(user_answer)+"$"))
    
    if(user_answer == 922.26):
        
        mar_button.close()
        mar_text.close()
        
        display(Markdown("Your calculation is correct!"))
        
    else:
        
        display(Markdown("Your calculation is incorrect. Try again."))     

if(mar_input != '' and user_input_valid == False):
    
    display(Markdown("Your answer contains invalid inputs or operations."))

**Question 3.** Categorize Emma’s income as fixed, variable or both. Explain.

emma3_text = w.Textarea( value='', placeholder='Write your answer here for Question 3.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
emma3_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(emma3_text)
display(emma3_button)

emma3_button.on_click( rerun_cell ) 

emma3_input = emma3_text.value

if(emma3_input != ''):
    
    emma3_text.close()
    emma3_button.close()
    display(Markdown("### Your answer for Question 3:"))
    display(Markdown(emma3_input))

<h2 align='center'>Interactive Exercise: Entering & Saving Spreadsheet Data</h2>

**Question 4.** By analyzing the bank statements for the two months, complete the following tables for each month.

$\hspace{0.35cm}$**a.)** For each row in the table, fill the **Expense Category** column with the appropriate expense label. The valid choices are listed below - write the associated upper case letter for each expense. Expand the **Description** column to see the expense entry.

**Categories: **

$$\text{(S) Savings, (U) Utilities, (C) Clothing, (E) Entertainment, (M) Miscellaneous, (P) Personal Care, (T) Transportation, (F) Food}$$

# Note to developers:
# 1. data in tables below obtained by converting relevant pages from Math20-3Unit1Key.pdf into .csv format.
# 2. this part of the interactive focuses on categorizing expenses

# Answer key for this lesson

feb_expenses_answer_key = ['S', 'T', 'F', 'U', 'F', 'F', 'F', 'C', 'E', 'S', 'F', 'F', 'E', 'M', 'M', 'F', 'F', 'M', 'M', 'C']
feb_fv_answer_key = ['V','V','V','V','F','F','F']

# Setting up the dataframe 

pd.options.display.max_rows = 50 

entry_types = {'Debit ($)': str , 'Balance ($)' : str}

february_df = pd.read_csv('./data/februarydebits.csv',converters=entry_types)
february_df.set_index('Transaction #',inplace=True)
february_df['Debit ($)'] = february_df['Debit ($)'].replace(np.nan,"0.00")
february_df['Expense Category'] = february_df['Expense Category'].replace(np.nan,"")

original_feb_df = february_df[['Date','Description','Debit ($)','Balance ($)']]

# Display interactive grid 1: categorizing expenses

q_february_df = q.show_grid( february_df , grid_options = grid_features )

# Recording answers

q4a_button = w.Button(button_style='info',description="Record Answers", layout=Layout(width='15%', height='30px'))

def record_spreadsheet(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+3)'))

display(q_february_df)
display(q4a_button)

q4a_button.on_click( record_spreadsheet )

# Recover entries

q4a_recover_button = w.Button(button_style='info',description="Reset all values", layout=Layout(width='15%', height='30px'))

def recover_entries(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+0)'))
    
display(q4a_recover_button)

q4a_recover_button.on_click( recover_entries )

# Obtain the changed dataframe

student_feb_df = q_february_df.get_changed_df()

# Check answers

answer_list = ['S','F','C','E','T','U','M']

answers_valid = check_answers(student_feb_df['Expense Category'],answer_list)

if(answers_valid == 0):
    
    display(Markdown("Some of your inputs are invalid. Please enter inputs from the following list: S,U,C,E,M,P,T,F"))


# Group the dataframe according to student's expense categories once student's answers are correct

if(answers_valid == 1):
    
    # Check if every entry matches the answer key
    
    student_answers = (student_feb_df['Expense Category'].values).tolist() 
    
    if( feb_expenses_answer_key == student_answers):
        
        display(Markdown("Your selections are correct!"))

        q4a_button.close()
        q4a_recover_button.close()
        q_february_df.close()
        
        q4a_grid_features = { 'fullWidthRows': True,
                          'syncColumnCellResize': True,
                          'forceFitColumns': True,
                          'rowHeight': 40,
                          'enableColumnReorder': True,
                          'enableTextSelectionOnCells': True,
                          'editable': False,
                          'filterable': False,
                          'sortable': False,
                          'highlightSelectedRow': True}
        
        student_q4a_df = q.show_grid( student_feb_df , grid_options = q4a_grid_features )
        
        display(student_q4a_df)
        
    else:
        
        display(Markdown("Some of your inputs are incorrect."))

$\hspace{0.35cm}$**b.)** Calculate the total of each expense category you used in (a). 

$\hspace{3cm}$This is done for you. Proceed to exercise (c).

q4b_df = pd.read_csv('./data/expensesum.csv')
q4b_df.set_index("Expense Category",inplace=True)
q_q4b_df = q.show_grid( q4b_df , grid_options = grid_features ) 
display(q_q4b_df)

$\hspace{0.35cm}$**c.)** For each category, determine whether it is **fixed** or **variable**. Enter F for fixed and V for variable.

# Setting up the dataframe 

fixed_or_var_df = pd.read_csv('./data/fixedorvar.csv')
fixed_or_var_df.set_index('Expense Category',inplace=True)
fixed_or_var_df['Fixed or Variable'] = fixed_or_var_df['Fixed or Variable'].replace(np.nan,"")

q_fixed_or_var_df = q.show_grid( fixed_or_var_df , grid_options = grid_features)

q4c_button = w.Button(button_style='info',description="Record Answers", layout=Layout(width='15%', height='30px'))

def record_spreadsheet(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+2)'))

display(q_fixed_or_var_df)
display(q4c_button)

q4c_button.on_click( record_spreadsheet )

# Obtain the changed dataframe

q4c_df = q_fixed_or_var_df.get_changed_df()

# Check answers

q4c_answer_list = ['V','F','V','F','V','V','V','V']
q4c_student_answer = (q4c_df['Fixed or Variable'].values).tolist()

def check_q4c(student_inputs):
    
    valid_inputs = 'VF'
    
    for entry in student_inputs:
        
        if(entry not in valid_inputs):
            
            display(Markdown("Please enter valid inputs only."))
            
            return False
        
        if(entry == ''):
            
            display(Markdown("Please fill all the entries in the spreadsheet above."))
            
            return False
        
    return True
        
if(check_q4c(q4c_student_answer) == True):
    
    if(q4c_student_answer == q4c_answer_list):
        
        display(Markdown("Your selections are correct!"))
        
        q4c_grid_features = { 'fullWidthRows': True,
                          'syncColumnCellResize': True,
                          'forceFitColumns': True,
                          'rowHeight': 40,
                          'enableColumnReorder': True,
                          'enableTextSelectionOnCells': True,
                          'editable': False,
                          'filterable': False,
                          'sortable': False,
                          'highlightSelectedRow': True}
        
        student_q4c_df = q.show_grid( q4c_df , grid_options = q4c_grid_features )
        
        q_fixed_or_var_df.close()
        
        display(student_q4c_df)
        
    else:
        
        display(Markdown("Some inputs are incorrect."))

**Question 5.** Construct a **monthly** conservative budget skeleton for Emma based upon her February and March data. To do this, compare the data for February and March and use the _highest_ expense amount for each category.

**Note: ** The **February Expense Data** and **March Expense Data** are given below.

entry_types = {'February Totals ($)': str , 'March Totals ($)' : str}

comparison_df = pd.read_csv('./data/expensecomparison.csv',converters = entry_types)
comparison_df.set_index('Expense Categories',inplace=True)
comparison_df['Highest Expense Amount ($)'] = comparison_df['Highest Expense Amount ($)'].replace(np.nan,"")

del comparison_df['Transaction #']

q_comparison_df = q.show_grid( comparison_df , grid_options = grid_features )

expense_button = w.Button(button_style='info',description="Record Answers", layout=Layout(width='15%', height='30px'))

def record_spreadsheet(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+3)'))    
    
display(q_comparison_df)
display(expense_button)

expense_button.on_click( record_spreadsheet )

# Recover entries

recover_button = w.Button(button_style='info',description="Reset all values", layout=Layout(width='15%', height='30px'))

def recover_entries(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+0)'))
    
display(recover_button)

recover_button.on_click( recover_entries )

# Obtain changed dataframe

student_comparison_df = q_comparison_df.get_changed_df()

# Answers 

correct_answers = ['80.00', '73.50', '91.95', '30.15', '189.45', '233.64', '206.00', '116.53']
student_answers = (student_comparison_df['Highest Expense Amount ($)'].values).tolist()

# Function to check if every entry is a valid input

def check_floats(input_array):
    
    valid_inputs = '0123456789.'
    
    for answer in input_array:
        
        current_user_input = all( ch in valid_inputs for ch in answer)
        
        if(current_user_input == False):
        
            return False
    
    return True

# Check if answer is correct

if(check_floats(student_answers) == False):
    
    display(Markdown("Please enter decimal numbers only."))
        
else:

    if(student_answers == correct_answers):

        display(Markdown("Your choices are correct!"))

        recover_button.close()
        expense_button.close()
        q_comparison_df.close()
      
        comparison_grid_features = { 'fullWidthRows': True,
                                  'syncColumnCellResize': True,
                                  'forceFitColumns': True,
                                  'rowHeight': 40,
                                  'enableColumnReorder': True,
                                  'enableTextSelectionOnCells': True,
                                  'editable': False,
                                  'filterable': False,
                                  'sortable': False,
                                  'highlightSelectedRow': True}
        
        student_comparison_df = q.show_grid( student_comparison_df , grid_options = comparison_grid_features )
        display(student_comparison_df)
        
    else:
        
        display(Markdown("Some of your entries are incorrect. Please fill them with the correct values. Make sure to write numbers in decimal form. Write 80.00 for 80, 206.00, etc."))

**Question 6.** If there is excess money, where should Emma put it? If there is not enough income for expenses, suggest how Emma can cover her expenses or reduce her expenses.

q6_text = w.Textarea( value='', placeholder='Write your answer here for Question 6.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
q6_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(q6_text)
display(q6_button)

q6_button.on_click( rerun_cell ) 

q6_input = q6_text.value

if(q6_input != ''):
    
    q6_text.close()
    q6_button.close()
    display(Markdown("### Your answer for question 6:"))
    display(Markdown(q6_input))

**Question 7.**

$\hspace{0.35cm}$**a.)** How much will Emma need to save each month to purchase a new base, in 5 months, that costs $\$828.45$ (including GST)?

q7a_text = w.Textarea( value='', placeholder='Write your answer here for Question 7.a.', description='', disabled=False , layout=Layout(width='100%', height='75px') )
q7a_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(q7a_text)
display(q7a_button)

q7a_button.on_click( rerun_cell ) 

q7a_input = q7a_text.value

if(q7a_input != ''):
    
    q7a_text.close()
    q7a_button.close()
    display(Markdown("### Your answer for question 7.a:"))
    display(Markdown(q7a_input))

$\hspace{0.35cm}$**b.)** Based upon her budget, will Emma be able to save enough? If not, modify her budget so that she can afford it. A new category has been added to show her savings for the bass.

**Note:** Income and expenses should be balanced at this point.

From the previous exercises, we saw that a conservative income for Emma was $\$922.26$. In this exercise, we want to create a budget amount in such a way that the sum of each category is exactly $\$922.26$.

# Prepare dataframes for Emma's February & March Transactions

ex_7b_df = pd.read_csv('./data/exercise7b.csv')
ex_7b_df[['Budgeted Amount ($)']] = ex_7b_df[['Budgeted Amount ($)']].replace(np.nan,"")
ex_7b_df.set_index('Category',inplace=True)

q_ex_7b = q.show_grid( ex_7b_df , grid_options = grid_features ) 

display(Markdown("<h2 align='center'>Emma's Modified Conservative Budget</h2>"))

display(q_ex_7b)

ex_7b_button = w.Button(button_style='info',description="Record Answers", layout=Layout(width='15%', height='30px'))

def record_spreadsheet(button_widget):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+3)'))    
    
display(ex_7b_button)

ex_7b_button.on_click( record_spreadsheet )

**Question 8.** Determine the percent of Emma’s income on each category. 

To calculate percentage of income for each category use the formula:

$$\text{Percent of Income} = \frac{\text{Amount Allotted for Expense}}{\text{Budgeted Income}}\times 100\%$$

**Note:** This part of the exercise is done for you and changes based on your inputs in exercise 7.b., the formula above is for your reference.

# Set up student inputs as a list

ex_7b_student_df = q_ex_7b.get_changed_df()
student_budget_input = ex_7b_student_df['Budgeted Amount ($)']
student_budget_col = (student_budget_input.values).tolist()

# Check if every entry is valid 

def check_ex_7b(student_inputs):

    valid_inputs = '0123456789. '

    for entry in student_inputs:

        for ch in entry:
            
            if(ch not in valid_inputs):
                
                display(Markdown("Please enter valid inputs only."))

                return False

    if(entry == ''):

        display(Markdown("Please fill all the entries in the spreadsheet above."))

        return False

    return True

# Check if student's budget matches the total income

valid_input = check_ex_7b(student_budget_col)

if(valid_input == True):
    
    # Convert every entry to float and get the sum
    
    budget_sum = 0
    
    for entry in student_budget_col:
        
        current_entry = eval(entry)
        budget_sum += current_entry
        
    # If the budget sum matches, then create the percentages chart 
    
    percentages_col = []
    
    if(budget_sum != 922.26): 
        
        display(Markdown("Your budget proposal does not total $922.26. Please try again."))
        
    else:
        
        for entry in student_budget_col:
            
            current_percent = round( eval(entry)/budget_sum , 4)
            percentages_col.append( round(current_percent*100,4) )
            
        indices = ['Savings (RESP)','Transportation','Utilities','Food','Clothing','Entertainment','Miscellaneous','Personal Care','Savings (Bass)']
            
        percentage_df = pd.DataFrame({'Percentage (%): ': percentages_col },index=indices)
        updated_ex_7b_student_df = pd.concat( [ex_7b_student_df,percentage_df] , axis = 1 )
        
        ex_7b_features = { 'fullWidthRows': True,
                          'syncColumnCellResize': True,
                          'forceFitColumns': True,
                          'rowHeight': 40,
                          'enableColumnReorder': True,
                          'enableTextSelectionOnCells': True,
                          'editable': False,
                          'filterable': False,
                          'sortable': False,
                          'highlightSelectedRow': True}
        
        q_ex_7b_updated = q.show_grid( updated_ex_7b_student_df , grid_options = ex_7b_features )
        
        display(Markdown("<h2 align='center'>Emma's Modified Budget Percentage Breakdown</h2>"))
        
        display(q_ex_7b_updated)

**Question 9.** Are there any categories that Emma is far above or far below the spending guidelines? How does being a high school student affect Emma’s consideration of the spending guidelines?

<img src="./images/spending_guidelines.jpg" alt="drawing" width="400px"/>


q9_text = w.Textarea( value='', placeholder='Write your answer here for Question 9', description='', disabled=False , layout=Layout(width='100%', height='75px') )
q9_button = w.Button(button_style='info',description="Record Answer", layout=Layout(width='15%', height='30px'))

display(q9_text)
display(q9_button)

q9_button.on_click( rerun_cell ) 

q9_input = q9_text.value

if(q9_input != ''):
    
    q9_text.close()
    q9_button.close()
    display(Markdown("### Your answer for question 9:"))
    display(Markdown(q9_input))

--- 
<h1 align='center'>Student Interactive Section</h1>

In this section, you will enter your own expense categories and see how your expense percentage breakdown compares to the spending guideline above.

# Create button and dropdown widget

number_of_cat = 13
dropdown_options = [ str(i+1) for i in range(number_of_cat) ] 
dropdown_widget = w.Dropdown( options = dropdown_options , value = '3' , description = 'Categories' , disabled=False )

categories_button = w.Button(button_style='info',description="Save", layout=Layout(width='15%', height='30px'))

# Display widgets

display(dropdown_widget)
display(categories_button)

categories_button.on_click( rerun_cell ) 

# Create dataframe

df_num_rows = int(dropdown_widget.value)
empty_list = [ '' for i in range(df_num_rows) ] 
category_list = [ i+1 for i in range(df_num_rows) ] 

# Set up data input for dataframe

df_dict = {'Category #': category_list, 'Budget ($)': empty_list , 'Expense Category': empty_list}

student_df = pd.DataFrame(data = df_dict)
student_df.set_index('Category #',inplace=True)

# Reorder column labels

student_df = student_df[['Expense Category','Budget ($)']]

# Set up & display as Qgrid

q_student_df = q.show_grid( student_df , grid_options = grid_features )
display(q_student_df)

# Create & display save entries widget button

save_student_entries_button = w.Button(button_style='info',description="Plot Pie Chart", layout=Layout(width='15%', height='30px'))
display(save_student_entries_button)

save_student_entries_button.on_click( rerun_cell ) 

# Convert qgrid to dataframe

student_updated_df = q_student_df.get_changed_df()

student_budget_col = student_updated_df['Budget ($)'].values.tolist()
student_labels_col = student_updated_df['Expense Category'].values.tolist()

# Check if a number if float

def isfloat(value):
    
    try:
        
        float(value)
        
        return True
    
    except ValueError:
        
        return False

# Function: Check for validity of budget column entries
# Input: Student's budget column values
# Output: Boolean, false if one of the entries is invalid

def check_budget_column(input_list):
    
    valid_inputs = '0123456789.'
    
    # Check if inputs are valid
    
    for entry in input_list:
        
        if( isfloat(entry) == False):
            
            return False
    
    return True

# Function: Calculate the percentage of each expense category
# Input: Student expense category lists and student budget column values
# Output: Percentages column 

def get_percentages(input_list):
    
    total = 0
    percentage_col = []
    
    # Obtain total
    
    for entry in input_list:
        
        entry = eval(entry)        
        total += entry
        
    # Obtain percentages
    
    for entry in input_list:
        
        entry = eval(entry)
        current_percentage = entry/total
        percentage_col.append( round(current_percentage*100,2) )
    
    return percentage_col

# If student input is valid, create a pie chart plot

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','darkseagreen','lightcyan','lightpink','coral','tan','slateblue','azure','tomato','lawngreen']

if(check_budget_column(student_budget_col) == True):
    
    student_values = get_percentages(student_budget_col)
    labels = student_labels_col
    
    plt.figure(figsize=(20,10))
    plt.rcParams['font.size'] = 20
    plt.title('Your Expense Category Percentage Breakdown',fontsize=25)
    plt.pie(student_values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=35)
    plt.axis('equal') 
    plt.show()
    
else:
    
    display(Markdown("Please enter decimal numbers only for the budget column"))

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)