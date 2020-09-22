![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/FractionMultiplication/FractionMultiplication.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

import uiButtons
%uiButtons

# Fractions and Multiplication

## Visualizing Fraction Multiplication

## Introduction
An important skill to have when it comes to fractions is knowing how to multiply them together.<br>

As we know, fractions are of the form $\frac{a}{b}$ with $a$ and $b$ integers and $b\neq 0$. <br>

You can think of $\frac{a}{b}$ as the number you get when you do $a\div b$. <br>
If we think of a fraction as a division problem then it makes sense that it works well with multiplication.<br>
Unlike addition, multiplying fractions is easy and straightforward. <br>

In this notebook we will look into two forms of fraction multiplication:
- multiplying two fractions together (e.g. $\dfrac{4}{7} \times \dfrac{2}{3}$ )
- multiplying a fraction by an integer (e.g. $\dfrac{4}{7} \times 3$ )

## Procedure
As mentioned earlier, multiplying two fractions together is simple.<br>
Let's say we want to multiply the fractions $\dfrac{4}{7}$ and $\dfrac{2}{3}$.<br>
All we have to do is multiply the numerators (top numbers) together, then multiply the denominators (bottom numbers) together. Let's take a look: 

$$
\frac{4}{7} \times \frac{2}{3}=\frac{4\times 2}{7\times 3}=\frac{8}{21}
$$ 

Let's try another example. Take the fractions $\dfrac{3}{5}$ and $\dfrac{2}{3}$. To multiply them we multiply the numerators together and the denominators together: 

$$
\frac{3\times 2}{5\times 3}=\frac{6}{15}
$$ 

In this example, you might notice that the result is not in lowest terms: both 6 and 15 are divisible by 3, so we get $\dfrac{6}{15} = \dfrac25$. In a later notebook, we'll focus on mechanics like this. For now, we want to focus on a visual understanding of the problem.

Now that we know how to multiply two fractions, let's think about what it actually means.<br>
Recall that a fraction simply represents a part of something. We can think of multiplying fractions together as taking a part of another part. In other words $\dfrac{1}{2}\times\dfrac{1}{2}$ is like saying $\dfrac{1}{2}$ of $\dfrac{1}{2}$ (one half **of** one half). If we have $\dfrac{1}{2}$ of a pizza and we want $\dfrac{1}{2}$ of that half what do we end up with?<br>

<img src="./images/pizza.png" width="400px">

We get $\dfrac{1}{4}$ because $\dfrac{1}{2}\times\dfrac{1}{2}=\dfrac{1}{4}$.<br>

Watch the video below to help us further visualize this concept.

%%html
<div align="middle">
<iframe id="vid1" width="640" height="360" src="https://www.youtube.com/embed/hr_mTd-oJ-M" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe> 
<p><a href="https://www.youtube.com/channel/UC4a-Gbdw7vOaccHmFo40b9g" target="_blank">Click here</a> for more videos by Khan Academy</p>
</div>
<script>
    $(function() {
        var reachable = false;
        var myFrame = $('#vid1');
        var videoSrc = myFrame.attr("src");
        myFrame.attr("src", videoSrc)
        .on('load', function(){reachable = true;});
        setTimeout(function() {
            if(!reachable) {
                var ifrm = myFrame[0];
                ifrm = (ifrm.contentWindow) ? ifrm.contentWindow : (ifrm.contentDocument.document) ? ifrm.contentDocument.document : ifrm.contentDocument;
                ifrm.document.open();
                ifrm.document.write('If the video does not start click <a href="' + videoSrc + '" target="_blank">here</a>');
                ifrm.document.close();
            }
        }, 2000)
    });
</script>

## Interactive visualization

The widget below allows you to visualize fraction multiplication as shown in the video. To begin, enter a fraction in the boxes below.

%%html
<script src="./d3/d3.min.js"></script>
<!-- <script src="https://d3js.org/d3.v3.min.js"></script> -->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
    });
</script>
<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
<style>
    .fractionInput {
          max-width: 40px;
    }
    
    .fractionBar {
          width: 40px;
          height: 3px;
          background-color: #000000;
    }
    
    .ingredientsInput {
        margin-left: 10px;
        margin-right: 10px;
        max-width: 40px;
        /* float: right; */
    }
    
    #speech {
        margin: 50px;
        font-size: 150%;
    }
    
    li {
        margin-bottom: 15px;
    }
</style>

