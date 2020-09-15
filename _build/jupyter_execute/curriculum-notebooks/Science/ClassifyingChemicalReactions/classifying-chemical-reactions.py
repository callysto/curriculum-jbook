![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ClassifyingChemicalReactions/classifying-chemical-reactions.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

(Click **Cell** > **Run All** before proceeding.) 

%matplotlib inline
from helper import *

# Classifying Chemical Equations

## Introduction

A **chemical equation** is used to describe the  process that involves the rearrangement of the atoms in the molecular or ionic structure of a substance or material. All chemical reactions involve the formation or destruction of chemical bonds wherein reactants are transformed into products. Chemical reactions take place all around us and within us. Many of these chemical reactions share similar characteristics to one another, which allow them to be grouped and classified in a number of different ways. One common classification scheme organizes chemical reactions into four types: 

* <a href="#combination">Combination reactions</a> 
* <a href="#decomposition">Decomposition reactions</a> 
* <a href="#single">Single replacement reactions</a>
* <a href="#double">Double replacement reactions</a>

## <a id="combination"> #1 Combination Reaction</a>

A **combination reaction** (also called a *synthesis reaction*) describes the process in which two or more reactants combine to form a new singular product. The general form for a combination reaction is given below: 

<img src="images/combination_reaction.svg" width="55%"/>

The reactant side may contain two or more elements or compounds, but the product side will always contain only one compound. This is the key characteristic of a combination reaction. Combination reactions may include reactions between two or more elements:

2H<sub>2</sub> + O<sub>2</sub> &rarr; 2H<sub>2</sub>O

Between elements and compounds:

O<sub>2</sub> + 2CO &rarr; 2CO<sub>2</sub>

Or between compounds:

CaO + CO<sub>2</sub> &rarr; CaCO<sub>3</sub>

The new bonds formed in the product are often lower in energy than the bonds in the reactants. When this occurs, energy is released, often in the form of heat. As a consequence, combination reactions are usually exothermic.

## Practice Problems

**Question:** *Select 'True' or 'False' for each of the follow statements.* 

randomize_1 = random.randint(1, 2)
if randomize_1 == 1:
    option_1 = "Combination reactions are often exothermic."; bool_1 = True
elif randomize_1 == 2:
    option_1 = "Combination reactions are often endothermic."; bool_1 = False

randomize_1 = random.randint(1, 4)
if randomize_1 == 1:
    option_2 = "Combination reactions always have two or more reactants, but only one product."; bool_2 = True
elif randomize_1 == 2:
    option_2 = "Combination reactions always have two or more reactants, but only one product."; bool_2 = True    
elif randomize_1 == 3:
    option_2 = "Combination reactions always have two or more reactants, and two or more products."; bool_2 = False
elif randomize_1 == 4:
    option_2 = "Combination reactions always have one reactant, and one product."; bool_2 = False

randomize_1 = random.randint(1, 6)
if randomize_1 == 1:
    option_3 = "The general form of a combination reaction is: A + B &rarr; AB."; bool_3 = True
elif randomize_1 == 2:
    option_3 = "The general form of a combination reaction is: A + B &rarr; AB."; bool_3 = True
elif randomize_1 == 3:
    option_3 = "The general form of a combination reaction is: A + B &rarr; AB."; bool_3 = True
elif randomize_1 == 4:
    option_3 = "The general form of a combination reaction is: AB &rarr; A + B."; bool_3 = False
elif randomize_1 == 5:
    option_3 = "The general form of a combination reaction is: AB + X &rarr; XB + A."; bool_3 = False
elif randomize_1 == 6:
    option_3 = "The general form of a combination reaction is: AB + XY &rarr; XB + AY."; bool_3 = False

randomize_1 = random.randint(1, 2)
if randomize_1 == 1:
    option_4 = "The product generated from a combination reaction is always a compound."; bool_4 = True
elif randomize_1 == 2:
    option_4 = "The product generated from a combination reaction is always an element."; bool_4 = False    

true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "True", "False")

