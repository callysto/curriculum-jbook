![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out Project

<div class="alert alert-block alert-info">

*This project is also available as a series of individual notebook files starting [here](./CALM-moving-out-1.ipynb)*

Imagine that you are in your early twenties and it is time to move out of your family home.

You work 40 hours per week and your wage is $15.00 per hour gross income (before deductions).

You will be required to calculate your net income and manage financial resources effectively.

You may choose to live with a roommate. If you choose to live with a roommate and share rent, you must each complete and hand in a separate assignment.

You will use the internet for all the information required to complete this project. However, you may want to also refer to flyers to find prices for food and household items.

Cells with a white background are ones that you can or should double-click on to edit.
</div>

<div class="alert alert-block alert-info">
<h2>My Personal Profile - Age Twenty-something</h2>
Complete these questions based on what your hope of plan to do with your life. Double-click on a cell in order to edit it.
</div>

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

10. A vehicle I would like to drive when I'm in my twenties is

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

<div class="alert alert-block alert-info">
    <h2>Income</h2>
</div>

<div class="alert alert-block alert-info">
<h3>Paycheque Definitions</h3>

<h4>Gross Income (pay/earnings)</h4>
The amount of income/earnings, for any pay period, before deductions
 
<h4>Net income (pay/earnings)</h4>
The amount of income/earnings, for any pay period, after deductions (Take home pay)

<h4>CPP - Canada Pension Plan</h4>
2.3% of gross income deducted for insurance in case of unemployment
 
<h4>Income Tax</h4>
A deduction paid to the Federal and Provincial government for taxes
 
<h4>LTD</h4>
A deduction for Long Term Disability insurance
 
<h4>Union Dues</h4>
Fees paid for membership in a union
 
<h4>Bonds</h4>
An investment in which a business or government pays a set interest rate
 
<h4>Advance Earnings</h4>
Deducted money that was received in advance of the pay cheque
 
<h4>Overtime Earnings</h4>
Pay received for working over 8 hours a day or 44 hours a week, whichever is greater
</div>

<div class="alert alert-block alert-info">
<h3>Calculating Net Income</h3>

Click on the code cell below, then press the `Run` button on the toolbar to calculate your net income. You may also change some values in the code to see how the results change.
</h3>

wagePerHour = 15  # this is your wage in $/hour
hoursPerDay = 8
daysPerMonth = 21

grossIncome = wagePerHour * hoursPerDay * daysPerMonth
print('Your gross income is $', grossIncome, 'per month.')

incomeTax = .15 + .10   # assume federal income tax is 15% and provincial is 10%
cpp = .0495             # assume Canada Pension Plan is 4.95%
ei = .0188              # assume Employment Insurance is 1.88%
unionDues = .0075       # 0.75% sounds reasonable for union dues

deductions = grossIncome * (incomeTax + cpp + ei + unionDues)
print('$', '{:.2f}'.format(deductions), ' will be taken off your paycheck.')

netIncome = grossIncome - deductions
print('Your net income is $', '{:.2f}'.format(netIncome), 'per month.')

<div class="alert alert-block alert-info">

We can also look at how your net income (take-home pay) changes based on your hourly wage. We will use [2019 taxation rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html) as well as [EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) and [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) rates. `Run` the cell below to generate a graph.
</div>

# Run this cell without editing it to generate a graph of Net Income vs Hourly Wage
def calculateFederalTax(income):
    taxBrackets = [47630, 95259, 147667, 210371]
    taxRates = [.15, .205, .26, .29, .33]
    taxes = []
    for i in range(0, len(taxBrackets)):
        taxes.append(taxBrackets[i] * taxRates[i])
    if income < taxBrackets[0]:
        tax = income * taxRates[0]
    elif income < taxBrackets[1]:
        tax = taxes[0] + (income - taxBrackets[0]) * taxRates[1]
    elif income < taxBrackets[2]:
        tax = taxes[1] + (income - taxBrackets[1]) * taxRates[2]
    elif income < taxBrackets[3]:
        tax = taxes[2] + (income - taxBrackets[2]) * taxRates[3]
    else:
        tax = taxes[3] + (income - taxBrackets[3]) * taxRates[4]
    return tax

def calculateProvincialTax(income):
    taxBrackets = [131220, 157464, 209952, 314928] # for Alberta
    taxRates = [.1, .12, .13, .14, .15]
    taxes = []
    for i in range(0, len(taxBrackets)):
        taxes.append(taxBrackets[i] * taxRates[i])
    if income < taxBrackets[0]:
        tax = income * taxRates[0]
    elif income < taxBrackets[1]:
        tax = taxes[0] + (income - taxBrackets[0]) * taxRates[1]
    elif income < taxBrackets[2]:
        tax = taxes[1] + (income - taxBrackets[1]) * taxRates[2]
    elif income < taxBrackets[3]:
        tax = taxes[2] + (income - taxBrackets[2]) * taxRates[3]
    else:
        tax = taxes[3] + (income - taxBrackets[3]) * taxRates[4]
    return tax

def calculateEI(income):
    eiMaxInsurableEarnings = 53100
    eiRate = 0.0162
    if income >= eiMaxInsurableEarnings:
        eiPremium = eiMaxInsurableEarnings * eiRate
    else:
        eiPremium = income * eiRate
    return eiPremium

def calculateCPP(income):
    cppMaxContributoryEarnings = 53900
    cppRate = 0.051
    if income >= cppMaxContributoryEarnings:
        cppPremium = cppMaxContributoryEarnings * cppRate
    else:
        cppPremium = income * cppRate
    return cppPremium

wages = []
grossIncomes = []
netIncomes = []
for wage in range(15, 150):
    wages.append(wage)
    grossAnnualIncome = wage * 8 * 240
    grossIncomes.append(grossAnnualIncome)
    incomeTax = calculateFederalTax(grossAnnualIncome) + calculateProvincialTax(grossAnnualIncome)
    eiPremium = calculateEI(grossAnnualIncome)
    cppPremium = calculateCPP(grossAnnualIncome)
    netIncome = grossAnnualIncome - (incomeTax + eiPremium + cppPremium)
    netIncomes.append(netIncome)

import plotly.graph_objects as go
fig = go.Figure()
#fig.add_trace(go.Scatter(x=wages, y=grossIncomes, name='Gross Income'))
fig.add_trace(go.Scatter(x=wages, y=netIncomes, name='Net Income'))
fig.update_layout(
    title=go.layout.Title(text='Net Income vs Hourly Wage'),
    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Hourly Wage')),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Income')))