%%html
<div class="fractionInputs" style="margin:20px">
    <h1 id="leftInputFractionText" style="float: left; display: none"></h1>
    <div id="opperandInput" style="float: left; display: block">
        <input type="text" class="fractionInput form-control form-control-sm" id="oppNumerator" placeholder="0" style="margin-bottom: -10px;">
        <hr align="left" class="fractionBar">
        <input type="text" class="fractionInput form-control form-control-sm" id="oppDenominator" placeholder="1" style="margin-top: -10px;">
    </div>
    <button type="button" id="continueBtn" class="btn btn-primary buttons" style="margin: 30px">Continue</button>

  </div>

  <div class="canvasDiv" style="clear: left">
    <svg height="500" width="500" viewbox="0 0 500 500" mlns="http://www.w3.org/2000/svg" id="mainCanvas" style="float: left">
      <rect id="mainBox" height="480" width="480" x="10" y="10" style="outline: solid #000000 3px; fill:#ffffff"></rect>
      <rect id="leftOpperand" height="480" width="0" x="10" y="10"></rect>
      <rect id="rightOpperand" height="0" width="480" x="10" y="10"></rect>
    </svg>
  </div>
  <div>
    <p id="speech">Enter a fraction inside the boxes provided then click continue.</p>
  </div>
    
  <div style="clear: left; margin-left: 10px">
    <button type="button" id="resetFractionBoxBtn" class="btn btn-primary buttons">Reset</button>
  </div>


## Multiplying a fraction by an integer

In this section we will talk about multiplying a fraction like $\dfrac{4}{7}$, with an integer such as $3$. A good example of when this could be useful is when you need to double a recipe. <br>

Doing multiplication of this form is simply a special case of multiplying two fractions together since any integer, such as $3$ in this case, can be rewritten as $\dfrac{3}{1}$. On a calculator, try inputting any number divided by $1$, and you will always get back the original number. <br>

Let's demonstrate this with an example. To multiply the fraction $\dfrac{4}{7}$ and the integer $3$, remember that we can write $3$ as $\dfrac31$. We get

$$
\frac{4}{7}\times\frac{3}{1} = \frac{4\times 3}{7\times 1}= \frac{12}{7} 
$$

**Note that $\dfrac{3}{1}$ is an improper fraction. Improper fractions follow all the same rules for multiplication as proper fractions.**

The big take away from this is that the denominator does not change as it is simply multiplied by $1$. This means we did not change the "whole", we only changed how many parts of the "whole" we have (the numerator). In effect all we did was triple our fraction, since our constant was 3. <br>

Let's practice what we just learned with a recipe example. Below you will see the ingredient list for the famous **Fresh Tomato and Basil Pasta Salad** recipe. This recipe makes enough for 4 servings, but we would like to double the recipe in order to serve 8 people. Apply what we have learned so far to double the ingredients list for the **tomato and basil pasta salad** in order to make 8 servings. 

(Enter your answer in the provided boxes. Fractions should be written using the _forward slash_ key "/" eg. 5/8. When your done click _check answer_ to see if you are correct!)

%%html
<div class="ingredientsList">
    <h1>Fresh Tomato and Basil Pasta Salad</h1>
    <img src="./images/pastaSalad.jpg" width=250 style="float: left; margin-right: 50px; box-shadow: 5px 6px 25px 3px grey">

      <ul style="max-width: 700px; margin-bottom">
        <li><label>3 medium ripe tomatoes, chopped --></label><input id="tomatoes" class="ingredientsInput"></input><label>tomatoes</label></li>
        <li><label>1/3 cup thinly sliced fresh basil --></label><input id="basil" class="ingredientsInput"></input><label>cup</label></li>
        <li><label>2 Tbsp. olive oil --></label><input id="olivOil" class="ingredientsInput"></input><label>Tbsp.</label></li>
        <li><label>1 clove garlic, minced --></label><input id="garlic" class="ingredientsInput"></input><label>clove</label></li>
        <li><label>1/2 tsp. salt --></label><input id="salt" class="ingredientsInput"></input><label>tsp.</label></li>
        <li><label>1/4 tsp. pepper --></label><input id="pepper" class="ingredientsInput"></input><label>tsp.</label></li>
        <li><label>8 oz. rotini pasta pasta, uncooked --></label><input id="pasta" class="ingredientsInput"></input><label>oz.</label></li>
        <li><label>3/4 cup Parmesan Style Grated Topping --></label><input id="parmesan" class="ingredientsInput"></input><label>cup</label></li>
      </ul>
      <button type="button" id="checkAnswerBtn">Check Answers</button>
      <button type="button" id="resetBtn">Reset</button>
</div>
<div>
    <h2 id="answerStatus"></h2>
</div>

## Conclusion
Throughout this notebook we looked at how easy multiplying fractions together really is. We also looked at how to work with a fraction multiplied by a constant. Lets recap what we have learned:

- When multiplying two fractions together we multiply the numerators together and the denominators together: $\dfrac{a}{b}\times\dfrac{c}{d}=\dfrac{a \times c}{b \times d} = \dfrac{ac}{bd}$