**Question:** *Which of the follow chemical reactions is a combination reaction?* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Ba + F<sub>2</sub> &rarr; BaF<sub>2</sub>" 
option_2 = "NaCl + AgNO<sub>3</sub> &rarr; AgCl + NaNO<sub>3</sub>"
option_3 = "CH<sub>4</sub> + 2O<sub>2</sub> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O"
option_4 = "2NaCl + F<sub>2</sub> &rarr; 2NaF + Cl<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Fe + S &rarr; FeS" 
option_2 = "2HBr + Cl<sub>2</sub> &rarr; 2HCl + Br<sub>2</sub>"
option_3 = "C<sub>2</sub>H<sub>5</sub>OH + 3O<sub>2</sub> &rarr; 2CO<sub>2</sub> + 3H<sub>2</sub>O"
option_4 = "Zn + 2HCl &rarr; ZnCl<sub>2</sub> + H<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "MgO + CO<sub>2</sub> &rarr; MgCO<sub>3</sub>" 
option_2 = "Na<sub>2</sub>CO<sub>3</sub> &rarr; Na<sub>2</sub>O + CO<sub>2</sub>"
option_3 = "4NH<sub>3</sub> + 3O<sub>2</sub> &rarr; 2N<sub>2</sub> + 6H<sub>2</sub>O"
option_4 = "NaNO<sub>3</sub> + KCl &rarr; KNO<sub>3</sub> + NaCl"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2S + 3O<sub>2</sub> &rarr; 2SO<sub>3</sub>" 
option_2 = "CaCO<sub>3</sub> &rarr; CaO + CO<sub>2</sub>"
option_3 = "C<sub>3</sub>H<sub>8</sub> + 5O<sub>2</sub> &rarr; 3CO<sub>2</sub> + 4H<sub>2</sub>O"
option_4 = "KBr + AgNO<sub>3</sub> &rarr; KNO<sub>3</sub> + AgBr"

multiple_choice(option_1, option_2, option_3, option_4)

## <a id="decomposition"> #2 Decomposition Reaction</a>

A **decomposition reaction** describes the process in which a single reactant breaks down to form two or more products. The general form for a decomposition reaction is given below:

<img src="images/decomposition_reaction.svg" width="55%"/>

The reactant side will always contain a compound, but the product side may contain two or more elements or compounds. This is the key characteristic of a decomposition reaction. For example, the products may include two or more elements:

2H<sub>2</sub>O &rarr; 2H<sub>2</sub> + O<sub>2</sub>

Elements and compounds:

2KClO<sub>3</sub> &rarr; 3O<sub>2</sub> + 2KCl

Or two or more compounds:

NH<sub>4</sub>Cl &rarr; NH<sub>3</sub> + HCl

The new bonds formed in the products are often higher in energy than the bonds in the reactant. When this occurs, some energy, usually in the form of heat, is needed. As a consequence, decomposition reactions are usually endothermic.

## Practice Problems

**Question:** *Select 'True' or 'False' for each of the follow statements.* 

randomize_2 = random.randint(1, 2)
if randomize_2 == 1:
    option_1 = "Decomposition reactions are often endothermic."; bool_1 = True
elif randomize_2 == 2:
    option_1 = "Decomposition reactions are often exothermic."; bool_1 = False

randomize_2 = random.randint(1, 4)
if randomize_2 == 1:
    option_2 = "Decomposition reactions always have one reactant, but two or more products."; bool_2 = True
elif randomize_2 == 2:    
    option_2 = "Decomposition reactions always have one reactant, but two or more products."; bool_2 = True
elif randomize_2 == 3:
    option_2 = "Decomposition reactions always have two or more reactants, and two or more products."; bool_2 = False
elif randomize_2 == 4:
    option_2 = "Decomposition reactions always have one reactant, and one product."; bool_2 = False

randomize_2 = random.randint(1, 6)
if randomize_2 == 1:
    option_3 = "The general form of a decomposition reaction is: AB &rarr; A + B."; bool_3 = True
elif randomize_2 == 2:
    option_3 = "The general form of a decomposition reaction is: AB &rarr; A + B."; bool_3 = True
