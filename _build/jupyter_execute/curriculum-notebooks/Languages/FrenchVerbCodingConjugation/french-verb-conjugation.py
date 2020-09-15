![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Languages/FrenchVerbCodingConjugation/French-Verb-Conjugation.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

import numpy as np
#import matplotlib.pyplot as plt
from IPython.display import display, Math, Latex, HTML, clear_output, Markdown, Javascript
import ipywidgets as widgets
from ipywidgets import interact, FloatSlider, IntSlider, interactive, Layout
from traitlets import traitlets
#module to conjugate
#import mlconjug
#from functools import partial
#import pickle


import plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)



# French Verb Conjugation
    
----

## Introduction

In this Jupyter Notebook by Callysto you will learn about French verb conjugation. Mastering the basics of verb conjugation is essential to reading and writing in French. There are some basic rules (and exceptions) that we will address. 

Because much of conjugation is algorithmic, one can write computer code to do the task for us. If you are interested in the programming aspects, please see the related notebook [French-Verb-Coding](CC-186-French-Verb-Coding.ipynb). 

#### Necessary background
- Some basic knowledge of French
- Elementary Python syntax

#### Outline of this notebook

We will cover several important topics
- a review of personal pronouns in French
- two important verbs, Être and Avoir
- the regular verbs, with endings "-er", "-ir" and "-re"
- exceptions to the regular verbs

#### Allons-y!

## Personal pronouns

Conjugation is the processing of force the verb in a sentence to "agree" with the subject of that sentence. Typically, the subject of a sentence is a pronoun, so to start conjugating verbs, we can review the personal pronouns in French. 

Below is table showing the subject pronouns in French. These will be used to separate the different cases of verb conjugation. 

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
#     margin=go.layout.Margin(
#     l=0,
#     r=0,
#     b=0,
#     t=0,
#     pad=0
#     )


data = [trace0]
fig = dict(data = data, layout = layout)

iplot(fig)

Our verb conjugation rules will be based on these personal pronouns, so it is good to get familiar with their translations. French makes a distinction between all of these different tense based on their person, whether or not they are masculine or feminine, and if they are plural or singular. 


## Two Important Verbs

Let's jump right to conjugating the two (arguably) most important verbs: To Be and To Have.



## 1. Être (to be)

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
etre_conjug = ['suis','es','est','sommes','êtes','sont']

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
    values = [french,etre_conjug],
    line = dict(color = 'black'),
    fill = dict(color = 'rgb(95,102,161)'),
    align = ['center', 'center'],
    font = dict(color = 'white', size = 14),
    height = 30
    )
)
layout = dict(
    width=500, 
    height=450)

data = [trace0]
fig = dict(data = data, layout = layout)

iplot(fig)

To use these in a sentence, you could write something like:
- Je suis un garçon.
- Elle est une fille.
- Nous sommes tous les humaines. 

Notice how in each sentence, the form of the verb changes to match subject pronoun. 

"Être" is an irregular verb, that does not obey a certain format, if you will, for conjugating verbs in the present tense. There many examples of exceptions, which we will explore further. But first, the next most important verb:

## 2. Avoir  (to have)

french = ["j'",'tu','elle, il, on','nous','vous','elles, ils']
avoir_conjug = ['ai','as','a','avons','avez','ont']

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
    values = [french,avoir_conjug],
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

Notice for the first person singular we have *j'* instead of *je*, this is due to the fact that the verb starts a vowel. This rule is similar to using "a" and "an" in English. 

## The Regular Verbs

There are three types of regular verbs, which are identified by their endings. They are:
- the "-er" verbs, such as "parler" (to speak)
- the "-ir" verbs, such as "finir" (to finish)
- the "-re" verbs, such as "vendre" (to sell)

Each of these three type has its own pattern for conjugation, which is shared by all other regular verbs of the same typs. Let's have a look at these.

## 1. The "-er" Regular Verbs

There is a general rubric for conjugating verbs that end in **er** in the present tense. 

We will illustrate this with the verb "parler" (to speak). The stem of the verb parler is "parl-". We conjugate it by adding on the endings "e", "es", "e", "ons", "ez" "ent" for the corresponding pronouns, as follows:

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
stem = ['parl-','parl-','parl-','parl-','parl-','parl-']
ending = ['e','es','e','ons','ez','ent']
parler_conjug = ['parle','parles','parle','parlons','parlez','parlent']


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
    values = [french,parler_conjug],
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