- A constant can always be rewritten as the constant over 1: $c = \dfrac{c}{1}$

- Multiplying a fraction with a constant, multiply the numerator by the constant and keep the denominator the same: $\dfrac{a}{b}\times c=\dfrac{a\times c}{b}=\dfrac{ac}{b}$

- Multiplying two fractions together is the same as saying _a part of a part_: $\dfrac{a}{b}\times\dfrac{c}{d}$ is like saying $\dfrac{a}{b}$ **of** $\dfrac{c}{d}$ (The equation $\dfrac{3}{5}\times\dfrac{1}{4}$ is the same as _three fifths **of** one quarter_)

%%html
<script>
var leftOpperand = {
    id: 'leftOpperand',
    numerator: Number(0),
    denominator: Number(0),
    colour: '#ff0066'
};

var rightOpperand = {
    id: 'rightOpperand',
    numerator: Number(0),
    denominator: Number(0),
    colour: '#0000ff'
};

var currentState = 0;

var getOpperandInput = function(numeratorInput, denominatorInput, opperand) {
  opperand.numerator = document.getElementById(numeratorInput).value;
  opperand.denominator = document.getElementById(denominatorInput).value;

}

var verticalDivide = function(xVal, lineNum) {
    var i = xVal;
    while(lineNum > 0){
      addLine(Number(i + 10), Number(i + 10), 10, Number(d3.select('#mainBox').attr('height')) + 10);
      i += xVal;
      lineNum --;
    }
};

var horizontalDivide = function(xVal, lineNum) {
    var i = Number(xVal);
    while(lineNum > 0){
      addLine(10, Number(d3.select('#mainBox').attr('width')) + 10, Number(i + 10), Number(i +10));
      i += xVal;
      lineNum --;
    }
};

var addLine = function (x1, x2, y1, y2,) {
    var dashed = '0,0';
    var stroke = 2;

    d3.select('#mainCanvas').append('line')
        .attr('class', 'divLine ')
        .attr('x1', x1)
        .attr('x2', x2)
        .attr('y1', y1)
        .attr('y2', y2)
        .style('stroke', 'black')
        .style('stroke-width', stroke);
};

var fillBox = function(box, width, height, colour, opacity) {
    d3.select('#' + box.id)
    .style('fill', colour)
    .style('opacity', opacity)
    .transition().delay(function (d, i) {
        return i * 300;
      }).duration(500)
        .attr('width', width)
        .attr('height', height);
};

var changeOpacity = function(box, opacity) {
    d3.select('#' + box.id).transition().delay(function (d, i) {
        return i * 300;
      }).duration(500)
        .style('opacity', opacity);

    d3.selectAll('.divLine').transition().delay(function (d, i) {
        return i * 100;
      }).duration(200)
    .style('opacity', opacity);
};

var resetInputs = function() {
    d3.select('#continueBtn').attr('disabled', null);
    d3.selectAll('.divLine').remove();
    d3.select('#leftOpperand').attr('width', 0);
    d3.select('#rightOpperand').attr('height', 0);
    d3.select('#leftInputFractionText').text('').style('display', 'none');
    clearInput('oppNumerator');
    clearInput('oppDenominator');
    leftOpperand.numerator = Number(0);
    leftOpperand.denominator = Number(0);
    rightOpperand.numerator = Number(0);
    rightOpperand.denominator = Number(0);

};

var isValid = function(numerator, denominator) {
  if (numerator < 0 || numerator > 12) {
    return false;
  }
  if (denominator <= 0 || denominator > 12) {
    return false;
  }
  return (numerator < denominator);
};

var updateMathJax = function() {
  MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
};

var showInputBox = function(inputId) {
  d3.select('#' + inputId).style('display', 'block');
};

var hideInputBox = function(inputId) {
  d3.select('#' + inputId).style('display', 'none');
};

var clearInput = function(inputId) {
  document.getElementById(inputId).value = '';
}

