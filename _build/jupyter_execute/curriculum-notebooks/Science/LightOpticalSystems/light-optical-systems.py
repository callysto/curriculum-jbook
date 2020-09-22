![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/LightOpticalSystems/light-optical-systems.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
import numpy as np
import math
import ipywidgets as widgets
from IPython.display import display, Math, Latex, HTML, IFrame
from astropy.table import Table, Column
from ipywidgets import interact, interactive

py.offline.init_notebook_mode(connected=True)
%matplotlib inline

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

'''Above, we are importing all the necessary modules in order to run the notebook. 
Numpy allows us to define arrays of values for our variables to plot them
matplotlib is what we use to create the figures
the display and widgets are to make the notebook look neat
'''

HTML('''<script>
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
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>''')
        
    


***
# Light and Optics
***

<img src="https://media.giphy.com/media/3o7OsM9vKFH2ESl0KA/giphy.gif" alt="Drawing" style="width: 600px;"/>
<center>Gif taken from https://giphy.com/gifs/fandor-sun-eclipse-3o7OsM9vKFH2ESl0KA/links, August 1st, 2018.</center>
<center> Figure 1: For hundreds of years, scientists have tried to understand the nature of light. With advances in technology, and inventions like telescopes, we have been able to see farther than ever before. </center> 

***

## Introduction

Throughout most of history, humans did not understand light as we do today. As science and technology have progressed over time, so too has our knowledge of the nature of light. 

In this lesson, when we say the word "light", we will be referring to visible light (light that comes from the sun, lightbulbs etc.). We will go over how a few key experiments kickstarted a new way of thinking, and a few of the ways that we are able to manipulate light. We will also talk about how our eyes enable us to see.

## Background

If you had to describe to someone what light is, you may have a hard time. Some people think of light as the absence of darkness, but even that doesn't say much about light itself.

Our understanding of light truly began around the 17th century, when a few individuals started to realize that light was not a mystical substance. Scientists (or "natural philosophers", as they were called during that time) recognized that certain properties of light were measurable, and that some properties could be manipulated. Sir Isaac Newton and Ole Rømer were among the first scientists to take a step in this direction.


> ### Isaac Newton's Prism Experiment

Sir Isaac Newton has made contributions to many fields of science and mathematics. In 1666, while spending time at his childhood home in Lincolnshire, England, Newton began experimenting with light. 

Using a small slit in his window shutters, Newton passed a narrow beam of sunlight through a glass prism. The light travelled through the prism, and projected a rainbow of color on the other side!

<img src="http://media.web.britannica.com/eb-media/10/7710-050-36C066AC.jpg" >

<center>Picture taken from http://media.web.britannica.com/eb-media/10/7710-050-36C066AC.jpg.</center>
<center> Figure 2: This picture shows how a prism can create a spectrum of color. This is what Newton would have seen in 1666.</center>

Later on, scientists determined that the prism was actually splitting light into its component parts. This phenomenon is called **dispersion**.

Through this experiment, Newton demonstrated that white light was actually made up of all the individual colors of the rainbow!

> ### Ole Rømer and the Speed of Light

For many years, people thought that if somebody lit a match, the light from that match would be instantly visible to everyone, no matter how far away they were. However, in 1676 Ole Rømer proved that this is not the case.

Rømer spent a long time studying the orbit of Io, one of Jupiter's moons. As part of his study, he began predicting the times when Io should be hidden behind Jupiter's shadow (these periods are called eclipses). However, Rømer saw that his predictions for when these eclipses should occur were not always accurate. 

<img src="https://media.giphy.com/media/DXIa1beDspYRy/giphy.gif" alt="Drawing" style="width: 300px;"/>
<center>Gif taken from https://giphy.com/gifs/timelapse-DXIa1beDspYRy, August 1st, 2018.</center>
<center> Figure 3: Here we can see Jupiter as it looks through a telescope. You might be able to see a black spot move from the left to the right across Jupiter's surface. This is actually one of Jupiter's many moons!</center> 

Rømer then realized that these errors may be because the distance between Io and the Earth was always changing. Rømer thought that when the distance between Io and the Earth increased, it might take a longer time for light coming from Io to reach Earth. If this were the case, then the light must be travelling at a finite speed!

After taking many measurements and using some clever mathematics, Rømer calculated the speed of light to be roughly 220,000,000 m/s, or 792,000,000 km/h.

Today, we have measured the speed of light to be 299,792,458 m/s. Although he was not exactly right, Rømer provided one of the first mathematical calculations for the speed of light. 

***
Since the time of Rømer and Newton, scientists have made many new discoveries about the nature of light. While not all of these discoveries agree with one another, here are two things we know for sure:
- Light is made up of a spectrum of color
- Light travels at a speed of 299,792,458 m/s

Now let's talk about some of the ways we can manipulate light.
***

## Reflection

We are all familiar with reflection; chances are, you look at your reflection more than once a day. But have you ever stopped to wonder what is really going on? 

Reflection is the term used to describe how light can change direction when it comes into contact with certain surfaces. 

When incoming light rays encounter a reflective surface, they bounce off the surface and continue moving in a new direction. The new direction in which it moves is determined by the **law of reflection**.

\begin{equation} 
\rm Law\: of\: Reflection: Angle\: of\: Incidence = Angle\: of\: Reflection
\end{equation}

On the animation below, click on the flashlight to turn it on, and move your mouse to change the angle of incidence.

#IFrame('Animations/reflect.html',width=500,height=320)

%%html
<iframe src='Animations/reflect.html' width=500 height=350></iframe>


As seen above, the **normal** is what we call the line that forms a 90$^{\circ}$ angle with  the surface. The **angle of incidence** is what we call the angle between the flash lights beam and the normal. Similarly, the **angle of reflection** is the angle that the newly reflected light beam makes with the normal. The law of reflection states that these two angles will always be equal.



## Refraction

Have you ever tried to reach down and grab an object sitting at the bottom of a pool of water? If you have, you may have noticed that the object isn't actually in the location that you thought it was.

<img src="http://legacy.sciencelearn.org.nz/var/sciencelearn/storage/images/contexts/light-and-sight/sci-media/video/refraction/668954-1-eng-NZ/Refraction.jpg" alt="Drawing" style="width: 450px;"/>
<center> Image taken from http://legacy.sciencelearn.org.nz/Contexts/Light-and-Sight/Sci-Media/Video/Refraction/(quality)/hi on August 3rd, 2018.</center>
<center> Figure 4: When you are looking into a body of water from above, the objects you see beneath the surface are not actually where they appear to be. </center>

This phenomenon occurs because the light travelling to your eyes from the bottom of the pool **refracts**, or changes its direction of travel, when it transitions from water to air. 

The **index of refraction** is a value that we use to show how much light will bend when travelling through a substance. For example, the index of refraction for air is approximately 1.00, and the index of refraction for water is about 1.33. Because these indexes are different, light will bend when passing from water to air, or vice versa.

Use the animation below to see how light refracts when passing from air to water. Click on the flashlight to turn it on.

#IFrame('Animations/refract.html',width=520,height=320)

%%html
<iframe src='Animations/refract.html' width=520 height=320></iframe>


Mathematically, reflection can be described using the following equation, known as Snell's Law:

\begin{equation} 
\textrm{Snells Law:}\: n_1\sin(\theta_1) = n_2\sin(\theta_2)
\end{equation}

where $n_1$ is the index of refraction for the first medium, $\theta_1$ is the incident angle, $n_2$ is the index of refraction for the second medium, and $\theta_2$ is the angle of refraction.

Light will bend *towards* the normal when travelling from a medium with a *lower* index of refraction to one with a *higher* index of refraction, and vice versa.

***
Some of the most beautiful sights in nature are caused by reflection and refraction. Here are a couple of examples:

### Rainbows

Rainbows are a result of both reflection and refraction. As its raining, each water droplet acts like a tiny prism, just like the one we saw in Figure 2. The water droplets split visible light into colors, and these colors are then reflected back towards our eyes. 

<img src="http://waterstories.nestle-waters.com/wp-content/uploads/2015/04/How-rainbow-forms-waterstories.jpg" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://waterstories.nestle-waters.com/environment/how-does-a-rainbow-form/ on August 3rd, 2018.</center>
<center> Figure 5: Water droplets use reflection and refraction to create the beautiful rainbows that we see while it is raining.</center>



### Mirages

Have you ever been driving on a sunny day, and up ahead it looks as though a stream of water is running across the road? You are really seeing a mirage.
Mirages also occur because of refraction, but they do not result in a display of color like a rainbow. This type of refraction occurs due to a difference in temperature between separate layers of air.

As we were describing before, refraction occurs when light travels from one substance to another. Well, it turns out that hot air and cold air are actually different enough to act as different substances. Therefore, light will refract when passing through one to the other. 

<img src="http://edex.s3-us-west-2.amazonaws.com/styles/kraken_optimized/s3/banner-mirage.jpg?itok=YXSTIo8_" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://edexcellence.net/articles/what-the-mirage-gets-wrong-on-teacher-development on August 3rd, 2018.</center>
<center> Figure 6: Although it may look like water running across the road, it is actually a mirage. These commonly occur in desert areas, where the road can become very hot.</center>

When you are looking at a mirage, it can look as though the air is wavy and fluid, which is why it is common to think that you are looking at water. This appearance occurs when layers of hot and cold air are mixing together, and light passing through these layers is constantly being refracted in different directions.

You may see a mirage appear on top of a hot roadway, behind the exhaust pipe of a plane or car, or around any other source of heat.

## Applications of Reflection and Refraction

### Lenses

If you have glasses, or contact lenses, then you are constantly using refraction in order to help you see! Lenses use refraction to point light in specific directions.

Generally speaking, there are two types of lenses: **convex** and **concave**.

To see how each type of lens affects light, use the following animation.

#IFrame('Animations/convex.html',width=520,height=420)

%%html
<iframe src='Animations/convex.html' width=520 height=430></iframe>


As seen above, a convex lens focuses light towards a specific point, while a concave lens will spread light away from a point. These lenses can be combined in many ways in order to produce different effects. For example, a camera lens uses a series of both convex and concave lenses in order to direct incoming light towards the back of the camera.

<img src="http://i.imgur.com/IH2ymaj.jpg" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://www.reddit.com/r/pic/comments/3o3b7w/camera_lens_cut_in_half/ on August 3rd, 2018.</center>
<center> Figure 5: This is what the inside of a camera lens looks like. The photographer can adjust how they want the picture to look by changing the distance between the individual lenses.</center>




## Vision

Our eyes are very complex organs, but the process that enables us to see is actually pretty simple. The basic steps are as follows:

1. Light enters the eye through the **pupil**
2. The convex **lens** behind the pupil directs incoming light towards the **retina**, which is like a screen at the back of our eye.
3. The retina then sends this image to the brain.
4. The brain then interprets the image. 

<img src="https://openclipart.org/image/2400px/svg_to_png/261647/EyeDiagram.png" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://openclipart.org/detail/261647/eye-diagram on August 3rd, 2018. </center>
<center> Figure 6: This diagram shows some of the key components of the eye that enable us to see.</center>

However, the image that is projected onto the retina is actually upside down! 

<img src="https://m.eet.com/media/1077748/max-hfield-01.gif" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://www.eetimes.com/author.asp?section_id=14&doc_id=1282795 on August 3rd, 2018.</center>
<center> Figure 7: The convex lens at the front of our eye actually flips images upside down.</center>

So the retina actually sends an upside down image to the brain, and the brain automatically flips the image rightside up.

Use the following link to see an animation showing how a convex lens flips images upside down:https://phet.colorado.edu/sims/geometric-optics/geometric-optics_en.html.


## Technology & Inventions

### The Telescope

The first telescope was made by Hans Lippershey in 1608, but it was Galileo Galilee who became famous by using it for astronomy. There are many different types of telescopes, but they all use reflection and refraction to make far away objects appear closer.

A telescope uses a large opening to collect incoming light, and then directs this light towards your eye by using mirrors and lenses.

<img src="https://www.skyandtelescope.com/wp-content/uploads/three-scopes.jpg" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://www.skyandtelescope.com/press-releases/tips-for-first-time-telescope-buyers/ on August 3rd, 2018.</center>
<center> Figure 8: Telescopes come in many different shapes and sizes.</center>

The reason why things look bigger when looking through a telescope is because of the lenses.


### The Microscope


- talk about invention of microscope
- why it works


## Conclusion

Our understanding of light is the result of hundreds of years of research and innovation. Along the way, we have created incredible new technologies that have allowed us to look further than ever before.

<img src="https://xenlife.com.au/wp-content/uploads/Hubble-Space-Telescope-650x250-1078x516.jpg" alt="Drawing" style="width: 400px;"/>
<center> Image taken from https://xenlife.com.au/hubble-space-telescope-important/ on August 3rd, 2018.</center>
<center> Figure 9: The Hubble Space Telescope has shown us pictures of galaxies that are billions of light years away.</center>
 



[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)