elif randomize_2 == 3:
    option_3 = "The general form of a decomposition reaction is: AB &rarr; A + B."; bool_3 = True
elif randomize_2 == 4:
    option_3 = "The general form of a decomposition reaction is: A + B &rarr; AB."; bool_3 = False
elif randomize_2 == 5:
    option_3 = "The general form of a decomposition reaction is: AB + X &rarr; XB + A."; bool_3 = False
elif randomize_2 == 6:
    option_3 = "The general form of a decomposition reaction is: AB + XY &rarr; XB + AY."; bool_3 = False

randomize_2 = random.randint(1, 2)
if randomize_2 == 1:
    option_4 = "The reactant in a decomposition reaction is always a compound."; bool_4 = True
elif randomize_2 == 2:
    option_4 = "The reactant in a decomposition reaction is always an element."; bool_4 = False    

true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "True", "False")

**Question:** *Which of the follow chemical reactions is a decomposition reaction?* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2Ni<sub>2</sub>O<sub>3</sub> &rarr; 4Ni + 3O<sub>2</sub>" 
option_2 = "Na<sub>2</sub>S + 2HCl &rarr; 2NaCl + H<sub>2</sub>S"
option_3 = "SeCl<sub>6</sub> + O<sub>2</sub> &rarr; SeO<sub>2</sub> + 3Cl<sub>2</sub>"
option_4 = "Ba + F<sub>2</sub> &rarr; BaF<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Al<sub>2</sub>O<sub>3</sub> &rarr; Al + O<sub>2</sub>" 
option_2 = "2NaOH + CaBr<sub>2</sub> &rarr; 2NaBr + Ca(OH)<sub>2</sub>"
option_3 = "Fe + S &rarr; FeS"
option_4 = "Zn + 2HCl &rarr; H<sub>2</sub> + ZnCl<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2NaClO<sub>3</sub> &rarr; 2NaCl + 3O<sub>2</sub>" 
option_2 = "MgO + CO<sub>2</sub> &rarr; MgCO<sub>3</sub>"
option_3 = "2NaCl + F<sub>2</sub> &rarr; 2NaF + Cl<sub>2</sub>"
option_4 = "CH<sub>4</sub> + 2O<sub>2</sub> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "CaCO<sub>3</sub> &rarr; CaO + CO<sub>2</sub>" 
option_2 = "2S + 3O<sub>2</sub> &rarr; 2SO<sub>3</sub>"
option_3 = "2Al + 3Cu(NO<sub>3</sub>)<sub>2</sub> &rarr; 3Cu + 2Al(NO<sub>3</sub>)<sub>3</sub>"
option_4 = "FeS + 2HCl &rarr; FeCl<sub>2</sub> + H<sub>2</sub>S"

multiple_choice(option_1, option_2, option_3, option_4)

## <a id="single"> #3 Single Replacement Reaction</a>

A **single replacement reaction** (also called a *single displacement reaction*) describes the process in which one element replaces another element in a compound. The general form for a single replacement reaction is given below:

<img src="images/single_displacement_reaction.svg" width="78%"/>

The reactant side always contains at least one pure element and one compound. Likewise, the product side always contains at least one pure element and one compound. Only positive ions (cations) can replace other positive ions, while only negative ions (anions) can replace other negative ions. In the general equation shown above, <b>X</b> must be positive because it replaces <b>A</b>. If <b>X</b> was negative, then it would replace <b>B</b>.

Below is an example of cation replacement, in which the positive ion (Ni<sup>2+</sup>) is replaced by another positive ion (Zn<sup>2+</sup>):

<span style="color:red">Ni</span>Cl<sub>2</sub> + <span style="color:blue">Zn</span> &rarr; <span style="color:blue">Zn</span>Cl<sub>2</sub> + <span style="color:red">Ni</span>

Below is an example of anion replacement, in which the negative ion (Br<sup>-</sup>) is replaced by another negative ion (Cl<sup>-</sup>):

