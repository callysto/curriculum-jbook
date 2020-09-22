![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/RadiatonAnimations/radiation-animations.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

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

utils_code = """
class TextBox {
  PVector location;
  PVector velocity;
  
  TextBox(float x_loc, float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }

  void update() {
    location.add(velocity);
  }
  
  void display(String message, int size, float[] col) {
    textSize(size);
    fill(col[0],col[1],col[2]);
    text(message, location.x, location.y);
  }
}

class Mover {
  PVector location;
  PVector velocity;
  
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }
  
  void update() {
    location.add(velocity);
  }
}

class Gamma extends Mover {
  Gamma(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  //creates squiggly lines for a gamma ray
  float[] twoLines(float x_val, float y_val, int i) {
    //upwards gamma
    if (i == 1) {
      // return the coordinates of two perpendicular lines
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val-10 },
        { x_val+3, y_val-10, x_val+15, y_val-12 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = { coords[1][2], coords[1][3] };
      return end;
    } else {
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val+10 },
        { x_val+3, y_val+10, x_val+15, y_val+8 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = {coords[1][2], coords[1][3]};
      return end;
    }
  }

  void drawArrow(float cx, float cy, int len, float angle) {
    pushMatrix();
    translate(cx, cy);
    rotate(radians(angle));
    line(0, 0, len, 0);
    line(len, 0, len-8, -8);
    line(len, 0, len-8, 8);
    popMatrix();
  }
  
  void display(int i, int angle) {
    stroke(255, 0, 0);
    float[] x = twoLines(location.x, location.y, i);
    float[] y = twoLines(x[0], x[1], i);
    float[] z = twoLines(y[0], y[1], i);
    drawArrow(z[0], z[1], 10, angle);
  }
}

float[][] position(float x_val, float y_val, float radius) {
  // make it produce the x and y coordinates for the 6 spots around it
  float y_dist = sin(radians(30)) * 2 * radius;
  float x_dist = cos(radians(30)) * 2 * radius;
  
  //coords is a list that contains the new coordinates for 6 circles around one circle
  float[][] coords = {
    { x_val, y_val-(2*radius) },
    { x_val+x_dist, y_val-y_dist },
    { x_val+x_dist, y_val+y_dist },
    { x_val, y_val+(2*radius) },
    { x_val-x_dist, y_val+y_dist },
    { x_val-x_dist, y_val-y_dist }
  };
  
  return coords;
}

boolean isItemInArray(float[][] array, float[] item) {
    for (int i = 0; i < array.length; i++) {
        // This if statement depends on the format of your array
        if (array[i][0] == item[0] && array[i][1] == item[1]) {
            return true;   // Found it
        }
    }
    return false;   // Not found
}
"""

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
        
    

# Nuclear Radiation: Alpha, Beta, and Gamma

<img src="https://media.giphy.com/media/3bvICesX0yIfu/giphy.gif" alt="Drawing" style="width: 750px;"/>

<center>Gif from [Giphy](https://giphy.com/gifs/hypnotic-3bvICesX0yIfu), June 20th, 2018.</center>

Figure 1: Here we see a sample of uranium undergoing radioactive decay inside a cloud chamber. The lines shooting out from the sample are made by fast moving charged particles ejected by the uranium. A cloud chamber such as this allows us to see how radiation can interact with its surroundings. Check out [this link](https://www.sciencealert.com/watch-uranium-emits-radiation-inside-cloud-chamber) for more info on cloud chambers.

## Introduction

The term "radiation" can be used to describe a broad spectrum of physical phenomena. Generally speaking, **radiation** refers to the emission of energy from a source in the form of either a wave, or a particle, and the ways in which these emissions are generated can vary significantly. 

In our daily lives, we interact with many forms of **electromagnetic radiation** (EMR) without a second thought, whether it be radio, microwave, infrared or visible light. However, there are other forms of radiation that may be less noticeable to the average person. 

In this notebook we will talk about three types of **nuclear radiation**: **alpha radiation, beta radiation, and gamma radiation**. We will talk about how these types of radiation are generated, how they interact with nature and their surroundings, and some of their useful applications. The analysis of various types of radiation can provide scientists with new ways to understand how the universe operates, and can result in previously unknown applications that make our lives easier.

## Background

Let's begin by outlining the general difference between wave radiation and particle radiation.

### Wave Radiation

All wave type radiation is classified as EMR. Electromagnetic radiation can be described as an interplay between electric and magnetic fields, with each oscillating along planes that are perpendicular to one another. Take a look at the gif below for a better visualization of this phenomenon:

<img src="http://www.ariel.ac.il/sites/cezar/ariel/ANIMATIONS/images/wave_movie.gif" alt="Drawing" style="width: 500px;"/>
<center>Image from http://www.ariel.ac.il/sites/cezar/ariel/ANIMATIONS/physics3.html</center>
<center> Figure 2: As the name suggests, electromagnetic waves consist of both electric and magnetic fields that propagate perpendicularly to one another. </center>
 

These waves are usually generated through interactions between subatomic particles within an atom. For example, visible light can be created when an electron changes energy levels within an atom. When an electron moves from a higher energy orbital to a lower energy orbital, the difference in energy is released as electromagnetic radiation. Take a look at the animation below that demonstrates how visible light can be generated within a hydrogen atom.

Click on the hydrogen atom to run the animation.

hydrogen_code = """
class TextBox {
  PVector location;
  PVector velocity;
  
  TextBox(float x_loc, float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }

  void update() {
    location.add(velocity);
  }
  
  void display(String message, int size, float[] col) {
    textSize(size);
    fill(col[0],col[1],col[2]);
    text(message, location.x, location.y);
  }
}

class Mover {
  PVector location;
  PVector velocity;
  
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }
  
  void update() {
    location.add(velocity);
  }
}

class Gamma extends Mover {
  Gamma(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  //creates squiggly lines for a gamma ray
  float[] twoLines(float x_val, float y_val, int i) {
    //upwards gamma
    if (i == 1) {
      // return the coordinates of two perpendicular lines
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val-10 },
        { x_val+3, y_val-10, x_val+15, y_val-12 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = { coords[1][2], coords[1][3] };
      return end;
    } else {
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val+10 },
        { x_val+3, y_val+10, x_val+15, y_val+8 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = {coords[1][2], coords[1][3]};
      return end;
    }
  }

  void drawArrow(float cx, float cy, int len, float angle) {
    pushMatrix();
    translate(cx, cy);
    rotate(radians(angle));
    line(0, 0, len, 0);
    line(len, 0, len-8, -8);
    line(len, 0, len-8, 8);
    popMatrix();
  }
  
  void display(int i, int angle) {
    stroke(255, 0, 0);
    float[] x = twoLines(location.x, location.y, i);
    float[] y = twoLines(x[0], x[1], i);
    float[] z = twoLines(y[0], y[1], i);
    drawArrow(z[0], z[1], 10, angle);
  }
}

float[][] position(float x_val, float y_val, float radius) {
  // make it produce the x and y coordinates for the 6 spots around it
  float y_dist = sin(radians(30)) * 2 * radius;
  float x_dist = cos(radians(30)) * 2 * radius;
  
  //coords is a list that contains the new coordinates for 6 circles around one circle
  float[][] coords = {
    { x_val, y_val-(2*radius) },
    { x_val+x_dist, y_val-y_dist },
    { x_val+x_dist, y_val+y_dist },
    { x_val, y_val+(2*radius) },
    { x_val-x_dist, y_val+y_dist },
    { x_val-x_dist, y_val-y_dist }
  };
  
  return coords;
}

boolean isItemInArray(float[][] array, float[] item) {
    for (int i = 0; i < array.length; i++) {
        // This if statement depends on the format of your array
        if (array[i][0] == item[0] && array[i][1] == item[1]) {
            return true;   // Found it
        }
    }
    return false;   // Not found
}
class HydrogenMover extends Mover {
  float rad;
  
  HydrogenMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
    rad = 0.02;
  }
  
  void update(int dist) {
    location.x = 350 + sin(rad)*(dist);
    location.y = 100 + cos(rad)*(dist);
    rad = rad + 0.02;
  }
  
  void display(int i, int rad) {
    stroke(0);

    //red
    if (i == 0) {
      fill(255, 0, 0);
    } else if (i == 1) {
      fill(12, 48, 224);
    } else if (i == 2) {
      fill(255, 255, 255);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

// Implementations are identical so using inheritance to "alias" Gamma
class Photon extends Gamma {
  Photon(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }
}

int x = 0;

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void setup() {
  size(700,200);
}

//create stationary proton
HydrogenMover proton = new HydrogenMover(350,100,0,0);
//create electron
HydrogenMover electron = new HydrogenMover(350,50,0,0);

HydrogenMover n3 = new HydrogenMover(350,100,0,0);
HydrogenMover n2 = new HydrogenMover(350,100,0,0);

Photon red = new Photon(350,100,2,0.5);

//create text for energy levels

// create text for n = 3
float n3x_loc = 420;
float n3y_loc = 100;
float n3x_vel = 0;
float n3y_vel = 0;
String n3_message = "n = 3";
int n3_size = 12;
float[] n3_col = {0,0,0};
TextBox n3_text = new TextBox(n3x_loc,n3y_loc, n3x_vel, n3y_vel);

// create text for n = 2
float n2x_loc = 375;
float n2y_loc = 100;
float n2x_vel = 0;
float n2y_vel = 0;
String n2_message = "n = 2";
int n2_size = 12;
float[] n2_col = {0,0,0};
TextBox n2_text = new TextBox(n2x_loc,n2y_loc, n2x_vel, n2y_vel);

void draw() {
  background(255);
  textSize(24);
  fill(0);
  text("Electron Transition in Hydrogen Atom", 145, 30);
  
  textSize(24);
  
  if (x == 1) {
    //shift electron to n = 2, emit light
    n3.display(2,120);
    n2.display(2,40);
    n2_text.display(n2_message, n2_size,n2_col);
    proton.display(1,16);
    electron.display(0,8);
    electron.update(20);
    red.display(0,20);
    red.update();
  } else {
    //make electron orbit around n = 3
    n3.display(2,120);
    n3_text.display(n3_message, n3_size,n3_col);
    n2.display(2,40);
    proton.display(1,16);
    electron.display(0,8);
    electron.update(60);
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas1");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas1"> </canvas>    
"""

html_code = html_template.format(utils_code+hydrogen_code)
HTML(html_code)

<center> Figure 3: The electron in the hydrogen atom changes from the $n = 3$ energy level to the $n = 2$ energy level. This transition results in the emission of a red photon.</center>

Other high energy interactions within an atom will create waves with higher energy, and vice-versa. Later on, we will talk about some of the high energy processes that create gamma rays.

### Particle Radiation

On the other hand, particle radiation consists of one or more solid particles being ejected from an atom. These ejections can arise from the **radioactive decay** of an unstable nuclei, or from a reaction between two separate nuclei, such as a particle collision, or a fission/fusion reaction. 

The term **radioactive decay** refers to the process whereby a large atomic nucleus breaks down into a smaller, more stable nucleus. Radioactive decay occurs when the forces holding the nucleus together (the strong and weak nuclear forces) become overwhelmed by the forces pulling it apart. When this happens, the nucleus will eject one or many particles in order to become smaller, and more stable.

Reactions such as **nuclear fission** and **nuclear fusion** can also create particle radiation. **Nuclear fission** is a type of nuclear reaction wherein the nucleus of an atom is forcibly split into two smaller nuclei, and **nuclear fusion** is the reverse: two smaller nuclei combine to form one larger nucleus. These processes require extreme conditions, vast amounts of energy, and can produce many different types of particle and wave radiation as a byproduct.  We won't go into much more detail about these processes, but here is a link to information on fission and fusion if you are interested: https://nuclear.duke-energy.com/2013/01/30/fission-vs-fusion-whats-the-difference.

In either case, whether it be a nuclear reaction or radioactive decay, one or many subatomic particles (protons, neutrons, electrons, neutrinos etc.) may be sent flying away from an atom at a high velocity. By recognizing the particles that have been ejected, and by measuring the energy that they carry, scientists are able to determine the source of the radiation and the processes that caused it. 


<img src="http://static.messynessychic.com/wp-content/uploads/2017/01/neil-degrasse-tyson-super-k-.jpg" alt="Drawing" style="width: 750px;"/>
<center>Image from http://www.messynessychic.com/2017/01/13/journey-to-the-centre-of-the-earth-in-a-rubber-dingy</center>
<center> Figure 4: Here we see Dr. Neil deGrasse Tyson inside the Super-Kamiokande Neutrino Detector in Japan. This incredibly sensitive device recognizes neutrino radiation coming from across the universe, and measures their energy and trajectory to provide information on the objects that have sent them to us. </center>


## Dangers of Radiation

Whether it be from sci-fi movies or real life threats of nuclear war, you are probably familiar with the potential devastation that comes from certain forms of radiation. With all of this information, you may be wondering: how are invisible waves and tiny particles so dangerous? Well, the danger arises from the potential for radiation to ionize other atoms that they come into contact with. 

When atoms within a biological cell are ionized, the functionality of the cell can be disrupted. The cell may repair itself improperly, or die altogether. When this happens on an acute level, many health issues can arise, including cancer. Both particle and wave radiation have the potential to ionize atoms, but some forms of radiation are more dangerous than others, as we will see in the sections below.


Now that you are more familiar with the differences between particle and wave radiation, let's get into the details of alpha, beta, and gamma radiation.
    
    

## Alpha ($\alpha$) Radiation

**Alpha radiation**, also known as **alpha decay**, occurs when a large unstable atomic nucleus radioactively decays and ejects an **alpha particle**. An alpha particle consists of two neutrons and two protons, and is identical to the nucleus of a helium-4 atom.

### Creation
The nucleus of an atom consists of protons and neutrons, which are bound together by the **strong nuclear force**. This force is very strong over small distances, but it is constantly in competition with the electromagnetic repulsion between the positively charged protons within the nucleus. 

In a large nucleus, the strong nuclear force can become overwhelmed by these electromagnetic repulsions, leading to the ejection of an alpha particle. By ejecting two protons and two neutrons, the nucleus loses two units of charge and the electromagnetic repulsions decrease in strength, lending more stability to the nucleus.

After the nucleus ejects the alpha particle, it becomes an element with an atomic number two less, and an atomic mass four less than the original atom.

Click on the nucleus to run the animation.

alpha_code = """
class AlphaMover extends Mover {
  AlphaMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int i) {
    stroke(0);

    if (i % 2 == 0) {
      fill(175);
    } else {
      fill(12,48,224);
    }

    ellipse(location.x, location.y, 16, 16);
  }
}

AlphaMover[] movers = {};

void addMover(float x_loc, float y_loc, float x_vel, float y_vel) {
  movers = (AlphaMover[])append(movers, new AlphaMover(x_loc, y_loc, x_vel, y_vel));
}

void setup() {
  size(700, 200);
  float[] center = {100.0, 100.0};
  float[][] all_coords = {};
  float[][] orig_coords = position(center[0], center[1], 8.0);
  
  //from the center, make 6 coords
  float[][] coords = position(center[0], center[1], 8.0);

  //make 6 particles
  for (int k = 0; k < 6; k++) {
    //if coords do not yet exist, make the circle, else, don't
    if (!isItemInArray(all_coords, coords[k])) {
      //create the mover
      // add the mover to the movers list
      addMover(coords[k][0], coords[k][1], 0, 0);
      
      //add coords to the list
      all_coords = (float[][])append(all_coords, coords[k]);
    }
  }

  //now change the center and make new circles
  for (int i = 0; i < 6; i++) {
    //redefine the center 
    center[0] = orig_coords[i][0];
    center[1] = orig_coords[i][1];

    //from the center, make 6 coords
    float[][] new_coords = position(center[0], center[1], 8.0);

    //make 6 particles
    for (int k = 0; k < 6; k++) {
      //if coords do not yet exist, make the circle, else, don't
      if (!isItemInArray(all_coords, new_coords[k])) {
        //create the mover
        // add the mover to the movers list
        addMover(new_coords[k][0], new_coords[k][1], 0, 0);

        //add coords to the list
        all_coords = (float[][])append(all_coords, new_coords[k]);
      }
    }
  }
}

AlphaMover[] make_alpha() {
  // each mouse click, eject an alpha particle
  AlphaMover[] alphas = {};
  float[] center = {100.0,100.0};
  
  //will use 0, 1, 2
  float[][] coords = position(center[0],center[1],8.0);
  float[][] get_center = position(coords[0][0],coords[0][1],8.0);
  //and this coord
  float[][] center_coord = {{get_center[3][0],get_center[3][1]}};
  
  float[][] alpha_coords = {};
  for (int k = 0; k < 3; k++) {
    alpha_coords = (float[][])append(alpha_coords,coords[k]);
  }
  alpha_coords = (float[][])append(alpha_coords,center_coord[0]);
  
  //alpha coords is now the list of coordinates for the alpha particle
  for (int k = 0; k < 4; k++) {
    alphas = (AlphaMover[])append(alphas,new AlphaMover(alpha_coords[k][0],alpha_coords[k][1],2,0));
  }
  return alphas;
}

// create text for alpha
float ax_loc = 50;
float ay_loc = 135;
float ax_vel = 0.5;
float ay_vel = 0;
String a_message = "Alpha Particle";
int a_size = 18;
float[] a_col = {9,49,245};
TextBox alpha_text = new TextBox(ax_loc,ay_loc, ax_vel, ay_vel);

// create the alpha particle
AlphaMover[] alphas = make_alpha();

int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  textSize(32);
  fill(0);
  text("Alpha Decay", 260, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < alphas.length; i++) {
      alphas[i].update();
      alphas[i].display(i);
      //draw alpha text
      alpha_text.update();
      alpha_text.display(a_message, a_size, a_col);
    }
    for (int i = 0; i < (movers.length - 4); i++) {
      movers[i].update();
      //movers[i].checkEdges();
      movers[i].display(i);
    }
    fill(9, 49, 245);
    text("Protons - 7", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 8", 20, 190);
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i);
      }
    fill(9, 49, 245);
    text("Protons - 9", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 10", 20, 190);
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas2");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas2"> </canvas>    
"""

html_code = html_template.format(utils_code+alpha_code)
HTML(html_code)

<center> Figure 5: Alpha particles move at a relatively slow speed compared to other forms of radiation. Notice now the number of protons and neutrons in the nucleus both decrease by two.</center>

### Physical Properties

The energy the alpha particle carries depends on the atom from which it came, with larger nuclei producing higher energy radiation. Due to the relatively large size of the alpha particle, and its positive charge, it usually does not travel very far before it interacts with some other form of matter. Therefore, we say that alpha radiation has a **low penetration**. In fact, alpha radiation can be blocked by only a few sheets of paper.
If it is carrying a sufficient amount of energy, an alpha particle can ionize another atom upon contact. This is the inherent danger of radiation. 

### Biological Effects

Due to its low penetration, alpha radiation has very little effect on biological matter when it originates from an external source. Most alpha particles will be stopped by thin clothing, or even dead skin cells. However, alpha radiation can become dangerous when it is contained within the body. The most common example of this is radon decay. 
The radioactive decay of heavy elements is a natural process that is constantly occuring in the Earth's crust. In the decay of uranium, a chain of elements are produced that eventually result in the formation of lead.

<img src="http://nuclearsafety.gc.ca/images/fact-sheet-images/20120727-fs-fi-uranium-238-f1-eng.gif" alt="Drawing" style="width: 750px;"/>
<center>Image from http://nuclearsafety.gc.ca/eng/resources/fact-sheets/polonium-210.cfm</center>
<center> Figure 6: This is the radioactive decay chain of Uranium-238, the most common isotope of uranium found in nature. As the element decays towards lead, different forms of radiation are produced. The rate at which this radiation is produced is determined by the half-life of each element. </center>

During this process, a colourless, odourless gas called radon-222 is produced. Radon-222 has a relatively short half-life, meaning it is constantly decaying into polonium-218, and releasing alpha particles. When radon-222 is inhaled in high doses, the interaction between alpha particles and atoms of your body can lead to increased risk of lung cancer.


## Beta ($\beta$) Radiation

**Beta radiation**, or **beta decay**, is another type of radioactive decay that results in the emission of a **beta particle** from the nucleus of an atom. A beta particle can be one of two things: an electron or a positron (a positively charged electron). 
Like alpha decay, beta decay is also the result of an unstable nucleus breaking down. However, unlike alpha decay, beta decay is a product of the **weak nuclear force**. 

The weak nuclear force acts on a subatomic level, between the quarks that compose protons and neutrons. We will not be discussing the weak nuclear force in detail here, but check out this link for more information: https://en.wikipedia.org/wiki/Weak_interaction#Interaction_types.

### Creation
There are two types of beta decay, known as $\beta^-$ (beta minus) and $\beta^+$ (beta plus) decay.

### $\beta^-$ Decay

$\beta^-$ decay typically occurs in a nucleus with a disproportionately high number of neutrons. In order to increase the stability of the nucleus, a neutron will change into a proton via the weak nuclear force, releasing an electron and an antineutrino in the process.

Click on the nucleus below to run the animation.

beta_minus_code = """
//for beta- decay, releases electron and anti neutrino
//large number of neutrinos, neurtino changes into a proton

class BetaMinusMover extends Mover {
  BetaMinusMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int i, int rad, int col) {
    stroke(0);

    //red
    if (col == 0) {
      fill(255, 0, 0);
    }
    //green
    else if (col == 1) {
      fill(35, 167, 6);
    }
    //blue
    else if (i % 3 ==0) {
      fill(12, 48, 224);
    } //grey
    else {
      fill(175);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

BetaMinusMover[] movers = {};

void addMover(float x_loc, float y_loc, float x_vel, float y_vel) {
  movers = (BetaMinusMover[])append(movers, new BetaMinusMover(x_loc, y_loc, x_vel, y_vel));
}

void setup() {
  size(700, 200);
  float[] center = {100.0, 100.0};
  float[][] all_coords = {};
  float[][] orig_coords = position(center[0], center[1], 8.0);
  
  //from the center, make 6 coords
  float[][] coords = position(center[0], center[1], 8.0);

  //make 6 particles
  for (int k = 0; k < 6; k++) {
    //if coords do not yet exist, make the circle, else, don't
    if (!isItemInArray(all_coords, coords[k])) {
      //create the mover
      // add the mover to the movers list
      addMover(coords[k][0], coords[k][1], 0, 0);
      
      //add coords to the list
      all_coords = (float[][])append(all_coords, coords[k]);
    }
  }

  //now change the center and make new circles
  for (int i = 0; i < 6; i++) {
    //redefine the center 
    center[0] = orig_coords[i][0];
    center[1] = orig_coords[i][1];

    //from the center, make 6 coords
    float[][] new_coords = position(center[0], center[1], 8.0);

    //make 6 particles
    for (int k = 0; k < 6; k++) {
      //if coords do not yet exist, make the circle, else, don't
      if (!isItemInArray(all_coords, new_coords[k])) {
        //create the mover
        // add the mover to the movers list
        addMover(new_coords[k][0], new_coords[k][1], 0, 0);

        //add coords to the list
        all_coords = (float[][])append(all_coords, new_coords[k]);
      }
    }
  }
}

BetaMinusMover[] make_betas() {
  // each mouse click, eject an alpha particle
  BetaMinusMover[] betas = {};
  //electron
  betas = (BetaMinusMover[])append(betas, new BetaMinusMover(100.0,100.0,4.0,-0.4));
  //antineutrino
  betas = (BetaMinusMover[])append(betas, new BetaMinusMover(100.0,100.0,4.0,0.4));
  return betas;
}

// create the alpha particle
BetaMinusMover[] betas = make_betas();
int x = 0;

// create text for electron
float ex_loc = 50;
float ey_loc = 120;
float ex_vel = 4;
float ey_vel = -0.4;
String e_message = "Electron";
int e_size = 18;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

// create text for antineutrino
float ax_loc = 50;
float ay_loc = 120;
float ax_vel = 4;
float ay_vel = 0.4;
String a_message = "Antineutrino";
int a_size = 18;
float[] a_col = {35, 167, 6};
TextBox anti_text = new TextBox(ax_loc,ay_loc, ax_vel, ay_vel);

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  textSize(32);
  fill(0);
  text("Beta Minus Decay", 220, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < betas.length; i++) {
      betas[i].update();
      betas[i].display(i,8,i);
    }
    //draw electron text
    elec_text.update();
    elec_text.display(e_message, e_size, e_col);
    //draw anti neutrino text
    anti_text.update();
    anti_text.display(a_message,a_size,a_col);
    
    for (int i = 0; i < (movers.length) - 2; i++) {
      movers[i].update();
      movers[i].display(i,16,2);
    }
    //add a proton
    movers[17].display(3,16,2);
    movers[18].display(3,16,2);
    fill(9, 49, 245);
    text("Protons - 8", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 11", 20, 190);
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i,16,2);
      }
    fill(9, 49, 245);
    text("Protons - 7", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 12", 20, 190);
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas3");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas3"> </canvas>    
"""

html_code = html_template.format(utils_code+beta_minus_code)
HTML(html_code)

<center> Figure 7: $\beta^-$ decay involves a neutron changing into a proton. Notice how the electron and antineutrino travel faster than the alpha particle in the previous animation.</center>

### $\beta^+$ Decay

$\beta^+$ decay will occur in a nucleus with a high number of protons. In contrast to $\beta^-$ decay, a proton will change into a neutron, releasing a positron and a neutrino.

Click on the nucleus below to run the animation.

beta_plus_code = """
//for beta+ decay, releases positrion and neutrino
//large number of protons, proton changes into a neutrino

class BetaPlusMover extends Mover {
  BetaPlusMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int i, int rad, int col) {
    stroke(0);

    //purple positron
    if (col == 0) {
      fill(154, 5, 198);
    }
    //orange neutrino
    else if (col == 1) {
      fill(255, 111, 6);
    }
    //grey neutrons
    else if (i % 3 == 0) {
      fill(175);
    }
    //blue protons
    else {
      fill(12, 48, 224);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

BetaPlusMover[] movers = {};

void addMover(float x_loc, float y_loc, float x_vel, float y_vel) {
  movers = (BetasPlusMover[])append(movers, new BetaPlusMover(x_loc, y_loc, x_vel, y_vel));
}

void setup() {
  size(700, 200);
  float[] center = {100.0, 100.0};
  float[][] all_coords = {};
  float[][] orig_coords = position(center[0], center[1], 8.0);
  
  //from the center, make 6 coords
  float[][] coords = position(center[0], center[1], 8.0);

  //make 6 particles
  for (int k = 0; k < 6; k++) {
    //if coords do not yet exist, make the circle, else, don't
    if (!isItemInArray(all_coords, coords[k])) {
      //create the mover
      // add the mover to the movers list
      addMover(coords[k][0], coords[k][1], 0, 0);
      
      //add coords to the list
      all_coords = (float[][])append(all_coords, coords[k]);
    }
  }

  //now change the center and make new circles
  for (int i = 0; i < 6; i++) {
    //redefine the center 
    center[0] = orig_coords[i][0];
    center[1] = orig_coords[i][1];

    //from the center, make 6 coords
    float[][] new_coords = position(center[0], center[1], 8.0);

    //make 6 particles
    for (int k = 0; k < 6; k++) {
      //if coords do not yet exist, make the circle, else, don't
      if (!isItemInArray(all_coords, new_coords[k])) {
        //create the mover
        // add the mover to the movers list
        addMover(new_coords[k][0], new_coords[k][1], 0, 0);

        //add coords to the list
        all_coords = (float[][])append(all_coords, new_coords[k]);
      }
    }
  }
}

BetaPlusMover[] make_betas() {
  // each mouse click, eject an alpha particle
  BetaPlusMover[] betas = {};
  
  betas = (BetaPlusMover[])append(betas,new BetaPlusMover(100.0,100.0,4.0,-0.4));
  betas = (BetaPlusMover[])append(betas,new BetaPlusMover(100.0,100.0,4.0,0.4));
  return betas;
}

// create the alpha particle
BetaPlusMover[] betas = make_betas();
int x = 0;

// create text for positron
float px_loc = 50;
float py_loc = 120;
float px_vel = 4;
float py_vel = -0.4;
String p_message = "Positron";
int p_size = 18;
float[] p_col = {154, 5, 198};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);

// create text for neutrino
float nx_loc = 50;
float ny_loc = 120;
float nx_vel = 4;
float ny_vel = 0.4;
String n_message = "Neutrino";
int n_size = 18;
float[] n_col = {255, 111, 6};
TextBox neut_text = new TextBox(nx_loc,ny_loc, nx_vel, ny_vel);

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  //title
  textSize(32);
  fill(0);
  text("Beta Plus Decay", 235, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < betas.length; i++) {
      betas[i].update();
      betas[i].display(i,8,i);
    }
    
    //draw positron text
    posi_text.update();
    posi_text.display(p_message, p_size, p_col);
    //draw neutrino text
    neut_text.update();
    neut_text.display(n_message,n_size,n_col);
    
    for (int i = 0; i < (movers.length) - 2; i++) {
      movers[i].update();
      movers[i].display(i,16,2);
    }
    //add a neutron
    movers[17].display(3,16,2);
    movers[18].display(3,16,2);
    fill(9, 49, 245);
    text("Protons - 11", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 8", 20, 190);
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i,16,2);
      }
    fill(9, 49, 245);
    text("Protons - 12", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 7", 20, 190);
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas4");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas4"> </canvas>    
"""

html_code = html_template.format(utils_code+beta_plus_code)
HTML(html_code)

Figure 8: $\beta^+$ decay involves a proton changing into a neutron. The ejected particles travel at the same speed as those in $\beta^-$ decay.

### Physical Properties

A beta particle is significantly less massive than an alpha particle, and only carries 1 unit of charge. To compare, the mass of a beta particle is approximately 1/8000 the mass of an alpha particle. Their low mass enables them to travel at ultrarelativistic speeds (speeds nearing the speed of light). With a small size and low charge, they are able to travel longer distances before interacting with matter, lending them a higher penetrating power than alpha particles. Beta particles are able to travel into soft tissue from external sources, although they will be blocked by material such as plastic or aluminum.

### Biological Effects

Like alpha particles, beta radiation has the potential to ionize the atoms they contact. Due to its penetrative power, beta radiation can cause external burns, tissue damage, and acute radiation poisoning. Some of the most common beta emitters are carbon-14, and yttrium-90. 

You may be familiar with the process known as radiocarbon dating: the method through which we can determine the age of organic matter. Radiocarbon dating measures the amount of carbon-14 in a dead organic sample, and compares this amount to the expected amount present while the sample was still alive. Carbon-14 is constantly decaying and emitting beta particles at a rate governed by it's half-life of 5,730 years, so the difference between the original amount present in a living sample and the measured amount tells us exactly how long it has been since the sample died.

<img src="http://1.bp.blogspot.com/-q1KfOPVR0r8/VgHUXZrQ4bI/AAAAAAAACCc/O8N0eel3MsY/s1600/c14_3.jpg" alt="Drawing" style="width: 500px;"/>
<center>Image from http://geologylearn.blogspot.com/2015/09/carbon-dating.html</center>
<center> Figure 9: Radiocarbon dating is the method that allows us to determine the age of fossils. </center>

Yttrium-90 is another example of a useful beta emitter. Yttrium-90 is used to treat cancer patients via radiation therapy. This procedure involves bombarding acute areas of cancerous tumors with beta radiation, in hopes that the destructive nature of the radiation will eradicate the tumor. The side effects of this therapy are congruent with the symptoms of radiation poisoning, but it is often effective in improving the patients quality of life. 

## Gamma ($\gamma$) Radiation

**Gamma radiation** differs from both alpha and beta radiation in that it does not take the form of a particle, but is rather a type of high energy EMR. There are a few different processes that can produce gamma rays, but each requires an event that releases a large amount of energy.

### Creation

#### Particle Collisions

When two particles carrying sufficient energy collide, they may create a gamma ray. The conditions creating such a collision are quite rare in the universe, and can only be created on Earth within particle accelerators or nuclear reactors.
Out in the universe, there are objects that are capable of producing gamma rays due to the extreme nature of their conditions. Black holes, neutron stars, supernova and quasars are a few examples of objects that regularly emit gamma radiation. The unique conditions required to produce gamma radiation enable us to gather information on these objects by analyzing the radiation they send to us.

#### Annihilation Reactions

When a particle collides with its antiparticle, an **annihilation** reaction can occur. For example, if an electron collides with a positron, they transform into pure energy in the form  gamma rays.

Click on the animation below to create an annihilation reaction.

annihilation_code = """
//annihilation reaction

//for beta- decay, releases electron and anti neutrino
//large number of neutrinos, neurtino changes into a proton

class AnnihilationMover extends Mover {
  AnnihilationMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int rad, int col) {
    stroke(0);

    //purple positron
    if (col == 0) {
      fill(154, 5, 198);
    }
    //red electron
    else if (col == 1) {
      fill(255, 0, 0);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

boolean check_collision(AnnihilationMover one, AnnihilationMover two) {
  //take the coordinates of each particle and check if they are the same
  
  if(one.location.x == two.location.x && one.location.y == two.location.y) {
    return true;
  } else {
    return false;
  }
}

//create two movers, a positron and an electron
//have them move to the same position
//from that position, eject two gamma rays

void setup() {
  size(700,200);
}

//make two movers
// create positron and electron
AnnihilationMover positron = new AnnihilationMover(50,50,2.0,0.25);
AnnihilationMover electron = new AnnihilationMover(50,150,2.0,-0.25);

//create gamma rays
Gamma g_up = new Gamma(435,100,2.0,-0.75);
Gamma g_down = new Gamma(435,100,2.0,0.75);

// create text for electron
float ex_loc = 25;
float ey_loc = 170;
float ex_vel = 2;
float ey_vel = -0.25;
String e_message = "Electron";
int e_size = 12;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

// create text for positron
float px_loc = 25;
float py_loc = 40;
float px_vel = 2;
float py_vel = 0.25;
String p_message = "Positron";
int p_size = 12;
float[] p_col = {154, 5, 198};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);

int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  textSize(20);
  fill(0);
  text("Annihilation Reaction", 250, 25);
  
  textSize(24);
  
  if (x == 0) {
    electron.display(8,1);
    positron.display(8,0);
    elec_text.display(e_message,e_size,e_col);
    posi_text.display(p_message,p_size,p_col);
  } else {
    if (check_collision(electron, positron) == true) {
      //draw two gamma rays
      //up
      g_up.update();
      g_up.display(1,330);
    
      ////down
      g_down.update();
      g_down.display(0,20);
    } else {
      posi_text.update();
      posi_text.display(p_message,p_size,p_col);
      positron.update();
      positron.display(8,0);
    
      elec_text.update();
      elec_text.display(e_message,e_size,e_col);
      electron.update();
      electron.display(8,1);
    }
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas5");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas5"> </canvas>    
"""

html_code = html_template.format(utils_code+annihilation_code)
HTML(html_code)

<center> Figure 10: An annihilation reaction. Upon collision, the particles are destroyed and create gamma rays in the process.</center>

Antimatter is not typically found on Earth under natural circumstances. It is often the byproduct of different nuclear reactions or particle collisions, and will not survive very long before undergoing an annihilation reaction.


#### Particle Acceleration

When a fast moving charged particle decelerates rapidly, this change in energy can be released in the form of a gamma ray. This phenomenon is also known as **bremsstrahlung** radiation. Bremsstrahlung will occur when a charged particle passes through an external electric or magnetic field at high velocity. The pull of the external field causes the particle to decelerate rapidly, and the kinetic energy that is lost is converted into radiation. When this energy difference is large enough, gamma rays may be emitted.

Click on the animation below to demonstrate bremsstrahlung radiation.

bremsstra_code = """
//this animation shows how the decceleration of a particle can produce gamma rays

// need a large stationary charge -- proton
//need an electron moving in a straight line, then need it to bend into an arc
//at the moment it bends, emit gamma rays
//electron goes off screen

import java.lang.*;

class BremsstraMover extends Mover {
  PVector acceleration;

  BremsstraMover(float x_loc,float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
    acceleration = new PVector();
  }

  void update() {
    location.add(velocity);
    velocity.add(acceleration);
  }
  
  void applyForce(PVector force) {
    acceleration = force;
  }
 
  PVector attract(BremsstraMover m, float G, float m1, float m2) {
    PVector force = PVector.sub(location, m.location);
    float distance = force.mag();

    distance = constrain(distance, 5.0, 25.0);
 
    force.normalize();
    float strength = (G * m1 * m2) / (distance * distance);
    force.mult(strength);
    return force;
  }
  
  void display(int rad, int col) {
    stroke(0);

    //blue proton
    if (col == 0) {
      fill(12, 48, 224);
    }
    //red electron
    else if(col == 1) {
      fill(255, 0, 0);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

// main function

//create stationary proton
BremsstraMover proton = new BremsstraMover(350,100,0,0);

// create text for positron
float px_loc = 305;
float py_loc = 120;
float px_vel = 0;
float py_vel = 00;
String p_message = "Positive Charge";
int p_size = 12;
float[] p_col = {12,48,224};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);

//create moving electron 
BremsstraMover electron = new BremsstraMover(8,30,9,2);

// create text for electron
float ex_loc = 8;
float ey_loc = 50;
float ex_vel = 9;
float ey_vel = 2;
String e_message = "Electron";
int e_size = 12;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

//create gamma rays
Gamma g_up = new Gamma(350,100,4.0,-1.0);
Gamma g_down = new Gamma(350,100,4.0,1.0);

int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void setup() {
  size(700,200);
  frameRate(35);
}

void draw() {
  background(255);
  textSize(20);
  fill(0);
  text("Bremsstrahlung Radiation", 230, 25);
  
  if (x == 0) {
    proton.display(16,0);
    electron.display(8,1);
    posi_text.update();
    posi_text.display(p_message,p_size,p_col);
    elec_text.display(e_message,e_size,e_col);
  } else{
    posi_text.update();
    posi_text.display(p_message,p_size,p_col);
    proton.display(16,0);
    PVector grav = proton.attract(electron, -9, 5.0, 2);
    electron.applyForce(grav);
    electron.update();
    electron.display(8,1);
  
    //emit gamma rays when it deccelerates
    if (electron.location.x > 288) {
      //draw two gamma rays
      //up
      g_up.update();
      g_up.display(1,330);
      ////down
      g_down.update();
      g_down.display(0,20);
    }
  }
}
"""

html_template = """
<script type="text/javascript" src="processing.js"></script> 
<script type="text/javascript">
  var processingCode = `{}`;
  var myCanvas = document.getElementById("canvas6");
  var jsCode = Processing.compile(processingCode);
  var processingInstance = new Processing(myCanvas, jsCode);
 </script>
<canvas id="canvas6"> </canvas>    
"""

html_code = html_template.format(utils_code+bremsstra_code)
HTML(html_code)

<center> Figure 11: As the electron comes closer to the positive charge, the electromagnetic force repels its motion. This sudden change in kinetic energy results in the emission of gamma rays.</center>

### Physical Properties

Gamma rays carry the most energy out of all types of EMR. Any photon carrying approximately 100 keV of energy or more is considered to be a gamma ray. As gamma rays carry no mass or charge, they have a penetrating power significantly higher than alpha or beta particles. Take a look at the image below to see a comparison between the three.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Alfa_beta_gamma_radiation_penetration.svg/800px-Alfa_beta_gamma_radiation_penetration.svg.png" alt="radiation penetration">
<center>Image from https://en.wikipedia.org/wiki/File:Alfa_beta_gamma_radiation_penetration.svg</center>
<center> Figure 12: Gamma rays have a very high penetrative power, although the likelihood of it being blocked increases with both the thickness and density of the material. </center>


### Biological Effects

The penetrative strength of gamma rays make them very dangerous to the human body. However, due to the rarity of their occurence, gamma rays should not be a major concern during your everyday life. Most gamma rays are blocked by the many layers of our atmosphere, and any gamma rays formed on Earth are usually held within the containers in which they were formed (nuclear reactors, particle accelerators etc.). 

## Exercises

Test your knowledge of radiation with the following questions.

def q_1(val):
    if val == "Radiation has the potential to ionize atoms.":
        display(Latex("Correct!"))
        display(Latex("Ionized atoms within biological cells can cause damage to the cell itself."))
    elif val == ' ':
        None
    else:
        display(Latex("Try Again!"))

display("What is it that makes radiation dangerous?")

a1 = 'Radiation is not biodegradable.'
a2 = "Radiation has the potential to ionize atoms."
a3 = "Radiation removes oxygen from the atmosphere."
interact(q_1, val = widgets.Dropdown(options=[' ',a1 ,a2, a3 ],value = ' ',description = 'Choose One:',disabled = False));


def q_2(val):
    if val == a3:
        display(Latex("Good stuff!"))
        display(Latex("Gamma radiation has no mass or charge, and can therefore go a long way before interacting with matter."))
    elif val == ' ':
        None
    else:
        display(Latex("Try Again!"))

display("Which type of radiation has the highest penetrative power?")

a1 = 'Alpha radiation'
a2 = "Beta radiation"
a3 = "Gamma radiation"
interact(q_2, val = widgets.Dropdown(options=[' ',a1 ,a2, a3 ],value = ' ',description = 'Choose One:',disabled = False));


def q_3(val):
    if val == a1:
        display(Latex("Right on!"))
        display(Latex("In beta minus decay, a neutron changes into a proton, ejecting an electron and an antineutrino."))
    elif val == ' ':
        None
    else:
        display(Latex("Try Again!"))

display("Which type of beta decay involves the conversion of a neutron into a proton?")

a1 = 'Beta minus'
a2 = "Beta plus"

interact(q_3, val = widgets.Dropdown(options=[' ',a1 ,a2],value = ' ',description = 'Choose One:',disabled = False));


def q_4(val):
    if val == a3:
        display(Latex("Excellent!"))
        display(Latex("A helium-4 nucleus is the exact same: two protons and two neutrons."))
    elif val == ' ':
        None
    else:
        display(Latex("Try Again!"))

display("An alpha particle is identical to what type of nucleus?")

a1 = 'Lithium'
a2 = "Carbon-14"
a3 = "Helium-4"
a4 = "Hydrogen"
interact(q_4, val = widgets.Dropdown(options=[' ',a1 ,a2, a3, a4],value = ' ',description = 'Choose One:',disabled = False));


## Conclusion

Upon their discovery, Ernest Rutherford named these three types of radiation according to the first three letters of the greek alphabet. He chose the names based on their respective penetrative power, with alpha being the weakest, then beta, followed by gamma.

Different forms of radiation can be both a useful tool, and a potential hazard. In any case, analyzing the properties of radiation allows us to determine the circumstances of its creation, and we use this information to learn about the objects that form it. There are fields of astronomy that are tailored to the analysis of specific forms of radiation, such as gamma, infrared, and radio, that unveil entirely new perspectives on various objects in the universe.


<img src="http://cdn.eso.org/images/screen/eso1205d.jpg" alt="Drawing" style="width: 750px;"/>
<center>Image from https://www.eso.org/public/images/eso1205d</center>
<center> Figure 13: Above are two images of the Helix Nebula. The one on the left is an image captured using infrared light, while the one on the right is captured in visible light. </center>

On the other hand, radiation can be used to cause widespread devastation. There are many areas in the world that are still unsafe due to the residual radiation caused by nuclear weapons, or nuclear waste. Therefore, it is important that the world becomes aware of the dangers associated with radiation.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)