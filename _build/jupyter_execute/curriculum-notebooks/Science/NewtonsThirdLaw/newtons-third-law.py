![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/NewtonsThirdLaw/newtons-third-law.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Newton's Third Law


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


## The Third Law

Let's remind ourselves of the Three Laws of motion from Newton:

1. A body at **rest** stays at **rest**. A body in **motion** stays in **motion**, with uniform speed in a straight line. A change happens only if a **force** acts on the body.

2. The **force** on the body equals the rate of change of its **momentum** (mass times velocity). 

3. For every **action**, there is an equal and opposite **reaction**.

In this notebook, we examine the Third Law:

#3. For every **action**, there is an equal and opposite **reaction**.

### Example 1

A familiar example of the Third Law we see often on TV or the Internet - a rocket blasting off to space.

The rocket demonstrates Newton's Third Law. In a NASA rocket, as in the video below, some chemicals inside the the rocket body are burned, creating hot gases that shoot out the bottom of the rocket. That motion of hot gases is the **action**. The rocket responds by moving in the opposite direction. That rocket motion is the **reaction**.

<img src="https://media.giphy.com/media/6yWV529bDk3WU/giphy.gif" width="480" height="350" />

(Image via Giphy.com)



### Example 2

A similar example is with a water bottle rocket, as in the video below. 

The child pumps air into the water bottle creating pressure inside the container. When the lid on the bottom open, the air pressure forces the water  out the bottom of the rocket. That motion of water is the **action.** The resulting **reaction** is the water bottle shooting up into the air.  

<img src="https://media.giphy.com/media/qGQ7uiYh4II2k/giphy.gif" width="480" height="270" />

(Image via Giphy.com)


### Example 3

### Equal and opposite

Equal reaction might not be obvious. In the video below, two people collide while holding big, bouncy balls. At the collision, one of them flies backwards (and lands comfortably on cushions). The other only slows down a bit.  The reaction seems opposite (goes in the reverse direction), but not really equal.

<img src="https://media.giphy.com/media/ri4ux6gkNifIs/giphy.gif" width="480" height="280" />

(Image via Giphy.com)


### Some details

So, what's happening here?

A more precise statement of Newton's Third Law is the following:

> #3. When two objects interact, there are two forces acting, one on each object, that are equal strength and opposite in direction. 

In the video above with the two people colliding, each has a **force** on them (the force through the balls). These are equal and opposite **forces** acting on them. The person on the left is big, heavy, and moving quickly with his feet planting firmly on the ground. He will firmly absorb any force, and only slow down a bit. 

The person on the right is small, light-weight, not moving initially, and lifts her feet off the floor. When the equal-sized force hits her, she flies back quickly because her momentum, and her velocity must make a big change in reaction to the force of the collision.

By the Second Law, a force causes a change in momentum (velocity times mass), so it is the change in **momentum** that must be equal. Here, the smaller person on the right, with lower mass, has to see a bigger change in velocity in the collision to have an equivalent change of momentum. So this person bounces back much faster.

 

### Example 4

### A train derailment 

Tragic accidents can happen when we forget Newton's Third Law. Here is an example of a train derailment, captured in the video below. The train is following Newton's laws of motion, but something went terribly wrong. 

<img src="https://media.giphy.com/media/oQLfkLMkDdfnG/giphy.gif" width="480" height="354" />

(Image via Giphy.com)

So, what went wrong here?

First, notice the train is turning in a curve - by Newton's First Law, there must be a force on the train causing it to deviate from a straight line. It's not hard to imagine that this force is the action of the rails on the ground pushing against the wheels of the train.

By the Third Law, the wheels/train push back on the rails. This is the equal, opposite force. Because it is a fast, heavy train, this results in a very strong force pushing on the rails.

Normally, the rails do not move (much) because they are cemented into the ground. In this derailment video, though, the force is so strong that the rails break! Once they are broken, there is nothing to push against the train. With no force, Newton's First Law says the train will have to move in a straight line. So it does, which means it leaves the curved track and crashes into the wall.

### A simulation

Following is a bouncing ball simulation, based on code by Ziggy Jonsson [Click here for the original](http://bl.ocks.org/ZJONSSON/1706849). Details are in this [paper](http://www.vobarian.com/collisions/2dcollisions2.pdf).

What we see in the animation is a collection of balls that bounce off each other in elastic collisions. Each ball has a different mass, proportional to the area of the ball. 

So when a small ball hits a big ball, there is a force acting on each ball, in equal and opposite directions. The difference in masses means the velocity of the small ball changes a lot, while the big ball only changes a little.



%%html
<iframe src="C3.html" width=500 height=500></iframe>

## Second and Third Law together


When two balls hit, the Third Law tells us that the force each feels is equal and opposite. The Second Law tells us the rate of change in **momentum** for each ball is equal to this force. 

This means the total change in **momentum** for the two balls is equal and opposite. That is to say that the total change in total momentum between two objects is

$$\Delta \vec{p}_1 = - \Delta \vec{p}_2, $$

where delta $\Delta$ means the ''change in'' the momentum $\vec{p}$. 
So $\Delta \vec{p} = \vec{p}(\mbox{after}) - \vec{p}(\mbox{before}).$

The letter $\vec{p}$ stands for momentum (*petere* in Latin), and is just the product of mass times velocity. 

Rewriting momentum as mass times velocity,  for the two balls (1 and 2) we have
$$ \Delta \left( m_1 \cdot \vec{v}_1 \right) = - \Delta \left( m_2 \cdot \vec{v}_2\right).$$
The minus sign on the right is to remind us that the change is in opposite directions.

For the balls in this simulation, the masses stay constant, and it is only the velocities that change, so we can write
$$ m_1 \cdot (\Delta \vec{v}_1) = - m_2 \cdot (\Delta  \vec{v}_2).$$

In other words, the relative change in velocities is related to the ratio of their masses,
$$ \Delta \vec{v}_1 = - \frac{m_2}{m_1} \cdot \Delta   \vec{v}_2.$$

So, if ball two has twice the mass of ball one, the change in speed of ball one is twice the change in ball two. 

## Example 3 - colliding people.

Recall in the thrid video above, we had a boy colliding into a girl. Suppose 
- the boy weighs 80 kg
- the girl weighs 40 kg
- the boy is running at 5 meters per second, and after the collision, has stopped dead.
How fast is the girl going?

Well, if we ignore the forces of their feet on the floor, we see the boy's change in velocity is 5 m/s. Since the ratio of masses $m_2/m_1$ is 2, the change in the girl's velocity must be twice as great. So she goes from 0 m/s to 10 m/s (which is very fast).

If you like, we can compute further:
- the boy's initial momentum is $80\times 5$ = $400$ kg m/s.
- Going to a dead stop, his change in momentum is $- 400$ kg m/s.
- The girl goes from zero to $40\times 10$ = $+400$ kg m/s.

So the change in momentum of the boy is equal and opposite the change in momentum of the girl.


## Where's the force?

Notice in the above example that we did not need to compute the force of the collision. This is one of the powerful aspects of Newton's Third Law. That is, without knowing any details of the forces involved, we can still figure out the change in velocities of the interacting bodies.

In fact, the forces can be quite complicated. With the boy and girl colliding, the force is transmitted through the bouncy ball. So it is a small force, extended over a rather long time (a few tenths of a second). If they were holding hard steel balls, the force of collision would have been very large, over a short time (a hundredth of a second, say). Fortunately, we don't need to know these details to use the Third Law.

## Conservation law

Newton's Third Law leads to the conservation of momentum law. This is a deeper physical result that holds true even in very complicated situations, with many bodies (not just two), and even for things like fluids, gases, and elastic solids.

It is easy to see this conservation of total momentum for the bouncing balls. We write
$$\mbox{Total Momentum}, \; \vec{p} = m_1\cdot \vec{v}_1 + m_2\cdot \vec{v}_2 + m_3\cdot \vec{v}_3 + \ldots$$
as the sum of the momenta of all the balls. 

Now, if two balls collide, say one and two, then the momentum of first ball goes up by $\mbox{ change in } (m_1 \cdot v_1)$ while the momentum of the second ball goes down by the same amount. This is the **equal and opposite** part of the Third Law. The Total Momentum stays the same, since this increase and decrease cancels out in the total sum of momenta.


## Summary of Newton's Third Law

The Third Law really is a physical law. It says that when two objects interact, it is through forces. Each object experiences a force, that is equal to, and opposite to the force on the other object. 

From the First and Second Laws, we know there are consequences to these forces. The objects will change their motion, and the size of the change of their velocities will depend on their relative masses. 

So when big things hit small things, the small thing has a bigger change in velocity. 

One important consequence of Newtons' Third Law is the conservation of total momentum for a system of particles. 

## Exercises

1. Suppose you are in your car, stopped at an intersection. A car hits you from behind (that is an action). What is the reaction? (What does your car do?)

2. If the car hitting you from behind has the same mass as yours, is the force your car experiences the same as the force the other car feels?

3. If the car hitting you from behind has 10 times the mass, is the force your car experiences the same as the force the other car feels? Explain. 

4. If the car hitting you from behind has 10 times the mass as yours, is the change in velocity your car experiences the same as the change in velocity the other car feels? Explain.

5. From the passenger's point of view, any big increase in velocity is a problem because at some point in an accident, you get stopped (by an airbag, a windshield, or a road surface). Explain why getting hit by a heavy truck is worse than getting hit by a light car. 

6. You and a friend are on a skating rink that is perfectly smooth, and your skates move frictionlessly on the ice. Standing face to face, if you push against each other, do you move? In which direction do each of you move?

7. As in 6, if you and your friend weigh the same, how fast do you move, compared to your friend?

8. As in 6, if you weigh twice as much as your friend, do you move twice as fast? Four times as fast? How fast?

6. A bird can lift itself into the sky by pushing the air with its wings. A rocket in outer space doesn't have air to push against -- so how does it move? (Hint -- think of the skaters. One skater could be like the rocket, the other skater is like the hot gases being pushed away from the rocket.)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)