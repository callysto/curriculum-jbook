![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-9.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 9
## Part 9 - Summary

🎒In this final notebook you will write some reflections and then collect all of your answers to submit to your teacher.

Make sure you have completed all of the activities, and run all of the cells even if they resulted in zero expenses. If you get any errors, read the error messages to determine what you may have missed.

#🎒Run this cell to calculate your total monthly expenses
import pandas as pd
import qgrid
%store -r
totalCostsValues = [transportationCost, 
                    monthlyFoodCost, 
                    monthlyHouseholdCost, 
                    monthlyClothingCost, 
                    monthlyGiftsCost, 
                    monthlyHealthCost, 
                    monthlyEntertainmentCost, 
                    monthlyEducationCost]
dfTotalCosts = pd.DataFrame({'Item': ['Transportation',
                                      'Food',
                                      'Household Items',
                                      'Clothing',
                                      'Gifts',
                                      'Health',
                                      'Entertainment',
                                      'Education'],
                            'Cost Per Month': totalCostsValues})

totalCostsPerMonth = pd.to_numeric(dfTotalCosts['Cost Per Month']).sum()
%store totalCostsPerMonth >>moving_out_11.txt
print('Your total expenses per month will be about $' + str('{:.2f}'.format(totalCostsPerMonth)) + '.')
print('This is about ' + str('{:.1f}'.format(totalCostsPerMonth / netIncome * 100)) + '% of your net income.')
dfTotalCosts

🎒Next, `Run` the following cell to display your one-time moving out expenses.

oneTimeExpenses = movingExpenses + fneCost
print(oneTimeExpenses)

🎒Answer the two questions in the next cell, then `Run` it to store your responses.

%%writefile moving_out_11.txt
✏️ 
1. Can you afford this lifestyle?

2. If not, what do you think you can change to have a balanced budget?
2. If yes, what do you plan to do with any extra money you might have?



## Reflections
🎒Explain in detail five things you have learned from this project. What was the most surprising or eye-opening learning you had completing this project? Be specific.

After you have recorded your responses in the next cell, `Run` it to store your answers.

%%writefile moving_out_12.txt
✏️

My one-time moving expenses will be about


My total expense per month will be about



Five things I learned from this project are

1. 

2. 

3. 

4. 

5. 


The most surprising or eye-opening part of this project was 

#✏️ Type your name between the '', e.g. 'Monty Python'
name = ''

#🎒Run this cell to finish up and check all of your answers

answerFilename = name.replace(' ', '_')+'_moving_out.txt'
answerFile = open(answerFilename, 'a')

for filenumber in range(1, 13):
    filename = 'moving_out_'+str(filenumber)+'.txt'
    try:
        file = open(filename, 'r')
        answerFile.write(file.read())
        file.close()
    except:
        print('Unable to open ' + filename)
answerFile.close()

print(name)
completeAnswerFile = open(answerFilename, 'r')
print(completeAnswerFile.read())

🎒You have now completed this moving out assignment. Submit the file `Name_moving_out.txt` to your teacher, or copy and past your answers from the output of the previous cell.

If you are interested in learning more about Jupyter notebooks and Python programming, check out [callysto.ca](https://callysto.ca).

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)