2Na<span style="color:red">Br</span> + <span style="color:blue">Cl<sub>2</sub></span> &rarr; 2Na<span style="color:blue">Cl</span> + <span style="color:red">Br<sub>2</sub></span>

Notice how the elements shown in <span style="color:blue">blue</span> replace the elements shown in <span style="color:red">red</span> in each of these examples.

## Practice Problems

**Question:** *Select 'True' or 'False' for each of the follow statements.* 

randomize_3 = random.randint(1, 2)
if randomize_3 == 1:
    option_1 = "Single replacement reactions are also called single displacement reactions."; bool_1 = True
elif randomize_3 == 2:
    option_1 = "Single replacement reactions are also called synthesis reactions."; bool_1 = False

randomize_3 = random.randint(1, 4)
if randomize_3 == 1:
    option_2 = "The reactants used in a single replacement reaction always include one element and one compound."; bool_2 = True
elif randomize_3 == 2:
    option_2 = "The reactants used in a single replacement reaction always include one element and one compound."; bool_2 = True
elif randomize_3 == 3:
    option_2 = "The reactants used in a single replacement reaction always include two elements and no compounds."; bool_2 = False
elif randomize_3 == 4:
    option_2 = "The reactants used in a single replacement reaction always include two compounds and no elements."; bool_2 = False
    
randomize_3 = random.randint(1, 6)
if randomize_3 == 1:
    option_3 = "The general form of a single replacement reaction is: AB + X &rarr; XB + A."; bool_3 = True
elif randomize_3 == 2:
    option_3 = "The general form of a single replacement reaction is: AB + X &rarr; XB + A."; bool_3 = True
elif randomize_3 == 3:
    option_3 = "The general form of a single replacement reaction is: AB + Y &rarr; AY + B."; bool_3 = True
elif randomize_3 == 4:
    option_3 = "The general form of a single replacement reaction is: AB &rarr; A + B."; bool_3 = False
elif randomize_3 == 5:
    option_3 = "The general form of a single replacement reaction is: A + B &rarr; AB."; bool_3 = False
elif randomize_3 == 6:
    option_3 = "The general form of a single replacement reaction is: AB + XY &rarr; XB + AY."; bool_3 = False

randomize_3 = random.randint(1, 4)
if randomize_3 == 1:
    option_4 = "The products generated from a single replacement reaction always include one element and one compound."; bool_4 = True
elif randomize_3 == 2:
    option_4 = "The products generated from a single replacement reaction always include one element and one compound."; bool_4 = True
elif randomize_3 == 3:
    option_4 = "The products generated from a single replacement reaction always include two elements and no compounds."; bool_4 = False    
elif randomize_3 == 4:
    option_4 = "The products generated from a single replacement reaction always include two compounds and no elements."; bool_4 = False 
    
true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "True", "False")

**Question:** *Which of the follow chemical reactions is a single replacement reaction?* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2Ag(NO<sub>3</sub>) + Cu &rarr; Cu(NO<sub>3</sub>)<sub>2</sub> + 2Ag" 
option_2 = "2Na + Cl<sub>2</sub> &rarr; 2NaCl"
option_3 = "2Ag<sub>2</sub>O &rarr; 4Ag + O<sub>2</sub>"
option_4 = "2MgI<sub>2</sub> + Mn(SO<sub>3</sub>)<sub>2</sub> &rarr; 2MgSO<sub>3</sub> + MnI<sub>4</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2KI + Br<sub>2</sub> &rarr; 2KBr + I<sub>2</sub>" 
option_2 = "2Ca + O<sub>2</sub> &rarr; 2CaO"
option_3 = "2NO<sub>2</sub> &rarr; 2O<sub>2</sub> + N<sub>2</sub>"
option_4 = "Na<sub>3</sub>PO<sub>4</sub> + 3KOH &rarr; 3NaOH + K<sub>3</sub>PO<sub>4</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Zn + H<sub>2</sub>SO<sub>4</sub> &rarr; ZnSO<sub>4</sub> + H<sub>2</sub>" 
option_2 = "2Li + S &rarr; Li<sub>2</sub>S"
option_3 = "C<sub>3</sub>H<sub>6</sub>O + 4O<sub>2</sub> &rarr; 3CO<sub>2</sub> + 3H<sub>2</sub>O"
option_4 = "Ca(OH)<sub>2</sub> &rarr; CaO + H<sub>2</sub>O"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Cl<sub>2</sub> + CaI<sub>2</sub> &rarr; CaCl<sub>2</sub> + I<sub>2</sub>" 
option_2 = "3H<sub>2</sub> + N<sub>2</sub> &rarr; 2NH<sub>3</sub>"
option_3 = "2Hg<sub>2</sub>O &rarr; 4Hg + O<sub>2</sub>"
option_4 = "AgNO<sub>3</sub> + KI &rarr; AgI + KNO<sub>3</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

