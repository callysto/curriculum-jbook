![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Languages/FrenchVerbCodingConjugation/French-Verb-Coding.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# French Verb Coding
    
----

## Introduction

In this Jupyter Notebook by Callysto you will learn about French verb conjugation and some basics of programming in Python. 

Mastering the basics of verb conjugation is essential to reading and writing in French. There are some basic rules and exceptions that should be addressed and to learn those details, you should look at this other Callysto notebook: [French-Verb-Conjugation](CC-186-French-Verb-Coding.ipynb)

For this notebook, we will only look at the **regular** French verbs and see how we can use them in a program to conjugate automatically. Along the way you will gain some insight into how this notebook was made and thus gain some exposure to some programming concepts.

#### Necessary background
- Some basic knowledge of French
- Elementary Python syntax

#### Allons-y!

## Startup code

This notebook will use Python code. To get started, we need to load in a few modules that have useful "helper" functions to get us going. Be sure to run the following code to get these modules activated. 

from IPython.display import display, clear_output, Markdown  
import ipywidgets as widgets
import plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)


## Personal pronouns

In order to start conjugating verbs, we must first learn what are the personal pronouns in French. These correspond to the usual English pronouns like I, you, he, she, etc. It is nice to put this into a table so the display is pretty.

We can make three lists or words, which are just strings of characters surrounded by quotes which indicate the start and end of each word. These three lists are stored as **variables,** as follows:
```
french = ['je','tu','elle, il, on','nous','vous','elles, ils']
english = ['I','you','she, he, one','we','you (plural or formal)','they']
person = ['First','Second','Third','First (plural)','Second (plural)','Third (plural)']
```

We then construct a table using some standard Python code, from a package called 'Plotly.' Don't worry too much about the details -- you can read about them on the Plotly web pages. For now, just notice that our three variables show up in the code at this line:
```
    values = [person,french,english],
```
That line tells the table builder where to get our words, to put into the table. 

With this following code, we build and display a table showing the subject pronouns in French. These pronouns will be used to separate the different cases of verb conjugation. 

#table for personal pronouns using plotly

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
english = ['I','you','she, he, one','we','you (plural or formal)','they']
person = ['First','Second','Third','First (plural)','Second (plural)','Third (plural)']


trace0 = go.Table(
  columnorder = [1,2,3],
  columnwidth = [10,10],
  header = dict(
    values = ['Person','French','English'],
    line = dict(color = 'rgb(0,0,0)'),
    fill = dict(color = 'rgb(0,35,48)'),
    align = ['center','center'],
    font = dict(color = 'white', size = 16),
    height = 40
  ),
  cells = dict(
    values = [person,french,english],
    line = dict(color = 'black'),
    fill = dict(color = 'rgb(95,102,161)'),
    align = ['center', 'center'],
    font = dict(color = 'white', size = 14),
    height = 30
    )
)
layout = dict(
    width=750, 
    height=450
)

data = [trace0]
fig = dict(data = data, layout = layout)

iplot(fig)

Our verb conjugation rules will be based on these personal pronouns, so it is good to get familiar with their translations. French makes a distinction between all of these different tenses based on their person, whether or not they are masculine or feminine, and if they are plural or singular. 



## Regular "er" verbs

Let's now look at the general rubric for conjugating verbs that end in **er** in the present tense. 

We will illustrate this with the verb "parler" (to speak). The stem of the verb parler is "parl-". We conjugate it by adding on the endings "e", "es", "e", "ons", "ez" "ent" for the corresponding pronouns. We put these into the data structure for the table, and build it as follows:

(Be sure to run the following cell, to generate the table.)

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
stem = ['parl-','parl-','parl-','parl-','parl-','parl-']
ending = ['e','es','e','ons','ez','ent']
conjug = ['parle','parles','parle','parlons','parlez','parlent']


trace0 = go.Table(
  columnorder = [1,2],
  columnwidth = [10,10],
  header = dict(
    values = ['Pronoun','Conjugation'],
    line = dict(color = 'rgb(0,0,0)'),
    fill = dict(color = 'rgb(0,35,48)'),
    align = ['center','center'],
    font = dict(color = 'white', size = 16),
    height = 40
  ),
  cells = dict(
    values = [french,conjug],
    line = dict(color = 'black'),
    fill = dict(color = 'rgb(95,102,161)'),
    align = ['center', 'center'],
    font = dict(color = 'white', size = 14),
    height = 30
    )
)
layout = dict(width=500, height=450)