var stateControler = function(state) {
  currentState = state;
  setSpeech(state);

  switch(state) {
    case 0 :
      resetInputs();
      showInputBox('opperandInput');
      break;
    case 1 :
      getOpperandInput('oppNumerator', 'oppDenominator', leftOpperand);
      d3.select('#leftInputFractionText')
        .text('$\\frac{'+leftOpperand.numerator+'}{'+leftOpperand.denominator+'} \\times$')
        .style('display', 'block');
      updateMathJax();
      verticalDivide(Number(d3.select('#mainBox').attr('width')/leftOpperand.denominator), Number(leftOpperand.denominator - 1));
      hideInputBox('opperandInput');
      break;
    case 2 :
      fillBox(leftOpperand, Number(d3.select('#mainBox').attr('width')/leftOpperand.denominator) * leftOpperand.numerator, Number(d3.select('#mainBox').attr('height')), leftOpperand.colour, 1);
      clearInput('oppNumerator');
      clearInput('oppDenominator');
      showInputBox('opperandInput');
      break;
    case 3 :
      getOpperandInput('oppNumerator', 'oppDenominator', rightOpperand);
      d3.select('#leftInputFractionText')
        .text('$\\frac{'+leftOpperand.numerator+'}{'+leftOpperand.denominator+'} \\times$' + '$\\frac{'+rightOpperand.numerator+'}{'+rightOpperand.denominator+'}$');
      updateMathJax();
      changeOpacity(leftOpperand, 0);
      horizontalDivide(Number(d3.select('#mainBox').attr('height')/rightOpperand.denominator), Number(rightOpperand.denominator - 1));
      hideInputBox('opperandInput');
      break;
    case 4 :
      fillBox(rightOpperand, Number(d3.select('#mainBox').attr('width')), Number(d3.select('#mainBox').attr('height')/rightOpperand.denominator) * rightOpperand.numerator, rightOpperand.colour, 0.5);
      break;
    case 5 :
      changeOpacity(leftOpperand, 1);
      d3.select('#continueBtn').attr('disabled', true);
      break;
    default:
      console.log('not a valid of state, returning to state 0');
      stateControler(0);
  }
};

var speech = [
    "Enter a fraction in the boxes provided, then click continue.",
    "Great! Now we see that the square has been divided into rectangles of equal size. The number of rectangles is given by the denominator. Click continue when ready.",
    "Some of the equal parts have been filled in with pink. The numerator equals the number of pink rectangles. The ratio of the area in pink to the total area is our fraction. Enter another fraction to multiply then click continue.",
    "Let’s focus on the second fraction. The first one is temporarily hidden for clarity. As before, the number of rectangles we see equals the denominator. Click continue when ready.",
    "Now we have a blue section representing the numerator of the second fraction. Click continue to multiply these two fractions.",
    "Awesome! The first fraction is back and overlaid with the second fraction. The number of rectangles in the purple section is the numerator of our answer. Notice that this is the product of the numerators. The total number of rectangles is the denominator of the product, and this is just the product of the two denominators!"
];

function setSpeech(state) {
    d3.select('#speech').text(speech[state]);
};

document.getElementById('continueBtn').onclick = function() {
  if(!isValid(Number(document.getElementById('oppNumerator').value), Number(document.getElementById('oppDenominator').value))){
      alert('Make sure your factions are proper and the denominators less than or equal to 12');
  }
  else {
    stateControler(currentState + 1);
  }
};

document.getElementById('resetFractionBoxBtn').onclick = function() {
  console.log("hello");
  resetInputs();
  stateControler(0);
};
</script>

%%html
<script type="text/javascript">
      var x = 2; //Recipie multiplyer

      getInput('checkAnswerBtn').onclick = function() {
        if(checkAnswers()) {
          d3.select('#answerStatus').text('Correct!! Good job.');
        } else {
          d3.select('#answerStatus').text('Not quite, keep trying!');        
        }
      };
        
        getInput('resetBtn').onclick = function() {
        var inputs = document.getElementsByClassName('ingredientsInput');
        for(var i = 0; i < inputs.length; i++) {
          inputs[i].value = '';
        }
        d3.selectAll('.ingredientsInput').style('background-color', '#ffffff');
        d3.select('#answerStatus').text('');
      };

      function checkAnswers() {
        var isCorrect = true;
        if(!checkAnswer('tomatoes', x*3))
          isCorrect = false;
        if(!checkAnswer('basil', x*(1/3)))
          isCorrect = false;
        if(!checkAnswer('olivOil', x*2))
          isCorrect = false;
        if(!checkAnswer('garlic', x*1))
          isCorrect = false;
        if(!checkAnswer('salt', x*(1/2)))
          isCorrect = false;
        if(!checkAnswer('pepper', x*(1/4)))
          isCorrect = false;
        if(!checkAnswer('pasta', x*8))
          isCorrect = false;
        if(!checkAnswer('parmesan', x*(3/4)))
          isCorrect = false;

        return isCorrect;
      };

      function checkAnswer(id, ans) {
        if(eval(getInput(id).value) === ans) {
          return answerCorrect(id);
        }
        return answerIncorrect(id);
      };

      function answerCorrect(id) {
        d3.select('#' + id).style('background-color', '#76D177');
        return true;
      }

      function answerIncorrect(id) {
        d3.select('#' + id).style('background-color', '#BB4646');
        return false;
      }

      function getInput(id) {
        return document.getElementById(id);
      };
</script>

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)