### Reactivity Series

The reactivity of a metal is determined by its tendency to donate electrons (a process known as **oxidation**). The reactivity of a halogen is determined by its tendency to accept electrons (a process known as **reduction**). A list or metals and halogens in order of their reactivity (highest to lowest) is called a **reactivity series** (or *activity series*). Only metals of higher reactivity can replace metals with lower reactivity. Likewise, only halogens of higher reactivity can replace halogens with lower reactivity. Below is a reactivity series for some common metals and halogens:

Metals       | Cations           | Halogens | Anions
---          | ---               | ---      | ---                                                          
Potassium    | K<sup>+</sup>     | Fluorine | F<sup>-</sup>                                                                
Sodium       | Na<sup>+</sup>    | Chlorine | Cl<sup>-</sup>
Calcium      | Ca<sup>2+</sup>   | Bromine  | Br<sup>-</sup>
Magnesium    | Mg<sup>2+</sup>   | Iodine   | I<sup>-</sup>
Aluminum     | Al<sup>3+</sup>   | 
Manganese    | Mn<sup>2+</sup>   |  
Zinc         | Zn<sup>2+</sup>   | 
Chromium     | Cr<sup>3+</sup>   | 
Iron         | Fe<sup>2+</sup>   | 
Cobalt       | Co<sup>2+</sup>   | 
Nickle       | Ni<sup>2+</sup>   | 
Tin          | Sn<sup>2+</sup>   | 
Lead         | Pb<sup>2+</sup>   | 
Hydrogen     | H<sup>+</sup>     | 
Copper       | Cu<sup>2+</sup>   | 
Mercury      | Hg<sup>2+</sup>   | 
Silver       | Ag<sup>+</sup>    | 
Gold         | Au<sup>3+</sup>   | 
Platinum     | Pt<sup>4+</sup>   | 

The reactivity series can be used to determine if a reaction will spontaneously occur. If the replacing element is more reactive (higher on the list) than the element it is replacing, then the reaction will spontaneously occur.

**Question:** *Using the reactivity series shown above, predict if each reaction will, or will not, spontaneously occur.* 

randomize_4 = random.randint(1, 2)
if randomize_4 == 1:
    option_1 = "Al + H<sub>2</sub>O &rarr;"; bool_1 = True
elif randomize_4 == 2:
    option_1 = "Ag + H<sub>2</sub>O &rarr;"; bool_1 = False

randomize_4 = random.randint(1, 2)
if randomize_4 == 1:
    option_2 = "AlPO<sub>4</sub> + Mg &rarr;"; bool_2 = True
elif randomize_4 == 2:
    option_2 = "AlPO<sub>4</sub> + Ni&rarr;"; bool_2 = False

randomize_4 = random.randint(1, 2)
if randomize_4 == 1:
    option_3 = "F<sub>2</sub> + CaCl<sub>2</sub> &rarr;"; bool_3 = True
elif randomize_4 == 2:
    option_3 = "Br<sub>2</sub> + CaCl<sub>2</sub> &rarr;"; bool_3 = False

randomize_4 = random.randint(1, 2)
if randomize_4 == 1:
    option_4 = "CuSO<sub>4</sub> + Zn &rarr;"; bool_4 = True
