![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ExploringSolarSystem/exploring-the-solar-system.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>



(Click **Cell** > **Run All** before proceeding.) 

#Import modules and packages 
import ipywidgets as widgets
import random
from IPython.display import clear_output, display, HTML, SVG

#----------

#import ipywidgets as widgets
#import random

#This function produces a multiple choice form with four options
def multiple_choice_4(option_1, option_2, option_3, option_4):
    option_list = [option_1, option_2, option_3, option_4]
    answer = option_list[0]
    letters = ["<b>(A)</b> ", "<b>(B)</b> ", "<b>(C)</b> ", "<b>(D)</b> "]

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Print the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        option_text_2 = letters[i] + option_text
        option_output = widgets.HTMLMath(value=option_text_2)
        display(option_output)
                
        #Stores the correct answer
        if option_text == answer:
            letter_answer = letters[i]

    button1 = widgets.Button(description="(A)"); button2 = widgets.Button(description="(B)")
    button3 = widgets.Button(description="(C)"); button4 = widgets.Button(description="(D)")
    
    button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
    button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
    
    container = widgets.HBox(children=[button1,button2,button3,button4])
    display(container)
    print(" ", end='\r')

    def on_button1_clicked(b):
        if "<b>(A)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "<b>(B)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "<b>(C)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Moccasin'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Lightgray'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "<b>(D)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)

# Exploring the Solar System

## Introduction

Scientists describe the **Solar System** as the collection of objects orbiting the Sun. The Solar System formed approximately 4.6 billion years ago from the gravitational collapse of a large **molecular cloud**, or **nebula**. This giant cloud, full of gas and dust, formed during an earlier period within the history of the universe. As the nebula contracted under gravity, it began to swirl faster and faster due to the conservation of angular momentum. This resulted in the formation of a **protoplanetary disk**. The majority of the nebula's matter collected at the centre of this disk to form a sphere, known as a **protostar**. The remaining matter continued to spin around the center, clumping together by gravity to form the **planets**. As the pressure and temperature increased at the centre of the protostar, some of the hydrogen began to fuse into helium - a process known as **nuclear fusion**. The energy released from this process initiated a self-sustaining fusion reaction and a new star, the **Sun**, was born. Streams of energized particles flowing outward from the Sun, known as the **solar wind**, blew away much of the remaining gas and dust from the protoplanetary disc into interstellar space. This ended the planetary formation process. This model of the Solar System's formation is known as the **nebular hypothesis**. However, it is important to remember that the scientific study of the Solar System and its formation remain active areas of research with many questions yet to be answered.

<img src="Images/formation_of_solar_system.svg" width="100%"/>

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Approximately how old is the Solar System?</i>"))

option_1 = "4.6 billion years" 
option_2 = "4.6 million years"
option_3 = "13.8 billion years"
option_4 = "4.5 billion years"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>What caused the molecular cloud to contract into the protoplanetary disk?</i>"))

option_1 = "Gravity" 
option_2 = "Nuclear fusion"
option_3 = "Angular momentum"
option_4 = "Magnetism"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Most of the material left behind from the formation of the Sun eventually became __________?</i>"))

option_1 = "Planets" 
option_2 = "Nebulae"
option_3 = "Solar wind"
option_4 = "Stars"

multiple_choice_4(option_1, option_2, option_3, option_4)

## Main Features of the Solar System

The main features of the Solar System include the **Sun**, the **planets**, and the **asteroid belt**. There are eight planets within the Solar System. The four closest to the Sun are called the **rocky inner planets**. These are named **Mercury**, **Venus**, **Earth**, and **Mars**. The rocky planets are composed primarily of rock and metal. During the formation of the rocky inner planets, these heavier substances were able to resist the high temperatures experienced close to the Sun. Most of the lighter substances within this region of the protoplanetary disk were vaporized and blown away by the solar wind. Further from the Sun, where the temperatures are much colder, the lighter substances and gases coalesced to form the two **gas giants**, **Jupiter** and **Saturn**. They are named the gas giants because more than 90% of their mass consists of hydrogen and helium. Their composition is therefore similar to that of the Sun, though they are considerably smaller in size. Beyond the gas giants, where the temperatures are even colder, are the two **ice giants**, **Uranus** and **Neptune**. Unlike the gas giants, the ice giants consist of only about 20% hydrogen and helium while the remaining mass is thought to consist of heavier elements, such as oxygen, carbon, nitrogen, and sulfur. The ice giants formed primarily by the gradual accumulation of frozen solids and ice which formed in the cold outermost regions of the protoplanetary disk.