This can be taken as the general rule for conjugating **er** verbs in the present tense. All you need to do is find the stem of the verb, which was parl- in this case and then apply these endings to figure out how to conjugate the verb for every personal pronoun.

For instance, try this yourself with the verb "changer" (to sing). The stem is "chant-", so what are the corresponding six conjucations, as in the table above?

This pattern works for most "er" verbs, and there are hundreds of them. Some common ones are:


- aimer	 (to like/love)
- arriver (to arrive, to happen)
- brosser (to brush)
- chanter (to sing
- chercher (to look for)
- danser (to dance)
- demander (to ask for)
- détester (to hate)
- donner (to give)
- écouter (to listen to)
- étudier (to study)
- gagner	(to win, to earn)
- habiter	(to live)
- jouer	(to play)
- manquer	(to miss)
- marcher	(to walk, to function)
- parler	(to talk, to speak)
- penser	(to think)
- regarder	(to watch, to look at)
- travailler	(to work)
- trouver	(to find)
- visiter	(to visit (a place)

There are also many exception for hte **er** verbs, which we will discuss below. 

## 2. The "-ir" Regular Verbs

There is a general rubric for conjugating verbs that end in **ir** in the present tense. 

We will illustrate this with the verb "finir" (to finish). The stem of the verb finit is "fin-". We conjugate it by adding on the endings "is", "is", "it", "issons", "issez" "issent" for the corresponding pronouns, as follows:

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
finir_stem = ['fin-','fin-','fin-','fin-','fin-','fin-']
ir_ending = ['is','is','eit','issons','issez','issent']
finir_conjug = ['finis','finis','finit','finisson','finissez','finissent']


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
    values = [french,finir_conjug],
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

This can be taken as the general rule for conjugating **ir** verbs in the present tense. All you need to do is find the *stem* of the verb, which was fin- in this case and then apply these endings to figure out how to conjugate the verb for every personal pronoun. 

For instance, try this yourself with the verb "grandir" (to grow). The stem is "grand-", so what are the corresponding six conjucations, as in the table above?

This pattern works for most "ir" verbs, and there are hundreds of them. Some common ones are:

- applaudir (to applaud)
- bâtir (to build)
- choisir (to choose)
- désobéir (to disobey)
- finir (to finish)
- grandir (to grow up)
- grossir (to gain weight)
- guérir (to heal, to get well)
- maigrir (to lose weight)
- obéir (to obey)
- punir (to punish)
- réfléchir (to think, to reflect)
- remplir (to fill)
- réussir (to succeed)
- vieillir (to grow old)

Again, though, there will be exceptions...

## 3. The "-re" Regular Verbs

There is a general rubric for conjugating verbs that end in **re** in the present tense. 

We will illustrate this with the verb "vendre" (to sell). The stem of the verb finit is "vend-". We conjugate it by adding on the endings "s", "s", "nothing", "ons", "ez" "ent" for the corresponding pronouns, as follows:

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
vendre_stem = ['vend-','vend-','vend-','vend-','vend-','vend-']
re_ending = ['s','s','','ons','ez','ent']
vendre_conjug = ['vends','vends','vend','vendons','vendez','vendent']


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
    values = [french,vendre_conjug],
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

This can be taken as the general rule for conjugating **re** verbs in the present tense. All you need to do is find the *stem* of the verb, which was vend- in this case and then apply these endings to figure out how to conjugate the verb for every personal pronoun. 

For instance, try this yourself with the verb "grandir" (to grow). The stem is "grand-", so what are the corresponding six conjugations, as in the table above?

This pattern works for most "re" verbs, and there are many of them. Some common ones are:

attendre (to wait)
défendre (to defend)
descendre (to descend)
entendre (to hear)
étendre (to stretch)
fondre (to melt)
pendre (to hang, or suspend)
perdre (to lose)
prétendre (to claim)
rendre (to give back, or return)
répondre (to answer)
vendre (to sell)

Again, though, there will be exceptions...

## 1. Exceptions to the regular er verbs

French is filled with exceptions, which makes it a bit of a difficult language to master as one has to basically dedicate the exceptions to memory. An exception for a verb means that it is not (maybe just partially) conjugating using the endings given above. Most exceptions arise in an alteration of the stem of the verb.

Thankfully there are not many exceptions for the **er** verbs.  Here are three notable ones:

## 1a. The  "-oyer" and "-uyer" exceptions:

For verbs like "envoyer" (to send) or "ennuyer" (to annoy) the stem changes the "y" to an "i" for all pronouns except nous and vous:

french = ["j'",'tu','elle, il, on','nous','vous','elles, ils']
envoyer_conjug = ['envoie', 'envoies','envoie','envoyons','envoyez','envoient']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,envoyer_conjug],
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

## 1b. The "e_er" or "é_er" exceptions:

Verbs like "acheter" (to buy) or "préférer" (to prefer) also follow an exception rule. The accent aigue becomes an accent grave, that is,  é becomes è, except in the nous and vous cases, where it does not change. Note this means the pronunciation of the letter changes as well. 

preferer_conjug = ['préfère','préfères','préfère','préférons','préférez','préfèrent']
french = ['je','tu','elle, il, on','nous','vous','elles, ils']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,preferer_conjug],
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

