![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-6.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 6
## Part 6 - Food and Supplies

📙In this section we will consider food and household supplies that you will need. You will be using a [dataframes from a Python library called pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe). These dataframes are like spreadsheets, and the code will look a little complicated, but it shouldn't be too bad.

### Meal Plan

Before we get into dataframes, though, you need to create a meal plan. With the [Canadian Food Guide](https://food-guide.canada.ca/en/food-guide-snapshot/) in mind, complete a 7-day meal plan considering nutritionally balanced choices at each meal. You can choose to eat out only twice on this menu.

You will then use this to decide your grocery needs for one week.

Replace the words "meal" in the cell below with the meals you plan to eat, then run the cell to store your plan.

%%writefile moving_out_8.txt
✏️

|Day|Breakfast|Lunch|Dinner|
|-|-|-|-|
|Monday| meal | meal | meal |
|Tuesday| meal | meal | meal |
|Wednesday| meal | meal | meal |
|Thursday| meal | meal | meal |
|Friday| meal | meal | meal |
|Saturday| meal | meal | meal |
|Sunday| meal | meal | meal |

### Food Shopping

📙From your meal plan make a shopping list of food needed to prepare three meals a day for one week. Research the price of these food items by going to grocery store websites, using grocery fliers, going to the grocery store, or reviewing receipts or bills with your family. Buying items in bulk is usually more economical in the long run, but for this exercise you only require food for one week so choose the smallest quantities possible.

`Run` the following cell to generate a data table that you can then edit.

Double-click on the "nan" values to put in your information. Use the "Add Row" and "Remove Row" buttons if necessary.

import pandas as pd
import qgrid
foodItemList = ['Vegetables','Fruit','Protein','Whole Grains','Snacks','Restaurant Meal 1','Restaurant Meal 2']
foodColumns = ['Size','Quantity','Price']
foodIndex = range(1,len(foodItemList)+1)
dfFood = pd.DataFrame(index=pd.Series(foodIndex), columns=pd.Series(foodColumns))
dfFood.insert(0,'Item(s)',foodItemList,True)
dfFood['Quantity'] = 1
dfFood['Price'] = 1
dfFoodWidget = qgrid.QgridWidget(df=dfFood, show_toolbar=True)
dfFoodWidget

📙After you have added data to the table above, `Run` the next cell to calculate your food costs for the month. It adds up weekly food costs and multiplies by 4.3 weeks per month.

foodShoppingList = dfFoodWidget.get_changed_df()
foodPrices = pd.to_numeric(foodShoppingList['Price'])
weeklyFoodCost = foodPrices.sum()
monthlyFoodCost = weeklyFoodCost * 4.3
%store monthlyFoodCost
print('That is about $' + str(weeklyFoodCost) + ' per week for food.')
print('Your food for the month will cost about $' + str('{:.2f}'.format(monthlyFoodCost)) + '.')

### Household Supplies and Personal Items

📙The following is a typical list of household and personal items. Add any additional items you feel you need and delete items you don’t need. Look for smaller quantities with a **one-month** budget in mind, or adjust pricing if buying in bulk.

`Run` the next cell to generate a data table that you can then edit.

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
dfHousehold['Quantity'] = 1
dfHousehold['Price'] = 1
dfHouseholdWidget = qgrid.QgridWidget(df=dfHousehold, show_toolbar=True)
dfHouseholdWidget

📙After you have added data to the above data table, `Run` the next cell to calculate your monthly household item costs.

householdShoppingList = dfHouseholdWidget.get_changed_df()
householdPrices = pd.to_numeric(householdShoppingList['Price'])
monthlyHouseholdCost = householdPrices.sum()
%store monthlyHouseholdCost
print('That is about $' + str(monthlyHouseholdCost) + ' per month for household items.')

### Furniture and Equipment

📙Think about items you need for your place. How comfortable do you want to be? Are there items you have already been collecting or that your family is saving for you? Discuss which items they may be willing to give you, decide which items you can do without, which items a roommate may have, and which items you will need to purchase. Although it is nice to have new things, remember household items are often a bargain at garage sales, dollar stores, and thrift stores.

`Run` the next cell to generate a data table that you can edit.

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
dfFne['Quantity'] = 1
dfFne['Price'] = 1
dfFneWidget = qgrid.QgridWidget(df=dfFne, show_toolbar=True)
dfFneWidget

📙Next `Run` the following cell to add up your furniture and equipment costs.

fneList = dfFneWidget.get_changed_df()
fnePrices = pd.to_numeric(fneList['Price'])
fneCost = fnePrices.sum()
%store fneCost
print('That is about $' + str(fneCost) + ' for furniture and equipment items.')

### Clothing

📙When calculating the cost of clothing for yourself, consider the type of work you plan to be doing and how important clothing is to you. Consider how many of each item of clothing you will purchase in a year, and multiply this by the cost per item. Be realistic.

`Run` the next cell to generate an editable data table.

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
dfClothing['Quantity Required'] = 1
dfClothing['Cost per Item'] = 1
dfClothingWidget = qgrid.QgridWidget(df=dfClothing, show_toolbar=True)
dfClothingWidget

📙Once you have added data to the above table, `Run` the next cell to add up your clothing costs.

clothingList = dfClothingWidget.get_changed_df()
clothingQuantities = pd.to_numeric(clothingList['Quantity Required'])
clothingPrices = pd.to_numeric(clothingList['Cost per Item'])
clothingList['Total Cost'] = clothingQuantities * clothingPrices
clothingCost = clothingList['Total Cost'].sum()
monthlyClothingCost =  clothingCost / 12
%store monthlyClothingCost
print('That is $' + str('{:.2f}'.format(clothingCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyClothingCost)) + ' per month for clothing.')
clothingList  # this displays the table with total cost calculations

### Health Care

📙Most people living and working in Alberta have access to hospital and medical services under the [Alberta Health Care Insurance Plan (AHCIP)](https://www.alberta.ca/ahcip.aspx) paid for by the government. Depending on where you work, your employer may offer additional benefit packages such as Extended Health Care that cover a portion of medical and dental expenses.  

If you do not have health benefits from your employer you will have to pay for medications, dental visits, and vision care.  

Allow money in your budget for prescriptions and over-the-counter medications.  

Budget for the dentist and optometrist.  One visit to the dentist including a check-up x-rays and teeth cleaning is approximately $330. You should see your dentist yearly.

A visit to the optometrist is approximately $120. You should normally see your optometrist once every 2 years, or once a year if you’re wearing contact lenses.

`Run` the next cell to display a data table that you can edit with your expected health costs.

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
dfHealth['Cost Per Year'] = 1
dfHealthWidget = qgrid.QgridWidget(df=dfHealth, show_toolbar=True)
dfHealthWidget

📙`Run` the next cell to add up your health care costs.

healthList = dfHealthWidget.get_changed_df()
healthCost = pd.to_numeric(healthList['Cost Per Year']).sum()
monthlyHealthCost =  healthCost / 12
%store monthlyHealthCost
print('That is $' + str('{:.2f}'.format(healthCost)) + ' per year, or about $' + str('{:.2f}'.format(monthlyHealthCost)) + ' per month for health care.')

📙Once again, `Run` the next cell to check that your answers have been stored.

print('Monthly food cost:', monthlyFoodCost)
print('Monthly household items cost:', monthlyHouseholdCost)
print('Furniture and equipment cost:', fneCost)
print('Monthly clothing cost:', monthlyClothingCost)
print('Monthly health cost', monthlyHealthCost)
with open('moving_out_8.txt', 'r') as file8:
    print(file8.read())

📙You have now completed this section. Proceed to [section 7](./CALM-moving-out-7.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)