*Use the interactive widget below to explore some of the main features of the Solar System.*

#import ipywidgets as widgets
#from IPython.display import clear_output, SVG

major_objects_output = widgets.Output()

class SolarSystemObject:
    def __init__(self, label, image):
        self.label = label
        self.image = image
        self.html = []
    
    def add_html(self, html):
        self.html.append(html)


class SolarSystem:
    def __init__(self):
        self.contents = [None]
        self.current = 0

    def add(self, label, image):
        self.last = SolarSystemObject(label, image)
        self.contents.append(self.last)

    def increment(self):
        self.current = (self.current + 1) % len(self.contents)

    def current_object(self):
        return self.contents[self.current]

    def next_object(self):
        return self.contents[(self.current + 1) % len(self.contents)]

solar_system = SolarSystem()

solar_system.add("the Sun", "solar_system_01_sun.svg")
solar_system.last.add_html("""<b>Circumference</b>: 109 x Earth <br> <b>Volume</b>: 1,301,019 x Earth <br> <b>Mass</b>: 333,060 x Earth <br> <b>Temperature</b>: 5,500<sup>o</sup>C <br> <b>Spectral Type</b>: Yellow dwarf <br> <b>Age</b>: 4.6 billion years""")
solar_system.last.add_html("The Sun is the most prominent feature of the Solar System, and it accounts for approximately 99.86% of all its mass. The main components of the Sun are hydrogen and helium, which make up 73% and 25% of the mass, respectively. The remaining 2% consists of heavier elements, such as oxygen, carbon, and iron. The Sun is so large that it could fit over 1 million Earths inside its volume. Within the core, nuclear fusion converts hydrogen into helium. This process releases an enormous amount of energy which radiates from the Sun in the form of heat and light.")

solar_system.add("Mercury", "solar_system_02_mercury.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.383 x Earth <br> <b>Volume</b>: 0.056 x Earth <br> <b>Mass</b>: 0.055 x Earth <br> <b>Distance from Sun</b>: 0.3871 AU (or 58 million km) <br> <b>Year</b>: 87.969 days <br> <b>Day</b>: 1407.5 hours <br> <b>Temperature</b>: -173/427<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: O<sub>2</sub>, Na, H<sub>2</sub>""")
solar_system.last.add_html("Mercury is the smallest and closest planet to the Sun. It is so small that 18 Mercury-sized planets could fit inside the volume of the Earth. The surface of Mercury is covered in craters due to its thin atmosphere, which provides little protection from meteors. Mercury has the smallest tilt of any planet in the Solar System at just 0.033 degrees. The planet was named after the Roman god often associated with trade and profit. Mercury has no known moons.")

solar_system.add("Venus", "solar_system_03_venus.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.950 x Earth <br> <b>Volume</b>: 0.857 x Earth <br> <b>Mass</b>: 0.815 x Earth <br> <b>Distance from Sun</b>: 0.723 AU (or 108 million km) <br> <b>Year</b>: 224.701 days <br> <b>Day</b>: 5832.4 hours <br> <b>Temperature</b>: 462<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: CO<sub>2</sub>, N<sub>2</sub>""")
solar_system.last.add_html("Venus is the second planet from the Sun and the second brightest object in our night sky. The surface of Venus is extremely hostile due to its thick atmosphere of carbon dioxide. This atmosphere creates a greenhouse effect by trapping heat from the Sun. Consequently, the surface temperature on Venus is 462<sup>o</sup>C, hot enough to melt lead. Unlike most of the other planets, Venus rotates in the opposite direction about its axis; an observer on Venus would see the Sun rise in the west and set in the east. The only other planet to exhibit this type of rotation is Uranus. The planet was named after the Roman goddess of love and beauty. Venus has no known moons.")