## 1c. The  " –eler " and " -eter " exceptions:

For verbs like "appeler" (to call) or "rejeter" (to reject) the letters "l" 
or "t" get doubled. Again, this does not hold for the nous and vous cases. 


french = ['je','tu','elle, il, on','nous','vous','elles, ils']
appeler_conjug = ['appelle','appelles','appelle','appelons','appelez','appellent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,appeler_conjug],
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

It's important to be aware of these exceptions, as you will be able to identify patterns in verbs of these forms and the exceptions themselves, like how it doesn't apply for nous and vous. Knowledge of the exceptions is crucial to mastering the language!

## 2. Exceptions to the regular ir verbs

Unfortunately, with the **ir** verbs, there are many, many exceptions.  Three important ones are as follows:

## 2a. Verbs like partir (to leave):

For "partir" (to leave), the keep is to drop the "t" from the stem in the singular case, and add the endings "s", "s", "t". For the plural case, you keep the "t". The conjgations go like this:

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
partir_conjug = ['pars','pars','part','partons','partez','partent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,partir_conjug],
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

Other irregular ir verbs like partir include
- dormir (to sleep)
- mentir (to lie)
- partir (to leave)
- sentir (to feel) 
- servir (to serve)
- sortir (to go out)


## 2b. Verbs that end in -llir, -frir, or -vrir

Curiously, these verbs conjugate like an "er" verb. Just take the stem and add the endings "e", "es", "s", "ons", "ez", "emt." For instance, here is the conjugation for ouvrir (to open):


french = ['je','tu','elle, il, on','nous','vous','elles, ils']
ouvrir_conjug = ['ouvre','ouvres','ouvre','ouvrons','ouvrez','ouvrent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,ouvrir_conjug],
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

Other ir verbs that follow this pattern include:
- couvrir (to cover)
- cueillir (to pick)
- offrir (to offer)
- ouvrir (to open)
- souffrir (to suffer)


## 2c. Verbs that end in -enir

These ones all follow a similar pattern. The stem changes in the singular cases and the endings are just like the first irregular ir case (like partir). Here is the conjugation for tenir (to hold): 

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
tenir_conjug = ['tiens','tiens','tient','tenons','tenez','tenent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,tenir_conjug],
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

Other verbs in this irregular category include: 
- appartenir (to belong)
- contenir (to contain)
- convenir (to suit)
- devenir (to become)
- maintenir (to maintain)
- obtenir (to obtain)
- parvenir (to reach, or achieve)
- prévenir (to warn, or prevent)
- retenir (to retain)
- revenir (to come back)
- soutenir (to support)
- (se) souvenir	(to remember)
- tenir (to hold)
- venir (to come)

## 2d. Other very irregular ir verbs

There are a dozen or so irregular ir verbs that don't fit any pattern. These include many that end in oir, as well as other like acquérir, asseoir, avoir, courir, devoir, falloir, mourir, pleuvoir, pouvoir, recevoir, savoir, servir, valoir, voir. You just have to learn these conjugations individually. 




## 3. Exceptions to the re verbs

As with the other two regular classes, the **re** verbs also have several exceptions. In all cases, the changes involve adding or dropping a consonant in the stem, and possibly adjusting the endings. A quick summary is to say that the unusual changes have to do with making the spelling match the prononciation of the verb forms. In some sense, it is easier to learn what the verbs sound like, and then spell them to match. 

There are four basic exceptions, as follows:

## 3a. The verb prendre (to take) and its relatives

Here, you just drop the "d" from the stem in the plural form, and add an extra "n" in the last case:


french = ['je','tu','elle, il, on','nous','vous','elles, ils']
prendre_conjug = ['prends','prends','prend','prenons','prenez','prennent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,prendre_conjug],
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

## 3b. The verbs battre (to fight) and mettre (to put)

Here, you just drop one "t" from the stem in the singular form:


french = ['je','tu','elle, il, on','nous','vous','elles, ils']
battre_conjug = ['bats','bats','bat','battons','battez','battent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,battre_conjug],
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

## 3c. The verbs rompre (to break) and its relatives
This one is such a tiny exception: an extra t in the third person singular:


french = ['je','tu','elle, il, on','nous','vous','elles, ils']
rompre_conjug = ['romps','romps','rompt','rompons','rompez','rompent']

trace0 = go.Table(
  columnorder = [1,2,3],
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
    values = [french,rompre_conjug],
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

## 3d. Finally, Verbs Ending in –aindre, –eindre, and –oindre

In this case, the dre/tre is dropped to form the stem, and in the plural cases, the letter g is inserted. Again, this is to get the prononciation to match the spelling. 

french = ['je','tu','elle, il, on','nous','vous','elles, ils']
craindre_conjug = ['crains','crains','craint','craignons','craignez','craignent']
joindre_conjug = ['joins','joins','joint','joignon','joignez','joignent']
peintre_conjug = ['peins','peins','peint','peignons','peignez','peignent']

trace0 = go.Table(
  columnorder = [1,2,3,4,5],
  columnwidth = [10,10],
  header = dict(
    values = ['Pronoun','Craindre','Joindre','Peintre'],
    line = dict(color = 'rgb(0,0,0)'),
    fill = dict(color = 'rgb(0,35,48)'),
    align = ['center','center','center','center'],
    font = dict(color = 'white', size = 16),
    height = 40
  ),
  cells = dict(
    values = [french,craindre_conjug,joindre_conjug,peintre_conjug],
    line = dict(color = 'black'),
    fill = dict(color = 'rgb(95,102,161)'),
    align = ['center', 'center','center','center'],
    font = dict(color = 'white', size = 14),
    height = 30
    )
)
layout = dict(width=500, height=450)

data = [trace0]
fig = dict(data = data, layout = layout)

iplot(fig)

## Coding Examples

---

How could one write code to see if someone conjugated a verb correctly? If you are interested in the programming aspects, please see the related notebook [French-Verb-Coding](CC-186-French-Verb-Coding.ipynb). 



#perhaps show how this work for a different verb and subject.

#manipulate this code for 'ir' verbs or try to write your own code to handle the exceptions above.
#remember to use the list user_answer for the user_inputs and don't forget to enter some inputs yourself ;)

# user_answer = [je.value,tu.value,elle.value,nous.value,vous.value,elles.value]

# french = ['je','tu','elle/il/on','nous','vous','elles/ils']
# endings = ['e','es','e','ons','ez','ent']

# for i in range(0,len(endings)):
#     n = len(endings[i])
#     #feel free to change what happens if they get it right or wrong.
#     if user_answer[i] != '':  #So that it doesn't print if nothing has been entered
#         if user_answer[i][-n:] != endings[i]:
#             print('The conjugation for "'+french[i]+'" is incorrect')
#         if user_answer[i][-n:] == endings[i]:
#             print('The conjugation for "'+french[i]+'" is correct!')


---
## Conclusion

In this Jupyter Notebook by Callysto you learned the basics of French verb conjugation in the present tense. In a related noteboo, we see we can expose the structure of the French verb conjugation rules to compose a program that checks if a user input the correct answers to conjugate a verb in the present tense. This is somewhat of a hallmark of coding. Taking some sort of structure of the problem at hand and exposing in the form of generalizable and applicable written code. Breaking down problems in this fashion is essential to computational thinking. 

Je te remercie pour avoir essayer les exercises donner. 

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)