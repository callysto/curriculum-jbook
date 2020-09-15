![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-3.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 3
## Part 3 - Accommodation

📚You will need somewhere to live. Think about the advantages and disadvantages of an [apartment](https://en.wikipedia.org/wiki/Apartment), [townhouse](https://simple.wikipedia.org/wiki/Townhouse)/[duplex](https://en.wikipedia.org/wiki/Duplex_(building)), and a [single detached house](https://en.wikipedia.org/wiki/Single-family_detached_home) and record your thoughts in the cell below. Remember to `Run` the cell once you have finished.

%%writefile moving_out_2.txt
✏️
Advantages of an Apartment
1. 
2. 
3. 
Disadvantages of an Apartment
1. 
2. 
3. 

Advantages of a Townhouse or Duplex
1. 
2. 
3. 
Disadvantages of a Townhouse or Duplex
1. 
2. 
3. 

Advantages of a Single Detatched House
1. 
2. 
3. 
Disadvantages of a Single Detatched House
1. 
2. 
3. 

The best choice of housing for a retired couple with no children 
who do not want to cut grass or do other maintenance is 
because

The best choice of housing for a middle-aged couple with two small children 
who what room for children and friends to visit is 
because

The best choice of housing for a young couple with a small child is 
because

The best choice of housing for a young, single person who travels frequently for work is 
because


The type of home I picture myself in when I decide to move out is (be descriptive)

### Finding a Rental Home

📚For the purpose of this project you will consider rental properties only. Find an online listing (e.g. from [Kijiji](https://www.kijiji.ca/)) for a suitable place to rent in the area you would like to live.

Carefully read the listing and fill in the information in the following cell, and `Run` the cell once you have finished.

%%writefile moving_out_3.txt
✏️

Link to listing: 

Address: 

Type of accomodation: 

Rent per month: 

Utilities included in rent: 

Damage deposit or security deposit amount: 

Other costs not included in rent (e.g. parking, coin laundry): 

Summary of other important information: 


### Roommate

📚Some expenses can be decreased by having a roommate. For the purposes of this project you may choose to have one roommate. Complete the statements then `Run` the cell below.

%%writefile moving_out_4.txt
✏️
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

### Moving Expenses
📚There are one-time moving expenses to consider. Follow the instructions in the code cell below to edit the numbers, then run the cell to calculate and store your expenses.

#✏️
# If you plan to have a roommate, change this to a 1 instead of a 0
roommate = 0

# Security Deposit or Damage Deposit: this is usually equal to one month's rent.
#  You can get your deposit back when you move out, if you take care of your home.
#  Some landlords also charge a non-refundable pet fee.
damageDeposit = 0
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


# 📚 You've finished editing numbers, now run the cell to calculate and store expenses

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

%store roommate
%store movingExpenses
print('Moving expenses will be about $' + str(movingExpenses))

📚`Run` the next cell to check that your answers have been stored. If you get an error, make sure that you have run all of the previous code cells in this notebook.

#📚 Run this cell to check that your answers have been stored.
print('Roommate:', roommate)
print('Moving expenses:', movingExpenses)
with open('moving_out_2.txt', 'r') as file2:
    print(file2.read())
with open('moving_out_3.txt', 'r') as file3:
    print(file3.read())
with open('moving_out_4.txt', 'r') as file4:
    print(file4.read())

📚You have now completed this section. Proceed to [section 4](./CALM-moving-out-4.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)