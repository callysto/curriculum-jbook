![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=EnglishLanguageArts/IntroductionToPoetry/poetry-introduction.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

%%html

<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

import curses 
from curses.ascii import isdigit 
import nltk
nltk.download('cmudict', quiet=True) 
#Set quiet to False if nltk isn't loading for "make your own haiku exercise" in case there's an error
from nltk.corpus import cmudict 
d = cmudict.dict()
import string

import ipywidgets as widgets
import IPython

# Poetry - Introduction

There are many different of types of poetry. We will look at four types:
- haiku (high-koo)
- diamante (dee-a-mon-tay) poem
- limerick (limm-err-ik)
- cinquain (sin-kain)

Each one has a structure that makes it unique. <br>
Some poems have a certain number of syllables. <br>
Some poems need to rhyme, though not all poems need to rhyme. 

#### Types of Poetry
1. Shape poetry
    - Makes a shape with the words in the poem
    - This includes diamante and cinquain poems
2. Rhyming poetry 
    - Has a rhyming pattern
    - This includes limericks
3. Haiku poetry
    - Has a haiku form
5. Narrative poetry
    - A long poem telling a story
4. Epic poetry
    - A narrative poem about a hero on an adventure


## Syllables

Syllables are parts of a word that are pronounced. <br>
For example, "hello" has 2 syllables: "**hel-lo**". "Elephant" has 3 syllables: "**el-e-phant**". <br>
Usually, every syllable has one vowel sound in it.<br>
Most vowels in words are not next to other vowels, so a single vowel, sometimes with consonants, is one syllable.<br>
Some vowel sounds are made with 2 vowels like "pair" which only has one syllable.<br>
There are some special words like naive (pronounced nigh-eve) that have 2 vowel sounds next to each other. So "naive" has 2 syllables.

There are different ways to tell how many syllables are in a word or sentence. 
1. How many times your mouth opens 
2. How a robot would speak 
3. Clapping with the syllables

Check how these are done in this video:

from IPython.display import YouTubeVideo
YouTubeVideo('TvcgVRULaWw')

## Practice

How many syllables are in these sentences? Hover over any word to show the word broken into its syllables.

%%html
<script type = "text/javascript" src="sources/syllables.js"></script>

%%html

<div id="sentence1"></div>

<script>
display(1);
</script>

ans1 = widgets.BoundedIntText(min=0, max=15, description='Syllables:')

def question1():
    IPython.display.clear_output()
    print("How many syllables are in the sentence above?")
    print("Write your answer in the box below. Then press enter.")
    IPython.display.display(ans1)
    
def checker1(a):
    question1()
    if ans1.value == 10:
        print("That's right!")
    else:
        print("Not quite, try again. Remember to hover over the words to see them broken down.")
        
question1()
ans1.observe(checker1, 'value')

%%html

<div id="sentence2"></div>

<script>
display(2);
</script>

ans2 = widgets.BoundedIntText(min=0, max=15, description='Syllables:')

def question2():
    IPython.display.clear_output()
    print("How many syllables are in the sentence above?")
    print("Write your answer in the box below. Then press enter.")
    IPython.display.display(ans2)
    
def checker2(a):
    question2()
    if ans2.value == 10:
        print("That's right!")
    else:
        print("Not quite, try again. Remember to hover over the words to see them broken down.")
        
question2()
ans2.observe(checker2, 'value')

## Haiku

<img style="float: right;" src="./images/WorldWithJapan.png" width="600x" height="200x">

A haiku is a type of Japanese style of poetry. It has a syllable structure that makes it unique. 

##### Topic
The topic of a haiku can be anything, but all three lines should be about the same topic.<br>
Usually, a title is included to tell the reader what the topic of the haiku is.

##### Structure
Haikus have 3 lines. The **first** and **last** line must have 5 syllables. <br>
The second line must have 7 syllables. 

**We call this structure a 5-7-5 syllable structure.**

None of the lines usually rhyme. The whole poem looks like this:

>  **Haikus**
>
> The first line has five.
>
> The second line has seven.
>
> The last has five too. 

 This is a haiku about the structure of haikus!  
 
 ### Exercise
 Read the poem below. Does it have the structure of a haiku?
 > **Our ride**
 >
 > We go away
 >
 > On a hot air balloon.
 >
 > It's so much fun!

answer = widgets.RadioButtons(options=['','Yes, "Our ride" follows the 5-7-5 syllable structure', 
                                       'No, "Our ride" does not follow the 5-7-5 syllable structure'], 
                              layout={'width': '600px'}, value = '')
truth = widgets.RadioButtons(options=['','Line 1 has 5. Line 2 has 7. Line 3 has 4.',
                                      'Line 1 has 4. Line 2 has 6. Line 3 has 4.',
                                      'Line 1 has 4. Line 2 has 7. Line 3 has 5.'], value = '')

def displays():
    IPython.display.clear_output()
    IPython.display.display(answer)

def check(a):
    displays()
    if answer.value == 'No, "Our ride" does not follow the 5-7-5 syllable structure':
        print("You are right!")
    else:
        print("Actually, this poem does not follow the 5-7-5 syllable structure.")
    print("How many syllables does each line have?")
    IPython.display.display(truth)
        
def check2(a):
    displays()
    IPython.display.display(truth)
    if truth.value == 'Line 1 has 4. Line 2 has 6. Line 3 has 4.':
        print("That's right! Haikus need the 5-7-5 syllable structure but this poem has a 4-6-4 structure.")
        print("That means this poem is not a haiku.")
    else:
        print("That's not right, try counting the syllables of each line again.")
        
displays()
answer.observe(check, 'value')
truth.observe(check2, 'value')

### Check a word's number of syllables:

Did one word stump you? Don't worry, just type in the word below. We'll tell you how many syllables are in that word. Feel free to use this when completing other exercises if you get stuck.

wordcheck = widgets.Textarea(description='Check a word:', style={'description_width': 'initial'})
checker = widgets.Button(description='Check')

def syllables(word): 
    count = [0]
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count[0] +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count[0] +=1
    if word.endswith('e'):
        count[0] -= 1
    if word.endswith('le'):
        count[0] +=1
    if count[0] == 0:
        count[0] +=1
    return count

def nsyl(word):
    try:
        return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
    except KeyError:
        if KeyError == ' ':
            return [0]
        else:
            return syllables(word)
        
def checking(a):
    count = 0
    IPython.display.clear_output()
    IPython.display.display(wordcheck, checker)
    word = wordcheck.value
    for chunk in word.split(): 
        count += nsyl(chunk)[0]
    print("There are",count,"syllables in",word)
    
IPython.display.display(wordcheck, checker)    
checker.on_click(checking)

*Try the word 'onomatopoeia' in this checker. This word has 6 syllables, but the checker says there's only 5. This is because this checker is NOT perfect. English is hard and there aren't many rules that this computer can follow to be right all the time. Onomatopoeia has 4 vowels in a row which is pronounced in two syllables, but this computer doesn't know that. Ask your teacher if you think this checker is wrong on a word.*

### Try writing your own haiku!
Write your haiku by typing each line of the poem on a new line. Don't include a title. Press submit when your poem is done.

poem = widgets.Textarea(description='Haiku:', layout={'height': '100px', 'width': '400px'})
submit = widgets.Button(description='Submit', button_style='success')

def syllables(word): 
    count = [0]
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count[0] +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count[0] +=1
    if word.endswith('e'):
        count[0] -= 1
    if word.endswith('le'):
        count[0] +=1
    if count[0] == 0:
        count[0] +=1
    return count

def nsyl(word): 
    try:
        return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
    except KeyError:
        if KeyError == ' ':
            return [0]
        else:
            return syllables(word)
        
phrase = poem.value        
#phrase = "This is troubling , There is a dragon ahead , go run for your life"
def check(phrase):
    syllables = []
    for sentence in phrase.split(':'):
        count = 0
        for word in sentence.split():
            wordcount = nsyl(word)
            count += wordcount[0]
        if count != 0:
            syllables.append(count)
    if syllables == [5, 7, 5]:
        print("This is a haiku!")
    else:
        print("This is not a haiku. If you think it is a haiku, it's best to double check with your teacher.")
        print(syllables)
        
def display(a):
    IPython.display.clear_output(wait=False)
    IPython.display.display(poem, submit)
    phrase = poem.value
    #phrase.translate(str.maketrans("", "", string.punctuation))
    for ch in string.punctuation:                                                                                                     
        phrase = phrase.replace(ch, "") 
    phrase = phrase.replace("\n", ":")
    check(phrase)
    
IPython.display.display(poem, submit)    
submit.on_click(display)    

##### Are you wondering how the computer is counting the syllables you typed? 

>Many people have worked really hard to create a dictionary that the computer can call to look up how many syllables are in a certain word. But not all words exist in this dictionary. There's also some rules about how syllables are made that help the computer guess the right number of syllables. Sometimes it's wrong though because English doesn't always follow easy rules.

## Diamante

A diamante poem is a type of shape poetry that has rules for each line.<br>
Not all types of shape poetry need rules.<br>
Some can be in the shape of the topic the poem is about.

##### Topic
A diamante poem is written about two topics, which can be similar or complete opposites.<br>
One topic is for the top of the diamond. The other topic if for the bottom of the diamond.<br>
This type of poem does not usually have a title because the first and line lines tell the reader the topic.

##### Structure
A diamante poem is a type of shape poetry that is written in the shape of a diamond. <br>
- It includes 7 lines. 
- The first topic is for the first 3 lines. 
- The other topic if for the last 3 lines. 
- The middle line, or 4th line, is about both topics. 
- None of the lines need to rhyme.

Each line has a specific rule. Look at the picture below to see the rules.

![structure](https://study.com/cimages/multimages/16/diamantepattern.jpg)
[source](https://study.com/academy/lesson/diamante-poems-lesson-for-kids.html)

An example of a diamante poem about opposites would be:
<div style="text-align:center">
    <span style="color:orange"> Day <br>
                                Light, coloured <br>
                                Shining, seeing, doing </span> <br>
    <span style="color:green"> Morning, Noon, Evening, Midnight </span> <br>
    <span style="color:blue"> Fading, sleeping, dreaming <br>
                                Dark, calm <br>
                                Night </span> <br>
    <div>

### Exercise

What would be a good Topic 1 and Topic 2 for this diamante poem?
<div style="text-align:center">
 <span style="color:orange"> ---Topic 1---  <br>
                             Striped, Hooved <br>
                             Grazing, Drinking, Running </span> <br>
 <span style="color:red"> One from Africa, one from Europe </span> <br>
 <span style="color:purple"> Galloping, Trotting, Neighing <br>
                             Majestic, Hairy <br>
                             ---Topic 2--- </span> <br>
<div>

Which 2 animals would best fit this poem?

topic1 = widgets.RadioButtons(options=['','Tiger', 'Zebra', 'Cow', 'Giraffe'], description='Topic 1', value = '')

def display2():
    IPython.display.clear_output()
    IPython.display.display(topic1)

def checks(a):
    display2()
    if topic1.value == 'Zebra':
        print("That's a great choice! It fits all the descriptions of the first 3 lines.")
    else:
        print("That choice might fit some of the descriptions of the first 3 lines, but not all of them. Try again.")
        
display2()
topic1.observe(checks, 'value')

topic2 = widgets.RadioButtons(options=['','Lion', 'Donkey', 'Horse', 'Pig'], description='Topic 2', value = '')

def display3():
    IPython.display.clear_output()
    IPython.display.display(topic2)
        
def checks2(a):
    display3()
    if topic2.value == 'Horse':
        print("Great choice! The last 3 lines decribe a horse!")
    else:
        print("That choice might fit some of the descriptions of the last 3 lines, but not all of them. Try again.")
        
display3()
topic2.observe(checks2, 'value')

## Limerick

You have probably heard limericks before because they are used very often.<br>
Limericks are a lot of fun to say out loud because they have a rhyming pattern. 

##### Topic
A limerick can be about anything. Like a haiku, all the lines are about the same topic. <br>
It's like a story that has a rhythm when you read it. Most limericks are nonsense stories. <br>
Most of them start with *"There once was a ..."* or *"There was a ..."*

##### Structure
Limericks have 5 lines and they rhyme in a specific pattern. 
- Lines 1, 2, and 5 all have the same number of syllables and rhyme. 
- They each have between 8 and 11 syllables. 
- Lines 3 and 4 have the same number of syllables and rhyme. 
- They have between 5 and 7 syllables. 

<span style="color:orange"> Don't worry too much about the syllables though, it's more important that it's easy to read and rhymes in the right order.<span/>

**Limericks have a AABBA rhyming structure.** <br>
Each letter stands for a line and the letters that are the same mean the lines rhyme. Like this:
<div style="text-align:center">
    <span style="color:blue"> There once was a black cat named Jack, <br>
        Who had a large bag on his back. </span> <br>
    <span style="color:red">He sat on a chair, <br>
        With nothing to wear, </span> <br>
    <span style="color:blue">Except his old dusty knap-sack.</span><br>
    <div>

Listen to this limerick from an episode of SpongeBob:

YouTubeVideo('GG19g9oiF-w')

This limerick tells a funny story about a man eating his shoe in his sleep. 

Lines 1, 2, and 5 had 8 syllables and all ended in the sound "oo".<br> 
Lines 3 and 4 had 5 syllables and all ended in the sound "ight". <br>
So it fits the pattern of a limerick!

#### Exercise

Choose color for every line by last word. Use a different colour for each new sound that has a rhyme.<br> 
If a line doesn't rhyme with any other line, then don't colour it with either colour.

#%%html
#
#<script type = "text/javascript" src="https://d3js.org/d3.v3.min.js"></script>
#<script type = "text/javascript" src="sources/HickoryHighlight.js"></script>

#%%html
#
#<div id="Highlight1">
#<input id="reset1" type="button" value="Reset" onclick="resetHL1()">
#</div>
#<div>
#<input id="submit1" type="button" value="Submit" onclick="submit1()"> 
#<br />
#<text x="50" y="300" font-family="sans-serif" font-size="15px" id="result"> </text>
#</div>
#
#<script>
#display1();
#</script>

from IPython.display import display

lines_1 = ['Hickory, dickory, dock.',
         'The mouse ran up the clock.', 
         'Ther clock struck one.', 
         'The mouse ran down',
         'Hickory, dickory, dock']
colors_1 =["","red","blue"] 
results_1=["","","","",""]
poem_lines_1 = [widgets.HTML(value='<font size="6">'+l+'</font>') for l in lines_1]
poem_buttons_1 = [widgets.ToggleButtons(options=colors_1,style={"button_width":"50px","button_heigth":"50px"}) for l in lines_1]
hboxes_1=[]
for i in range(len(lines_1)):
    hboxes_1.append(widgets.HBox([poem_lines_1[i],poem_buttons_1[i]]))
display(widgets.VBox(hboxes_1))

btn_1=widgets.Button(description='Submit')
display(btn_1)

result_1 = widgets.HTML(value='')
display(result_1)

def on_click0_1(change):
    poem_lines_1[0].value='<font color="'+change['new']+'" size="6">'+lines_1[0]+'</font>'
    results_1[0]=change['new']
def on_click1_1(change):
    poem_lines_1[1].value='<font color="'+change['new']+'"" size="6">'+lines_1[1]+'</font>'
    results_1[1]=change['new']
def on_click2_1(change):
    poem_lines_1[2].value='<font color="'+change['new']+'"" size="6">'+lines_1[2]+'</font>'
    results_1[2]=change['new']
def on_click3_1(change):
    poem_lines_1[3].value='<font color="'+change['new']+'"" size="6">'+lines_1[3]+'</font>'
    results_1[3]=change['new']
def on_click4_1(change):
    poem_lines_1[4].value='<font color="'+change['new']+'"" size="6">'+lines_1[4]+'</font>'
    results_1[4]=change['new']

poem_buttons_1[0].observe(on_click0_1, 'value')
poem_buttons_1[1].observe(on_click1_1, 'value')
poem_buttons_1[2].observe(on_click2_1, 'value')
poem_buttons_1[3].observe(on_click3_1, 'value')
poem_buttons_1[4].observe(on_click4_1, 'value')
    
def check_result_1(button):
    if (results_1==["red","red","blue","blue","red"]) or (results_1==["blue","blue","red","red","blue"]):
        result_1.value="That's right! This poem's pattern is AABBA"
    else:
        result_1.value="Not Quite. Look at the words again. It's about sound and not spelling."

btn_1.on_click(check_result_1)   

pattern2 = widgets.RadioButtons(options=['','Yes, the two patterns match', 'No, the two patterns do not match'], value = '')

def display5():
    IPython.display.clear_output()
    print("Does this pattern match the rhyming pattern of a limerick?")
    IPython.display.display(pattern2)

def check5(a):
    display5()
    if pattern2.value == 'Yes, the two patterns match':
        print("You are right!")
    else:
        print("Actually, the two patterns do match.")
    print("A limerick's rhyming pattern is AABBA and so is this poem's rhyming pattern. Hickory dickory dock is a limerick!")
        
display5()
pattern2.observe(check5, 'value')

#### Try another one!

It works exactly the same way, and if one line doesn't rhyme with any others, then don't use a colour on it.

lines_2 = ['Little Miss Muffet sat on a tuffet',
         'eating her curds and whey,', 
         'along came a spider,', 
         'who sat down beside her',
         'and frightend Miss Muffet away.']
colors_2 =["","red","blue"] 
results_2=["","","","",""]
poem_lines_2 = [widgets.HTML(value='<font size="6">'+l+'</font>') for l in lines_2]
poem_buttons_2 = [widgets.ToggleButtons(options=colors_2,style={"button_width":"50px","button_heigth":"50px"}) for l in lines_2]
hboxes_2=[]
for i in range(len(lines_2)):
    hboxes_2.append(widgets.HBox([poem_lines_2[i],poem_buttons_2[i]]))
display(widgets.VBox(hboxes_2))

btn_2=widgets.Button(description='Submit')
display(btn_2)

result_2 = widgets.HTML(value='')
display(result_2)

def on_click0_2(change):
    poem_lines_2[0].value='<font color="'+change['new']+'" size="6">'+lines_2[0]+'</font>'
    results_2[0]=change['new']
def on_click1_2(change):
    poem_lines_2[1].value='<font color="'+change['new']+'"" size="6">'+lines_2[1]+'</font>'
    results_2[1]=change['new']
def on_click2_2(change):
    poem_lines_2[2].value='<font color="'+change['new']+'"" size="6">'+lines_2[2]+'</font>'
    results_2[2]=change['new']
def on_click3_2(change):
    poem_lines_2[3].value='<font color="'+change['new']+'"" size="6">'+lines_2[3]+'</font>'
    results_2[3]=change['new']
def on_click4_2(change):
    poem_lines_2[4].value='<font color="'+change['new']+'"" size="6">'+lines_2[4]+'</font>'
    results_2[4]=change['new']

poem_buttons_2[0].observe(on_click0_2, 'value')
poem_buttons_2[1].observe(on_click1_2, 'value')
poem_buttons_2[2].observe(on_click2_2, 'value')
poem_buttons_2[3].observe(on_click3_2, 'value')
poem_buttons_2[4].observe(on_click4_2, 'value')

def check_result_2(button):
    if (results_2==["","red","blue","blue","red"]) or (results_2==["","blue","red","red","blue"]) \
    or (results_2==["blue","red","","","red"]) or (results_2==["blue","","red","red",""]) \
    or (results_2==["red","blue","","","blue"]) or (results_2==["red","","blue","blue",""]):
        result_2.value="That's right! This poem's pattern is ABCCB."
    else:
        result_2.value="Not Quite. Look at the words again. Remember not all lines have to rhyme."

btn_2.on_click(check_result_2)  

pattern = widgets.RadioButtons(options=['','Yes, the two patterns match', 'No, the two patterns do not match'], value = '')

def display4():
    IPython.display.clear_output()
    print("Does this pattern match the rhyming pattern of a limerick?")
    IPython.display.display(pattern)

def check4(a):
    display4()
    if pattern.value == 'No, the two patterns do not match':
        print("You are right!")
    else:
        print("Actually, the two patterns don't match.")
    print("A limerick's rhyming pattern is actually AABBA. This poem is close though, so many people do call this poem a limerick.")
        
display4()
pattern.observe(check4, 'value')

## Cinquain

A cinquain poem was named that because it's close to the latin word for "five".<br> 
This is relevant because this poem has 5 lines. <br>
A cinquain is also a type of shape poetry like the diamante, but each line has different rules and the result is a different shape.

##### Topic
A cinquain can be about anything. All the lines are about the same topic. <br>
There usually isn't a title because the first and last lines act as a title by telling the reader the topic.

##### Structure
- It has 5 lines. 
- Each line has rules like the diamante poem. 
- A cinquain poem has these rules:

![cinquain](https://littlelearningangels.weebly.com/uploads/7/1/2/4/71241245/published/download-1.jpg?1512469267)
[source](https://littlelearningangels.weebly.com/cinquain-poetry.html)

Here's an example of a cinquain:

> Flower
>
> Sweet, Beautiful
>
> Growing, Blooming, Smelling
>
> Has a lovely scent
>
> Rose

### Extend your knowledge

Take your favourite book and write a poem about its story. <br>
You can use any book and any style of poem from this notebook. <br>
Can you make one of each type of poem about the same story?

## What did we learn?

We learned that:
* There are many types of poetry. Not all of them rhyme.
* Haikus have a 5-7-5 syllable structure
* Limericks have a AABBA rhyming structure
* Diamantes and cinquains are shape poetry with rules for each line

You can write many poems with all the things you learned in this notebook! <br>
Poems are a great way to tell a story with only a few words.

If you want to read more poetry, go to your school or public library and look for:
* *Where the Sidewalk Ends* by Shel Silverstein
* *A Bad Case of the Giggles* by Bruce Lansky
* *Vanishing Trick* by Ros Asquith 
* *Poetry for Young People* by Emily Dickinson

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)