![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-1.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 1

*This project is also available as a single notebook file [here](./CALM-moving-out.ipynb)*

📘Imagine that you are in your early twenties and it is time to move out of your family home. You work 40 hours per week and your wage is $15.00 per hour (gross income, meaning before deductions).

You will be required to calculate your net income and manage financial resources effectively.

You may choose to live with a roommate. If you choose to live with a roommate and share rent, you must each complete and hand in a separate assignment.

You will use the internet for all the information required to complete this project. However, you may want to also refer to flyers to find prices for food and household items.

### Technology
This project uses Jupyter notebooks, which are documents that contain formatted text and computer code (Python code in this case). This will allow you to do calculations much easier, and without a calculator.

The text and code blocks are called "cells", this is a *Markdown* (text) cell.

Cells that contain a pencil emoji (✏️) are ones you should edit. Cells with a book emoji (e.g. 📘) are for you to read (or `Run`) without editing.

#📘This is a code cell.
# Run the code by selecting this cell then clicking on the  ►Run  button in the toolbar at the top.

2 + 3

#📘This is another code cell for you to run.
# Every line that starts with a  #  character is ignored when the computer runs the code

firstNumber = 2
secondNumber = 3
product = firstNumber * secondNumber
print(product)

📘That's the basics of a Jupyter notebook, if you want to learn more and Jupyter [click here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).

For now, though, let's get on with your CALM assignment.

## Part 1 - Personal Profile

📘Complete these questions based on what your hope of plan to do with your life. Once you have answered all of the questions in the code cell below, run the cell using the `Run` button on the tool bar and it will store your answers in a text file.

%%writefile moving_out_1.txt
✏️
My name is 
1. I will move out of my family home at the age of 
2. My educational path will be 
3. My occupation or job at that time will be 
4. I expect to take home $      each month.
5. I (will / will not) be married sometime in my twenties.
6. By the age of 30 I will likely have     children.
7. I (will / will not) buy a home sometime in my twenties.
8. My home or living accommodations will be described as
9. I will be living in or near the city/town of 
10. A vehicle I would like to drive when I am in my twenties is
11. Other things I own will be
    1. 
    2. 
    3. 
12. I (will / will not) plan to travel in my twenties.
13. If I plan to travel, some of my vacations will be
    1. 
    2. 
    3. 
14. My major accomplishments or bucket list items in my twenties will be
    1. 
    2. 
    3. 


📘`Run` the next cell to check that your answers have been stored in a file.

#📘 Run this cell to check that your file contains your answers.
# If you get an error, make sure you have run the code cell above.
with open('moving_out_1.txt', 'r') as file:
    print(file.read())

📘You have now completed this section. Proceed to [section 2](./CALM-moving-out-2.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)