![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/SourcesOfEnergy/resources-and-recycling.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

import myMagics
%uiButtons

# Sources of Energy 

## Learning Summary
Students will begin to understand the importance of managing waste properly. They will learn about the different sources of energy. In addition, they will learn that these energy sources are not unlimited and can run out. By the end of this notebook, students will understand which energy sources are renewable and non-renewable. They will learn and begin to think about the good and bad traits of energy sources as well as the lifespan of the source. Students will be prompted to think about the efficiency of the energy source after taking all factors into consideration. 

## Solar Energy

Solar energy is energy that comes from the sun. The earth receives more energy from the sun in one hour than the whole world uses in one year. Solar energy is used to generate electricity using solar panels. A solar panel works by allowing particles of light to knock electrons free from atoms, generating a flow of electricity. Unfortunately, solar panels need solar cells to work which are created from already existing materials such as silicon, which is not an unlimited resource. 

Solar panels are hard to manufacture making solar energy use low. Once they are made, solar panels do not release any pollution into the air. Energy from the sun is produced every day which means it will never run out, making it a renewable resource.

<img src="http://www.mountainjunkiegear.com/wp-content/uploads/2013/04/How-Solar-Panels-Work.jpg" style="margin: 0 auto; width: 1000px;">

#### Source Image: Solar Panels for your Home, Nov. 2015. Retrieved from http://www.mountainjunkiegear.com/wp-content/uploads/2013/04/How-Solar-Panels-Work 

## Oil Energy and Natural Gas Energy
The most used source of energy around the world is oil. Oil occurs naturally and takes over a  million years to form from old plants and bacteria. Oil comes from far underground. It is brought to the surface by special pumps and pipes. Most electricity, fuel and everyday things such as plastic come from this source. The most common use of oil that you may know is gasoline for vehicles. Oil is a fossil fuel. A fossil fuel is a source of energy that does not reproduce at the rate it is being used making it a non-renewable resource.

from IPython.display import YouTubeVideo
YouTubeVideo('WW8KfUJdTNY', width=800, height=300)

##### Source Video: Crude Oil Extraction, July 2016. Retrieved from https://www.youtube.com/watch?time_continue=83&v=WW8KfUJdTNY

Similarly, natural gas is found underground all over the world. It is often located around coal or oil pockets in the earth. The word 'natural' means that it is a gas formed by natural chemical processes that occur on earth. Natural gas is a by-product of decomposing biomass such as trees, grass, animals, wood and leaves. 

Your house uses natural gas every day for heating, cooking and electricity. How does natural gas get from deep within the ground all the way to your house to be used? Natural gas companies drill thousands of feet into the earth and use big pumps to bring it to the surface. Then they send the gas to your town through gas pipes buried underground. A gas company brings it to your house in smaller pipes. Each household in Alberta pays a natural gas bill each month. Since it is produced from the same processes as oil, natural gas is a fossil fuel too making it a non-renewable source.

## Coal Energy
Another major source of energy around the world is coal. Most of the coal we use now was formed 300 million years ago. The energy in coal comes from energy that was stored in giant plants that lived hundreds of millions of years ago in swamp forests, even before the dinosaurs! 

<img src="http://www.dynamicscience.com.au/tester/solutions1/electric/electricenergy.gif" style="margin: 0 auto; width: 1000px;">

#### Source Image: Energy Conservation, n.d. Retrieved from http://www.dynamicscience.com.au/tester/solutions1/electric/electricenergy

In the above diagram we see that plants are the only organisms on Earth that can harness solar energy and convert it into a more usable form called chemical energy. Chemical energy is trapped in the form of wood and other plant matter. Coal is also a source of chemical energy because when the plant matter died, it formed layers at the bottom of swamps. Water and dirt began to pile up on top of the dead plant remains and years of pressure formed the rock we call coal.

Humans dig up coal and burn it. When coal is burned it turns into chemical energy and heat energy. The heat energy is used to heat water into super-hot steam. Steam occurs when water heats up to such a high temperature that it changes from a liquid to a gas. Steam is kinetic energy. Kinetic energy is the energy of motion, or in other words the movement of particles. The steam (or kinetic energy) causes a generator to spin and produces electrical energy. Coal is a fossil fuel making it non-renewable. Humans use coal at a faster rate than it reproduces.

The law of conservation of energy states that energy cannot be created nor can it be destroyed. It can, however, change forms. Take the process outlined in the animation below. At every step there is a loss of energy. The efficiency of the process is given as an estimated percentage.

<img src="http://www.dynamicscience.com.au/tester/solutions1/electric/powerstation/Untitled-17.gif" style="margin: 0 auto; width: 1000px;">

#### Source Image: Energy Conservation, n.d. Retrieved from http://www.dynamicscience.com.au/tester/solutions1/electric/electricenergy

%%html
    <style>
        #list {
            margin: 20px 0;
            padding: 0;
        }
        #list li {
            list-style: none;
            margin: 5px 0;
        }

        .energy {
            font-family: 'Courier New', Courier, monospace;
            font-size: 15px;
        }

        .answerSelect {
            margin: 10px 10px;
        }

        .correct {
            color: green;
            font-size: 25px;
            display: none;
        }

        .wrong {
            color: red;
            font-size: 25px;
            display: none;
        }

        .ansBtn {
            cursor: pointer;
            border: solid black 1px;
            background: #d3d3d3;
            padding: 10px 5px;
            border-radius: 0px;
            font-family: arial;
            font-size: 20px;
        }

        .ansBtn:hover {
            background: #f3f3f3;
        }
            
        .redtext {
            color: red;
        }
        
        .greentext {
            color: green;
        }
            
    </style>
    
    <body>
    <div style="height: 300px">
        <ul id="list">
            <li>
            <label for="q1">1) What process captures solar energy?</label>
                <select name="q1" id="q1" class="answerSelect">
                    <option value="default" selected>Select an Answer</option>
                    <option value="evaporation">Evaporation</option>
                    <option value="photosynthesis">Photosynthesis</option>
                    <option value="respiration">Respiration</option>
                    <option value="condensation">Condensation</option>
                </select>
                <span class="correct" id="Q1C">&#10003</span>
                <span class="wrong" id="Q1W">&#10007</span>
            </li>
            <li>
            <label for="q2">2) Which is the most inefficient energy conversion step in the process outlined above?</label>
                <select name="q2" id="q2" class="answerSelect">
                    <option value="default" selected>Select an Answer</option>
                    <option value="kinetic into mechanical">Kinetic into mechanical</option>
                    <option value="chemical into heat">Chemical into heat</option>
                    <option value="mechanical into electrical">Mechanical into electrical</option>
                    <option value="solar into chemical">Solar into chemical</option>
                </select>
                <span class="correct" id="Q2C">&#10003</span>
                <span class="wrong" id="Q2W">&#10007</span>
            </li>
            <li>
            <label for="q3">3) The more steps in the process of generating electrical energy the</label>
                <select name="q3" id="q3" class="answerSelect">
                    <option value="default" selected>Select an Answer</option>
                    <option value="less electrical energy that is generated">Less electrical energy that is generated</option>
                    <option value="the more electrical energy that is generated">The more electrical energy that is generated</option>
                </select>
                <span class="correct" id="Q3C">&#10003</span>
                <span class="wrong" id="Q3W">&#10007</span>
            </li>
            <li>
            <label for="q4">4) The energy lost is in the form of</label>
                <select name="q4" id="q4" class="answerSelect">
                    <option value="default" selected>Select an Answer</option>
                    <option value="Electrical">Electrical</option>
                    <option value="Heat">Heat</option>
                    <option value="Chemical">Chemical</option>
                    <option value="Mechanical">Mechanical</option>
                </select>
                <span class="correct" id="Q4C">&#10003</span>
                <span class="wrong" id="Q4W">&#10007</span>
            </li>
            <li>
            <label for="q5">5) What type of energy is carried by steam</label>
                <select name="q5" id="q5" class="answerSelect">
                    <option value="default" selected>Select an Answer</option>
                    <option value="Electrical">Electrical</option>
                    <option value="Chemical">Chemical</option>
                    <option value="Mechanical">Mechanical</option>
                    <option value="Kinetic">Kinetic</option>
                </select>
                <span class="correct" id="Q5C">&#10003</span>
                <span class="wrong" id="Q5W">&#10007</span>
            </li>
        </ul>
        <span class="ansBtn" id="ansBtn" onclick="checkAns()">Check Answers!</span>
    </div>
    
    <script src="main.js"></script>
