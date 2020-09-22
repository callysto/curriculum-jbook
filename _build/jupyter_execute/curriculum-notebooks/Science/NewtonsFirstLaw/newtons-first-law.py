![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/NewtonsFirstLaw/NewtonsFirstLaw.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Newton's First Law

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


## Curling 

As a demonstration of Newton's laws. Watch how the rocks move in straight lines, then bounce when they hit.

%%html
<iframe width="560" height="315" src="https://www.youtube.com/embed/Kwz-cicOUFk?start=9" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### The curling video demonstrates Newton's three laws:

1. A body at **rest** stays at **rest**. A body in **motion** stays in **motion**, with uniform speed in a straight line. A change happens only if a **force** acts on the body.

2. The **force** on the body equals the rate of change of its **momentum** (mass times velocity). 

3. For every **action**, there is an equal and opposite **reaction**. 
    
The curling video demonstrates Newton's three laws as a particular example. In these curling videos, we see:

1. A rock that is not moving on the ice, stays still until something hits it. A rock sliding on the ice continues to slide until it hits something. You can sense the force at work if you imagine your hand stuck between two rocks as they hit. Ouch, that would hurt -- it is a strong force.

2. When a fast rock hits another rock, you can imagine the force is bigger. Your hand stuck between would get hurt even more! We see the faster rock causes a bigger change in the motion as it hits. So a bigger force gives a bigger change in momentum.

3. When two rocks hit each other, one moves one way, the other moves in a different direction. While we haven't put numbers onto the motion, we can see that one change in motion is opposite to the other. This is the equal and opposite reaction. 

And what's with the sweeping and the brooms? The sweepers are melting the ice, creating the thin layer of water on the surface to reduce the friction on the curling rock, allowing it to travel fast and straight. 

## Newton's first law

Newton's first law would be a surprise to the ancient Greeks, and even to some of us today, because it goes against our experience. The ancients believed that for most objects, the natural state was rest. For instance, you slide a chair along the floor and then is comes to a stop. You drop a rock from your hand, and it falls to the ground and stops. You paddle a boat to get it moving, and when you stop paddling, the boat stops. Everything likes to stop. If you want something to move, you have to push it, and keep pushing if you want it to keep moving. 

Planets, and the moon, were considered special because they keep moving without anything obvious pushing them. At least to the ancients, they were considered special. 

Newton said **No**. Things that are moving, will keep moving, until something makes them stop. When you push a chair across the floor, the reason it stops is because of the force of friction from the floor acting on the chair's leg. A boat stops in the water because of the drag force of the water on the boat. Even a curling rock will eventually come to rest, because there is still a tiny bit of friction between the rock and the very slippery icy surface of the curling rink. Everything that comes to a stop does so because of some force acting on it. 

Planets, and the moon, don't stop moving because there is nothing in space acting as friction to slow down their motion. 

Newton also noted that moving objects will move in a straight line, with constant velocity, unless there is a force acting on it. So the curling rock moves straight until it hits something, resulting in a force that pushes it off course from a straight line. A rock that you throw would travel straight, until you notice that gravity is pulling it into a curved path as it falls to the ground. 

Even the planet, and moon, travel in curved paths (ellipses) because the force of gravity is causing them to move away from the straight line path they would take if there was no force on them.

It was Newton who realized that the force that causes a rock to fall to the ground is the same force that keeps the moon going around the Earth.

This property of a body to stay in uniform motion (or rest) is called inertia.

## Simulation of Newton's first law

We can create a simulation of Newton's first law by doing a numerical simulation of curling.

Below, we have four circles (curling stones) in a line. They will not move, until some force acts on them. (The first law).

We see a fifth stone comes in from the left, hits the first stone in the line and causes it to move. Then one stone hits the other, and the other, and the other, until the last one shoots out the end.

The simulations will repeat every few seconds. 

%%html
<iframe src="C1.html" width=500 height=500></iframe>

## A better simulation

Of course, this is a "perfect" simulation, where all five stones are in a perfectly straight line. A more realistic situation will have the stones slightly misaligned. In the simulation below, the first stone in the line is slightly out of place. A much more interesting collision is the result.

Notice, however, once a stone is hit, it moves in a straight line, at a constant speed. This is also in the statement of Newton's first law. If there is no force acting on the object, it will move at uniform speed in a constant direction.



%%html
<iframe src="C2.html" width=500 height=500></iframe>

## Consequence of the First Law

An immediate consequence of the first law is that if an object is **NOT** moving at a uniform speed, or not in a straight line, there must be some force acting on it. It is interesting to look at many examples, and figure out what is the force on the object. Here are a few examples.



**Human cannonball:**

- the cannon forces her into the air at high speed
- the arc of her motion shows there must be a force (gravity) making her path deviate from a straight line. 

![cannonball](images/cannonball.gif)

**Soccer ball:**

- the ball is falling towards the player, in a curve due to gravity
- the force of his kick gets the ball moving towards the goal
- the curve as the ball heads to the goal is from the air pushing unevening as the ball spins rapidly

![soccer ball](images/wiffle.gif)

**Planets:**

The planets don't move in straight lines, so there must be some force causing them to deviate from the straight, uniform path. Newton's discovery of uniform gravitation was an application of his first law -- that something making the planets' path curve is gravity. The same force that causes soccer balls and cannon balls to fall. 

![planets](images/planets.gif)

## Many forces simulation

In typical situations, there are many forces in action. In the following simulation of the famous *Newton's Cradle,* there are at least four forces at work:

- gravity, which makes the pendulums swing back and force
- collision force, when the balls hit each other
- elastic force, where the wire connecting the balls to the anchor are actually springs
- friction forces, which causes the pendulums to slowly die down and stop.

Note you can use the mouse to "grab" a pendulum and position it where you want. See if you can cause motions that highlight each of these forces.



%%html
<iframe src="C3.html" width=500 height=500></iframe>

## Summary of Newton's first law

The first law is a qualitative law -- there are no numbers here, no formula.

It simply states that an object at rest stays at rest; a moving object moves in a straight line at uniform speed. **Unless there is a force acting on the object.**

So if there are no forces, the motion is very simple. If the motion is not simple, there must be some force acting. So the interesting question is, what is the force causing a complicated motion.

### Looking forward

Newton's second and third las are *quantitative.* They tell us how the size and direction of a force affect the motion of the object, in a very precise manner. More on this in a later notebook.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)