data = [trace0]
fig = dict(data = data, layout = layout)

iplot(fig)

This can be taken as the general rule for conjugating **er** verbs in the present tense. All you need to do is find the *stem* of the verb, which was parl- in this case, and then apply these endings to figure out how to conjugate the verb for every personal pronoun. 

We now try to apply this using code.


## Coding Examples

---

How could one write code to see if someone conjugated a verb correctly? The following exercise will test your knowledge of French verb conjugation and also introduce you to some aspects of coding. 


Let's  start the coding with an example. I ask you to input an answer to: "Conjugate the verb *fermer* to the first person singular in the present tense". How do I check whether or not you input the correct answer?

In reular Python, to get a user to input a value, we create a *variable* that holds the user input:

``` python 
x = input()
```
then test that variable to see if it is correct or not. 

However, in a Jupyter notebook like this one, it is better to create a **text widget** which is simply a small text box on the screen where the user can type in his or her answer. We create and display the widget two commands like this:

``` python
aText = widgets.Text(value = None, 
                  placeholder = "Conjugate 'fermer' present tense, 1st person singular.")
display(aText)
```

The variable aText just refers to the text box that will be on the screen, and the placeholder is the instruction that will be placed in that box. 

When the user enters a word in the box, we want the computer to *do something.* In this case, we should define a function that does what we want. Here is a definition of the *doIt* function that does what we want: tests the text in the box to see if it is correct or not:
``` python
def doIt(x):
    clear_output()
    display(x)
    if x.value != None:
        if x.value == "ferme":
            print('Correct!')
        else:
            print('Incorrect, please try again. Make sure you use only letters, no quotes, no spaces.')
    return
```
In this function, the variable x just points to our text box, and x.value is a **string**, which a short list of characters, that the user has typed into the box. This will be what we use to check against the correct answer. In our case, the correct answer is "ferme" and we use the **if** statement to check. 


The code above deserves some explanation.

- We used the quotations around the answer (`'ferme'`) as this is how Python recognizes strings. Since our variable x.value was held as a string we want to check it against something that is itself a string. 
- If you want to check that the variable is equal to the correct answer we used ==.
- The `print` statement was the operation that we chose to do when the `if` statement was fulfilled. 
- The if statement requires the colon at the end of the statement and whatever operation you choose to perform given that the statement is fulfilled needs to be indented within the statement. 

Finally, we must tell the aText object to attach the doIt function to itself, so it runs the code once the user enters the text and hits the return button. 

The final code looks like this:

aText = widgets.Text(value = None, 
                  placeholder = "Conjugate 'fermer' present tense, 1st person singular.")
display(aText)

def doIt(x):
    clear_output()
    display(x)
    if x.value != None:
        if x.value == "ferme":
            print('Correct!')
        else:
            print('Incorrect, please try again. Make sure you use only letters, no quotes, no spaces.')
    return

aText.on_submit(doIt)

** Try it! ** Enter some text in the box above to see what happens for the correct and incorrect cases.

## Generalizing

--- 

Code that has multiple uses, and is more broadly useful, is typically a lot more valuable. In our case, how could we write a program that checks the correct answer for any verb, tense, and personal pronoun? This would be a generalization of the simple case that we constructed above. This is a lot more of a complex problem that will have to be broken down. 

The exercise will be: Conjugate the verb "___ -er" in the present tense in every subject. 

Since we have knowledge of the endings for "-er" verbs in the present tense, our problem reduces to analyzing if each of the student's answers fits the form that the conjugated verb should take in that subject. Steps we require then:

1. We need to extract the root from each verb.
2. See if the remainder of the verb has the correct ending.
3. Make sure all answers are correct. 

To achieve this we will employing the use of a *list*. A list is a data type which has some sort of ordering to it. The ordering gives us the means to *index* an *element* of the list. For example, we have the list:

```python
subjects = ['je','tu','il, elle, on','nous','vous','ils/elles']
```
(Note the square brackets)

"subjects" is a comma separated list of string objects. We can do things like index the list:

```python 
subjects[0] = 'je'
subjects[1] = 'tu'
subjects[2] = 'il, elle, on'
```
Notice how the indexing starts from 0. This means if you have **n** elements in a list `v`, and you want to index the last element of the list, you would write `v[n-1]`.