solar_system.add("Earth", "solar_system_04_earth.svg")
solar_system.last.add_html("""<b>Circumference</b>: 40,030 km <br> <b>Volume</b>: 1.083 x 10<sup>12</sup> km<sup>3</sup> <br> <b>Mass</b>: 5.972 x 10<sup>24</sup> kg <br> <b>Distance from Sun</b>: 1 AU (or 150 million km) <br> <b>Year</b>: 365.25 days <br> <b>Day</b>: 24 hours <br> <b>Temperature</b>: -89/57<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: N<sub>2</sub>, O<sub>2</sub>""")
solar_system.last.add_html("Earth is the third planet from the Sun, the largest of the inner rocky planets, and the fifth largest planet in the Solar System. It is the only planet in the Solar System known to support life. The main surface feature of the Earth is its oceans, which cover more than 71% of its surface. The age of the Earth has been estimated to be around 4.54 billion years old. It is the only planet not named after a Roman or Greek deity. Instead the name is derived from an English word meaning ground. The Earth has one moon, simply called 'the moon'.")
    
solar_system.add("Mars", "solar_system_05_mars.svg")
solar_system.last.add_html("""<b>Circumference</b>: 0.532 x Earth <br> <b>Volume</b>: 0.151 x Earth <br> <b>Mass</b>: 0.107 x Earth <br> <b>Distance from Sun</b>: 1.524 AU (or 228 million km) <br> <b>Year</b>: 686.971 days <br> <b>Day</b>: 24.6 hours <br> <b>Temperature</b>: -153/20<sup>o</sup>C (min/max) <br> <b>Atmosphere</b>: CO<sub>2</sub>, N<sub>2</sub>, Ar""")
solar_system.last.add_html("Mars is the fourth planet from the Sun. It is considerably colder and drier than Earth, with a thin dusty atmosphere. The surface of Mars is covered in red, rusty soil. Yet despite this hostile description, the planet contains many striking features, such as polar ice caps, canyons, craters, mountains, volcanoes, and deserts. During an earlier and warmer era, the surface of Mars once featured lakes and oceans of liquid water. Mars was named after the Roman god often associated with war. Mars has two moons, Phobos and Deimos.")


solar_system.add("the Asteroid Belt", "solar_system_06_asteroid_belt.svg")
solar_system.last.add_html("The Asteroid Belt is a region of space located between the orbits of Mars and Jupiter. It is occupied by millions of oddly-shaped objects called asteroids. The four largest asteroids within the belt are Ceres, Vesta, Pallas, and Hygiea. These four asteroids contain about half of all the mass within the entire Asteroid Belt. In the early history of the Solar System, protoplanets developing within this region would have been greatly affected by the gravity of Jupiter. As Jupiter passed by, it would have pulled on the protoplanets, causing numerous collisions between them, which prevented them from fusing together. What resulted instead of a planet was a belt of asteroids. The orbits of these asteroids are still significantly affected by Jupiter to this day.")

solar_system.add("Jupyter", "solar_system_07_jupiter.svg")
solar_system.last.add_html("<b>Circumference</b>: 10.973 x Earth <br> <b>Volume</b>: 1,321 x Earth <br> <b>Mass</b>: 317.8 x Earth <br> <b>Distance from Sun</b>: 5.203 AU (or 778 million km) <br> <b>Year</b>: 4,332.59 days <br> <b>Day</b>: 9.92 hours <br> <b>Temperature</b>: -145<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He")
solar_system.last.add_html("Jupiter is the fifth planet from the Sun and the first of the gas giants. It is also the largest planet in the Solar System. The mass of Jupiter is greater than 2.5 times the mass of all the other planets combined. As a gas giant, Jupiter lacks a well-defined solid surface. The atmosphere of Jupiter features many layers of clouds and a Great Red Spot, which is a persistent anticyclonic storm larger in size than the Earth. The planet was named after the king of the Roman gods, who is often associated with the sky and thunder. Jupiter has 79 known moons. The largest include Io, Europa, Ganymede, and Callisto.")