elif randomize_4 == 2:
    option_4 = "CuSO<sub>4</sub> + Hg &rarr;"; bool_4 = False
   
true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "Will occur", "Will not occur")

## <a id="double"> #4 Double Replacement Reaction </a>

A **double replacement reaction** (also called a *double displacement reaction*) describes the process in which the positive and negative ions from two compounds replace one another. The general form for a double replacement reaction is given below:

<img src="images/double_displacement_reaction.svg" width="92%"/>

The reactant side always contains two compounds. Likewise, the product side always contains two compounds. Only positive ions (cations) can exchange places with other positive ions. Likewise, only negative ions (anions) can exchange places with other negative ions.

An example of a double replacement reaction is:

<span style="color:red">NaCl</span> + <span style="color:blue">AgNO<sub>3</sub></span> &rarr; <span style="color:blue">Ag</span><span style="color:red">Cl</span> + <span style="color:red">Na</span><span style="color:blue">NO<sub>3</sub></span>

## Practice Problems

**Question:** *Select 'True' or 'False' for each of the follow statements.* 

randomize_5 = random.randint(1, 2)
if randomize_5 == 1:
    option_1 = "Double replacement reactions are also called double displacement reactions."; bool_1 = True
elif randomize_5 == 2:
    option_1 = "Double replacement reactions are also called analysis reactions."; bool_1 = False

randomize_5 = random.randint(1, 4)
if randomize_5 == 1:
    option_2 = "The reactants used in a double replacement reaction always include two compounds."; bool_2 = True
elif randomize_5 == 2:
    option_2 = "The reactants used in a double replacement reaction always include two compounds."; bool_2 = True
elif randomize_5 == 3:
    option_2 = "The reactants used in a double replacement reaction always include two elements."; bool_2 = False
elif randomize_5 == 4:
    option_2 = "The reactants used in a double replacement reaction always include one element and one compound."; bool_2 = False
    
randomize_5 = random.randint(1, 6)
if randomize_5 == 1:
    option_3 = "The general form of a double replacement reaction is: AB + XY &rarr; XB + AY."; bool_3 = True
elif randomize_5 == 2:
    option_3 = "The general form of a double replacement reaction is: AB + XY &rarr; XB + AY."; bool_3 = True
elif randomize_5 == 3:
    option_3 = "The general form of a double replacement reaction is: AB + XY &rarr; AY + XB."; bool_3 = True
elif randomize_5 == 4:
    option_3 = "The general form of a double replacement reaction is: A + B &rarr; AB."; bool_3 = False
elif randomize_5 == 5:
    option_3 = "The general form of a double replacement reaction is: AB &rarr; A + B."; bool_3 = False
elif randomize_5 == 6:
    option_3 = "The general form of a double replacement reaction is: AB + X &rarr; XB + A."; bool_3 = False

randomize_5 = random.randint(1, 4)
if randomize_5 == 1:
    option_4 = "The products generated from a double replacement reaction always include two compounds."; bool_4 = True
elif randomize_5 == 2:
    option_4 = "The products generated from a double replacement reaction always include two compounds."; bool_4 = True
elif randomize_5 == 3:
    option_4 = "The products generated from a double replacement reaction always include two elements."; bool_4 = False    
elif randomize_5 == 4:
    option_4 = "The products generated from a double replacement reaction always include one element and one compound."; bool_4 = False 
    
true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "True", "False")

