![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-7.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 7
## Part 7 - Gifts and Entertainment

📓Once again we will be using some dataframes to record data and do some calculations.

### Gifts and Charitable Donations

In a year, how many birthday or Christmas gifts do you purchase for friends and family members? How much do you spend on gifts?

Do you donate to any charities? Charitable donations are tax-deductable so you will essentially get 25% back at tax time. This means if you plan to donate \\$100 then you can record it as \\$75 in the table below.

`Run` the following cell to create a data table, and add your data to it.

Double-click on the "nan" values to put in your information. Use the "Add Row" and "Remove Row" buttons if necessary.

import pandas as pd
import qgrid
giftsList = range(1,7)
giftsColumns = ['Name','Occasion','Amount']
dfGifts = pd.DataFrame(index=pd.Series(giftsList), columns=pd.Series(giftsColumns))
dfGifts['Amount'] = 1
dfGiftsWidget = qgrid.QgridWidget(df=dfGifts, show_toolbar=True)
dfGiftsWidget

📓After you have added data to the table above, `Run` the next cell to calculate your gifts and donations costs for the month.

giftsList = dfGiftsWidget.get_changed_df()
giftsCost = pd.to_numeric(giftsList['Amount']).sum()
monthlyGiftsCost =  giftsCost / 12
%store monthlyGiftsCost
print('That is $' + str('{:.2f}'.format(giftsCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyGiftsCost)) + ' per month for gifts and donations.')

### Recreation and Entertainment

📓Recreation is highly personal and reflects your values. In this section plan for such things as concerts, athletics or memberships, skiing, travelling, hobbies, buying a boat or other recreational equipment, music, movies, parties, and other events or items.

For some items like yearly holidays or subscriptions divide by 12 for the monthly costs. For areas such as coffee or other drinks you may need to figure out what you typically spend daily or weekly to determine the monthly cost. Be totally honest in this section as these costs can sneak up on you if you don’t keep accurate accounting of your spending.

#✏️use this cell to calculate monthly cost from yearly cost (optional)
yearlyCost = 0
print(yearlyCost / 12)

#✏️use this cell to calculate monthly cost from weekly cost (optional)
weeklyCost = 0
print(weeklyCost * 4.3)

#✏️Follow the instructions, then run this cell to calculate entertainment expenses.

# What would you spend on movies, videos, concerts, and other events?
events = 0

# What do you spend on things like coffee with friends
socialBeverages = 0

# Consider any lifestyle choices such as health or diet supplements, cigarettes, etc.
lifestyle = 0

# How much would it cost to holiday? Remember to divide a yearly amount by 12
travel = 0

# Consider the replacement of lost, stolen, broken, or cracked devices,
# as well as video games, computers, and subscription costs
electronics = 0

# Do you have any hobbies that you need to buy supplies or equipment for?
hobbies = 0

# Memberships or entrance fees to gyms, clubs, or other recreation facilities 
memberships = 0

# Do you enjoy playing soccer, hockey, basketball, golf, snowboarding, or other sports?  
# Think about the cost to play and the equipment you will need.
sports = 0

# Pets If you have an average size dog, you can plan on spending $50 per month on food, bones, toys, etc.   
# If you plan to have a pet, Wealthsimple estimates that a dog costs about $100 to $180 per month
# for food, toys, etc. and a cat is about half of that
# A yearly trip to the vet with vaccinations is approximately $150, and an emergency vet trip is expensive.
pets = 0

# Can you think of anything else you might want to spend money on?
other = 0

monthlyEntertainmentCost = events + socialBeverages + lifestyle + travel + electronics + hobbies + memberships + sports + pets + other
%store monthlyEntertainmentCost
print('That is about $' + str(monthlyEntertainmentCost) + ' per month for recreation and entertainment.')

#### Reflections

📓It can cost a lot of money to have the "extras" in life. How does this section reflect your values? Any surprises here? Do you notice any areas of concern, or are there things you can justify as necessary to your happiness and wellbeing?

Answer in the cell below, then `Run` the cell to store your answer.

%%writefile moving_out_9.txt
✏️
Thinking about gifts and entertainment, 

📓Run the next cell to check that your answers have been stored.

print('Monthly gifts and donations cost:', monthlyGiftsCost)
print('Monthly entertainment cost:', monthlyEntertainmentCost)
with open('moving_out_9.txt', 'r') as file9:
    print(file9.read())

📓You have now completed this section. Proceed to [section 8](./CALM-moving-out-8.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)