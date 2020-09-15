![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-5.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 5
## Part 5 - Transportation

📕We will just be comparing the cost of purchasing and operating a vehicle to the cost of a monthly bus pass.

### Owning and Operating a Car

Complete this section regardless of whether you already have a car or decide against owning a car.

Find an advertisement for a vehicle (new or used) that you would like to drive. If you already a vehicle consider the next vehicle you would purchase if you were to upgrade or replace your car in the event of huge repair bill or accident.

To find out how much car insurance will cost, use one of these online [insurance](https://www.lowestrates.ca/insurance/auto/alberta) [quote](https://www.insurancehotline.com/Quote/Auto?postalCode=T8A4Y1#Vehicles) [sites](https://www.pcinsurance.ca/en/).

As well, look up and record the cost of [registering a vehicle](https://www.alberta.ca/vehicle-registration-renewal.aspx), and list the approximate current price of fuel.

Complete the statements then `Run` the cell.

%%writefile moving_out_6.txt
✏️
Link to vehicle advertisement:

I chose this vehicle because: 

The total price of this vehicle is: 

Year: 

Make: 

Model: 

Car insurance will cost about $   per month.

To register a car in Alberta costs $

Fuel is currently $  per litre.

### Car Loan

📕Now let's consider the cost of a loan to purchase that vehicle. Enter the purchase price and `Run` the code cell to calculate monthly costs.

#✏️
purchasePrice = 5000

interestRate = 0.07  # assume a 7% interest rate
financingTerm = 48  # 48 months is four years

monthlyInterest = interestRate / 12
monthlyCarPayment = purchasePrice * (monthlyInterest) * ((1+monthlyInterest) ** financingTerm) / (((1+monthlyInterest) ** financingTerm)-1)
totalCarCost = monthlyCarPayment * financingTerm
print('Purchasing this vehicle with financing will cost $' + str('{:.2f}'.format(monthlyCarPayment)) + ' per month.')
print('The total cost of the vehicle over', financingTerm, 'months will be $' + str('{:.2f}'.format(totalCarCost)))

### Other Vehicle Expenses

📕Operating a vehicle is expensive and we often don’t realize the costs of repairs, oil changes, tires, gas, registration, or depreciation. Keep in mind there are additional costs for driving offenses such as speeding, running a red light, distracted driving, and parking tickets.

According to the Canadian Automobile Association the average Canadian drives 20,000 km per year for work, recreation and travel.    

Go to the Canadian Automobile Associate (CAA) [Driving Cost Calculator](http://caa.ca/car_costs) to 
estimate the operating cost for the year, make, and model of your selected vehicle.

Fill in your numbers and `Run` the code cell below. If you get an error, check that you have run the cell above this one.

#✏️
vehicleInsurance = 0
otherVehicleExpenses = 0

vehicleCosts = monthlyCarPayment + vehicleInsurance + otherVehicleExpenses
%store vehicleCosts
print('Estimated vehicle costs per month are $' + str('{:.2f}'.format(vehicleCosts)) + '.')

📕Type your responses in the code cell below, and `Run` the cell once you have finished.

%%writefile moving_out_7.txt
✏️

My estimated vehicle costs per month are $

An adult monthly bus pass costs: $    in (Sherwood Park / Edmonton / myCity).
or
I will be attending post-secondary, so U-Pass costs: $    per semester.


I have decided that for transportation I will 
because

📕In the code cell below, enter the cost of a monthly bus pass (e.g. `busPass = 98`) and your decision about transportation:

`transportationDecision = 1` if you plan to take the bus

`transportationDecision = 2` if you plan to drive a vehicle

Then `Run` the cell to calculate and store your responses.

#✏️ Enter the cost of a monthly bus pass
busPass = 0

#✏️ Change this to 1 for taking the bus or 2 for driving a vehicle
transportationDecision = 0

#📕 Run this cell when you've answered the questions above in order to calculate monthly transportation costs.
transportationCost = 0
if transportationDecision == 1:
    transportationCost = busPass
    print('You will be spending $' + str(transportationExpenses) + ' per month to take the bus.')
elif transportationDecision == 2:
    transportationCost = vehicleCosts
    print('You will be spending approximately $' + str('{:.2f}'.format(vehicleCosts)) + ' for your vehicle.')
else:
    print('Please change transportationDecision to 1 or 2 and run the cell again.')
%store transportationCost

📕`Run` the next cell to check that your answers have been stored.

#📕 Run this cell to check that your answers have been stored
print('Transportation cost:', transportationCost)
with open('moving_out_6.txt', 'r') as file6:
    print(file6.read())
with open('moving_out_7.txt', 'r') as file7:
    print(file7.read())

📕You have now completed this section. Proceed to [section 6](./CALM-moving-out-6.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)