</body>

## Biomass Energy

Perhaps one of the oldest forms of fuel known is biomass fuel. Biomass is any kind of biological matter that humans can burn in order to produce heat or energy. Biomass mainly consists of wood, leaves, and grass. 

All biomass has storages of carbon and when biomass is burned the carbon is released into the atmosphere as CO2 gas. Resources such as wood, leaves and grass are NOT fossil fuels because biomass is said to be carbon neutral. Carbon neutral means that the amount of carbon released when biomass is burned is equal to the amount of carbon that is naturally needed in the environment for processes like photosynthesis. 

As humans we must remember that trees take years to grow so if we carelessly use wood, it may not always be a resource immediately available for use. When someone in Alberta cuts down a tree to burn it for energy, it is said that one tree must be planted to replace it. Humans across Canada work to replace trees at the rate in which we use them making biomass a renewable source.

##### Biomass Fun Facts! 
1) If you’ve ever been near a campfire or a fireplace, you’ve witnessed biomass energy through the burning of wood.

2) Biomass has been around since the beginning of time when man burned wood for heating and cooking.

3) Wood was the biggest energy provider in the world in the 1800’s.

4) Garbage can be burned to generate energy as well. This not only makes use of trash for energy, but reduces the amount of trash that goes into landfills. This process is called Waste-to-Energy.