What is the value of `subjects[4]`? Run the following code to test yourself:

#Simple list test

a = widgets.Text(value = None, placeholder = "What is the value of subjects[4]?")
display(a)

def callback(sender):
    clear_output()
    display(a)
    if a.value != None:
        if a.value == "vous":
            print('Correct!')
        if a.value != "vous":
            print('Incorrect, please try again. Make sure you use only letters, no quotes, no spaces.')
    return

a.on_submit(callback)


A more useful list to us would be:

``` python

endings = ['e','es','e','ons','ez','ent']

```

These are the verb endings given for conjugating "-er" verbs in the present tense. Now we just need to some means of analyzing their answer to see if they used the right ending. 

Say that we store all of their answers in a list like:

```python
answers = ['x1','x2','x3','x4','x5','x6']
```
This elements of the list, labelled "x1, x2, ..." are variables, which are themselves strings. Their position in the list indicates which subject they were trying to conjugate to, for instance x1 $\rightarrow$ 'je'. The convenience of storing the answers like this will become apparent soon.

If we wanted to perform a simple check, say whether or not they simply got the correct form, and not necessarily the correct spelling, we would use the following:

```python
for i in range(0,6):
    
    n = len(endings[i])
    if answers[i][-n:] != endings[i]:
        print('Incorrect')
```
**What does this do?**

This short little piece of code checks to see if they got the right ending. Let's look at some the tools that it uses.

**What does the `for` statement do?**
```python
for i in range(0,6):
```
This is another essential programming tool known as the `for` loop. Within the `for` loop, the indented code block is executed, then the next iteration of the loop is performed, in our case the index $i$ is increased to $i+1$. This continues until all iterations are done. It provides a means of counting or iterating through a process. In our case we want to iterate over every element in the list and perform the check in the `if` statement.

Notice the code `range(0,6)` tells us the index `i` will start at `i=0` and end at `i=5`. It stops before 6.

**The `if` statement**

Again we used the "!=" to see if two strings are not equal to each other. Firstly, we have declared a variable in the loop:
```python
n = len(endings[i])
```
This is simply the length of the ending. So for `endings[5]`, which is the string 'ent', the length is `n = 3`. This gives us a way of checking the last letters of the respective answer. We accomplish by using:

```python
answers[i][-n:]
```
The first index, `answers[i]` gives us the `i+1` element of the list answers (since we begin indexing from 0). e.g. `answers[3] = 'x4'`. The second index we used, `answers[i][-n:]`, indexes the element of the list. How are we indexing an already indexed list you might ask? Well, this is because a string is conveniently broken up into the characters that make it up. This gives us a way of indexing any "letter" of the string. For example, if `x1 = 'mange'` then `x1[3] = 'g'`. This is very nice for us, since we can employ this to check the ending of their answers. To index the last element of a string, or a list, we use the negative. e.g. `x1[-1] = 'e'`. To take out an entire section of a list or string we used "slice notation", this is why there is the extra colon. e.g. `x1[-3:] = 'nge'`. In our case we only wanted to index the last `n` letters of the string because this is the amount of letters in the ending that we wanted to check against. If all the answers were correct then the entire `for` loop would run and the `if` statement would never be fulfilled!

----


Now this was quite a bit of information, so let's test your knowledge on what we've done so far and then we'll work on generalizing this further for a different case.

For the lists:

```python 
endings = ['e','es','e','ons','ez','ent']
answers = ['mange','manges','mange','mangeons','manger','mangent']
```

ques1 = "Which element of answers is incorrect? Use index notation , i.e. `answers[]`"
ques2 = "What part should be changed? Use the double index notation, i.e. `answers[][]`"
ques3 = "What should the ending be? Use index notation again, i.e. `endings[]`"
ques4 = "If I wanted to check the first three answers, how would the `for` loop initial statement look like? \
        Please use `i` as the index."
ans1 = widgets.Text(value = None)
ans2 = widgets.Text(value = None)
ans3 = widgets.Text(value = None)
ans4 = widgets.Text(value = None)


def callback1(sender):
    if ans1.value != None:
        clear_output()
        display(Markdown(ques1))
        display(ans1)
        if ans1.value == 'answers[4]' or ans1.value == 'answers[-2]':
            display(Markdown('Correct!'))
        else:
            display(Markdown('Not quite! Please try again.'))
        display(Markdown(ques2))
        display(ans2)
        display(Markdown(ques3))
        display(ans3)
        display(Markdown(ques4))
        display(ans4)       
    return

