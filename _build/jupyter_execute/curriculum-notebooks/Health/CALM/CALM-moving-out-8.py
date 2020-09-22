![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Health/CALM/CALM-moving-out-8.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# CALM - Moving Out 8
## Part 8 - Education and Investments

### Education

📚Education is a costly expense that usually pays for itself in the long run. Your parents may have been saving money for you to attend post-secondary in an [RESP](https://www.canada.ca/en/services/benefits/education/education-savings/resp.html), but many individuals will pay their own way through post-secondary working full- or part-time jobs and perhaps taking out student loans.

It is wise to invest some time to see if you qualify for the many grants, scholarships, or bursaries. If you are paying for your education you will need to work the costs into your budget. If you are planning to attend postsecondary you should have already investigated the cost in your Occupational Research activity.

Record your answers in the next cell, then `Run` the cell to store your responses.

%%writefile moving_out_10.txt
✏️
I (am / am not) planning to attend any type of post-secondary education.

I (will / will not) be paying for my own education

I (have / have not) looked into bursaries, grants, and scholarships.

During my post-secondary education, I will be living (at home / on my own).

📚If you plan to attend a postsecondary school, change the values for `tuitionPerYear` and `booksAndSuppliesPerYear` and then `Run` the cell. 

#✏️Leave the next two lines with 0s if you don't plan to attend postsecondary, then run the cell
tuitionPerYear = 0
booksAndSuppliesPerYear = 0

#📚
tuitionPerMonth = tuitionPerYear / 12
booksAndSuppliesPerMonth = booksAndSuppliesPerYear / 12
monthlyEducationCost = tuitionPerMonth + booksAndSuppliesPerMonth
%store monthlyEducationCost
print('You will likely be spending $' + str('{:.2f}'.format(monthlyEducationCost)) + ' per month for education.')

### Savings and Investments

📚When you do move out, what do you think you will be saving money for? Education, a car, a house, retirement, early retirement?

1.	The secret to retirement is to **pay yourself first**:
    1. aim for 10% of each paycheck
    2. Put this money into an account like a [TFSA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account.html) or [RRSP](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/registered-retirement-savings-plan-rrsp.html) that you don’t spend until retirement. 
2.	Keep an [emergency fund](https://www.investopedia.com/terms/e/emergency_fund.asp) for unexpected things like a job loss, break-ups, and break-downs.
    1. This should be about three months worth of basic living expenses
    2. While it can (and perhaps should) be invested somewhere, it needs to be a [liquid asset](https://www.investopedia.com/terms/l/liquidasset.asp)
3.	Have some short term (3 – 6 months) and long-term **financial goals**.

Record your answers in the next cell, then `Run` it.

%%writefile moving_out_11.txt
✏️

I plan to retire by the time I am 

I intend to have $   set aside for emergencies.

My short-term financial goals are:
1. 
2. 

My long-term financial goals are:
1. 
2. 

📚`Run` the next cell to check that your answers have been stored.

#📚Run this cell to check that your answers have been stored
print('Monthly education cost:', monthlyEducationCost)
with open('moving_out_10.txt', 'r') as file10:
    print(file10.read())
with open('moving_out_11.txt', 'r') as file11:
    print(file11.read())

📚You have now completed this section. Proceed to the summary in [section 9](./CALM-moving-out-9.ipynb)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)