fig.show()

<div class="alert alert-block alert-info">
<h3>Accommodation Options</h3>

Using [Kijiji](https://www.kijiji.ca) or other internet sources, investigate each of the following options and add information to the cells below. Edit each white cell by double-clicking on it.
</div>

#### Apartment
Advantages:
1. 
2. 
3. 

Disadvantages:
1. 
2. 
3. 

Approximate cost per month: 

#### Townhouse or Duplex
Advantages:
1. 
2. 
3. 

Disadvantages:
1. 
2. 
3. 

Approximate cost per month: 

#### Single Detached House
Advantages:
1. 
2. 
3. 

Disadvantages:
1. 
2. 
3. 

Approximate cost per month: 

The best choice of housing for a retired couple with no children who do not want to cut grass or do other maintenance is _______ because

The best choice of housing for a middle-aged couple with two small children who what room for children and friends to visit is _______ because

The best choice of housing for a young couple with a small child is _______ because

The best choice of housing for a young, single person who travels frequently for work is _______ because

The type of home I picture myself in when I decide to move out is (be descriptive)

<div class="alert alert-block alert-info">

For the purpose of this project you will consider rental properties only. Find an online listing for a suitable place to rent and include a screenshot below if possible.

Carefully read the listing and fill in the information in the following cell.
</div>

Address: 

Type of accomodation: 

Rent per month: 

Utilities included in rent: 

Damage deposit or security deposit amount: 

Other costs not included in rent (e.g. parking, coin laundry): 

Summary of other important information: 

<div class="alert alert-block alert-info">
<h2>Expenses</h2>

Expenses are the money that you spend on necessary or desired goods and services.

Some expenses can be decreased by having a roommate. For the purposes of this project you may choose to have one roommate.

Complete the statements in the cells below.
</div>

Advantages of living on my own are:
1. 
2. 
3. 

Disadvantages of living on my own are:
1. 
2. 
3. 

Advantages of living with a roommate are:
1. 
2. 
3. 

Disadvantages of living with a roommate are:
1. 
2. 
3. 

I have decided to live (on my own / with a roommate) because 

Essential characteristics of a roommate are:
1. 
2. 
3. 
4. 

<div class="alert alert-block alert-info">
<h3>Housing Expenses</h3>

When investigating costs, be aware of "introductory specials" or contracts where the price increases. For these calculations use the price after the introductory offer.

The CMHC (Canadian Home and Mortgage Corporation) [recommends](https://www.cmhc-schl.gc.ca/en/finance-and-investing/mortgage-loan-insurance/calculating-gds-tds) that you should not spend more than 35% of your net income on housing costs.
</div>

I have decided to use the following service providers:
(remove any lines that are not applicable)

Natural Gas (Heat): 

Electricity: 

Tenant Insurance: 

Mobile Phone: 

Landline: 

Internet:  

TV, Video, Music Subscriptions: 

<div class="alert alert-block alert-info">
<h4>Calculating Housing Expenses</h4>

Follow the instructions in the code cell below to edit the numbers, then `Run` the cell to calculate your monthly housing expenses.

</div>

rent = 900

# change this to 1 if you plan to have a roommate
roommate = 0

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

# Now you've finished adjusting the code, run the cell to calculate your monthly housing costs
if roommate == 1:
    monthlyBills = (rent + heating + electricity + waterAndWaste + internet) / 2 + tenantInsurance + phone + streaming
else:
    monthlyBills = rent + heating + electricity + waterAndWaste + tenantInsurance + phone + internet + streaming

print('Your monthly bills will be approximately $' + str('{:.2f}'.format(monthlyBills)) + '.')

<div class="alert alert-block alert-info">
<h2>Moving Expenses</h2>
    
As well as the monthly expenses there are one-time moving expenses to consider. Change the numbers in the following cell, if necessary, then `Run` the cell to display the calculated value.
</div>

# Security / Damage Deposit: this is usually equal to one month's rent.
#  You can get your deposit back when you move out, if you take care of your home.
#  Some landlords charge a non-refundable pet fee.
damageDeposit = rent
petFee = 0

# If you plan to have a pet, estimate the cost of the pet, toys, furniture, etc.
petPurchase = 1000

# There are sometimes utility activation or hookup costs
electricalActivation = 10
naturalGasActivation = 10
waterActivation = 0
internetActivation = 0
mobilePhoneActivitation = 25

mobilePhonePurchase = 300

furnitureAndAppliances = 500

movingCosts = 300

# You've finished editing numbers, now run the cell to add up expenses

if roommate == 1:
    movingExpenses = (
        damageDeposit + 
        electricalActivation + 
        naturalGasActivation + 
        waterActivation + 
        internetActivation + 
        furnitureAndAppliances
        ) / 2 + mobilePhoneActivitation + mobilePhonePurchase + movingCosts + petFee + petPurchase
else:
    movingExpenses = (
        damageDeposit +
        electricalActivation + 
        naturalGasActivation + 
        waterActivation + 
        internetActivation + 
        furnitureAndAppliances + 
        mobilePhoneActivitation + 
        mobilePhonePurchase + 
        movingCosts + 
        petFee + 
        petPurchase
        )

print('Moving expenses will be about $' + str(movingExpenses))

<div class="alert alert-block alert-info">
<h3>Transportation</h3>

Find the cost of a monthly bus pass, and compare that to purchasing and operating a vehicle. Other forms of transportation exist, but we will just be comparing these two.
</div>

An adult monthly bus pass costs: $ .

or

I will be attending postsecondary, so U-Pass (or similar) costs: $    per semester.

<div class="alert alert-block alert-info">
<h4>Owning and Operating a Car</h4>

Complete this section regardless if you already have a car or ultimately decide against owning a car.

Find an advertisement for a vehicle that you would like to drive. If you already own your own vehicle consider the next vehicle you would purchase if you were to upgrade or replace your car in the event of huge repair bill or accident. If possible, include a screenshot of the advertisement.
</div>

I chose this vehicle because: 

The total price of this vehicle is: 

Year: 

Make: 

Model: 

<div class="alert alert-block alert-info">
Now let's consider the cost of a loan to purchase that vehicle. Enter the purchase price and run the code cell to calculate monthly costs.
</div>

purchasePrice = 5000
interestRate = 0.07  # assume a 7% interest rate
financingTerm = 48  # 48 months is four years

monthlyInterest = interestRate / 12
monthlyCarPayment = purchasePrice * (monthlyInterest) * ((1+monthlyInterest) ** financingTerm) / (((1+monthlyInterest) ** financingTerm)-1)
totalCost = monthlyCarPayment * financingTerm
print('Purchasing this vehicle with financing will cost $' + str('{:.2f}'.format(monthlyCarPayment)) + ' per month.')
print('The total cost of the vehicle over', financingTerm, 'months will be $' + str('{:.2f}'.format(totalCost)))

<div class="alert alert-block alert-info">
    
To find out how much car insurance will cost, use one of these online [insurance](https://www.lowestrates.ca/insurance/auto/alberta) [quote](https://www.insurancehotline.com/Quote/Auto?postalCode=T8A4Y1#Vehicles) [sites](https://www.pcinsurance.ca/en/).

As well, look up and record the cost of [registering a vehicle](https://www.alberta.ca/vehicle-registration-renewal.aspx), and list the approximate current price of fuel.
</div>

Car insurance will cost about $   per month.

To register a car in Alberta costs $

Fuel is currently $  per litre.

<div class="alert alert-block alert-info">

Operating a vehicle is expensive and we often don’t realize the costs of repairs, oil changes, tires, gas, registration, or depreciation. Keep in mind there are additional costs for driving offenses such as speeding, running a red light, distracted driving, and parking tickets.

According to the Canadian Automobile Association the average Canadian drives 20,000 km per year for work, recreation and travel.    

Go to the Canadian Automobile Associate (CAA) [Driving Cost Calculator](http://caa.ca/car_costs) to 
estimate the operating cost for the year, make, and model of your selected vehicle.
</div>

The likely monthly operating costs for this vehicle are: 

<div class="alert alert-block alert-info">

Fill in your numbers in the cell below, then run it to calculate your estimated vehicle costs as compared to public transportation.

</div>

# The cost of monthly adult bus pass
busPass = 0

# The costs of a vehicle
monthlyPayment = 0
vehicleInsurance = 0
vehicleOperatingCosts = 0

vehicleCosts = monthlyPayment + vehicleInsurance + vehicleOperatingCosts
print('Estimated vehicle costs per month are $' +str(vehicleCosts)+ ' which is $' +str(vehicleCosts - busPass)+ ' more than a bus pass.')

<div class="alert alert-block alert-info">

Determine the method of transportation you will be using. Will you use your own car? Take public transportation? Will you have to pay for parking if you drive? Can you car pool? What is your decision? Explain your reasons.

Then run the code cell below it to finish calculating transportation costs.

</div>

I have decided to 

because

<div class="alert alert-block alert-info">

In the code cell below, record your decision about transportation:

`transportationDecision = 1` if you plan to take the bus

`transportationDecision = 2` if you plan to drive a vehicle

Then `Run` the cell to calculate your monthly transportation costs.

</div>

transportationDecision = 0

#Run this cell after you have recorded your decision above (1 or 2).
transportationCost = 0
if transportationDecision == 1:
    transportationCost = busPass
    print('You will be spending $' + str(transportationExpenses) + ' per month to take the bus.')
elif transportationDecision == 2:
    transportationCost = vehicleCosts
    print('You will be spending approximately $' + str('{:.2f}'.format(vehicleCosts)) + ' for your vehicle.')
else:
    print('Please change transportationDecision to 1 or 2 and run the cell again.')

<div class="alert alert-block alert-info">
<h3>Food and Household Supplies</h3>

With the [Canadian Food Guide](https://food-guide.canada.ca/en/food-guide-snapshot/) in mind, complete a 7-day menu plan considering nutritionally balanced choices at each meal. Use this plan to decide your grocery needs for one week. You can choose to eat out only twice on this menu.

</div>

|Day|Breakfast|Lunch|Dinner|
|-|-|-|-|
|Monday| meal | meal | meal |
|Tuesday| meal | meal | meal |
|Wednesday| meal | meal | meal |
|Thursday| meal | meal | meal |
|Friday| meal | meal | meal |
|Saturday| meal | meal | meal |
|Sunday| meal | meal | meal |

<div class="alert alert-block alert-info">
<h4>Food Shopping</h4>

From your menu plan make a shopping list of food needed to prepare three meals a day for one week. Research the price of these food items by going to grocery store websites, using grocery fliers, going shopping to the grocery store, or reviewing the receipts or bills with your family. Buying items in bulk may be more economical in the long run, but for this exercise you only require food for one week so choose the smallest quantities possible.

`Run` the following cell to generate a data table that you can then edit.

Double-click on the "nan" values to put in your information. Use the "Add Row" and "Remove Row" buttons if necessary.

</div>

import pandas as pd
import qgrid
foodItemList = ['Vegetables','Fruit','Protein','Whole Grains','Snacks','Restaurant Meal 1','Restaurant Meal 2']
foodColumns = ['Size','Quantity','Price']
foodIndex = range(1,len(foodItemList)+1)
dfFood = pd.DataFrame(index=pd.Series(foodIndex), columns=pd.Series(foodColumns))
dfFood.insert(0,'Item(s)',foodItemList,True)
dfFoodWidget = qgrid.QgridWidget(df=dfFood, show_toolbar=True)
dfFoodWidget

<div class="alert alert-block alert-info">

After you have added data to the table above, `Run` the next cell to calculate your food costs for the month. It adds up weekly food costs and multiplies by 4.3 weeks per month.

</div>

foodShoppingList = dfFoodWidget.get_changed_df()
foodPrices = pd.to_numeric(foodShoppingList['Price'])
weeklyFoodCost = foodPrices.sum()
monthlyFoodCost = weeklyFoodCost * 4.3
print('That is about $' + str(weeklyFoodCost) + ' per week for food.')
print('Your food for the month will cost about $' + str(monthlyFoodCost) + '.')

<div class="alert alert-block alert-info">
<h4>Household Supplies and Personal Items</h4>

The following is a typical list of household and personal items. Add any additional items you feel you need and delete items you don’t need. Look for smaller quantities with a <b>one-month</b> budget in mind, or adjust pricing if buying in bulk.

`Run` the next cell to generate a data table that you can then edit.

</div>

householdItemList = ['Toilet Paper','Tissues','Paper Towel',
                     'Dish Soap','Laundry Detergent','Cleaners',
                     'Plastic Wrap','Foil','Garbage/Recycling Bags',
                     'Condiments','Coffee/Tea','Flour','Sugar',
                     'Shampoo','Conditioner','Soap','Deodorant',
                     'Toothpaste','Mouthwash','Hair Products','Toothbrush',
                     'Makeup','Cotton Balls','Shaving Gel','Razors',
                    ]
householdColumns = ['Size','Quantity','Price']
householdIndex = range(1,len(householdItemList)+1)
dfHousehold = pd.DataFrame(index=pd.Series(householdIndex), columns=pd.Series(householdColumns))
dfHousehold.insert(0,'Item(s)',householdItemList,True)
dfHouseholdWidget = qgrid.QgridWidget(df=dfHousehold, show_toolbar=True)
dfHouseholdWidget

<div class="alert alert-block alert-info">

After you have added data to the above data table, `Run` the next cell to calculate your monthly household item costs.

</div>

householdShoppingList = dfHouseholdWidget.get_changed_df()
householdPrices = pd.to_numeric(householdShoppingList['Price'])
monthlyHouseholdCost = householdPrices.sum()
print('That is about $' + str(monthlyHouseholdCost) + ' per month for household items.')

<div class="alert alert-block alert-info">
<h3>Furniture and Equipment</h3>

Think about items you need for your place. How comfortable do you want to be? Are there items you have already been collecting or that your family is saving for you? Discuss which items they may be willing to give you, decide which items you can do without, which items a roommate may have, and which items you will need to purchase. Although it is nice to have new things, remember household items are often a bargain at garage sales, dollar stores, and thrift stores.

`Run` the next cell to generate a data table that you can edit.

</div>

fneItemList = ['Pots and Pans','Glasses','Plates','Bowls',
               'Cutlery','Knives','Oven Mitts','Towels','Cloths',
               'Toaster','Garbage Cans','Kettle','Table','Kitchen Chairs',
               'Broom and Dustpan','Vacuum Cleaner','Clock',
               'Bath Towels','Hand Towels','Bath Mat',
               'Toilet Brush','Plunger',
               'Bed','Dresser','Night Stand','Sheets','Blankets','Pillows',
               'Lamps','TV','Electronics','Coffee Table','Couch','Chairs',
                ]
fneColumns = ['Room','Quantity','Price']
fneIndex = range(1,len(fneItemList)+1)
dfFne = pd.DataFrame(index=pd.Series(fneIndex), columns=pd.Series(fneColumns))
dfFne.insert(0,'Item(s)',fneItemList,True)
dfFneWidget = qgrid.QgridWidget(df=dfFne, show_toolbar=True)
dfFneWidget

<div class="alert alert-block alert-info">

Next `Run` the following cell to add up your furniture and equipment costs.

</div>

fneList = dfFneWidget.get_changed_df()
fnePrices = pd.to_numeric(fneList['Price'])
fneCost = fnePrices.sum()
print('That is about $' + str(fneCost) + ' for furniture and equipment items.')

<div class="alert alert-block alert-info">
<h3>Clothing</h3>

When calculating the cost of clothing for yourself, consider the type of work you plan to be doing and how important clothing is to you. Consider how many of each item of clothing you will purchase in a year, and multiply this by the cost per item. Be realistic.

`Run` the next cell to generate an editable data table.

</div>

clothingItemList = ['Dress Pants','Skirts','Shirts','Suits/Jackets/Dresses'
                    'T-Shirts/Tops','Jeans/Pants','Shorts',
                    'Dress Shoes','Casual Shoes','Running Shoes',
                    'Outdoor Coats','Boots','Sports Clothing',
                    'Pajamas','Underwear','Socks','Swimsuits'
                   ]
clothingColumns = ['Quantity Required','Cost per Item']
clothingIndex = range(1,len(clothingItemList)+1)
dfClothing = pd.DataFrame(index=pd.Series(clothingIndex), columns=pd.Series(clothingColumns))
dfClothing.insert(0,'Item(s)',clothingItemList,True)
dfClothingWidget = qgrid.QgridWidget(df=dfClothing, show_toolbar=True)
dfClothingWidget

<div class="alert alert-block alert-info">

`Run` the next cell to add up your clothing costs.

</div>

clothingList = dfClothingWidget.get_changed_df()
clothingQuantities = pd.to_numeric(clothingList['Quantity Required'])
clothingPrices = pd.to_numeric(clothingList['Cost per Item'])
clothingList['Total Cost'] = clothingQuantities * clothingPrices
clothingCost = clothingList['Total Cost'].sum()
monthlyClothingCost =  clothingCost / 12
print('That is $' + str('{:.2f}'.format(clothingCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyClothingCost)) + ' per month for clothing.')
clothingList  # this displays the table with total cost calculations

<div class="alert alert-block alert-info">
<h3>Charitable Donations and Gifts</h3>

In a year, how many birthday or Christmas gifts do you purchase for friends and family members? How much do you spend on gifts?

Do you donate to any charities? Charitable donations are tax-deductible so you will essentially get 25% back at tax time. This means if you plan to donate \\$100 then you can record it as \\$75 in the table below.

`Run` the next cell to display a data table that you can edit with your expected health costs.

</div>

giftsList = range(1,7)
giftsColumns = ['Name','Occasion','Amount']
dfGifts = pd.DataFrame(index=pd.Series(giftsList), columns=pd.Series(giftsColumns))
dfGiftsWidget = qgrid.QgridWidget(df=dfGifts, show_toolbar=True)
dfGiftsWidget

<div class="alert alert-block alert-info">

`Run` the next cell to add up your gifts and donations costs.

</div>

giftsList = dfGiftsWidget.get_changed_df()
giftsCost = pd.to_numeric(giftsList['Amount']).sum()
monthlyGiftsCost =  giftsCost / 12
print('That is $' + str('{:.2f}'.format(giftsCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyGiftsCost)) + ' per month for gifts and donations.')

<div class="alert alert-block alert-info">
<h3>Health Care</h3>

Most people living and working in Alberta have access to hospital and medical services under the [Alberta Health Care Insurance Plan (AHCIP)](https://www.alberta.ca/ahcip.aspx) paid for by the government. Depending on where you work, your employer may offer additional benefit packages such as Extended Health Care that cover a portion of medical and dental expenses.  

If you do not have health benefits from your employer you will have to pay for medications, dental visits, and vision care.  

Allow money in your budget for prescriptions and over-the-counter medications.  

Budget for the dentist and optometrist.  One visit to the dentist including a check-up x-rays and teeth cleaning is approximately $330. You should see your dentist yearly!

A visit to the optometrist is approximately $120. You should normally see your optometrist once every 2 years, or once a year if you’re wearing contact lenses.

`Run` the next cell to display a data table that you can edit with your expected health costs.

</div>

healthItems = [
    'Pain Relievers','Bandages','Cough Medicine',
    'Prescriptions','Dental Checkup',
    'Optometrist','Glasses','Contacts','Contact Solution',
    'Physiotherapy','Massage'
]
healthColumns = ['Cost Per Year']
healthIndex = range(1,len(healthItems)+1)
dfHealth = pd.DataFrame(index=pd.Series(healthIndex), columns=pd.Series(healthColumns))
dfHealth.insert(0,'Item or Service',healthItems,True)
dfHealthWidget = qgrid.QgridWidget(df=dfHealth, show_toolbar=True)
dfHealthWidget

<div class="alert alert-block alert-info">

`Run` the next cell to add up your health care costs.

</div>

healthList = dfHealthWidget.get_changed_df()
healthCost = pd.to_numeric(healthList['Cost Per Year']).sum()
monthlyHealthCost =  healthCost / 12
print('That is $' + str('{:.2f}'.format(healthCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyHealthCost)) + ' per month for health care.')

<div class="alert alert-block alert-info">
<h3>Recreation and Entertainment</h3>

Recreation is highly personal and reflects your values. In this section plan for such things as concerts, athletics or memberships, skiing, travelling, hobbies, buying a boat or other recreational equipment, music, movies, parties, and other events or items.

For some items like yearly holidays or subscriptions divide by 12 for the monthly costs. For areas such as coffee or other drinks you may need to figure out what you typically spend daily or weekly to determine the monthly cost. Be totally honest in this section as these costs can sneak up on you if you don’t keep accurate accounting of your spending.

Use the next few code cells to calculate monthly entertainment costs.

</div>

# use this cell to calculate monthly cost from yearly cost (optional)
yearlyCost = 0
print(yearlyCost / 12)

# use this cell to calculate monthly cost from weekly cost (optional)
weeklyCost = 0
print(weeklyCost * 4.3)

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
print('That is about $' + str(monthlyEntertainmentCost) + ' per month for recreation and entertainment.')

<div class="alert alert-block alert-info">
<h4>Reflections</h4>

It can cost a lot of money to have the ‘extras’ in life! How does this section reflect your values? Any surprises here? Do you notice any areas of concern, or are there things you can justify as necessary to your happiness and wellbeing?

Answer in the cell below.

</div>

This 

<div class="alert alert-block alert-info">
<h3>Education</h3>

Education is a costly expense that usually pays for itself in the long run. Your parents may have been saving money for you to attend postsecondary in an RESP, but a good number of individuals will pay their own way through postsecondary working full or part-time jobs and perhaps taking out student loans.

It is wise to invest some time to see if you qualify for the many grants, scholarships, or bursaries. If you are paying for your education you will need to work the costs into your budget. If you are planning to attend postsecondary you have already investigated the cost in your Occupational Research.

</div>

I (am / am not) planning to attend any type of postsecondary education.

I (will / will not) be paying for my own education

I (have / have not) looked into bursaries, grants, and scholarships.

During my postsecondary education, I will be living (at home / on my own).

<div class="alert alert-block alert-info">
    
If you are planning on attending postsecondary, change the values in the next cell. Otherwise just `Run` the cell without editing it.

</div>

tuitionPerYear = 0
booksAndSuppliesPerYear = 0

tuitionPerMonth = tuitionPerYear / 12
booksAndSuppliesPerMonth = booksAndSuppliesPerYear / 12
monthlyEducationCost = tuitionPerMonth + booksAndSuppliesPerMonth
print('You will likely be spending $' + str('{:.2f}'.format(monthlyEducationCost)) + ' per month for education.')

<div class="alert alert-block alert-info">
<h3>Savings and Investments</h3>

When you do move out, what do you think you will be saving money for? Education, a car, a house, retirement, early retirement?

1.	The secret to retirement is to **pay yourself first**:
    1. Aim to save 10% of each paycheck.
    2. Put this money into an account like a TFSA or RRSP that you don’t spend until retirement. 
2.	Keep an **emergency fund** for unexpected things like a job loss, break-ups, and break-downs.
3.	Have some short term (3 – 6 months) and long-term **financial goals**.

</div>

I plan to retire by the time I am 

I intend to have $   set aside for emergencies.

My short-term financial goals are:
1. 
2. 

My long-term financial goals are:
1. 
2. 

<div class="alert alert-block alert-info">

Run this cell once you have completed all of the above activities.

Ensure that you have run all of the previous cells, even if they result in zero expenses.

</div>

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

oneTimeExpenses = movingExpenses + fneCost



totalCostsPerMonth = pd.to_numeric(dfTotalCosts['Cost Per Month']).sum()
print('Your total expense per month will be about $' + str('{:.2f}'.format(totalCostsPerMonth)) + '.')
print('This is about ' + str('{:.1f}'.format(totalCostsPerMonth / netIncome * 100)) + '% of your net income.')
dfTotalCosts

<div class="alert alert-block alert-info">
<h2>Summary</h2>

Can you afford your lifestyle?
</div>

Yes / No

<div class="alert alert-block alert-info">
If no, then what can you change to have a balanced budget? Describe a financial recovery plan.
</div>

I 

<div class="alert alert-block alert-info">
If yes, what will you do with the excess money?
</div>

I 

<div class="alert alert-block alert-info">
Explain in detail five things you have learned from this project. What was the most surprising or eye-opening learning you had completing this project? Be specific.
</div>

1. 

2. 

3. 

4. 

5. 



<div class="alert alert-block alert-info">
    You have now completed your <b>CALM - Moving Out Project</b>. Check with your teacher if you should download it as a pdf or in some other format in order to submit it.
</div>

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)