def callback2(sender):
    if ans2.value != None:
        clear_output()
        display(Markdown(ques1))
        display(ans1)
        display(Markdown(ques2))
        display(ans2)
        if ans2.value == 'answers[4][4:]' or ans2.value == 'answers[4][-2:]' or \
            ans2.value == 'answers[4][-1]'  or ans2.value == 'answers[4][5]':
            display(Markdown('Correct!'))
        else:
            display(Markdown('Not quite! Please try again. You might need a colon in there.'))
        display(Markdown(ques3))
        display(ans3)
        display(Markdown(ques4))
        display(ans4)       
        return
    
def callback3(sender):    
    if ans3.value != None:
        clear_output()
        display(Markdown(ques1))
        display(ans1)
        display(Markdown(ques2))
        display(ans2)
        display(Markdown(ques3))
        display(ans3)
        if ans3.value == 'endings[4]' or ans3.value == 'endings[-2]':
            display(Markdown('Correct!'))
        else:
            display(Markdown('Not quite! Please try again.'))
        display(Markdown(ques4))
        display(ans4)       
        return
    
def callback4(sender):
    if ans4.value != None:
        clear_output()
        display(Markdown(ques1))
        display(ans1)
        display(Markdown(ques2))
        display(ans2)
        display(Markdown(ques3))
        display(ans3)
        display(Markdown(ques4))
        display(ans4)       
        if ans4.value == 'for i in range(0,3):' or ans4.value == 'for i in range(3):':
            display(Markdown('Correct!'))
        else:
            display(Markdown("Not quite! Please try again. Don't forget the colon :"))
    return

ans1.on_submit(callback1)
ans2.on_submit(callback2)
ans3.on_submit(callback3)
ans4.on_submit(callback4)

display(Markdown(ques1))
display(ans1)
display(Markdown(ques2))
display(ans2)
display(Markdown(ques3))
display(ans3)
display(Markdown(ques4))
display(ans4)       


## Automatic conjugation

Of course, the rules for conjugation for the regular verbs are very straightforward. So we could write code to handle these by computer. The basic rule is to decide whether the verb is an **er**, **ir**, or **re** verb. Based on that, we decide which endings to add onto the stem.

For instance, a simple **if** statement can check whether the verb is an **er** type, find the stem, and then compute the conjugations appropriately:
```
        if aVerb.value[-2:]=='er':
            stem = aVerb.value[:-2]
            for i in range(6):
                conjug[i] = stem+er_endings[i]
```

To handle the three different regular cases, we should have lists for the three different types of endings:
```
er_endings = ['e','es','e','ons','ez','ent']
ir_endings = ['is','is','it','issons','issez','issent']
re_endings = ['s','s','','ons','ez','ent']
```

To put the code together, we can have three **if** statements to test which of the three types of verbs we have, then add on the appropriate endings to the stem. Some code to do this looks like the following. Try running it yourself.

pronouns = ['je','tu','elle, il, on','nous','vous','elles, ils']
er_endings = ['e','es','e','ons','ez','ent']
ir_endings = ['is','is','it','issons','issez','issent']
re_endings = ['s','s','','ons','ez','ent']
stem = ''
aVerb = widgets.Text(value = None, description = 'Infinitive', placeholder = "Enter a verb")

display(aVerb)

def callback5(sender):    
    if aVerb.value != None:
        if aVerb.value[-2:]=='er':
            stem = aVerb.value[:-2]
            for i in range(6):
                conjug[i] = stem+er_endings[i]
            clear_output()
            display(aVerb)
            display(Markdown('An **er** verb with stem **' + stem + '-**' + ' and conjugations:'))
            display(conjug)
            return
        if aVerb.value[-2:]=='ir':
            stem = aVerb.value[:-2]
            for i in range(6):
                conjug[i] = stem+ir_endings[i]
            clear_output()
            display(aVerb)
            display(Markdown('An **ir** verb with stem **' + stem + '-**' + ' and conjugations:'))
            display(conjug)
            return
        if aVerb.value[-2:]=='re':
            stem = aVerb.value[:-2]
            for i in range(6):
                conjug[i] = stem+re_endings[i]
            clear_output()
            display(aVerb)
            display(Markdown('An **re** verb with stem **' + stem + '-**' + ' and conjugations:'))
            display(conjug)
            return
        clear_output()
        display(aVerb)
        display(Markdown("I don't recongnize this kind of verb. Try again."))
        return
    
    