## Wind Energy

Wind is a newer source of energy. The use of wind for energy production, mainly electricity, has only been developed recently. Most wind power is converted to electricity by using giant machines called wind turbines. Wind is a natural resource that will never run out making wind a renewable resource. Wind that occurs naturally moves the turbines. The turbines power a generator. A generator is a device that converts mechanical energy to electrical energy. In this case the mechanical energy is the movement of the turbines created by the wind. This mechanical energy is changed into electrical energy that can be used in a home. 

Did you know that Alberta has a wind energy capacity of 1,483 megawatts. Alberta's wind farms produce enough electricity each year to power 625,000 homes, which is 8 percent of Alberta's electricity demand. 

<img src="https://i.gifer.com/so8.gif" style="margin: 0 auto; width: 1000px;">

#### Source Image: #Wind, n.d. Retrieved from https://gifer.com/en/so8

## Water Energy
The correct term for water energy is hydropower. Hydro means water. The first use of water for energy dates back to around 4000 B.C. They used a water wheel during Roman times to water crop and supply drinking water to villages. Now, water creates energy in hydro-dams. A hydro-dam produces electricity when water pushes a device called a turbine. This turbine spins a generator which converts mechanical energy into electrical energy. In this case the mechanical energy that occurs is when the water pushes the turbine. Water is considered a resource that will never run out. It is plentiful and is replenished every time it rains.  

<img src="http://www.wvic.com/images/stories/Hydroplants/hydroplant-animate.gif" style="margin: 0 auto; width: 1000px;">

#### Source Image: Wisconsin Valley Improvement Company, n.d. Retrieved from http://www.wvic.com/content/how_hydropower_works.cfm

## Nuclear Energy

Nuclear energy uses the power of an atom to create steam power. Atoms can create energy in two different ways: nuclear fission which is when the inside of an atom is split or nuclear fusion which is done by fusing the inside of two atoms. 

The energy produced by the Sun, for example, comes from nuclear fusion reactions. Hydrogen gas in the core of the Sun is squeezed together so tightly that four hydrogen particles combine to form one helium atom. This is called nuclear fusion. When one of these two physical reactions occurs (nuclear fission or nuclear fusion) the atoms experience a slight loss of mass. The mass that is lost becomes a large amount of heat energy and light. This is why the sun is so hot and shines brightly. Did you know that Albert Einstein discovered his famous equation, E = mc2, with the sun and stars in mind? In his equation, Einstein invented a way to show that "Energy equals mass times the speed of light squared."  

The heat generated in nuclear fusion and nuclear fission is used to heat up water and produce steam, which is then used to create electricity. The separation and joining of atoms occurs safely within the walls of a nuclear power station. Nuclear power generates nuclear waste that can be dangerous to human health and the environment. 


from IPython.display import YouTubeVideo
YouTubeVideo('igf96TS3Els', width=800, height=300)

#### Source Video: Nuclear Power Station, July 2008. Retrieved from https://www.youtube.com/watch?v=igf96TS3Els

## Geothermal Energy

