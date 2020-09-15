![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-2.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 2
## Part 2 - Income

📗Now let's take a look at your potential income. First, some definitions:

### Paycheque Definitions
#### Gross Income (pay/earnings)
The amount of income/earnings, for any pay period, before deductions
 
#### Net income (pay/earnings)
The amount of income/earnings, for any pay period, after deductions (Take home pay)

#### CPP - Canada Pension Plan
2.3% of gross income deducted for insurance in case of unemployment
 
#### Income Tax
A deduction paid to the Federal and Provincial government for taxes
 
#### LTD
A deduction for Long Term Disability insurance
 
#### Union Dues
Fees paid for membership in a union
 
#### Bonds
An investment in which a business or government pays a set interest rate
 
#### Advance Earnings
Deducted money that was received in advance of the pay cheque
 
#### Overtime Earnings
Pay received for working over 8 hours a day or 44 hours a week, whichever is greater

### Calculating Net Income

📗Click on the code cell below, then click the `Run` button on the toolbar to calculate your net income. You may also change some values in the code to see how the results change.

#✏️
wagePerHour = 15  # this is your wage in $/hour
hoursPerDay = 8
workdaysPerMonth = 21

grossIncome = wagePerHour * hoursPerDay * workdaysPerMonth
print('Your gross income is $', grossIncome, 'per month.')

incomeTax = .15 + .10   # assume federal income tax is 15% and provincial is 10%
cpp = .0495             # assume Canada Pension Plan is 4.95%
ei = .0188              # assume Employment Insurance is 1.88%
unionDues = .0075       # 0.75% sounds reasonable for union dues

deductions = grossIncome * (incomeTax + cpp + ei + unionDues)
print('$', '{:.2f}'.format(deductions), ' will be taken off your paycheck.')

netIncome = grossIncome - deductions
print('Your net income is $', '{:.2f}'.format(netIncome), 'per month.')
%store netIncome        # store that value in memory for later notebooks

## Graphing Income
📗
We can also look at how your net income (take-home pay) changes based on your hourly wage. We will use [2019 taxation rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html) as well as [EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) and [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) rates. `Run` the cell below (without editing it) to generate a graph.
</div>

#📗
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
fig.add_trace(go.Scatter(x=wages, y=grossIncomes, name='Gross Income'))
fig.add_trace(go.Scatter(x=wages, y=netIncomes, name='Net Income'))
fig.update_layout(
    title=go.layout.Title(text='Net Income vs Hourly Wage'),
    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Hourly Wage')),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Income')))
fig.show()

📗The graph shows that the difference between gross income and net income (after deductions) increases as wage increases. For more information about this, you may want to read about [progressive taxation](https://en.wikipedia.org/wiki/Progressive_tax).

You have now completed this section. Proceed to [section 3](./CALM-moving-out-3.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)