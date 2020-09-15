![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/Percentage/Percents.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

**Run the cell below, this will add two buttons. Click on the "initialize" button before proceeding through the notebook**

import uiButtons
%uiButtons

%%html
<script src="https://d3js.org/d3.v3.min.js"></script>

# Percentages
## Introduction
In this notebook we will discuss what percentages are and why this way of representing data is helpful in many different contexts. Common examples of percentages are sales tax or a mark for an assignment.

The word percent comes from the Latin adverbial phrase *per centum* meaning “*by the hundred*”.

For example, if the sales tax is $5\%$, this means that for every dollar you spend the tax adds $5$ cents to the total price of the purchase. 

A percentage simply represents a fraction (per hundred). For example, $90\%$ is the same as saying $\dfrac{90}{100}$. It is used to represent a ratio.

What makes percentages so powerful is that they can represent any ratio. 

For example, getting $\dfrac{22}{25}$ on a math exam can be represented as $88\%$: $22$ is $88\%$ of $25$.

## How to Get a Percentage
As mentioned in the introduction, a percentage is simply a fraction represented as a portion of 100. 

For this notebook we will only talk about percentages between 0% and 100%. 

This means the corresponding fraction will always be a value between $0$ and $1$. 

Let's look at our math exam mark example from above. The student correctly answered $22$ questions out of $25$, so the student received a grade of $\dfrac{22}{25}$. 

To represent this ratio as a percentage we first convert $\dfrac{22}{25}$ to its decimal representation (simply do the division in your calculator). 

$$\dfrac{22}{25} = 22 \div 25 = 0.88$$ 

We are almost done: we now have the ratio represented as a value between 0 and 1. To finish getting the answer to our problem all we need to do is multiply this value by $100$ to get our percentage. $$0.88 \times 100 = 88\%$$

Putting it all together we can say $22$ is $88\%$ of $25$.

Think of a grade you recently received (as a fraction) and convert it to a percentage. Once you think you have an answer you can use the widget below to check your answer. 

Simply add the total marks of the test/assignment then move the slider until you get to your grade received.

%%html
    <style>
        .main {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .slider {
            width: 100px;
        }

        #maxVal {
            border:1px solid #cccccc;
            border-radius: 5px;
            width: 50px;
        }
    </style>
    <div class="main" style="border:2px solid black; width: 400px; padding: 20px;border-radius: 10px; margin: 0 auto; box-shadow: 3px 3px 12px #acacac">
        <div>
            <label for="maxValue">Enter the assignment/exam total marks</label>
            <input type="number" id="maxVal" value="100">
        </div>
        <div>
            <input type="range" min="0" max="100" value="0" class="slider" id="mySlider" style="width: 300px; margin-top: 20px;">
        </div>
        <h4 id="sliderVal">0</h3>
    </div>

    <script>
        var slider = document.getElementById('mySlider');
        var sliderVal = document.getElementById('sliderVal');

        slider.oninput = function () {
            var sliderMax = document.getElementById('maxVal').value;
            if(sliderMax < 0 || isNaN(sliderMax)) {
                sliderMax = 100;
                document.getElementById('maxVal').value = 100;
            }
            d3.select('#mySlider').attr('max', sliderMax);
            sliderVal.textContent = "If you answered " + this.value + "/" + sliderMax + " correct questions your grade will be " + ((
                this.value / sliderMax) * 100).toPrecision(3) + "%";
        }
    </script>

## Solving Problems Using Percentages

Now that we understand what percentages mean and how to get them from fractions, let's look at solving problems using percentages. Start by watching the video below to get a basic understanding.

%%html
<div align="middle">
<iframe id="percentVid" width="640" height="360" src="https://www.youtube.com/embed/rR95Cbcjzus?end=368" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen style="box-shadow: 3px 3px 12px #ACACAC">
</iframe> 
<p><a href="https://www.youtube.com/channel/UC4a-Gbdw7vOaccHmFo40b9g" target="_blank">Click here</a> for more videos by Math Antics</p>
</div>
<script>
    $(function() {
        var reachable = false;
        var myFrame = $('#percentVid');
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

As shown in the video, taking $25\%$ of 20 "things" is the same as saying $\dfrac{25}{100}\times\dfrac{20}{1}=\dfrac{500}{100}=\dfrac{5}{1}=5$. 

Let's do another example, assume a retail store is having a weekend sale. The sale is $30\%$ off everything in store.

Sam thinks this is a great time to buy new shoes, and the shoes she is interested in are regular price $\$89.99$.<br>
If Sam buys these shoes this weekend how much will they cost? If the sales tax is $5\%$, what will the total price be?

<img src="https://orig00.deviantart.net/5c3e/f/2016/211/b/d/converse_shoes_free_vector_by_superawesomevectors-dabxj2k.jpg" width="300">
<img src="https://www.publicdomainpictures.net/pictures/170000/nahled/30-korting.jpg" width="300">

Let's start by figuring out the sale price of the shoes before calculating the tax. To figure out the new price we must first take $30\%$ off the original price.

So the shoes are regular priced at $\$89.99$ and the sale is for $30\%$ off $$\$89.99\times 30\%=\$89.99\times\frac{30}{100}=\$26.997$$ We can round $\$26.997$ to $\$27$. 

Ok we now know how much Sam will save on her new shoes, but let's not forget that the question is asking how much her new shoes will cost, not how much she will save. All we need to do now is take the total price minus the savings to get the new price: $$\$89.99- \$27=\$62.99$$ Wow, what savings!

Now for the second part of the question: what will the total price be if the tax is $5\%$?

We must now figure out what $5\%$ of $\$62.99$ is $$\$62.99\times5\%=\$62.99\times\frac{5}{100}=\$3.15$$ Now we know that Sam will need to pay $\$3.15$ of tax on her new shoes so the final price is $$\$62.99+\$3.15=\$66.14$$

A shortcut for finding the total price including the sales tax is to add 1 to the tax ratio, let's see how this works:
$$\$62.99\times\left(\frac{5}{100}+1\right)=\$62.99\times1.05=\$66.14$$

You can use this trick to quickly figure out a price after tax.

## Multiplying Percentages together
Multiplying two or more percentages together is probably not something you would encounter often but it is easy to do if you remember that percentages are really fractions. 

Since percentages is simply a different way to represent a fraction, the rules for multiplying them are the same. Recall that multiplying two fractions together is the same as saying a *a fraction of a fraction*. For example $\dfrac{1}{2}\times\dfrac{1}{2}$ is the same as saying $\dfrac{1}{2}$ of $\dfrac{1}{2}$. 

Therefore if we write $50\%\times 20\%$ we really mean $50\%$ of $20\%$.

The simplest approach to doing this is to first convert each fraction into their decimal representation (divide them by 100), so $$50\%\div 100=0.50$$ and $$20\%\div 100=0.20$$

Now that we have each fraction shown as their decimal representation we simply multiply them together: $$0.50\times0.20=0.10$$ and again to get this decimal to a percent we multiply by 100 $$0.10\times100=10\%$$ Putting this into words we get: *$50\%$ of $20\%$ is $10\%$ (One half of $20\%$ is $10\%$)*.

## Sports Example

As we know, statistics play a huge part in sports. Keeping track of a team's wins/losses or how many points a player has are integral parts of today's professional sports. Some of these stats may require more interesting mathematical formulas to figure them out. One such example is a goalie’s save percentage in hockey. 

The save percentage is the ratio of how many shots the goalie saved over how many he/she has faced. If you are familiar with the NHL you will know this statistic for goalies as Sv\% and is represented as a number like 0.939. In this case the $0.939$ is the percentage we are interested in. You can multiply this number by $100$ to get it in the familiar form $93.9\%$. This means the Sv\% is $93.9\%$, so this particular goalie has saved $93.9\%$ of the shots he's/she's faced.

You will see below a "sport" like game. The objective of the game is to score on your opponent and protect your own net. As you play the game you will see (in real time) below the game window your Sv% and your opponents Sv%. Play a round or two before we discuss how to get this value.

_**How to play:** choose the winning score from the drop down box then click "Start". In game use your mouse to move your paddle up and down (inside the play area). Don't let the ball go in your net!_

%%html
	<style>
		.mainBody {
			font-family: Arial, Helvetica, sans-serif;
		}
		#startBtn {
			background-color: cornflowerblue;
 			border: none;
 			border-radius: 3px;
  			font-size: 14px;
  			color: white;
  			font-weight: bold;
  			padding: 2px 8px;
  			text-transform: uppercase;
		}
	</style>
<div class="mainBody">
<div style="padding-bottom: 10px;">
		<label for="winningScore">Winning Score: </label>
		<select name="Winning Score" id="winningScore">
			<option value="3">3</option>
			<option value="5">5</option>
			<option value="7">7</option>
			<option value="10">10</option>
		</select>
		<button type="button" id="startBtn">Start</button>
	</div>
	<canvas id="gameCanvas" width="600" height="350" style="border: solid 1px black"></canvas>

	<div>
		<ul>
			<li>Player's point save average: <output id="playerAvg"></output></li>
			<li>Computer's point save average: <output id="compAvg"></output></li>
		</ul>
	</div>
</div>

If you look below the game screen you will see "Player's point save average" and "Computer's point save average". You might also have noticed these values changed every time a save was made (unless Sv% was 1) or a score happened, can you come up with a formula to get these values?

The Sv% value is the ratio of how many saves was made over how many total shots the player faced so our formula is $$Sv\%=\frac{saved \ shots}{total \ shots}$$

Let's assume the player faced $33$ shots and let in $2$, then the player's Sv% is $$Sv\%=\frac{(33-2)}{33}=0.939$$ *Note: $(33-2)$ is how many shots where saved since the total was $33$ and the player let in $2$*

## Questions

%%html
    <style>
        hr {
            width: 60%;
            margin-left: 20px;
        }
    </style>
    <main>
        <div class="questions">
            <ul style="list-style: none">
                <h4>Question #1</h4>
                <li>
                    <label for="q1" class="question">A new goalie played his first game and got a shutout (did not let
                        the other team score) and made 33 saves, what is his Sv%? </label>
                </li>
                <li>
                    <input type="text" id="q1" class="questionInput">
                    <button id="q1Btn" onclick="checkAnswer('q1')" class="ansBtn">Check Answer</button>
                </li>
                <li>
                    <p class="q1Ans" id="q1True" style="display: none">&#10003 That's right! Until the goalie let's
                        his/her
                        first goal in he/she will have a Sv% of 1</p>
                </li>
                <li>
                    <p class="q1Ans" id="q1False" style="display: none">Not quite, don't forget to take the total
                        amount of shots minus how many went in the net</p>
                </li>
            </ul>
        </div>
        <hr>
        <div class="questions">
            <ul style="list-style: none">
                <h4>Question #2</h4>
                <li>
                    <label for="q2" class="question">If a goalie has a Sv% of .990 can he/she ever get back to a Sv% of
                        1.00?</label>
                </li>
                <li>
                    <select id="q2">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    <button id="q2Btn" onclick="checkAnswer('q2')" class="ansBtn">Check Answer</button>
                </li>
                <li>
                    <p class="q2Ans" id="q2True" style="display: none">&#10003 That's correct, the goalie could get back
                        up to
                        0.999 but never 1.00</p>
                </li>
                <li>
                    <p class="q2Ans" id="q2False" style="display: none">Not quite, the goalie could get back up to 0.999
                        but never 1.00</p>
                </li>
            </ul>
        </div>
        <hr>
        <div class="questions">
            <ul style="list-style: none">
                <h4>Question #3</h4>
                <li>
                    <label for="q3" class="question">A student received a mark of 47/50 on his unit exam, what
                        percentage did he get?</label>
                </li>
                <li>
                    <input type="text" id="q3" class="questionInput">
                    <button id="q3tn" onclick="checkAnswer('q3')" class="ansBtn">Check Answer</button>
                </li>
                <li>
                    <p class="q3Ans" id="q3True" style="display: none">&#10003 That's correct!</p>
                </li>
                <li>
                    <p class="q3Ans" id="q3False" style="display: none">Not quite, try again</p>
                </li>
            </ul>
        </div>
        <hr>
        <div class="questions">
            <ul style="list-style: none">
                <h4>Question #4</h4>
                <li>
                    <label for="q4" class="question">In a class of 24 students, 8 students own cats, 12 students own dogs
                        and 6 students own both cats and dogs. What is the percentage of students who own both cats and
                        dogs?</label>
                </li>
                <li>
                    <input type="text" id="q4" class="questionInput">
                    <button id="q4tn" onclick="checkAnswer('q4')" class="ansBtn">Check Answer</button>
                </li>
                <li>
                    <p class="q4Ans" id="q4True" style="display: none">&#10003 That's correct!</p>
                </li>
                <li>
                    <p class="q4Ans" id="q4False" style="display: none">Not quite, try again</p>
                </li>
            </ul>
        </div>

    </main>
        <script>
        checkAnswer = function(q) {
            var val = document.getElementById(q).value;
            var isCorrect = false;
            $("."+q+"Ans").css("display", "none");
            switch(q) {
                case 'q1' : Number(val) === 1 ? isCorrect = true : isCorrect = false; break;
                case 'q2' : val === 'No' ? isCorrect = true : isCorrect = false; break;
                case 'q3' : (val === '94%'|| val === '94.0%' || Number(val) === 94) ? isCorrect = true : isCorrect = false;break;
                case 'q4' : (Number(val) === 25 || val === '25%' || val === '25.0%') ? isCorrect = true : isCorrect = false; break;
                default : return false;
            }

            if(isCorrect) {
                $("#"+q+"True").css("display", "block");
            } else {
                $("#"+q+"False").css("display", "block");
            }
        } 
    </script>


## Conclusion

As we saw in this notebook, percentages show up in many different ways and are very useful when describing a ratio. It allows for demonstrating any ratio on a familiar scale ($100$) to make data easier to understand. In this notebook we covered the following: 
- A percentage simply represents a fraction
- To convert any fraction to a percent we turn it into it's decimal form and add $100$
- A percentage of an amount is simply a fraction multiplication problem
- To add or subtract a percentage of an amount we first find the percent value than add/subtract from the original value
- When adding a percentage to an amount we an use the decimal form of percent and add $1$ to it (for example $\$12\times(0.05+1)=\$12.60$)
 
 Keep practising converting fractions to percentages and it will eventually become second nature!

%%html
<script>
		var canvas;
		var canvasContext;
		var isInitialized;

		var ballX = 50;
		var ballY = 50;
		var ballSpeedX = 5;
		var ballSpeedY = 3;

		var leftPaddleY = 250;
		var rightPaddleY = 250;

		var playerSaves = 0;
		var playerSOG = 0;
		var compSaves = 0;
		var compSOG = 0;

		var playerScore = 0;
		var compScore = 0;
		var winningScore = 3;
		var winScreen = false;

		var PADDLE_WIDTH = 10;
		var PADDLE_HEIGHT = 100;
		var BALL_RADIUS = 10;
		var COMP_SPEED = 4;

		document.getElementById('startBtn').onclick = function () {
			initGame();
			var selection = document.getElementById('winningScore');
			winningScore = Number(selection.options[selection.selectedIndex].value);
			canvas = document.getElementById('gameCanvas');
			canvasContext = canvas.getContext('2d');
			canvasContext.font = '50px Arial';
			ballReset();

			if (!isInitialized) {
				var framesPerSec = 60;
				setInterval(function () {
					moveAll();
					drawAll();
				}, 1000 / framesPerSec);
				isInitialized = true;
			}

			canvas.addEventListener('mousemove', function (event) {
				var mousePos = mouseYPos(event);
				leftPaddleY = mousePos.y - PADDLE_HEIGHT / 2;
			});
		}

		function updateSaveAvg() {
			var playerSaveAvgTxt = document.getElementById('playerAvg');
			var compSaveAvgTxt = document.getElementById('compAvg');

			var playerSaveAvg = playerSaves / playerSOG;
			var compSaveAvg = compSaves / compSOG;

			playerSaveAvgTxt.textContent = ((playerSaveAvg < 0 || isNaN(playerSaveAvg)) ? Number(0).toPrecision(3) + (' (0.0%)') :
				playerSaveAvg.toPrecision(3) + (' (' + (playerSaveAvg * 100).toPrecision(3) + '%)'));
			compSaveAvgTxt.textContent = ((compSaveAvg < 0 || isNaN(compSaveAvg)) ? Number(0).toPrecision(3) + (' (0.0%)') :
				compSaveAvg.toPrecision(
					3) + (' (' + (compSaveAvg * 100).toPrecision(3) + '%)'));

		}

		function initGame() {
			playerScore = 0;
			compScore = 0;
			playerSaves = 0;
			playerSOG = 0;
			compSaves = 0;
			compSOG = 0;
			ballSpeedX = 5;
			ballSpeedY = 3;
		}

		function ballReset() {
			if (playerScore >= winningScore || compScore >= winningScore) {
				winScreen = true;
			}
			if (winScreen) {
				updateSaveAvg();
				if (confirm('Another game?')) {
					winScreen = false;
                    initGame();
				} else {
					return;
				}
			}
			ballX = canvas.width / 2;
			ballY = canvas.height / 2;
			ballSpeedY = Math.floor(Math.random() * 4) + 1;
			var randomizer = Math.floor(Math.random() * 2) + 1;
			if (randomizer % 2 === 0) {
				ballSpeedY -= ballSpeedY;
			}
			flipSide();
		}

		function flipSide() {
			ballSpeedX = -ballSpeedX;
		}

		function moveAll() {
			if (winScreen) {
				return;
			}
			computerMove();
			ballX += ballSpeedX;
			if (ballX < (0 + BALL_RADIUS)) {
				if (ballY > leftPaddleY && ballY < leftPaddleY + PADDLE_HEIGHT) {
					playerSaves++;
					playerSOG++;
					flipSide();
					var deltaY = ballY - (leftPaddleY + PADDLE_HEIGHT / 2);
					ballSpeedY = deltaY * 0.35;
				} else {
					playerSOG++;
					compScore++;
					if (compScore === winningScore) {
						updateSaveAvg();
						drawAll();
						alert('Computer wins, final score: ' + playerScore + '-' + compScore);
					}
					ballReset();
				}
			}
			if (ballX >= canvas.width - BALL_RADIUS) {
				if (ballY > rightPaddleY && ballY < rightPaddleY + PADDLE_HEIGHT) {
					compSaves++;
					compSOG++;
					flipSide();
					var deltaY = ballY - (rightPaddleY + PADDLE_HEIGHT / 2);
					ballSpeedY = deltaY * 0.35;
				} else {
					compSOG++;
					playerScore++;
					if (playerScore === winningScore) {
						updateSaveAvg();
						drawAll();
						alert('You win, final score: ' + playerScore + '-' + compScore);
					}
					ballReset();
				}
			}
			ballY += ballSpeedY;
			if (ballY >= canvas.height - BALL_RADIUS || ballY < 0 + BALL_RADIUS) {
				ballSpeedY = -ballSpeedY;
			}
			updateSaveAvg();
		}

		function computerMove() {
			var rightPaddleYCenter = rightPaddleY + (PADDLE_HEIGHT / 2)
			if (rightPaddleYCenter < ballY - 20) {
				rightPaddleY += COMP_SPEED;
			} else if (rightPaddleYCenter > ballY + 20) {
				rightPaddleY -= COMP_SPEED;
			}
		}

		function mouseYPos(event) {
			var rect = canvas.getBoundingClientRect();
			var root = document.documentElement;
			var mouseX = event.clientX - rect.left - root.scrollLeft;
			var mouseY = event.clientY - rect.top - root.scrollTop;
			return {
				x: mouseX,
				y: mouseY
			};
		}

		function drawAll() {

			colorRect(0, 0, canvas.width, canvas.height, 'black');
			if (winScreen) {
				drawNet();
				drawScore();
				return;
			}
			//Left paddle
			colorRect(1, leftPaddleY, PADDLE_WIDTH, PADDLE_HEIGHT, 'white');
			//Right paddle
			colorRect(canvas.width - PADDLE_WIDTH - 1, rightPaddleY, PADDLE_WIDTH, PADDLE_HEIGHT, 'white');
			//Ball
			colorCircle(ballX, ballY, BALL_RADIUS, 'white');

			drawNet();

			drawScore();

		}

		function colorRect(x, y, width, height, drawColor) {
			canvasContext.fillStyle = drawColor;
			canvasContext.fillRect(x, y, width, height);
		}

		function colorCircle(centerX, centerY, radius, drawColor) {
			canvasContext.fillStyle = 'drawColor';
			canvasContext.beginPath();
			canvasContext.arc(centerX, centerY, radius, 0, Math.PI * 2, true);
			canvasContext.fill();
		}

		function drawScore() {
			canvasContext.fillText(playerScore, (canvas.width / 2) - (canvas.width / 4) - 25, 100);
			canvasContext.fillText(compScore, (canvas.width / 2) + (canvas.width / 4) - 25, 100);
		}

		function drawNet() {
			for (var i = 0; i < 60; i++) {
				if (i % 2 === 1) {
					colorRect(canvas.width / 2 - 3, i * 10, 6, 10, 'white')
				}
			}
		}
	</script>

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)