**Question:** *Which of the follow chemical reactions is a double replacement reaction?* 

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "2NaOH + CaBr<sub>2</sub> &rarr; 2NaBr + Ca(OH)<sub>2</sub>" 
option_2 = "3Mg + N<sub>2</sub> &rarr; Mg<sub>3</sub>N<sub>2</sub>"
option_3 = "2Ni<sub>2</sub>O<sub>3</sub> &rarr; 4Ni + 3O<sub>2</sub>"
option_4 = "3AgNO<sub>3</sub> + Ni &rarr; Ni(NO)<sub>3</sub> + 3Ag"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Li<sub>2</sub>SO<sub>4</sub> + BaCl<sub>2</sub> &rarr; 2LiCl + BaSO<sub>4</sub>" 
option_2 = "4Li + O<sub>2</sub> &rarr; 2Li<sub>2</sub>O"
option_3 = "Al<sub>2</sub>O<sub>3</sub> &rarr; Al + O<sub>2</sub>"
option_4 = "2AlBr<sub>3</sub> + 3Cl<sub>2</sub> &rarr; 2AlCl<sub>3</sub> + 3Br<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "Na<sub>2</sub>S + 2HCl &rarr; 2NaCl + H<sub>2</sub>S" 
option_2 = "2Cr + 3O<sub>2</sub> &rarr; 2CrO<sub>3</sub>"
option_3 = "CaCO<sub>3</sub> &rarr; CaO + CO<sub>2</sub>"
option_4 = "2Na + 2H<sub>2</sub>O &rarr; 2NaOH + H<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#import random
#from IPython.display import clear_output, display, HTML

option_1 = "HCl + NaOH &rarr; NaCl + H<sub>2</sub>O" 
option_2 = "MgO + H<sub>2</sub>O &rarr; Mg(OH)<sub>2</sub>"
option_3 = "H<sub>2</sub>CO<sub>3</sub> &rarr; CO<sub>2</sub> + H<sub>2</sub>O"
option_4 = "2NaI + Br<sub>2</sub> &rarr; 2NaBr + I<sub>2</sub>"

multiple_choice(option_1, option_2, option_3, option_4)

### Solubility Chart

Often, double replacement reactions result in the precipitation of one product. **Precipitation** occurs when a substance is deposited in the form of a solid from a solution. A solubility chart can be used to determine whether or not a product will precipitate or remain in solution. An example of a solubility chart is shown below:

Anions                                    | Cations that form soluble compounds | Cations that form insoluble compounds
---                                       | ---                                 | ---                                                             
Nitrate (NO<sub>3</sub><sup>-</sup>)      | All                                 | None
Acetate (CH<sub>3</sub>COO<sup>-</sup>)   | All                                 | None
Chlorate (ClO<sub>3</sub><sup>-</sup>)    | All                                 | None
Perchlorate (ClO<sub>4</sub><sup>-</sup>) | All                                 | None
----------------------------------- | ----------------------------------- | -----------------------------------
Chloride (Cl<sup>-</sup>)                 | Most                                | Ag, Hg(I), Pb(II)
Bromide (Br<sup>-</sup>)                  | Most                                | Ag, Hg(I), Pb(II)
Iodide (I<sup>-</sup>)                    | Most                                | Ag, Hg(I), Pb(II)
----------------------------------- | ----------------------------------- | -----------------------------------
Fluoride (F<sup>-</sup>)                  | Most                                | Mg, Ca, Sr, Ba, Pb(II)
----------------------------------- | ----------------------------------- | -----------------------------------
Sulfate (SO<sub>4</sub><sup>2-</sup>)     | Most                                | Ba, Pb(II), Sr
----------------------------------- | ----------------------------------- | -----------------------------------
Carbonate (CO<sub>3</sub><sup>2-</sup>)   | (Group 1 Metals), NH<sub>4</sub>      | Most
Sulfite (SO<sub>3</sub><sup>2-</sup>)     | (Group 1 Metals), NH<sub>4</sub>      | Most
Phosphate (PO<sub>4</sub><sup>3-</sup>)   | (Group 1 Metals), NH<sub>4</sub>      | Most
Chromate (CrO<sub>4</sub><sup>2-</sup>)   | (Group 1 Metals), NH<sub>4</sub>      | Most
----------------------------------- | ----------------------------------- | -----------------------------------
Sulfide (S<sup>2-</sup>)                  | (Group 1 Metals), NH<sub>4</sub>, Ca, Ba, Sr | Most
Hydroxide (OH<sup>-</sup>)                | (Group 1 Metals), NH<sub>4</sub>, Ca, Ba, Sr | Most

To use the solubility chart, match the anion and cation in the compound using the rows and columns on the chart. If the resulting compound is located in the second column, then the compound is soluble. If the compound is located in the third column, then the compound is insoluble.