Geothermal energy is generated by the high temperature of earth's core heating water into steam. The term 'geo' means earth and the word 'thermal' means heat, which means geothermal is 'heat from the earth.' Geothermal energy plants convert large amounts of steam (kinetic energy) into usable electricity. Geothermal energy plants are located in prime areas. Canada does not have any commercial geothermal energy plants. 

Note, there exists a device called a geothermal heat pump that can tap into geothermal energy to heat and cool buildings. A geothermal heat pump system consists of a heat pump, an air delivery system (ductwork), and a heat exchanger-a system of pipes buried in the shallow ground near the building. In the summer, the heat pump moves heat from the indoor air into the heat exchanger. In the winter, the heat pump removes heat from the heat exchanger and pumps it into the indoor air delivery system. 

Why is geothermal energy a renewable resource? Because the source of geothermal energy is the unlimited amount of heat generated by the Earth's core. It is important to recognize geothermal energy systems DO NOT get their heat directly from the core. Instead, they pull  heat from the crust—the rocky upper 20 miles of the planet's surface. 

from IPython.display import YouTubeVideo
YouTubeVideo('y_ZGBhy48YI', width=800, height=300)

#### Source Video: Energy 101: Geothermal Heat Pumps, Jan. 2011.

## Renewable Energy Sources vs. Non-renewable

Renewable energy sources are energy sources that can be replaced at the same rate they are used. The source is plentiful and generally quite efficient. An example of a renewable energy source is wind. Wind is a renewable energy source because there is a limitless supply that is naturally produced. 

Non-renewable energy sources are those that run out more quickly than they are naturally reproduced. Usually these energy sources take millions of year to produce and they have a bigger negative impact on the earth compared to alternate sources. An example of a non-renewable energy source is oil. Oil is non-renewable because humans are using it faster than it is being replaced naturally on earth.  

In order to get comfortable with the two types of Energy Sources, try identifying the renewable energy sources from the non-renewable in the activity below.

