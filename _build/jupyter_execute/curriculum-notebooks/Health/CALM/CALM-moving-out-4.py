![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-4.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 4
## Part 4 - Expenses

📒Expenses are the money that you spend on necessary or desired goods and services.

When investigating these costs, be aware of "introductory specials" or contracts where the price increases. For these calculations use the price after the introductory offer.

The CMHC (Canadian Home and Mortgage Corporation) [recommends](https://www.cmhc-schl.gc.ca/en/finance-and-investing/mortgage-loan-insurance/calculating-gds-tds) that you should not spend more than 35% of your net income on housing costs.

Complete the statements then `Run` the cell.

%%writefile moving_out_5.txt
✏️
I have decided to use the following service providers (remove any lines that are not applicable)

Natural Gas (Heat): 

Electricity: 

Tenant Insurance: 

Mobile Phone: 

Landline: 

Internet:  

TV, Video, Music Subscriptions: 

### Calculating Housing Expenses

📒Follow the instructions in the code cell below to edit the numbers, then `Run` the cell to calculate your monthly housing expenses.

#✏️
rent = 900

# Natural Gas is hard to estimate, depending on different circumstances, but rough guidelines are:
#  Average 1200 sq. ft. house - $94 per month
#  New energy efficient average home (1200 sq. ft.) - $67 per month
#  Large new home (1800 sq. ft.) - $90 per month
#  Larger older home with heated garage - $128 per month
# enter 0 if this is included in your rent
heating = 94

# Electricity:
#  an average two-bedroom apartment will cost about $50 per month
#  a small 1100 square foot home with the usual appliances will cost $75 per month
#  a large home with many appliances, a hot tub, and air conditioning will cost over $120 per month
electricity = 75

# Water and Waste will be about 60 for an apartment, 100 for a house
waterAndWaste = 100

# Tenant Insurance: each individual must have their own tenant insurance to cover their belongings
# in case of fire, theft, flooding, or natural disaster. Landlords have insurance on the building
# but not on your personal possessions. Use the following chart to estimate how much you would pay:
#  Value    Annual Premium (we will divide this by 12 to get the monthly cost)
#  $10,000  $92
#  $20,000  $159
#  $30,000  $208
#  $40,000  $268
#  $50,000  $305
#  $60,000  $367
tenantInsurance = 367 / 12

# Mobile Phone: check out various service providers and choose a plan
phone = 65

# TV and Internet Access: check out Shaw and Telus to see what plans are available
internet = 100
streaming = 14


# 📒 Now you've finished adjusting the code, run this cell to calculate your monthly housing costs.

#recall the values that we stored in previous notebooks
%store -r
try:
    roommate
except NameError:
    roommate = 0
if roommate == 1:
    monthlyExpenses = (rent + heating + electricity + waterAndWaste + internet) / 2 + tenantInsurance + phone + streaming
else:
    monthlyExpenses = rent + heating + electricity + waterAndWaste + tenantInsurance + phone + internet + streaming

%store monthlyExpenses
print('Your monthly bills will be approximately $' + str('{:.2f}'.format(monthlyExpenses)) + '.')

📒`Run` the next cell to check that your answers have been stored.

#📒 Run this cell to check that your answers have been stored
print('Monthly expenses:', monthlyExpenses)
with open('moving_out_5.txt', 'r') as file:
    print(file.read())

📒You have now completed this section. Proceed to [section 5](./CALM-moving-out-5.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)