solar_system.add("Saturn", "solar_system_08_saturn.svg")
solar_system.last.add_html("<b>Circumference</b>: 9.140 x Earth <br> <b>Volume</b>: 763.594 x Earth <br> <b>Mass</b>: 95.161 x Earth <br> <b>Distance from Sun</b>: 9.5 AU (or 1,427 million km) <br> <b>Year</b>: 10,759.22 days <br> <b>Day</b>: 10.66 hours <br> <b>Temperature</b>: -178<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He")
solar_system.last.add_html("Saturn is the sixth planet from the Sun, the second of the gas giants, and the second largest planet in the Solar System. It is the only planet less dense than water. Saturn's most distinguishing feature is its spectacular ring system, which is composed primarily of ice and rock. These rings extend over 282,000 km from the planet and are thought to be fragments of comets, asteroids, or moons that were broken up by Saturn's powerful gravitational field. The planet was named after the Roman god who fathered Jupiter. Saturn has 53 official moons, with an additional 9 known moons awaiting confirmation. The largest include Titan, Rhea, and Iapetus.")
 
solar_system.add("Uranus", "solar_system_09_uranus.svg")
solar_system.last.add_html("<b>Circumference</b>: 3.981 x Earth <br> <b>Volume</b>: 63.085 x Earth <br> <b>Mass</b>: 14.536 x Earth <br> <b>Distance from Sun</b>: 19.2 AU (or 2,871 million km) <br> <b>Year</b>: 30,687.15 days <br> <b>Day</b>: 17.23 hours <br> <b>Temperature</b>: -216<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He, CH<sub>4</sub>")
solar_system.last.add_html("Uranus is the seventh planet from the Sun and the first of the ice giants. It is the only planet known to rotate on its side with an axial tilt of 97.77 degrees. This peculiar axis of rotation may have resulted from a collision with another planet-sized object in Uranus' early history. Like Venus, Uranus also features a retrograde rotation about its axis. More than 80% of its mass consists of icy materials (primarily water, methane, and ammonia). Uranus features a system of rings, though they are considerably fainter than those of Saturn. The planet was named after the Greek god of the Sky. It is the only planet named after a god of Greek mythology. Uranus has 27 known moons. The largest include Miranda, Ariel, Umbriel, Titania, and Oberon.")

solar_system.add("Neptune", "solar_system_10_neptune.svg")
solar_system.last.add_html("<b>Circumference</b>: 3.865 x Earth <br> <b>Volume</b>: 57.723 x Earth <br> <b>Mass</b>: 17.148 x Earth <br> <b>Distance from Sun</b>: 30.1 AU (or 4,498 million km) <br> <b>Year</b>: 60,190.03 days <br> <b>Day</b>: 16.11 hours <br> <b>Temperature</b>: -201<sup>o</sup>C (mean) <br> <b>Atmosphere</b>: H<sub>2</sub>, He, CH<sub>4</sub>")
solar_system.last.add_html("Neptune is the eighth planet from the Sun, the second of the ice giants, and the most distant planet in the Solar System. It is also the windiest planet in the solar system, with clouds moving across the atmosphere at speeds exceeding 2,100 km/h. Neptune was named after the Roman god of the sea. Neptune has 6 faint rings and 13 moons. The largest of these moons is Triton, which comprises more than 99.5% of the mass orbiting Neptune.")

solar_system.add("the Kuiper Belt", "solar_system_11_kuiper_belt.svg")
solar_system.last.add_html("The Kuiper Belt is a region of space located beyond the orbit of Neptune. Like the Asteroid Belt, the Kuiper Belt is occupied by millions of small bodies that formed during the early stages of the Solar System. However, unlike the Asteroid Belt, the majority of these small bodies are composed of icy materials instead of rock. The most notable objects in the Kuiper Belt include the dwarf planets Pluto, Eris, Haumea, and Makemake. The objects within the Kuiper Belt are strongly influenced by Neptune's gravity, and vice versa. One of Neptune's moons, Triton, may have originated from the Kuiper Belt.")