%%html

  <!-- Question 1 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <!-- Is Solar Energy a Renewable Energy Source? <p> tag below -->
    <p>Is Solar Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <!-- Each <li> tag is a list item to represent a possible Answer
        q1c1 stands for "question 1 choice 1", question 2 choice 3 would be 
        q2c3 for example. You can change this convention if you want its just 
        what I chose. Make sure all answers for a question have the same
        name attribute, in this case q1. This makes it so only a single
        radio button can be selected at one time-->
        <input type="radio" name="q1" id="q1c1" value="right">
        <label for="q1c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q1" id="q1c2" value="wrong">
        <label for="q1c2">No, it is a Non-Renewable Energy Source.</label>
      </li>
    </ul>
    <!-- Give a unique id for the button, i chose q1Btn. Question 2 I 
    I would choose q2Btn and so on. This is used to tell the script
    which question we are interested in. -->
    <button id="q1Btn">Submit</button>
    <!-- this is where the user will get feedback once answering the question,
    the text that will go in here will be generated inside the script -->
    <p id="q1AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>

  <!-- Question 2 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Oil Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q2" id="q2c1" value="wrong">
        <label for="q2c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q2" id="q2c2" value="right">
        <label for="q2c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q2Btn">Submit</button>
    <p id="q2AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>

  <!-- Question 3 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Natural Gas a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q3" id="q3c1" value="wrong">
        <label for="q3c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q3" id="q3c2" value="right">
        <label for="q3c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q3Btn">Submit</button>
    <p id="q3AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>


  <!-- Question 4 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Coal Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q4" id="q4c1" value="wrong">
        <label for="q4c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q4" id="q4c2" value="right">
        <label for="q4c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q4Btn">Submit</button>
    <p id="q4AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>


  <!-- Question 5 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Biomass Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q5" id="q5c1" value="right">
        <label for="q5c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q5" id="q5c2" value="wrong">
        <label for="q5c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q5Btn">Submit</button>
    <p id="q5AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>


  <!-- Question 6 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Wind Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q6" id="q6c1" value="right">
        <label for="q6c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q6" id="q6c2" value="wrong">
        <label for="q6c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q6Btn">Submit</button>
    <p id="q6AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>


  <!-- Question 7 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Water Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q7" id="q7c1" value="right">
        <label for="q7c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q7" id="q7c2" value="wrong">
        <label for="q7c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q7Btn">Submit</button>
    <p id="q7AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>

  <!-- Question 8 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Nuclear Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q8" id="q8c1" value="wrong">
        <label for="q8c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q8" id="q8c2" value="right">
        <label for="q8c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q8Btn">Submit</button>
    <p id="q8AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>



  <!-- Question 9 -->
  <div>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    <p>Is Geothermal Energy a Renewable Energy Source?</p>
    <ul style="list-style-type: none">
      <li>
        <input type="radio" name="q9" id="q9c1" value="right">
        <label for="q9c1">Yes, it is Renewable.</label>
      </li>
      <li>
        <input type="radio" name="q9" id="q9c2" value="wrong">
        <label for="q9c2">No, it is a Non-Renewable Energy Source. </label>
      </li>
    </ul>
    <button id="q9Btn">Submit</button>
    <p id="q9AnswerStatus"></p>
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
    &nbsp;&nbsp; 
    &nbsp;&nbsp;
  </div>





  <script>
    // Question 1
    // This looks at which question is being checked, pass in the buttons id
    document.getElementById("q1Btn").onclick = function () {
    // This if statment is used for the correct answer, in this case choice 3 is correct
      if (document.getElementById("q1c1").checked) {
    // "Correct Answer" field is where you can add any text to be displayed when it is correct
        document.getElementById("q1AnswerStatus").innerHTML = "Correct Answer!";
      } else {
    // "Wrong Answer" field is where you can add any text to be displayed when it is wrong
        document.getElementById("q1AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };

    // Question 2
    document.getElementById("q2Btn").onclick = function () {
      if (document.getElementById("q2c2").checked) {
        document.getElementById("q2AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q2AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };
      // Question 3
    document.getElementById("q3Btn").onclick = function () {
      if (document.getElementById("q3c2").checked) {
        document.getElementById("q3AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q3AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 4
    document.getElementById("q4Btn").onclick = function () {
      if (document.getElementById("q4c2").checked) {
        document.getElementById("q4AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q4AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 5
    document.getElementById("q5Btn").onclick = function () {
      if (document.getElementById("q5c1").checked) {
        document.getElementById("q5AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q5AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 6
    document.getElementById("q6Btn").onclick = function () {
      if (document.getElementById("q6c1").checked) {
        document.getElementById("q6AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q6AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 7
    document.getElementById("q7Btn").onclick = function () {
      if (document.getElementById("q7c1").checked) {
        document.getElementById("q7AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q7AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 8
    document.getElementById("q8Btn").onclick = function () {
      if (document.getElementById("q8c2").checked) {
        document.getElementById("q8AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q8AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };  // Question 9
    document.getElementById("q9Btn").onclick = function () {
      if (document.getElementById("q9c1").checked) {
        document.getElementById("q9AnswerStatus").innerHTML = "Correct Answer!";
      } else {
        document.getElementById("q9AnswerStatus").innerHTML = "Wrong Answer :(";
      }
    };
  </script>

## The Good and Bad Traits of Energy Sources

Now that we understand each of the energy sources, it is important to weigh the good and the bad traits of each energy source. Efficient means the energy technique is achieving maximum productivity with minimum wasted effort or expense. Note that the bad traits of an energy source are usually negative side effects that we are trying to lessen or prevent while gathering usable energy.  


<img src="https://thesolarscoop.com/wp-content/uploads/2018/03/Solar.jpg" style="margin: 0 auto; width: 1000px;">

#### Source Image: EcoFasten, March 2018. Retrieved from https://thesolarscoop.com/wp-content/uploads/2018/03/Solar

%%html
<head>
<style>

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Solar</h1>
<p></p>
<table style="width:100%" table align="left">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Solar energy has recently experienced decreasing costs and high public support. </td>
    <td style="text-align:left">Solar energy is intermittent, i.e. electricity production is dependent on sunlight.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">Low CO2 emissions.</td>
    <td style="text-align:left">Expensive but in recent years the cost of solar energy equipment has decreased.</td>
    
  </tr>
  <tr>
    <td style="text-align:left">Easy to install, little operation and maintenance work.</td>
    <td style="text-align:left">Forecasts are more unpredictable in comparison to fossil fuels (but better than wind).</td>
    
  </tr>
</table>

<h3></h3>
<p></p>

</body>
</html>

from IPython.display import Image
Image(url= "https://ak5.picdn.net/shutterstock/videos/17748445/thumb/5.jpg", width=1000, height=300)

#### Source Image: Shutterstock, n.d. Retrieved from https://www.shutterstock.com/video/clip-17748445-close-up-industrial-oil-pump-jack-working

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Oil</h1>
<p></p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Oil is cheap to produce and refine. </td>
    <td style="text-align:left">Burning oil for electricity is a major source of air pollution on Earth and leads to health concerns and environmental damage. </td>
   
  </tr>
  <tr>
    <td style="text-align:left">Unlike the renewable energy sources such as solar and wind energy that are weather dependent sources of power, Oil represents a reliable, ready-to-use source of energy.</td>
    <td style="text-align:left">Burning oil for energy releases harmful gases into the atmosphere such as carbon dioxide (CO2), carbon monoxide (CO), nitrogen oxides (NOx), and sulfur dioxide (SO2, causes acid rain). </td>
    
  </tr>
  <tr>
    <td></td>
    <td style="text-align:left">Despite the fact that oil energy can get jobs done in a less expensive way, it is not a renewable source of energy. There will come a time when we run out of supply.</td>
    
  </tr>
</table>

<h3></h3>
<p></p>

</body>
</html>


from IPython.display import Image
Image(filename="images/gasmap.jpg", width=1000, height=300)

#### Source Image: Studentenergy, n.d. Retrieved from https://www.studentenergy.org/topics/natural-gas

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Natural Gas</h1>
<p></p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Emits the least CO2 compared to the other forms of non-renewable fossil fuels.</td>
    <td style="text-align:left">Gas drilling has a negative impact on the environment.</td>
   
  </tr>
  <tr>
    <td style="text-align:left"> Natural gas hot water heaters typically heat water twice as fast as electric heaters.</td>
    <td style="text-align:left">Some regions that sell natural gas face political instability. This usually occurs when a country is dependent on natural gas as their only source of income. </td>
    
  </tr>
  <tr>
    <td></td>
    <td style="text-align:left">Natural gas is the more expensive energy source in comparison to other fossil fuels.</td>
    
  </tr>
</table>

<h3></h3>
<p></p>


</body>
</html>

from IPython.display import Image
Image(url= "https://images.theconversation.com/files/125332/original/image-20160606-26003-1hjtcr5.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=496&fit=clip", width=1000, height=100)

#### Source Image: The Conversation, June 2016. Retrieved from http://theconversation.com/is-coal-the-only-way-to-deal-with-energy-poverty-in-developing-economies-54163

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Coal</h1>
</p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Coal provides stable and large-scale electricity generation.</td>
    <td style="text-align:left">Coal power plants emit high levels of CO2.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">Coal power has a competitive production cost. Fuel costs are low and coal markets are well-functioning.</td>
    <td style="text-align:left">Technologies to reduce coal power plant CO2 emissions are expensive.</td>
    
  </tr>
  <tr>
    <td></td>
    <td style="text-align:left">Coal mining impacts the landscape and infrastructure leading to erosion and displacement of animals from their natural habitats.</td>
    
  </tr>
</table>


</body>
</html>

from IPython.display import Image
Image(url= "https://media.nationalgeographic.org/assets/photos/000/317/31713.jpg", width=1000, height=100)

#### Source Image: National Geographic, Photographs by USDA, V. Zutshi, S. Beaugez, M. Hendrikx, S. Heydt, M. Oeltjenbruns, A. Munoraharjo, F. Choudhury, G. Upton, O. Siudak, M. Gunther, R. Singh. Retrieved from https://www.nationalgeographic.org/photo/2biomass-crops-dup/

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Biomass</h1>
<p></p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Biomass resources are abundant, cost-effective and political risk is limited.</td>
    <td style="text-align:left">Requires large storage space.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">By using biomass in power production instead of fossil fuels, CO2 emissions are significantly reduced.</td>
    <td style="text-align:left">Burning of biomass still emits a fair level of CO2 and without proper management of biomass usage this CO2 could easily become a green house gas. </td>
    
  </tr>
  <tr>
    <td style="text-align:left">Properly managed biomass is carbon neutral over time. If not done in a sustainable way, biomass burning is doing more harm than good.</td>
    <td></td>
    
  </tr>
</table>


</body>
</html>



from IPython.display import Image
Image(url= "https://d32r1sh890xpii.cloudfront.net/article/718x300/1ffb18f07cf19289be69259800495f00.jpg", width=1000, height=300)

#### Source Image: Oilprice, n.d. Retrieved from https://oilprice.com/Alternative-Energy/Wind-Power/US-Wind-Energy-Demand-Surges.html

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Wind</h1>
<p></p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Wind power emits essentially no CO2 across its life cycle.</td>
    <td style="text-align:left">Has an impact on the landscape, wildlife and also emits noise.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">Has no fuel costs.</td>
    <td style="text-align:left">Dependent on available wind.</td>
    
  </tr>
  <tr>
    <td></td>
    <td style="text-align:left">Has significant investment costs.</td>
    
  </tr>
</table>


</body>
</html>


from IPython.display import Image
Image(filename="images/hydroelectric.jpg")

#### Source Image: What is Hydroelectric Power Plant? How Does It Work?, Jul. 2020. Retrieved from https://www.usgs.gov/media/images/flow-water-produces-hydroelectricity

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Hydro</h1>

<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Hydro power has almost no emissions that impact the climate or the environment.</td>
    <td style="text-align:left">Hydro power plants are a significant encroachment on the landscape and impact river ecosystems.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">Provides large-scale and stable electricity generation.</td>
    <td style="text-align:left">Constructing a new hydro power plant requires a substantial investment.</td>
    
  </tr>
  <tr>
    <td style="text-align:left">Has no fuel costs. Hydro power plants have a long economic life.</td>
    <td></td>
    
  </tr>
</table>


</body>
</html>

from IPython.display import Image
Image(url= "https://images.theconversation.com/files/178921/original/file-20170719-13558-rs7g2s.jpg?ixlib=rb-1.1.0&rect=0%2C532%2C4000%2C2377&q=45&auto=format&w=496&fit=clip", width=1000, height=300)

#### Source Image: Harga, n.d. Retrieved from https://www.tokoonlineindonesia.id/small-nuclear-power-reactors-future-or-folly.html

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Nuclear</h1>
<p></p>
<table style="width:100%">
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">Nuclear power emits low levels of CO2 across its life cycle.</td>
    <td style="text-align:left">The management of high-level waste requires storage in secure facilities for a very long time.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">Provides stable and large-scale electricity generation.</td>
    <td style="text-align:left">Construction of a new nuclear power plant requires major investments.</td>
    
  </tr>
  <tr>
    <td style="text-align:left">Costs for fuel, operation and maintenance are normally relatively low.</td>
    <td style="text-align:left">If nuclear waste spills or is handled incorrectly it has serious effects on the environment. </td>
    
  </tr>
</table>


</body>
</html>

from IPython.display import Image
Image(url= "https://www.longrefrigeration.com/wp-content/uploads/2017/06/Depositphotos_59228621_s-2015.jpg", width=1000, height=100)

#### Source Image: Long Heating and Cooling Geothermal Heat Pumps, June 2017. Retrieved from https://www.longrefrigeration.com/how-geothermal-energy-works/depositphotos_59228621_s-2015/

%%html
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h1>Geothermal</h1>
<p></p>
<table style="width:100%"> 
  <tr>
    <th style="text-align:center">Good Traits</th>
    <th style="text-align:center">Bad Traits</th> 
  </tr>
  <tr>
    <td style="text-align:left">It only requires heat from the earth to work, a limitless supply.</td>
    <td style="text-align:left">High costs to construct geothermal plants.</td>
   
  </tr>
  <tr>
    <td style="text-align:left">It is simple and reliable, unlike the unpredictability of solar or wind energy.</td>
    <td style="text-align:left">Sites must be located in prime areas, requiring long distance transportation of the resourse through pipe, which is often costly.</td>
    
  </tr>
  <tr>
    <td style="text-align:left">It is a domestic source of energy found throughout the world. This means that geothermal energy is used in many households across the world, mainly for heating/cooling systems. </td>
    <td style="text-align:left">Emits some sulfur dioxide (SO2). </td>
    
  </tr>
</table>


</body>
</html>



## Conclusion
In this notebook students learned about the 9 most popular sources of energy. The student should have a more clear understanding of the differences between renewable energy sources and non-renewable energy sources. Note that the good and bad traits of each energy source prompted the student to think about the efficiency of each energy source.

### And now a *"FeW FUn ENeRGy JokES"* to conclude!
* What did Godzilla say when he ate the nuclear power plant? 
            “Shocking!”
* Why did the lights go out? 
            Because they liked each other!
* What would a barefooted man get if he steps on an electric wire? 
            A pair of shocks!
* Why is wind power popular? 
            Because it has a lot of fans!

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)