For example, consider the following reaction:

AgNO<sub>3</sub> + KCl &rarr; AgCl + KNO<sub>3</sub>

There are two products, AgCl and KNO<sub>3</sub>, formed in this reaction. For AgCl, the anion is chloride (Cl<sup>-</sup>) and the cation is silver (Ag<sup>+</sup>). Matching the anion and cation on the solubility table above (row 5, column 3) indicates that the compound is insoluble. In other words, the compound will form a precipitate. 

For KNO<sub>3</sub>, the anion is nitrate (NO<sub>3</sub><sup>-</sup>) and the cation is potassium (K<sup>+</sup>). Matching the anion and cation on the solubility table above (row 1, column 2) indicates that the compound is soluble. In other words, the compound will remain in solution.

**Question:** *Using the solubility chart shown above, predict if each compound highlighted in <span style='color:red'>red</span> will dissolve or form a precipitate.*

randomize_6 = random.randint(1, 2)
if randomize_6 == 1:
    option_1 = "Pb(NO<sub>3</sub>)<sub>2</sub> + 2AgCl &rarr; PbCl<sub>2</sub> + <span style='color:red'>2AgNO<sub>3</sub></span>"; bool_1 = True
elif randomize_6 == 2:
    option_1 = "Pb(NO<sub>3</sub>)<sub>2</sub> + 2AgCl &rarr; <span style='color:red'>PbCl<sub>2</sub></span> + 2AgNO<sub>3</sub>"; bool_1 = False

randomize_6 = random.randint(1, 2)
if randomize_6 == 1:
    option_2 = "Mg(NO<sub>3</sub>)<sub>2</sub> + 2NaOH &rarr; Mg(OH)<sub>2</sub> + <span style='color:red'>2NaNO<sub>3</sub></span>"; bool_2 = True
elif randomize_6 == 2:
    option_2 = "Mg(NO<sub>3</sub>)<sub>2</sub> + 2NaOH &rarr; <span style='color:red'>Mg(OH)<sub>2</sub></span> + 2NaNO<sub>3</sub>"; bool_2 = False

randomize_6 = random.randint(1, 2)
if randomize_6 == 1:
    option_3 = "ZnSO<sub>4</sub> + BaCl<sub>2</sub> &rarr; <span style='color:red'>ZnCl<sub>2</sub></span> + BaSO<sub>4</sub>"; bool_3 = True
elif randomize_6 == 2:
    option_3 = "ZnSO<sub>4</sub> + BaCl<sub>2</sub> &rarr; ZnCl<sub>2</sub> + <span style='color:red'>BaSO<sub>4</sub></sub>"; bool_3 = False

randomize_6 = random.randint(1, 2)
if randomize_6 == 1:
    option_4 = "CaCl<sub>2</sub> + Na<sub>2</sub>CO<sub>3</sub> &rarr; CaCO<sub>3</sub> + <span style='color:red'>2NaCl</span>"; bool_4 = True
elif randomize_6 == 2:
    option_4 = "CaCl<sub>2</sub> + Na<sub>2</sub>CO<sub>3</sub> &rarr; <span style='color:red'>CaCO<sub>3</sub></span> + 2NaCl"; bool_4 = False
   
true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, "Soluble", "Precipitate")

## Conclusion

* A **chemical reaction** is a process that involves the rearrangement of the atoms in the molecular or ionic structure of a substance or material.
* One common classification scheme organizes chemical reactions into four types: *combination, decomposition, single replacement, and double replacement reactions*.
* The **general form** for each reaction type is given as follows:
  + **Combination reaction:** A + B &rarr; AB
  + **Decomposition reaction:** AB &rarr; A + B
  + **Single replacement reaction:** AB + X &rarr; XB + A
  + **Double replacement reaction:** AB + XY &rarr; XB + AY
* The reactivity series can be used to determine if a reaction will spontaneously occur.
* A solubility chart can be used to determine whether or not a product will form a precipitate or remain in solution.

Images in this notebook represent original artwork.

2+2

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)