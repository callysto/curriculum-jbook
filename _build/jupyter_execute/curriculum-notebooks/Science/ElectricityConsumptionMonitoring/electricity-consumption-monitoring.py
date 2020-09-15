![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/ElectricityConsumptionMonitoring/electricity-consumption-monitoring.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Electricity Consumption Monitoring 

## Instructions before you start:
Once the notebook has loaded, click the fast forward button ">>" in the menu bar above. Click "Yes" to restart and run.

%%html
<button onclick="run_all()">Run All Cells</button> 
<script>
function run_all(){
    Jupyter.actions.call('jupyter-notebook:run-all-cells-below');
    Jupyter.actions.call('jupyter-notebook:save-notebook');
}
</script>

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
    
$( document ).ready(function(){ code_shown=false; $('div.input').hide() });
</script>

<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>



## Introduction

In this notebook we will be discussing what electricity is, how it is used and how it is monitored. We will also be discussing what circuit diagrams are and how they relate to electricity in your homes.

### What is Electricity?

In simplest terms electricity is the presence or flow of electrons. If you don't remember what electrons are from your other science courses they are found in atoms. Atoms are the basic building blocks of matter. 

<img src="images/atom.png" alt="" width=500 align=middle>

You can find electrons, protons and neutrons in an atom. Negatively charged electrons orbit around the nucleus of the atom which is made up of positively charged protons and neutrons with no charge. Electrons are attracted to the protons in the nucleus. Electrons are much lighter than the nucleus and can be transferred from one atom to another.


### Static and Current Electricity

Two types of electricity will be discussed, static and current electricity. **Static Electricity** is the build up of electrons on an object. A static charge can be formed when the electrons on one object move to another. An example of this would be sliding down a slide and your hair standing on end. 

<img src="images/staticCharge.jpg" alt="" width=500 align=middle>

This results from electrons being transferred from you to the slide leaving you with a net positive charge. You are left with positive charge at the ends of your hair causing them to be repelled from each other and making them stand up.

The other type of electricity is current electricity. **Current Electricity** is the flow of electrons or electrical energy from one atom to another and in general terms from one place to another. 

<img src="images/electricCurrentAnimation.gif" alt="" width=500 align=middle>

Current electricity is normally called **Electric Current**. An example of an electric current would be charging your cell phone. 

<img src="images/electricCurrent.jpg" alt="" width=500 align=middle>

Electrons flow from your cell phone charger through the charging cord and into your cell phone creating an electric current. In this notebook we will be focusing on current electricity or electric current and how it is monitored and used throughout our homes. In the rest of the notebook electrical current will generally be referred to as just electricity.

### Electricity Units
Before we move on to the rest of the notebook we need to cover the units that are used when measuring the amount of electricity being used. As electrical current travels through a device the electrons lose energy which can be used to do useful things like produce heat or do work like turning motors. We are often interested how fast this energy is being used, that is **Power**. The unit used to measure the power or the rate of electricity being used is **Watts (W)**. A Watt is one Joule of energy transferred per second.  The power used by a device when it is on is given in Watts.

Another unit of energy that is used is the **Watt-hour**. A **Watt-hour (Wh)** describes the total amount of electricity (energy) used over the course of an hour. It is a combination of how fast electrical power is being used. To get a better understanding of a Watt-hour let's convert it to Joules of energy.

> A Watt measures the amount of Joules per second and can be written as:
>
> $\large 1 \hspace{1mm} \text{Watt} = 1 \hspace{1mm} \text{W} = 1\hspace{1mm}\frac{\text{Joule}}{\text{second}} = 1\hspace{1mm}\frac{\text{J}}{\text{s}}$ 
>
> In an hour there are 60 minutes and 60 seconds in each minute. The total number of seconds in an hour would be 60x60 = 3600 seconds
>
> $\large 1 \hspace{1mm} \text{hour} = 3600 \hspace{1mm} \text{seconds} = 3600 \hspace{1mm}\text{s}$
> 
> Thus in 1 Watt-hour we have 1 J being used every second over the course of an hour. If a Joule is used every second of the hour and there are 3600 seconds in the hour then 1 Watt-hour is equivalent to 3600 Joules.
>
> $\large 1 \hspace{1mm} \text{Wh} = 1\hspace{1mm}\frac{\text{J}}{\text{s}} \times 3600 \hspace{1mm}\text{s} = 3600 \hspace{1mm}\text{J}$ 
>
> Compared to the Joule, a Watt-hour is a more convenient unit to measure the amount of energy consumed by an item over the course of some time.

### Kilo, Mega and Giga 

Some other terms you may see in this notebook are **kilowatts (kW)**, **megawatts (MW)** and **gigawatts (GW)**. A kilowatt is 1000 watts, a megawatt is 1 million watts and a gigawatt is 1 billion watts. You will also see the term **kilowatt-hours (kWh)** which is 1000 Watt-hours. It can also be thought of as using electricity for 1 hour at a rate of 1000 watts. 



## Electricity Use

It is common knowledge that electricity is used to power our homes, vehicles and the various electronic devices we use on a daily basis. So how much electrical power does it actually take to charge your smart phone, use your oven or run a refrigerator? In this section we will answer those questions and take a look at the electricity use of various electronic devices.

### Efficiency Labels

If you have ever looked at the back of a washing machine, dryer or other electrical appliances you may have noticed a label giving a number of kilowatt-hours (kWh) per year. This label is known as an efficiency label giving energy-related information about the product. In Canada this label is known as the EnerGuide label. Examples of this label are below.

<table>
<tr>
    <td><img src="images/label1.jpg" alt="EnerGuide" width="450"/></td>
    <td><img src="images/label2.jpg" alt="EnerGuide&EnergyStar" width="450"/></td>
</tr>
</table>

There are four key pieces of information that the EnerGuide label tells us:

1. It tells us the annual energy consumption of the appliance in kilowatt-hours. 
2. On the label it has the annual energy consumption for the most efficienct and least efficient models and were the appliance falls in between them. 
3. The energy consumption indicator positions the appliance model based on a comparison of other models in the same class. 
4. The label also has the type and capacity of models that make up the appliance class as well as the model number. 

We are most interested in the annual energy consumption since it tells us the average amount of electricity the appliance uses over the course of a year. It should be noted that not all electrical appliances  have an EnerGuide label as it is not manadatory for all electrical appliances.

### Device Electrical Power Use

Now that we have gotten the terminology and brief introduction about electricity over we can look at how much electricity everyday devices actually use. Below is table of various devices and their average kWh usage.

<table> 
    <tr>
        <th>Electrical Devices/Appliances</th> 
        <th>Device Power Usage</th> 
    </tr> 
    <tr> 
        <td>Portable Heater (1500 W)</td> 
        <td>1.5 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Electric Furnace (with fan)</td> 
        <td>10.0 kWh per hour</td> 
    </tr>
    <tr> 
        <td>Central Air Conditioner (3 ton)</td> 
        <td>3.0 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Ceiling Fan</td> 
        <td>0.075 kWh per hour</td> 
    </tr>
    <tr> 
        <td>Oven</td> 
        <td>2.3 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Microwave Oven</td> 
        <td>1.0 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Coffee Maker</td> 
        <td>0.12 kWh per brew</td> 
    </tr> 
    <tr> 
        <td>Dishwasher</td> 
        <td>0.6 kWh per load</td> 
    </tr> 
    <tr> 
        <td>Toaster</td> 
        <td>0.04 kWh per use</td> 
    </tr> 
    <tr> 
        <td>Refrigerator</td> 
        <td>0.05 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Plasma TV (40-49 inches)</td> 
        <td>0.4 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>LCD TV (40-49 inches)</td> 
        <td>0.012 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Desktop Computer</td> 
        <td>0.15 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Laptop</td> 
        <td>0.03 kWh per hour</td> 
    </tr>     
    <tr> 
        <td>Radio</td> 
        <td>0.02 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Clothes Washer (500 W)</td> 
        <td>0.5 kWh per load</td> 
    </tr> 
    <tr> 
        <td>Clothes Dryer (5000 W)</td> 
        <td>5.0 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Vacuum Cleaner</td> 
        <td>0.75 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Iron</td> 
        <td>1.08 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Hair Dryer</td> 
        <td>1.5 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Curling Iron</td> 
        <td>0.05 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Incandescent Light Bulb (60 W)</td> 
        <td>0.06 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Compact Flourescent (15 W)</td> 
        <td>0.015 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Halogen Light Bulb (300 W)</td> 
        <td>0.3 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Xbox One (Playing a Game)</td> 
        <td>0.112 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Playstation 4 (Playing a Game)</td> 
        <td>0.137 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Wii U (Playing a Game)</td> 
        <td>0.034 kWh per hour</td> 
    </tr> 
    <tr> 
        <td>Cellphone</td> 
        <td>0.01 kWh per hour</td> 
    </tr> 
</table>



If you want to determine how much electricity you have used for a device on the table above you can use the calculator below.  The energy used is just the power times the amount of time or number of usages. All you have to do is select the device and then enter the amount of hours the device was used for. Depending on the device selected you may enter the number of loads done or times it was used instead of the hours.

import ipywidgets as widgets
from IPython.display import display, Math, Latex
import traitlets
from IPython.display import Markdown as md
import random

error = False

usage_list = [0.0, 1.5, 10.0, 3.0, 0.075, 2.3, 1.0, 0.12, 0.6, 0.04, 0.05, 0.4, 0.012, 0.15, 0.03, 0.02, 0.5, 5.0, 0.75, 1.08, 1.5, 0.05, 0.06, 0.015, 0.3, 0.112, 0.137, 0.034, 0.01]

output1 = widgets.HTML(
    value='<font size="4"> Device: </font>',
)
output2 = widgets.HTML(
    value='<font size="4"> Number of Hours: </font>',
)

calculation_output = widgets.HTML('')
error_output = widgets.HTML('')

device_choice = widgets.Dropdown(
    options={' ':0,'Portable Heater': 1, 'Electric Furnace': 2, 'Air Conditioner': 3, 'Ceiling Fan': 4, 'Oven': 5, 'Microwave Oven': 6, 'Coffee Maker': 7, 'Dishwasher': 8, 'Toaster': 9, 'Refrigerator': 10, 'Plasma TV': 11, 'LCD TV': 12, 'Desktop Computer': 13, 'Laptop': 14, 'Radio': 15, 'Clothes Washer':16, 'Clothes Dryer': 17, 'Vacuum Cleaner': 18, 'Iron': 19, 'Hair Dryer': 20, 'Curling Iron': 21, 'Incandescent Bulb': 22, 'Compact Flourescent': 23, 'Halogen Bulb': 24, 'Xbox One': 25, 'Playstation 4': 26, 'Wii U': 27, 'Cellphone Charge': 28},
    value=0,
    description='',
)

hours_input = widgets.Text(
    value='0',
    placeholder='',
    description='',
    disabled=False   
)

calculate_button = widgets.Button(
    value=False,
    description='Calculate',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Calculate the number of kWh',
    continuous_update=True
)

device_choice.layout.width = '150px'
hours_input.layout.width = '100px'

device_widget = widgets.HBox(children=[output1, device_choice])
hours_widget = widgets.HBox(children=[output2, hours_input])

display_widget = widgets.VBox(children=[device_widget, hours_widget, calculate_button, calculation_output, error_output])


def calculate_output(change):
    global error
    global usage_list
    
    calculation_output.value = ''
    error_output.value = ''
    error = False
    
    check_error()
    
    if(not(error)):
        input_hours = float(hours_input.value)
        kwh = usage_list[device_choice.value]*input_hours
        kwh = round(kwh, 3)
        
        calculation_output.value = '<font size="4"> ' + str(kwh) + ' kWh used.</font>'
        
        
def check_error():
    global error
    
    if(device_choice.value == 0):
        error_output.value = '<font size="4"> ERROR: You have not selected a device.</font>'
        error = True
    else:
        try:
            input_hours = float(hours_input.value)
        except ValueError:
            error_output.value = '<font size="4"> ERROR: That is not a valid number.  Please enter a valid number.</font>'
            error = True

            
def check_value(change):
    if(device_choice.value == 7):
        output2.value='<font size="4"> Number of Brews: </font>'
    elif(device_choice.value == 8):
        output2.value='<font size="4"> Number of Loads: </font>'
    elif(device_choice.value == 9):
        output2.value='<font size="4"> Number of Uses: </font>'
    elif(device_choice.value == 16):
        output2.value='<font size="4"> Number of Loads: </font>'
    else:
        output2.value='<font size="4"> Number of Hours: </font>'
            

calculate_button.on_click(calculate_output)
device_choice.observe(check_value, names='value')

display_widget

### Electrical Energy Monitoring

To monitor your electrical energy use you would need to measure how many **Watts** are being used by your electrical devices over the time they are being used. Your local power company is able to monitor how much electrical energy you use from an electricity meter attached to the outside of your home. The electricity meter is monitoring the main electrical line running into your home so it can measure the electrical energy used by the entire home. Some examples of electricity meters that you may recognize are below. You may also notice on the images that the electricity meters measure the electrical energy in kWh that we learnt about above. 

<table>
<tr>
    <td><img src="images/meter2.jpg" alt="1" width="300"/></td>
    <td><img src="images/meter.jpg" alt="2" width="300"/></td>
    <td><img src="images/meter3.jpg" alt="3" width="300"/></td>
</tr>
</table>

There are also a variety of smaller electrical meters that can monitor the usage of individual devices and appliances. A few of these meters are below.

<table>
<tr>
    <td><img src="images/monitor2.png" alt="1" width="350"/></td>
    <td><img src="images/monitor1.jpg" alt="2" width="250"/></td>
    <td><img src="images/monitor3.jpg" alt="3" width="350"/></td>
</tr>
</table>

You can use such devices to monitor the energy consumption of appliances in your house and potentially replace them to energy efficient appliances to save power.

## Circuit Diagrams

Now that we have covered what electricity is, the various electrical devices and how it is monitored let's take a look at **circuit diagrams**. A circuit diagram is a graphical representation of an **electrical circuit**. An electrical circuit  is a network of electrical devices connected together. All of the electronic devices in your home make up a very complicated electrical circuit that can be represented with a circuit diagram. We are just starting to learn about circuit diagrams so we will be using simple examples such a light bulb connected to a battery that you can see below.

<img src="images/circuit1.png" alt="" width=500 align=middle>

We will cover six different circuit components that can make up a circuit, namely switches, power sources, resistors, lights, motors and wires. 

1. A **switch** can either be open or closed. If it is open the electricity can't flow through the swtich. If it is closed the electricity can flow through the switch. A switch can be thought of as a light switch. If the light switch is on the electricity is flowing and if it is off the electricity is not.

2. A **power source** is any type of device that provides power/electricity. The simple example of a power source we will use is a battery that provides electricity to electrical devices.

3. A **resistor** is a component that resists the flow of electricity when it flows through it. The resistor limits the flow of electricity in the circuit. Electrical energy will be lost as heat when electricity flows through a resistor. An example of needing to use a resistor would be when you have two devices in a circuit and one of the devices can only handle so much electricity. You would then need a resistor to limit the flow of electricity to the device. 

4. A **light** will be some device that produces light. Electrical energy will be lost to this radiant energy as electricity powers the light. The simple example we will use is a light bulb/lamp that generates light.

5. A **motor** is a device that is used to convert electrical energy into mechanical energy. Motors are used in a variety of electrical devices ranging from a vehicle motor to a motor in a refrigerator. 

6. A **wire** is a component that is conductive and allows electricity to flow through it. Wires are used to connect the other various components together.


### Units

Before we continue on we need to cover some units that are commonly used for the components that make up a circuit. We have already covered **Watts** and **Joules**, we will also cover **Volts**, **Amperes**, **Ohms** and **Coulombs**. 

A **coulomb (C)** is defined as a of charge. One coulomb is the amount of charge contained in $6.24 \times 10^{18}$ electrons or 6.24 quintillion electrons.

An **ampere (A)** is a unit used to measure electrical current (electricity). It is a measurement of the number of electrons flowing through a circuit. It is defined as one Coulomb of charge passing a certain point in a circuit in one second.

A **volt (V)** is a unit of electric potential or electromotive force that causes the electrons to flow. A volt can be defined as the potential difference between two points. In terms of **Joules** and **Coulombs** one volt will impart one joule of energy per coulomb of charge that passes through the two points. The power sources in the circuit will have units of volts as they create the flow of electrons.

An **ohm ($\Omega$)** is a unit of electrical resistance that can be defined as one volt per ampere ($\Omega = V/A)$ . The higher the resistance in ohms the lower the flow of electricity. As you can guess the resistors have units of ohms since they resist the flow of electricity. Each device in a circuit will also have some resistance to them that slows the flow of the electrons. For example the resistance in a lamp causes it to lose heat energy in addition to the energy emitted as light.

### Symbols

Each of the components in a circuit are represented by specific symbols as listed below.

1. The symbol commonly used for a switch is below. A circuit is considered a closed circuit when all the switches in it are closed and electricity is flowing. When a switch is open in a circuit it is considered an open circuit.

<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/switch.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            Open</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/switchclosed.png" alt="2" width="150" style="padding-bottom:0.5em"/>
            Closed</div>
        </td>
    </tr>
</table>

2. The symbol for power sources of a single cell battery and double cell battery are below. You can see on the single cell battery there is a positive(+) and negative(-) sign on the two sides. The two signs represent the two terminals on the battery where the long line is the positive terminal and short line is the negative terminal. Electricity flows out of the negative terminal into the circuit and comes back in the positive terminal. 

<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/cell.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            1V Battery</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/battery(2V).png" alt="2" width="150" style="padding-bottom:0.5em"/>
            2V Battery</div>
        </td>
    </tr>
</table>

3. The symbol for a resistor is below. There are two commonly used symbols to represent resistors that are below too.

    <table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/resistor.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            Resistor</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/resistor(1ohm).png" alt="2" width="150" style="padding-bottom:0.5em"/>
            1 Ohm Resistor</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/resistor(2ohm).png" alt="2" width="150" style="padding-bottom:0.5em"/>
            2 Ohm Resistor</div>
        </td>
    </tr>
    </table>

    There is also a symbol for a variable resistor. This resistor allows the resistance to be adjusted.
    
<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/variableresistor.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            Variable Resistor</div>
        </td>
    </tr>
</table>

4. The symbol for a light bulb/lamp is below.

<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/lamp(1V).png" alt="1" width="150" style="padding-bottom:0.5em"/>
            1V Lamp</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/lamp(2V).png" alt="2" width="150" style="padding-bottom:0.5em"/>
            2V Lamp</div>
        </td>
    </tr>
</table>

5. The symbol for a motor is below.

<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/motor.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            Motor</div>
        </td>
    </tr>
</table>

6. The symbol for wires are below.

<table>
    <tr>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/wire3.png" alt="1" width="150" style="padding-bottom:0.5em"/>
            Straight Wire</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/wire1.png" alt="2" width="150" style="padding-bottom:0.5em"/>
            Corner</div>
        </td>
        <td>
            <div style="width:150 px; font-size:120%; text-align:center;">
            <img src="images/wire2.png" alt="2" width="150" style="padding-bottom:0.5em"/>
            Link</div>
        </td>
    </tr>
</table>

### Creating the Circuit Diagram

When you draw a circuit there are two vital components that you will need to make it work. 

1. A power source to provide electricity to the devices in the circuit 
2. Wires to connect all the components together and allow electricity to flow through the circuit.

The more devices you have connected in your circuit the greater the power sources you will need. This can be achieved by having multiple batteries in a row. For example most TV remotes require at least two batteries in them to give them enough electrical power.

Please feel free to play around with the circuit builder program below and build and run your own circuit. The program is from the website http://www.cleo.net.uk/consultants_resources/science/circuitWorld/circuitworld.html and will require you to have Adobe Flash Player download and enabled in your web browser.

#### Program Instructions

Using this program is relatively simple. The various circuit components/devices we have covered are on the left side and can be clicked on and moved over to the grid to the right. 

Each of the devices and components will need to be connected together by the wires. 

Once everything has been connected together you can hit the run button on the bottom left to run the circuit. If the devices don't seem to be working, like a bulb not lighting up you may need to add more batteries to the circuit to provide more electricity.

There are other devices and components on the left that we have not covered. They are an ammeter and a buzzer. An ammeter measures the current in a circuit in **amps** and a buzzer just buzzes as expected. Feel free to use those components and devices in the circuit.

from IPython.core.display import HTML
display(HTML('<embed src="images/circuitworld.swf" width="825" height="600"></embed></object>'))
display(HTML('© 2019 CLEO (Cumbria and Lancashire Education Online)'))

## Conclusion

In this notebook we have covered a variety of topics related to electricity monitoring and consumption. We looked at what electricity is, the units that it is measured in and the devices used to measure and monitor its consumption. The efficiency of the various electronic devices and appliances used in our homes were looked into to see how much electricity they actually use. We also looked at what circuit diagrams are, how you create them and the various components that a used in them. 

We have covered a lot of information in this notebook related to electricity and the various devices and appliances that use it but these topics are quite complex so we weren't able to cover everything. I encourage the reader to continue looking into these topics as they are both unique and interesting.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)