#Toggle images
def show_major_objects():
    current_object = solar_system.current_object()
    if current_object:
        display(SVG("Images/%s" % current_object.image))
        display(*[widgets.HTMLMath(value=html) for html in current_object.html])
    else:
        display(SVG("Images/solar_system_00_blank.svg"))
    next_object = solar_system.next_object()
    if next_object:
        display(widgets.HTMLMath(value="<b><i>Press the 'Explore!' button again to learn more about %s.</i></b>" % next_object.label))
        
explore_major_objects_button = widgets.Button(description="Explore!", button_style = 'success')
display(explore_major_objects_button)

def major_objects_clicked(button):
    solar_system.increment()
    with major_objects_output:
        clear_output(wait=True)
        show_major_objects()

explore_major_objects_button.on_click(major_objects_clicked)
display(major_objects_output)
with major_objects_output:
    show_major_objects()


#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Which four planets make up the inner rocky planets?</i>"))

option_1 = "Mercury, Venus, Earth, Mars" 
option_2 = "Mercury, Venus, Earth, Neptune"
option_3 = "Jupiter, Saturn, Uranus, Neptune"
option_4 = "Venus, Earth, Mars, Jupiter"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Which two planets are called the gas giants?</i>"))

option_1 = "Jupiter, Saturn" 
option_2 = "Jupiter, Venus"
option_3 = "Saturn, Venus"
option_4 = "Mars, Jupiter"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Which two planets are called the ice giants?</i>"))

option_1 = "Uranus, Neptune" 
option_2 = "Jupiter, Saturn"
option_3 = "Saturn, Uranus"
option_4 = "Saturn, Neptune"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Which is the largest planet in the Solar System?</i>"))

option_1 = "Jupiter" 
option_2 = "Saturn"
option_3 = "Earth"
option_4 = "Uranus"

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML

display(widgets.HTMLMath(value="<b>Question:</b> <i>Which is the smallest planet in the Solar System?</i>"))

option_1 = "Mercury" 
option_2 = "Mars"
option_3 = "Venus"
option_4 = "Neptune"

multiple_choice_4(option_1, option_2, option_3, option_4)

## Lesser Features of the Solar System

**Dwarf planets**: A dwarf planet is similar to a regular planet in that it has a spherical shape and directly orbits a star. However unlike planets, dwarf planets share their orbital zone with other bodies of significant size. For example, **Ceres** is located within the asteroid belt and thus shares its orbital zone with many asteroids. **Pluto**, **Eris**, **Haumea**, and **Makemake** are dwarf planets located in the **Kuiper belt**, a region of space located beyond Neptune that contains many small bodies, all remnants from the Solar System's formation.

**Asteroids**: Asteroids are small oddly-shaped objects scattered throughout the solar system. The vast majority of asteroids are located in the Asteroid Belt between Mars and Jupiter. There are two additional groups of asteroids, known as the **Trojan asteroids**, that are co-orbital with Jupiter. Asteroids are composed primarily of nickel, iron, titanium, and water.

**Meteoroids**: A meteoroid is a space rock, typically less than 1 m wide. Most meteoroids are fragments from comets or asteroids, while others originate from the debris ejected from impacts. When a meteor impacts Earth, the recoverable fragments are called **meteorites**. It is estimated that 25 million meteoroids enter the Earth's atmosphere each day, though most are below 1 mm in size. While most of these impacts go unnoticed, meteors on the scale of tens of centimeters to several meters can be observed as **shooting stars** at night.

**Comets**: A comet is a small, icy object that usually follows an elliptical orbit around the Sun. As it passes close to the Sun, it warms and releases gases that streak behind it like a tail. It is this feature that distinguishes a comet from an asteroid. Most comets are believed to originate from either the Kuiper belt, or the **Oort cloud**, a spherical cloud of icy objects surrounding our solar system. The Oort cloud extends well-beyond Neptune and into interstellar space.

## Measuring Distances in the Solar System

One common unit used to measure distances in the Solar System is the **astronomical unit (AU)**. One AU equals the average distance between the Sun and the Earth, or about 150 million km. 

Below is a table showing the average distances of each planet from the Sun in units of AU and km. Note the convenience of using AU when comparing distances between planets. 