aVerb.on_submit(callback5)



## Exceptions
Of course, this code does not handle exceptions, only the three regular cases.

#### Exercise

Try adding an **if** statement to test for an exception, say if the verb is "Avoir." In this case, the conjugation will be `['ai','as,'a','avons','avez','ont']`. See if you can modify the code above to handle this special case.

Should you test for exceptions first in your code, or test for the three regular cases first?

Once you succeed at that, try handling the exceptional verb "Être."

## Making it nice

Perhaps you liked the nice tables that we used to display verb conjugations, as in the notes above. We can add a function to our code that replicated this table. Our code then changes, to display the table instead of the list of conjugations. The resulting coding is as follows. Note the newly defined function `displayTable()` which builds the table for us. 

pronouns = ['je','tu','elle, il, on','nous','vous','elles, ils']
er_endings = ['e','es','e','ons','ez','ent']
ir_endings = ['is','is','it','issons','issez','issent']
re_endings = ['s','s','','ons','ez','ent']
stem = ''
aVerb2 = widgets.Text(value = None, description = 'Infinitive', placeholder = "Enter a verb")

display(aVerb2)

def callback6(sender):    
    if aVerb2.value != None:
        if aVerb2.value[-2:]=='er':
            stem = aVerb2.value[:-2]
            for i in range(6):
                conjug[i] = stem+er_endings[i]
            clear_output()
            display(aVerb2)
            display(Markdown('An **er** verb with stem **' + stem + '-**'))
            displayTable2()
            return
        if aVerb2.value[-2:]=='ir':
            stem = aVerb2.value[:-2]
            for i in range(6):
                conjug[i] = stem+ir_endings[i]
            clear_output()
            display(aVerb2)
            display(Markdown('An **ir** verb with stem **' + stem + '-**'))
            displayTable2()
            return
        if aVerb2.value[-2:]=='re':
            stem = aVerb2.value[:-2]
            for i in range(6):
                conjug[i] = stem+re_endings[i]
            clear_output()
            display(aVerb2)
            display(Markdown('An **re** verb with stem **' + stem + '-**'))
            displayTable2()
            return
        clear_output()
        display(aVerb2)
        display(Markdown("I don't recongnize this kind of verb. Try again."))
        return

    
aVerb2.on_submit(callback6)

def displayTable2():
    trace0 = go.Table(
      columnorder = [1,2],
      columnwidth = [10,10],
      header = dict(
        values = ['Pronoun','Conjugated'],
        line = dict(color = 'rgb(0,0,0)'),
        fill = dict(color = 'rgb(0,35,48)'),
        align = ['center','center'],
        font = dict(color = 'white', size = 16),
        height = 40
      ),
      cells = dict(
        values = [pronouns,conjug],
        line = dict(color = 'black'),
        fill = dict(color = 'rgb(95,102,161)'),
        align = ['center', 'center'],
        font = dict(color = 'white', size = 14),
        height = 30
        )
    )
    layout = dict(width=500, height=450)
    data = [trace0]
    fig = dict(data = data, layout = layout)
    iplot(fig)


## Many exceptions

Of course, French has many exceptions to the rules for conjugating verbs. To write code to handle them all, you could consider creating a list will all the exceptions in it, and a corresponding list of conjugations for each exception. 

Try this out if you like -- this is an interesting exercise in understanding the complexity of a language, as not everything is simply a simple set of rules. It is also an interesting exercise in how to make code that can handle such complexity. 



---
## Conclusion

In this Jupyter Notebook by Callysto you learned the basics of French verb conjugation in the present tense. You also learned about some basic aspects used in programming such as `for` loops, `if` statements. You additionally learned about strings, lists, and indexing. You were also challenged to see to create your own program  for dealing with irregular verbs. 

We saw that we could expose the structure of the French verb conjugation rules to compose a program that creates the correct responses to conjugate a verb in the present tense. This is somewhat of a hallmark of coding. Taking some sort of structure of the problem at hand and exposing in the form of generalizable and applicable written code. Breaking down problems in this fashion is essential to computational thinking. 

Je vous remercie d'avoir essayé les exercices donnés.


[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)