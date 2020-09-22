![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/MethodsUsedInStudyingTheEarth/methods-used-in-studying-the-earth.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Methods used in Scientific Study of the Earth

from IPython.display import HTML, Image

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')

## Introduction
Over the past 4.6 billion years, the Earth has been constantly changing. As we know, the earth is always spinning and plate tectonics results in the the movement and formation of different continents. These changes occur over millions of years and can be observed from the surface by observing land forms and types of rocks in  the area. There are many specific indications that showcase different changes. These indications can be separated into two categories, sudden change and gradual change.
### Sudden Change
After a change occurs in the subsurface, it is brought to the surface as an event that is commonly classified as a "natural disaster" such as earthquakes and volcanoes. The main cause of these events is plate tectonics. Earth's crust is divided into many pieces called plates which move in relation to one another. Typically, plates move at a rate of 10cm/yr which seems very slow. As the plates move, they exert pressure on one another can result in earthquakes or volcanic eruptions.


from __future__ import print_function
from IPython.display import Image, HTML, clear_output
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import random

<img src="https://www.sciencealert.com/images/parks-plates_cascadia_subduction_zone_revised-01.jpg" alt="Volcano" width="420" />

Figure 1: Cross section of the volcano. One plate is being subducted underneath the other. The subducted plate is melting by the hot mantle which causes lava to reach the surface and escape through the surface in a volcanic eruption. This process can also cause earthquakes. (ScienceAlert)


### Gradual Change
Over time, much of the surface of the Earth has been subject to long term changes by wind and water. Rivers are channels of water which erode the surrounding area as they continue to flow while wind displaces dust and dirt, changing the shapes of the formations.

![erosion](images/erosion.jpg)

Figure 2: Erosion by fast moving water can cause different landforms to be created such as a waterfall. (Alexandra falls, NWT, Canada. Photo credits: Alyson Birce)

## Modelling Earth's Interior
From the surface of the Earth, we have seen the different types of changes. The trends regarding the magnetic and gravitational fields can provide insight into the cross section of the Earth. From lots of research, the current model of the Earth is shown below.

![Cross section](https://prd-wret.s3-us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/atom_page_medium/public/thumbnails/image/earthxsection.jpg?itok=mIG3lL0v)

Figure 3: Cross section of the Earth (U.S Geological Survey)

## Tools/ Techniques
There are a variety of methods that are used to observe the subsurface at a depth that can not be reached by simply using a shovel.

### Seismographs
A Seismograph is an instrument that is used to record fluctuations in the ground shown in figure 4. This is commonly used to predict and record earthquakes. There are 3 types of earthquake waves: p waves, s waves and surface waves which occur in that order respectively. All of these can be seen on seismograph records as seen in Figure 5 below. An earthquake begins at a set point called the Focal point which the source of wave propagation. P waves are also referred to as primary waves and are recorded first as they move the fastest and it is transmitted through the whole Earth. S waves are also referred to as secondary waves and are the second wave to be recorded. These waves can not travel through liquids such as the mantle. This can be seen in Figure 5. A surface wave is the mechanical wave that causes the most damage during the Earthquake.

![seismograph](images/seismograph.jpg)

Figure 4: The Seismograph instrument used to record earthquakes. (Indiana State University)

![Earth GIF](https://media.giphy.com/media/kQPS6ASP23cvC/giphy.gif)

Figure 5: This diagram shows how the waves propagate through the earth during the earthquake. The focal point is marked by the white circle at the beginning of the video, then the waves propagate outwards. The P waves are marked with red lines, the S waves are marked with blue lines and the surface waves are marked with yellow lines. (GIPHY)

### Core Drills
When analyzing the composition of the subsurface, we can use a drill to extract a long cylinder section of Earth. This is used to determine the composition which is useful when looking for evidence of oil.

![core drill](https://upload.wikimedia.org/wikipedia/commons/5/5b/Drilling_mechanical-drill-head.jpg)
Figure 6: A drill bit for taking core samples

![core samples](https://upload.wikimedia.org/wikipedia/commons/d/db/Drill_core_repository_-_Geological_and_Mining_Institute_of_Spain_03.JPG)
Figure 7: Geological core samples

## Describing Rocks and Minerals
### Definitions
**Rock** - a natural substance which is composed of minerals.
**Mineral** - a naturally occurring chemical compound that is not produced by life processes.
Rocks and minerals can not be accurately identified by colour alone. The other properties must be taken into account for proper identification. These properties include luster, transparency, cleavage and fracture, and the Moh's hardness scale. In this section, we will explore each of the properties.
### Luster
This describes the "shinyness" of the sample. This assists with categorizing minerals as metals verses non-metals.

![pyrite](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Pyrite_3.jpg/320px-Pyrite_3.jpg)
Figure 8: Pyrite with a metallic luster

![kaolinite](https://upload.wikimedia.org/wikipedia/commons/9/94/KaolinUSGOV.jpg)
Figure 9: Kaolinite with a dull luster

### Transparency
Can you see through the mineral? If so, how much?

![quartz](https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz%2C_Tibet.jpg/239px-Quartz%2C_Tibet.jpg)
Figure 10: Quartz, which is relatively transparent (photo by [JJ Harrison](https://www.jjharrison.com.au))

![transparent calcite](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/RM463c-calcite-butterfly-twin.jpg/166px-RM463c-calcite-butterfly-twin.jpg)
Figure 11: A transparent form of calcite (photo by [Joan Rosell](https://www.rosellminerals.com/minerales.php?idmineral=160&yng=1))

### Cleavage and Fracture
This describes the shape of the rock if it were to break.
**Fracture** - When the rock breaks, the edges appear rough and cracked.

![fractured graphite](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Glassy_carbon_and_a_1cm3_graphite_cube_HP68-79.jpg/290px-Glassy_carbon_and_a_1cm3_graphite_cube_HP68-79.jpg)
Figure 12: Fractured graphite (photo by [Alchemist-hp](www.pse-mendelejew.de))

**Cleavage** - When the rock breaks, it would break along a plane where the edges appear smooth as if they were cut. This can be further subdivided into subcategories based on the number of directions the planes run. These are shown below.

![categories of cleavage](http://academic.brooklyn.cuny.edu/geology/grocha/mineral/images/cleavage.jpg)
Figure 13: Subcategories of cleavage based on the number of planes that are apparent (by [David Seidemann and David Leveson](http://academic.brooklyn.cuny.edu/geology/grocha/rocks/index.html))

### Moh's Hardness scale
The hardness of a rock is ranked on a scale of 1-10 based on how easy it can be scratched. Common rocks as well as tools can be used to compare hardness, for example fingernail have a hardness of about 2.5. Typically the chosen material is scratched against the surface of the unknown rock. The surface that ends up with a scratch mark is the softer substance.

![hardness scale](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Mohssche-haerteskala_hg.jpg/454px-Mohssche-haerteskala_hg.jpg)
Figure 14: Mohs hardness kit, containing one specimen of each mineral on the ten-point hardness scale (from [Wikipedia](https://en.wikipedia.org/wiki/Mohs_scale_of_mineral_hardness))

### References
1. ScienceAlert, Discover Ideas on Active volcanoes, Pinterest, accessed 3 July 2018
<https://www.pinterest.com.au/pin/849421179688448478 >
2. U.S Geological Survey, Earth Cross-Section, accessed 3 July 2018
<https://www.usgs.gov/media/images/earth-cross-section>
3. Nevada Seismological Laboratory, Seismic Deformation, accessed 3 July 2018
<http://crack.seismo.unr.edu/ftp/pub/louie/class/100/seismic-waves.html>
4. GIPHY, Earth GIFs, accessed 3 July 2018
<https://media.giphy.com/media/kQPS6ASP23cvC/giphy.gif>
5. Wintershall, The Well, accessed 6 July 2018
<https://www.wintershall.com/technology-innovation/drilling.html>
6. The Northern Miner, accessed 6 July 2018
<http://www.northernminer.com/news/balmoral-delivers-more-high-grade-nickel-pgm-at-grasset/1003214678/>
7. geology.com, Hematite, accessed 6 July 2018
<https://geology.com/minerals/hematite.shtml>
8. geology rocks and minerals, quartzite, accessed 6 July 2018
<https://flexiblelearning.auckland.ac.nz/rocks_minerals/rocks/quartzite.html>
9. Wikipedia, accessed 28 January 2019
<https://en.wikipedia.org/wiki/Quartz>
10. Lock Haven, calcite, accessed 6 July 2018
<https://www.lockhaven.edu/~dsimanek/14/stereo.htm>
11. Arkansas Geological Survey, zinc ore, accessed 9 July 2018
<https://arkansasgeological.wordpress.com/tag/sphalerite/>
12. Brooklyn College, Cleavage, accessed 9 July 2018
<http://academic.brooklyn.cuny.edu/geology/grocha/mineral/cleavage.html>
13. Amazon, Moh's Hardness scale, accessed 9 July 2018
<https://www.amazon.com/Mohs-Hardness-Scale-Collection-specimens/dp/B00K24O1G8>


[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)