Planet             | Distance in astronomical units (AU) | Distance in kilometers (km) 
---                | ---          | ---
Mercury            | 0.39         | 58,065,000 
Venus              | 0.72         | 108,450,000  
Earth              | 1.00         | 150,000,000 
Mars               | 1.52         | 228,600,000 
Jupiter            | 5.20         | 780,450,000 
Saturn             | 9.50         | 1,425,000,000 
Uranus             | 19.20        | 2,880,000,000 
Neptune            | 30.10        | 4,515,000,000 

#import ipywidgets as widgets
#from IPython.display import display, HTML
#import random

random_number_1 = random.randint(0,6)
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
answers = ["0.61 AU", "0.28 AU", "0.52 AU", "4.20 AU", "8.50 AU", "18.20 AU", "29.10 AU"]
planet = planets[random_number_1]
answer = answers[random_number_1]

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(answers,3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(answers,3)

display(widgets.HTMLMath(value="<b>Question:</b> <i>If we assume that the orbits of the planets are essentially circles, what is the closest distance possible between Earth and " + planet + " (in units of AU)?"))

option_1 = answer 
option_2 = choice_list[0]
option_3 = choice_list[1]
option_4 = choice_list[2]

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML
#import random

random_number_2 = random.randint(0,6)
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
answers = ["92 million km", "42 million km", "79 million km", "630 million km", "1,275 million km", "2,730 million km", "4,365 million km"]
planet = planets[random_number_2]
answer = answers[random_number_2]

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(answers,3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(answers,3)

display(widgets.HTMLMath(value="<b>Question:</b> <i>If we assume that the orbits of the planets are essentially circles, what is the closest distance possible between Earth and " + planet + " (in units of km)?"))

option_1 = answer 
option_2 = choice_list[0]
option_3 = choice_list[1]
option_4 = choice_list[2]

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML
#import random

random_number_3 = random.randint(0,6)
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
answers = ["1.39 AU", "1.72 AU", "2.52 AU", "6.20 AU", "10.50 AU", "20.20 AU", "31.10 AU"]
planet = planets[random_number_3]
answer = answers[random_number_3]

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(answers,3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(answers,3)

display(widgets.HTMLMath(value="<b>Question:</b> <i>If we assume that the orbits of the planets are essentially circles, what is the farthest distance possible between Earth and " + planet + " (in units of AU)?"))

option_1 = answer 
option_2 = choice_list[0]
option_3 = choice_list[1]
option_4 = choice_list[2]

multiple_choice_4(option_1, option_2, option_3, option_4)

#import ipywidgets as widgets
#from IPython.display import display, HTML
#import random

random_number_4 = random.randint(0,6)
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
answers = ["208 million km", "258 million km", "379 million km", "930 million km", "1,575 million km", "3,030 million km", "4,665 million km"]
planet = planets[random_number_4]
answer = answers[random_number_4]

#Create three choices that are unique (and not equal to the answer) 
choice_list = random.sample(answers,3)
while choice_list.count(answer) >= 1:
    choice_list = random.sample(answers,3)

display(widgets.HTMLMath(value="<b>Question:</b> <i>If we assume that the orbits of the planets are essentially circles, what is the farthest distance possible between Earth and " + planet + " (in units of km)?"))

option_1 = answer 
option_2 = choice_list[0]
option_3 = choice_list[1]
option_4 = choice_list[2]

multiple_choice_4(option_1, option_2, option_3, option_4)

## Conclusion

* The **Solar System** is a term used to describe the collection of objects orbiting the Sun.
* The Solar System formed approximately 4.6 billion years ago.
* The Sun makes up about 99.86% of all the mass in the Solar System. It consists predominately of hydrogen and helium.
* The four rocky inner planets are called **Mercury**, **Venus**, **Earth**, and **Mars**.
* The two gas giants are called **Jupiter** and **Saturn**.
* The two ice giants are called **Uranus** and **Neptune**.
* Other important objects in the Solar System include **dwarf planets**, **asteroids**, **meteoroids**, and **comets**.
* **Astronomical units (AU)** are commonly used to measure distances in the Solar System.

Images in this notebook represent original artwork.

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

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)