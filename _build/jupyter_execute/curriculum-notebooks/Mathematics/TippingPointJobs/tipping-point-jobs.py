![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/TippingPointJobs/tipping-point-jobs.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Tipping Point - Jobs

## Which job pays better?

## Congratulations!

So you've got a new job... Oh, wait, you have two job offers!?!  Well, congratulations twice!

Let's take a look at the two companies offering a job:


Job One            |  Job Two
:-------------------------:|:-------------------------:
![](images/Acme.png)  |  ![](images/Bigby.png)

Both companies **Acme** and **Bigby** are Electronic Supply companies, and are offering you a sales position.

**Which job should you take?** Well, let's look how much each job pays.

1. Acme offers a base salary of $\$$1200 per month, plus 3\% commission on sales over $\$$1000. 
2. Bigby offers a base salary of $\$$250 per month, plus 18\% commission on all sales.
 
 
**Your Task:** Figure out which job pays better.

**Need a Hint?**

It seems clear that your salary will depend on how much you sell each month. 

You can consider various sales amounts, and calculate how much you'd earn at either job with those same sales amounts. 

Since this notebook module can interpret basic math operations, we can type in the formulas for salary. 

Acme pays a base salary of $\$$1200 plus 3\% on sales, we can write this formula as

$$ Acme\ pay = 1200 + .03*(sales-1000). $$

Meanwhile, Bigby pays a base salary of $\$$250 plus 18\% on sales, we can write this formula as

$$ Bigby\ pay = 250 + .18*sales.$$

## Calculations with Python

Consider the examples below.

Let's start the calculation with no sales at all. You can do this in your head, but let's try it out in Python code.

## For zero sales
1200 + 0, 250 + 0

The above calculation tells us that for zero sales, Acme pays $\$$1200 and Bigby pays $\$$250. So Acme pays better in this case.

Let's next try sales of $\$$2000

## For 2000 dollars in sales
1200 + .03*(2000-1000), 250 + .18*2000

That is, for $\$$2000 in sales, Acme pays $\$$1230 and Bigby pays $\$$610. So Acme also pays better in this case.

Now let's be more ambitious, and say you can make $\$$10,000 in sales. How much will you make?

## for 10000 in sales
1200 + .03*(10000-1000), 250 + .18*10000

Here, for $\$$10000 in sales, Acme pays $\$$1470 and Bigby pays $\$$2050. So this time, Bigby pays better!

## Graphical Comparison

It seems that once your sales are high enough, Bigby pays better than Acme does. 

Let's plot some curves to show this. We can use Python to make a quick plot, with a few lines of code as follows.


First, we load in some code packages for plotting, in the following three lines.

from numpy import linspace, maximum
from ipywidgets import interact
import plotly.graph_objects as go

Now we define a few variables for sales and company pay, then plot the data in a scatter plot graph.

sales = linspace(0,10000)
bigby = 250 + .18*sales
acme = 1200 + .03*maximum(sales-1000,0)
go.Figure(go.Scatter(x=sales, y=acme, name='Acme')).add_trace(go.Scatter(x=sales,y=bigby,name="Bigby"))

### Comments on the code

The variable **sales** is a list of possible sales values, from 0 to 10,000, set up using the **linspace** function.

The variable **bigby** is the same formula we used above, adding 18\% of sales to a base salary of $\$$250. 

The variable **acme** is just a little more complicated. We use the **maximum** function to make sure we only get a commision on sales **over** $\$$1000.

The **go.Figure** command creates a scatter plot with the **Acme** data, overlaid with a second trace of the **Bigby** data.

With this plot, you can pan and zoom in on the lines, to investigate the data more directly.

## The Tipping Point

It seems clear from the calculations above, and from the graphs, that eventually Bigby pays more than Acme once the sales get high enough.

The **tipping point** is the point where the sales are big enough that Bigby pays more. 

How can we find this tipping point?

One way is to simply use Python. Type in a value for **sales** in the code below, replacing the number **4000** with a number of your choice. Try to find the number where these two pay values are equal.


sales = 4000
1200 + .03*(sales-1000), 250 + .18*sales

✏️ **Exercise:** Double click on this cell and enter the value(s) you find for **sales** where both pays are the same?

## Tipping point with interactive tools
Python lets you do this calculation automatically. Just type in the box below, and it will compute the Acme and Bigby pay. Again, try to find the value for **sales** so that the two pays are equal. **Note**, the following expressions use Python lambda functions and interactive Jupyter widgets; try these links to learn more about [lambda functions](https://realpython.com/python-lambda/) and [widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html).

interact(lambda sales: [1200+.03*(float(sales)-1000),250+.18*float(sales)],sales='4000');

You can also use a slider in Python to play around with the sales, as follows:

Again, try to find the point where the two companies pay the same. 

interact(lambda sales: [1200+.03*(sales-1000),250+.18*sales],sales=(6000,7000));

✏️ **Exercise:** Double click on this cell and enter the value(s) you find for **sales** where both pays are the same?

## Tipping point by algebra

And a final way: set the two pay formulas to be equal, and solve for **sales**.
    
$$ 1200 + .03\times (sales - 1000) = 250 + .18 \times sales.$$
    
What do you find for **sales**?

If yoy prefer to **solve for x**, try this formula:

$$ 1200 + .03(x - 1000) = 250 + .18  x.$$

The solution for **x** is the dollar value of sales where Bigby and Acme pay you the same. Any more sales, and Bigby pays more.



✏️ **Exercise:** Double click on this cell and enter your answer for **x** which solves this equation.



## Minimum wage

The minimum wage is the lowest pay a company can pay you, per hour, and stay within the law. 

**Exercise:** How much do you need to sell, in order to get paid at least as much as a minimum wage salary?

This is a challenging question, and an important one before you take on a new job. You must consider:
- what is the minimum wage in your area?
- how many hours would you typically work in a year?

For instance, in Alberta, the minimum wage is $\$$15 per hour. Most people work about 40 hours a week, for 50 weeks a year, which is 2000 hours per year. 

That results in an annual salary of $\$$30,000 per year, or $\$$2,500 per month.

$$ 2,500 = 30,000 \div 12.$$

Working at Bigby gives you more money, so let's find out how many dollars in sales at Bigby are needed to make the same as minimum wage.  

Remembering our formulas above are for monthly pay, we solve:
$$ 2,500 = 250 + .18x.$$

**Exercise:** What do you find for the value of **x**?

## ✏️ You can use this area to calculate the answer in Python. Solve for x in the above equation. 



## Sanity check

You'll find $x$ is over $\$$10,000 per month. That means you'll need to sell over a hundred and twenty thousand dollars worth of electronics every year, just to make minimum wage.

Does that sound like a lot to sell?

**Exercise:** Exactly how much in sales **per year** do you need to make minimum wage, in Alberta?


## ✏️ Use this area to calculate the answer in Python. 
## Take the answer x from the last Exercise, and convert from monthly to yearly sales.



## Working hard at Acme

It seems obvious that Acme pays much less than Bigby, when the sales are large.  So let's check with this exercise.

**Exercise:** Following the calculations as above, how many dollars in sales are needed at Acme to match the minimum wage month of $\$$2,500?

**Do you need a hint?** Try solving this equation for **x** (and explain why this is the one you want):

$$ 2,500 = 1200 + .03(x-1000).$$

## ✏️ Use this area to calculate your answer in Python. 



**Exercise:** Given your answers, how much more do you need in sales at Acme to match the monthly minimum wage, than you need at Bigby? (Bigby should be looking pretty good to you now!)

## ✏️ Use this area to calculate your answer in Python. 



## Another province.

What is minimum wage in your province? (You can look it up on the internet.) For instance, in Saskatchewan, it is $\$$11 per hour. In Ontario, $\$$14 per hour.

**Exercise:** 
- Imitating the calculations above, what is the monthly minimum wage salary in your province?
- How much product do you have to sell per month at Bigby, in order to match this month minimum wage salary?

## ✏️ Use this area to calculate your answer in Python. 



## Summary

- We learned that different jobs can have different pay rates.
- By creating formulas for the pay, we can determine which job pays better.
- We can make the comparison by individual calculations, by plotting data, or using some algebra.
- Knowing the minimum wage for your province gives you something to compare with, and perhaps aiming higher.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)