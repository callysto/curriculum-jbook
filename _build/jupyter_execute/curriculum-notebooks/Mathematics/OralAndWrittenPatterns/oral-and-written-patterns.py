![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/OralAndWrittenPatterns/Oral-and-Written-Patterns.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

# Patterns: Oral and written

## Introduction

Patterns appear all around us in everyday life, and in nature. 
Here are some examples of patterns in action:

from IPython.core.display import HTML

HTML('''
<html>
<head>
<style>
* {
    box-sizing: border-box;
}

.column {
    float: left;
    width: 33.33%;
    padding: 5px;
}

/* Clearfix (clear floats) */
.row::after {
    content: "";
    clear: both;
    display: table;
}
</style>
</head>
<body>


<div class="row">
  <div class="column">
    <p style="text-align: center;"> <b>Nature</b></p> 
<img src="https://i.redd.it/f3y77ihpx5cy.gif" alt="drawing" style="width: 400px;"/>
  </div>
  <div class="column">
    <p style="text-align: center;"><b>Greek Mythology</b>
<img src="http://www.gifmania.co.uk/Fantasy-Animated-Gifs/Animated-Fantasy-Animals/Hydra/Jason-Vs-Hydra-87071.gif" alt="drawing" style="width: 400px;"/>
  </div>
  <div class="column">
   <p style="text-align: center;"><b>Building</b>
    <img src="https://media1.giphy.com/media/3o85xkpCruOJPGtBMQ/giphy.gif" alt="drawing" style="width: 400px;"/>
  </div>
</div>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</html>''')


One of the fun parts of math is discovering how we can use math to understand the world around us. Today we're going to learn how math can help us understand patterns!

## Background

Today we're going to look at patterns that we can describe using numbers. All of the patterns we're going to talk about today are called **Sequences**, where there is an ordering to the pattern, imagine how the alphabet has the ordering: A, B, C, D, and so on. A is the *first* item in our sequence, and Z is the *last* element in our sequence. Not all sequences have an end, some of then keep going, and going, and going! Another simple sequence is the positive number line, where the next number is the previous number plus one.

### The Alphabet as a sequence
![](images/AlphabetSequence.svg )


If we wanted to represent the sequence in a table as we often do with sequences, we'll use n to represent when the term appears in the sequence, and x will represent the term itself:

| $n$|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $x$| A | B | C | D | E | F| G | H | I | J | K | L|M | N | O | P | Q | R| S | T | U | V | W | X| Y| Z|

### The Counting Numbers
![](images/PositiveNumberLine.svg )


## Examples

There is a greek  tale where the hero Hercules has to fight a three headed Hyrda, which can regrow it's heads. Infact, everytime it loses a head, TWO grow in it's place. How can we think of this as a pattern? Well to start let's say it has just one head, after hercules removes this head, now there are two in it's place. Next there is three heads, then four heads, and so on!  For this example, let's break it down at look at some small cases first. 

<ul>
<li>The first number in the pattern: 3  <- The number of heads the hydra has to start </li>

<li>The second number in the pattern: 4 <- After one head is cutoff</li>

<li>The third number in the pattern: 5 <- After another head</li>

<li>The fourth number in the pattern: 6 <- Another one</li>
    
</ul>



Does this sound familiar? That's because the **rule** for the hydra pattern is the similar to the number line we saw above. A rule lets us accurately describe a sequence in a formula. We call it a rule because every item in our sequence will follow the rule. We want to try and make a rule as simple as possible. Then if we wanted to know how many heads the hydra had after 25 cuts we can know right away without counting from 1 cut up to 25 cuts.

Let's think about it in words, first we have the amount from the previous step, then we takeaway one head which hercules chose to cut off, and then we add two heads which grow in it's place. 

If we wanted to write it as a rule, we can do it like this:

$ x_n = n + 2 $

This is saying the n'th number ($x_n$) in the pattern is equal to $n + 2$ because there was initially 3 heads. Adding a number to n will change the starting point of our sequence, think about how if you're asked to count starting at 1 or starting at 5, you count the same way, just starting at a different number! Keep reading to find out how we figured out this rule. remember that n always will start at 1, and increment from there. Remember we start at the first term, so that means n=1.

## Arithmetic Sequences

Above we defined what a **rule** is, now lets talk about types of sequences. 

**Arithmetic Sequences** increase by a fixed number which we call the **difference**, as it is the difference between two consecutive terms in the sequence! This means the gap between the 99th and the 100th term is the same as between the 1st and the 2nd. 

Let's do an example, here are two representations of an arithmetic sequence: 
<center> ** Number Line** </center>

<img src="images/ArithmeticSequence.svg" width=600px>

<center>**Table**</center>
 
| $n$           | $x$           | 
|:-------------:|:-------------:| 
| 1 | 1 | 
| 2 | 3 |   
| 3 | 5 |   
| 4 | 7 |
| 5 | 9 |
| 6 | 11|


Try to find out what the difference, starting value and rule are! Once you're ready, however below to see the answers:
<!---Could it be worthwhile to hide the solutions, best options?-->

The above difference is 2, and the starting value is 1, one **rule** for this arithmetic sequence is this:
$ x_n = 2(n-1) + 1 = 2n - 2 + 1 = 2n -1 $

In general, the rule of an arithmetic sequence has the form:

$ x_n = a(n-1) + b $

where a is the difference, and b is the first value


### Arithmetic Sequence Visualization

HTML('''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'''
)

HTML('''
<form id="frm1_diff" action="/action_page.php">
    Enter the <b>difference</b> for the arithmetic sequence:
    <input type="number" name="quantity" value="3" min="1" max="5">
</form>
    
<form id="frm2_initArith" action="/action_page.php">
    Enter the <b>inital value</b> for the arithmetic sequence:
    <input type="number" name="quantity" value="1" min="0" max="50">
</form>

<div id="arithButton">
     <i>Run the cell before plotting</i>
    <input name="Plot sequence"
           type="button"
           value="Plot sequence"
        />
</div>
    
<svg width="1100" height="120" id="ARITH">
    
    <line x1="0" y1="50" x2="1000" y2="50" stroke="black"/>
    <rect x="0" y="30" width="2" height="40" fill="black"/>
    <rect x="983" y="30" width="2" height="40" fill="black"/>
    <text x="970" y="85" fill="black">50</text>
    <text x="0" y="85" fill="black">0</text>
</svg>
<script src="./scripts/ArithmeticNumberLine.js"</script>
''')


## Geometric Sequences

**Geometric Sequences** can increase very quickly compared to arithmetic sequences. To get the next term in a geometric sequence, we **multiply** the previous term by a constant, this is different from the arithmetic sequence which **adds** a constant to the previous term. Let's do another example:

<center> ** Number Line** </center>
<img src="images/GeometricSequence.svg" width=600px>

<center>**Table**</center>
 
| $n$           | $x$           | 
|:-------------:|:-------------:| 
| 1 | 1 | 
| 2 | 2 |   
| 3 | 4 |   
| 4 | 8 |
| 5 | 16 |
| 6 | 32|

In the above sequence, we can see that our terms appear to be double the previous rate, for example the ratio of $2:4$ is the same as the ratio of $4:8$, or $8:16$ and so on. These ratios can all be simplified to $1:2$. The term **common ratio** refers to the simplified right hand side of the ratio of any two consecutive terms. So for example, the common ratio of this sequence is $2$.

If we look at the table, we can see that each term is twice as large, that means that we can imagine it's just multiplied by two. So thinking about what the 5th term would be, it should have been doubled 4 times from the first term, so that means

$\text{first term} * 2 * 2 * 2 * 2 = \text{5th term}$ 

**Exponents** give us an easier way to represent this, as remember that $2^4 = 2*2*2*2$, since exponents represent multiplying the **base**, in this case 2, 4 times. Sometimes people would say this is "two raised to the power of 4". Not only does it keep showing your work simpler, think about saying $2^{12}$ as 

>*"Two raised to the power of 12"* 

versus 

>*"Two times two times two times two times two times two times two times two times two times two times two times two times"*

So using exponents, we can express the fifth term as the first term times $2^4$. Remember, because the first term hasn't been doubled yet, we only want to raise 2 to the power of 4, **not** 5. It's easy to get tripped up on this! Let's look at how this works in general.

For our example above, a general rule to find any term is:

$x_n = 2^{n-1}$

See how we're raising 2 to the (n-1)th power? that's because as we observed above, the first term specifically hasn't been doubled yet. How does that workout? $x_1 = 2^{1-1} = 2^{0} = 1$. In case you haven't encountered 0 powers yet, just remember that any number to the power 0 is equal to 1.

Any geometric sequence can be describe using exponents rule:

$x_n = ar^{n-1}$

Where a is the first term in the sequence, and r represents the common ratio of the geometric sequence. 

Try out some different common ratios and initial values to see what sort of geometric sequences you can produce!

### Geometric Sequence Visualization

HTML('''
    
<form id="frm1_ratio" action="/action_page.php">
    Enter the <b>common ratio</b> for the geometric sequence:
    <input type="number" name="quantity" value="3" min="1" max="5">
</form>
    
<form id="frm2_initGeo" action="/action_page.php">
    Enter the <b>inital value</b> for the geometric sequence:
    <input type="number" name="quantity" value="1" min="0" max="50">
</form>

<div id="geoButton">
    <i>Run the cell before plotting</i>
    <input name="Plot sequence"
           type="button"
           value="Plot sequence"
        />
</div>
    
<svg width="1000" height="120" id="GEO">
    
    <line x1="0" y1="50" x2="1000" y2="50" stroke="black"/>
    <rect x="0" y="30" width="2" height="40" fill="black"/>
    <text x="0" y="85" fill="black">0</text>
    <rect x="983" y="30" width="2" height="40" fill="black"/>
    <text x="970" y="85" fill="black">50</text>
</svg>
<script src="./scripts/GeometricNumberLine.js"></script>''')

### Arithmetic and Geometric Questions

* Given the arithmetic sequence below, what is the initial value  and difference for this sequence? You may use the visualization tool above to help you find the answers.

| $n$| 1 | 2 | 3 | 4 | 5 | 6 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $x$|2 | 6 | 10 | 14 | 18 | 22|



* What would happen if the difference for a sequence was a negative number? Remember that the difference describes the gap between two terms. Could we have a negative initial value aswell? 


* What if the common ratio was a proper fraction? What about if it was a negative number? How can we understand a negative ratio?


* It's possible to explain a sequence using more than one rule. Try to come up with a sequence which can be explained using a geometric rule AND an arithmetic rule!




## The Fibonacci Sequence

![](images/frazzComic.gif)

We have just scratched the surface of patterns. While arithmetic and geometric sequences are quite useful, there are also other unique patterns which are quite interesting to look at. One of the most famous patterns is called the Fibonacci Sequence. We can find examples of it all throughout nature. That green gif at the beginning of this notebook is a Romanesco Broccoli, and the number of spirals on one head is a Fibonacci number. A **Fibonacci number** is any number which appears in the Fibonacci sequence. More locally, the Fibonacci sequence arises if we look at the cones of a pine tree. The rule for the Fibonacci sequence is a bit more complex than the previous sequences we've looked at, as it's not increasing by a constant or a constant ratio. Instead, to get the next term in the sequence, we add the previous two terms together. Here's the rule expressed mathematically:

$x_n = x_{n-1} + x_{n-2} \text{  ( if n is bigger than 2 )}$

$x_1 = 1 \textit{ and } x_2 = 1$

Let's put it to work and figure out the first few numbers in the sequence, starting with 1 and 1:

$1 + 1 = 2 = x_3$

$1 + 2 = 3 = x_4$

$2 + 3 = 5 = x_5$

$3 + 5 = 8 = x_6$

$5 + 8 = 13 = x_7$

Here's a video by ViHart talking about spirals and the Fibonacci sequence in nature:

from IPython.display import YouTubeVideo
YouTubeVideo('ahXIMUkSXX0')

## Triangle and Square Numbers

There are even interesting patterns we can find in real life, and model them using rules! For example, if you've heard of the square of a number, lets say n, the square is $n^2 = n * n$. This also can be interpreted as a square with side length n. We can also visualize it as dots on a grid, and the square of n is how many dots are in the square with n dots as a side. 

![]( images/square_nums.svg )

The rule to determine how many dots we need is then simply:

$x_n = n^2$

What if instead of drawing squares, we wanted to draw triangles? This is where things get a little more tricky. 

![]( images/triangle_nums.svg )

The rule for the triangle numbers is a little trickier than for the square numbers. Realize that just as in the square numbers, n is the side length of the triangle. It is as follows:

$x_n = \frac{n(n+1)}{2}$

Trying this rule we can see that it is correct for the first few cases:

$x_1 = \frac{1(1+1)}{2} = \frac{1(2)}{2} = 1$

$x_2 = \frac{2(2+1)}{2} = \frac{2(3)}{2} = 3$

$x_3 = \frac{3(3+1)}{2} = \frac{3(4)}{2} = 6$

At first you may think perhaps at some point there should be a fraction since we're dividing by 2. However the whole numbers alternate between odd and even, so that means between $n$ and $(n+1)$ in the numerator, one of these terms *must* be even so there will be a cancellation possible.

The rule for the triangle numbers arises in many places, for example if you wanted to build a house of cards, or determine how many logs are in a triangular stack, you could save a lot of headache by using the rule and counting the side length instead of counting up every individual piece.

### More questions

* Can you draw a pinecone and count the spirals like in the video? Click this [link](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibnat.html#section4.2) and go to section 4.2
 to look at some other pinecones and their spirals.
 
 
* What if we changed the starting two terms in the Fibonacci sequence for other numbers? Try substituting in different numbers and drawing the new sequence in a graph, number line or writing it in table. It won't be the Fibonacci sequence but a new sequence you came up with, what are you going to name your new discovery?


* How many dots are in the following triangle? Remember that we can use the rule described above to save a lot of time and frustration counting! (Hint: Start by figuring out what your n value is, what does n mean? )

![]( images/big_triang.svg )

## Conclusion 

What did you learn about patterns in this notebook? We discussed the concepts of arithmetic and geometric sequences, and more patterns found in real life. We learned ways to concisely express complicated patterns using simple language and mathematics. Here is a brief review of the terms and concepts we touched on:

A **rule** describes a sequence or pattern in a concise way, possibly using a formula. To determine the nth term, we would look at the rule for the case of $x_n$. 

The **initial value** is another way to say *the first term in the sequence*.



**Arithmetic sequences** increased by a fixed amount between terms, this fixed amount is called the **difference**. 

The standard rule for arithmetic sequences is:
$ x_n = an + b $
Where a is the difference and b is the initial value.



**Geometric sequences** increased by a **common ratio** which we can think of as the ratio between two sequential terms. 

The standard rule for geometric sequences is:
$x_n = ar^{n-1}$
Where a is the first term in the sequence, and r represents the common ratio of the geometric sequence. 

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)