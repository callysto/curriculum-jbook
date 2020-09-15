![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Science/HeatAndTemperature/heat-and-temperature.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Heat and Temperature

## INSTRUCTIONS BEFORE YOU START:
### Once the notebook has loaded click the fast forward button ">>" in the menu bar above. Click "Yes" to restart and run. 
### If the "Run All Cells" button has loaded the reader can also click it to run all the cells.

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

## Heat and Temperature: How Human Needs Led to the Technologies for Obtaining and Controlling Thermal Energy

## Introduction

In this notebook we will give a brief overview of thermal energy and then move on to the uses of thermal energy in society and how our uses of it have changed throughout history. We will start by identifying and explaining common devices and systems used to generate, transfer, or control thermal energy. Then we will look at how human purposes have led to the development of heat-related materials and technologies. 

### Thermal Energy

First we begin by giving a brief definition of what thermal energy is. A more complete and involved definition will be given in following notebooks. In the most basic sense thermal energy is the energy we associate with temperature.  At a microscopic level it is made up of the energy of vibration, rotation, and motion of the particles and molecules that make up matter.  As the particles and molecules move faster they contain more thermal energy and the temperature of matter is higher.


<img src="images/Matter_Temperature.jpg" alt="MatterTemp" width=500 align=middle>

As the temperature increases the thermal energy also increases. It's important to note that thermal energy of an object is given by its internal energy and not by its temperature. We can increase the thermal energy of an object  by placing it next to an object warmer than itself. The warmer object will heat the cooler object through the transfer of thermal energy. As the thermal energy of the cooler object increases the thermal energy of the warmer object will decrease. 

Before we move on let's discuss a few of the ways thermal energy can be generated. It could be generated due to chemical reactions, such as when you light a fire. Thermal energy is generated from the chemical reactions occuring as the wood burns. Thermal energy can also be generated mechanically by rubbing two objects together. For example you could rub your hands together and the energy from the motion of your hands is converted to an increase in thermal energy at a microcoping level. The energy in an electrical current can also generate an increase in thermal energy.  An electrical cord for instance will warm to the touch due to electrical energy being converted in part to the thermal energy of the wire. Finally light energy can be converted to thermal energy as anyone who has stood in the sunshine can affirm.

This will be as far as we go into a definition about thermal energy as a more precise and complete one will be given in follow up notebooks.

## Devices and Systems used to Generate, Transfer, or Control Thermal Energy

In this section we are going to cover multiple common devices and systems that are used to generate, transfer, or control thermal energy in some way. Most of these devices and systems are seen everyday, but we might not be fully aware of them. We will start off by considering devices and systems that we have in our homes. I want to let the reader know that we will be explaining what the devices do but we won't be going into detail about how they function since that will be covered in a later notebook. This section is to get the reader familiar with the devices and what they accomplish.  

### Exercise

Try to think of and list as many devices and systems that are used to generate, transfer or control thermal energy. If you want you can add them to the list below. You can work with a partner if you are running out of ideas. The **Add** button adds what you type in the box to the list, the **Remove** button removes the last item in the list and the **Clear List** button clears the list.

import ipywidgets as widgets
from IPython.display import display, Math, Latex
import traitlets
from IPython.display import Markdown
import random

output_list = []

list_output = widgets.HTML('')

text_box = widgets.Text(
    value='',
    placeholder='Enter list item',
    description='',
    disabled=False   
)

add_item_button = widgets.Button(
    value=False,
    description='Add',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Add to list',
    continuous_update=True
)

remove_item_button = widgets.Button(
    value=False,
    description='Remove',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Remove from list',
    continuous_update=True
)

clear_list_button = widgets.Button(
    value=False,
    description='Clear List',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Clear List',
    continuous_update=True
)

add_item_button.layout.width = '100px'
remove_item_button.layout.width = '100px'
clear_list_button.layout.width = '100px'

clear_list_button.layout.margin = '0px 0px 10px 600px'
list_output.layout.margin = '20px 0px 0px 0px'

list_widget = widgets.HBox(children=[text_box, add_item_button, remove_item_button])

display_widget = widgets.VBox(children=[clear_list_button, list_widget, list_output])


def update_Add(change):
    if(not (text_box.value == '')):
        output_list.append(text_box.value)
        list_length = len(output_list)
        text_box.value = ''
        
        list_output.value = "<ul style='list-style-type:circle'>"
        for i in range(list_length):
            list_output.value = list_output.value + "<li>" + output_list[i] + "</li>"
        
        list_output.value = list_output.value + "</ul>"
    
def update_Remove(change):    
    list_length = len(output_list)
    if(not(list_length == 0)):
        del output_list[list_length-1]
        
        list_output.value = "<ul style='list-style-type:circle'>"
        for i in range(len(output_list)):
            list_output.value = list_output.value + "<li>" + output_list[i] + "</li>"
        
        list_output.value = list_output.value + "</ul>"
        
    
def update_Clear(change):
    del output_list[:]
    list_output.value = ''

add_item_button.on_click(update_Add)
remove_item_button.on_click(update_Remove)
clear_list_button.on_click(update_Clear)


display_widget

Once you have completed the exercise above click the button below to open up the next section. In the section we will cover various devices that may be on your list and explain how they relate to generating, transferring or controlling thermal energy.

button_click = False

show_button = widgets.Button(
    value=False,
    description='Show Next Section',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show Next Section',
    continuous_update=True
)

def update_Show(change):
    global button_click
    
    if(not button_click):
        display(Markdown(
"""
### Air Conditioner/Furnace & Thermostat
The first devices we cover are common to most homes and buildings and they are the air conditioner, furnace and thermostat. An air conditioner is used to remove thermal energy and moisture from a home or building and cooling it in turn. A furnace on the other hand is used to add thermal energy to a home or building by heating the air in it. The thermostat is used to control the temperature in a home or building by controlling the furnace and air conditioner. Thermostats have advanced enough that they can automatically adjust the temperature based on the time of day by preference of the building owner.
All of these devices together create a system that generate, transfer and control the thermal energy in a home or building. Some devices not mentioned yet like windows, insultation, building materials also contribute to this system since they maintain the thermal energy of a home or building by not allowing it to transfer outside the home or building.

### Refrigerator/Freezer
Other common devices found in almost every home are the refrigerator and freezer. A refrigerator or freezer keeps the air inside it a constant cold temperature. The refrigerator or freezer does this by constantly cycling and cooling the air similar to an air conditioner. As mentioned above a house is made with insulation to keep the transfer of thermal energy low and a refrigerator and freezer are designed the same way to keep the cold air inside from escaping out. Refrigerators and freezers are much smaller than a house so keeping the thermal energy lower is easier since it doesn't use as much energy to keep the air colder.
<center><img src="images/refrigerator.png" alt="fridge" width="350"></center>

### Stove/Oven
A device that would be the opposite of a refrigerator or freezer would be an oven or stove. An electrical oven generates thermal energy by heating up elements inside it which in turn heat up the air inside it. It is also insulated to keep the thermal energy inside from escaping. A stove generates thermal energy the same way by heating up elements but it is not insulated so pots or pans may transfer the heat from the elements to the food. The amount of thermal energy generated by the elements is controlled from the dials on the stove/oven.

### Barbecue
A barbecue is another device that is used to generate and control thermal energy. This is done by natural gas or propane being burned through the burners on the barbecue or by charcoal being burned to generate the thermal energy. The dials control how much propane or natural gas is burned and the amount of charcoal determine how much thermal energy is generated.

### Water Heater
Another very common device in homes is a hot water heater. A hot water heater uses electricity or natural gas to increase the thermal energy and temperature of the water in its tank. The hot water is then distributed throughout the house when required. Where the hot water ends up is controlled by a person turning on a hot water tap.

### Insulation/Building Materials
Insulation and building materials are both used to control the transfer of thermal energy from one object or space to another. Insulation can be as simple as a layer of air enclosed between two materials like a thermos or could be specialized material similar to that used in a house. The insulating material acts as a barrier to stop the thermal energy from one side transferring to the other. Just as in a house if it's winter time you usually don't want the inside of the house to be the same temperature as the outside so we use insulation to stop this. That said, even with good insulation some thermal energy will constantly be lost from your house in the winter but your furnace is used to constantly add this thermal energy back to keep the temperature of the house constant.
The building materials used also act as an insulator since they form the shell of the building or object. In North America wood is typically used when building the shell of a house since it's cheap and it's a better insulator than concrete, brick or steel. Structures and objects made of concrete, brick, steel, or some type of metal are typically stronger than wood but are usually a lot more expensive which is why houses are generally made of wood or similar material.
<center><img src="images/thermos.jpg" alt="thermos" width="350"></center>

### Doors and Windows
The other devices that are common to every home or building are the doors and windows which also contribute to the insulation of a building. Single pane windows don't act as good insulators since glass is not a good insulator but double pane windows have been developed to have a layer of air or some type of gas inbetween the panes that insulate much better than a single pane.
There are also varying types of doors that are better at insulating a house than others. A thin door doesn't insulate very well from the outside which is why usually thicker doors are used on the outsides of homes. The doors and windows need to be sealed well otherwise the outside and inside air will be able to mix and change the thermal energy. If the doors and windows aren't sealed well then the furnace or air conditioner would have to use more energy to keep the thermal energy in the house or building constant.

### Fans
A device that is a component to many different appliances and things around the home is a fan. Fans are used to transfer the thermal energy generated throughout the appliance. A convection oven has a fan that distributes the thermal energy generated by the elements around the oven to heat up the food evenly. A fridge, air conditioner and freezer will have fans to circulate the cooled air around the appliance or home. Fans are commonly used to transfer thermal energy from its current space to another and along with some vents or ducts also control where that thermal energy is going.

### Hair Dryer
A hair dryer is another device that generates and transfers thermal energy. An element inside the hair dryer will generate the heat and thermal energy and then a fan will blow and transfer the heat and thermal energy out.

### Washing Machine and Dryer
The last devices we will look at are a washing machine and dryer. When the washing machine is running a warm or hot cycle it typically heats the water it needs with an internal element but if it is an older version it will get the hot water it needs from the hot water heater. A dryer is used to dry the clothes that are wet from the washing machine. The dryer uses an element to generate thermal energy and a fan transfers the thermal energy throughout the dryer to the clothes.
"""))    
    button_click = True
    
show_button.on_click(update_Show)

show_button

## Heat-Related Materials and Technologies Developed for Human Purposes

To understand why we developed heat-related materials and technologies for our own purposes we only need to understand the function of the material or technology. When we look back throughout history a lot of the heat-related materials and technology developed were to make survival easier. In modern days we are improving upon those materials and technologies and making them more efficient and easier for people to acquire them. There are also heat-related materials and technologies for making our lives more convenient or for generating energy. 

We will explain the purposes for the devices and systems mentioned in the section above and then move onto heat-related materials and some other technologies that haven't been listed. The list of devices and systems above can be broken down into a few main purposes. The first purpose is for shelter or a place to live in for survival. Our second purpose is for subsistence or for food and water and the third would be for convenience.

### Exercise

Before you move onto the next section go through the devices and technologies that have been listed above and any others you may have on your list and try to determine the purposes for them. These purposes will have to do with their function but there will also be broader purposes that are to do with survival, convenience and others.

- Air Conditioner
- Furnace
- Thermostat
- refrigerator
- Freezer
- Stove
- Oven
- barbecue
- Water Heater
- Insulation
- Building Materials
- Doors
- Windows
- Fans
- Hair Dryer
- Washing Machine & Dryer

button_click2 = False

show_button2 = widgets.Button(
    value=False,
    description='Show Next Section',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Show Next Section',
    continuous_update=True
)

def update_Show2(change):
    global button_click2
    
    if(not button_click2):    
        display(Markdown("""
#### Shelter
- Air Conditioner/Furnace & Thermostat
- Insulation/Building Materials
- Doors and Windows
- Fans

The devices listed above all have to do with keeping a house or building at a certain temperature. The Air conditioner/Furnace are concerned with cooling down or heating up the building based on the thermostat setting while the insulation/building materials and doors and windows are concerned with keeping the temperature outside from affecting the temperature inside. The fans on the air conditioner/furnace keep the air circulating in a home to maintain a constant temperature over the whole building.
These devices don't necessarily mean your survival but as most people are aware we live on a planet with a wide variety of climates. If you lived in a location where the temperatures dropped well below zero degrees celsius then a furnace could determine your survival. Now if you lived in a location that reached very hot temperatures then your survival could depend on an air conditioner.

#### Food and Water
- Refrigerator/Freezer
- Stove/Oven
- Barbeque

The devices above have to do with food or water. These devices have to do with both survival and convenience. A refrigerator/freezer allows you to store food and keep food and drinks a lot longer than if they were left out in the open. This doesn't necessarily have to do with survival but without being able to store the food you could potentially run out of it. The stove, oven and barbeque are used to cook the food or boil water. Without being able to cook the food or boil water you could be exposing yourself to a dangerous bacterium or virus. This is why raw meat needs to be cooked and unclean water need to be boiled otherwise you could become quite sick.

#### Convenience
- Water Heater
- Hair Dryer
- Washing Machine and Dryer

These are heat-related devices that are more for convenience than survival. You can make the argument that the hot water from the water heater used in the washing machine, for washing hands or for dishes ensures they are cleaned better but it doesn't mean your survival would be put in jeporady by it. A hair dryer or clothes dryer is for convenience since they make drying your hair or clothes easier and faster. The washing machine is mostly for convenience since it reduces the amount of work and time it takes to wash clothes.
"""))

    button_click2 = True
    
show_button2.on_click(update_Show2)

show_button2

### Purposes

Now let's focus on the some of the main purposes for which heat-related materials and technologies have been developed. As mentioned above the purposes can be reduced down to the broad categories of survival and convenience. There is also the purpose for electrical energy generation that will be looked at last. 


#### Survival

We have already touched on survival in a couple of the sections above. These days there are a lot of heat-related materials and technologies that people do not realize they depend on. In the past the heat-related materials and technologies would have been more obvious since people could understand them but currently they have advanced enough that people might not understand them and take them for granted. We've addressed some heat-related materials and technologies above that relate to our survival and we will go through a few more to ensure we have a decent understanding of how much materials and technologies have an impact upon our survival. 

> **House (Shelter)**
>
> An easy example to understand how heat-related materials and technologies have enabled our survival is to examine our shelter or house. This has been looked at above but here we will examine how the heat-related materials and technologies in a house have developed and advanced through history. In particular we will look at the material the home is made of and the technologies used with adjusting the temperature of it. 
>
> The first heat-related technology we look at is burning wood for thermal energy. Burning wood for thermal energy has been used throughout history and still today. The use of burning coal came next and became popular in the 19th century from its abundance, availability and its ability to generate higher heat output than wood. Along with better materials to burn came advancing ventilation and delivery systems for the thermal energy generated in houses. With the use of natural gas becoming popular in the late 19th century and the discovery of electricity the modern heating system started to take shape. With the discovery of electricity and the use of natural gas and a hundred years later the modern furnace was invented and can be found in most houses. Through the use of electricity the air conditioner was invented in the early 20th century and has continually increased in popularity since then. It has also advanced in efficiency and technology till the modern unit we know and use in the majority of homes today. 
>
> The material a home is made of can have an effect on survival since it effects how much thermal energy escapes from a house and thus how much the temperature changes. Throughout history houses were usually made out of stone, brick, or concrete like material and in North America homes are typically made out of wood or similar material. These materials are still in use today but have advanced to better keep the temperature and thermal energy of a home constant. The biggest advancement would be the development of insulating material used in between the walls of a house to limit the transfer of thermal energy to the outside of the home. 
>
> In moderate climates these materials, devices and technologies would not add up to survival on a normal day but even in moderate climates there can be extreme climate changes that without shelter someone's life would be in danger. This is even more evident living in the Northern Hemispheres where Winter and extremely low temperatures occur. In the past a house or shelter has been linked with survival and is even more today since we have spread out to regions with extreme climates. 

> **Food/Water**
>
> No matter what climate we live in the food and water we eat and drink are necessary for our survival. When the water we drink is not clean of bacteria or viruses we could become quite sick. To rid water of bacteria and viruses it needs to be boiled for a few minutes to ensure the bacteria and viruses are killed. In the past burning wood and coal would have been the primary ways to generate thermal energy to boil water. With the discovery of electricity there have been plenty of technology and devices developed like a stove to boil water. 
>
> The food we eat can contain harmful bacteria and viruses if it is not properly cleaned or cooked. When food is grown in the ground it needs to be properly cleaned to stop any harmful bacteria or viruses from being eaten. The simplest method to cleaning food is to thoroughly wash it with clean water. When cooking raw meat we need to be sure it is cooked fully otherwise we could become quite sick from eating it. In the past food would have been cooked from the thermal energy generated by burning wood or coal but these days we have multiple devices that generate thermal energy to cook food. Common devices used to cook food are a stove, oven, microwave and barbeque. 
>
> Without having clean water to drink or food that has been properly cleaned and cooked we could ingest some pretty harmful bacteria and viruses that could be life threatening. 

<table>
<tr>
    <td><img src="images/OldStove.jpg" alt="Old" width="300"/></td>
    <td><img src="images/modernstove2.jpg" alt="New" width="300"/></td>
</tr>
</table>

> **Clothing**
>
> The most common example of a heat-related material that is pertinent to our survival would be the clothing we wear. Similar to ones house, clothing is most useful to our survival in harsh climates. During the summer if it is hot out we can remove clothing to become cooler but during the winter we need warmer clothing that will allow us to survive if we have to go outside. In the past clothing would have been made of animal hides but we have come a long way in being able to make our own clothing. Through the discovery of new materials and technologies we are able to create or use material that is thinner and more efficient at retaining or releasing thermal energy. Winter is the season of the year that would be considered the harshest and is the reason we have developed specific clothing like jackets, pants, gloves and headwear to retain your thermal energy and allow you to survive outdoors. During the other seasons of the year clothing is more for comfort and convenience since you could survive outdoors without it.

<table>
<tr>
    <td><img src="images/OldClothing.jpg" alt="Old" width="250"/></td>
    <td><img src="images/modernwinterjacket.jpg" alt="New" width="250"/></td>
</tr>
</table>


#### Convenience and Comfort

When you have a house to live in and clean food and water most of the other heat-related materials and technologies are for making your life easier. These materials and devices have advanced in efficiency and technology throughout history to provide you with more convenience, time and comfort. We will discuss a few examples below and look at how they have changed over time. 

> **Hot Water**
> 
> Hot water can have an effect on survival but these days we use it more for convenience and comfort. If you have ever lost hot water in your home you quickly realize a shower with cold water is not very comfortable.  When cleaning clothes, dishes and anything else hot water is more effective and efficient than using cold water. 
>
> To obtain hot water you only need to heat up water. In the past water would have been heated using thermal energy from burning wood or some other fuel source. These days with the use of electricity a hot water heater uses an element to heat up the water. 

> **Washing Machine and Dryer**
>  
> A washing machine and dryer are used for convenience and saving time. In the past clothes and sheets would have been washed by hand using a washboard or similar device and would have been hung on a washing line to dry. Washing by hand is hard work and time consuming and clothes take a long time to air dry. A washing machine takes out the hard work and time spent hand washing clothes, and a dryer reduces the time it takes for the clothes to dry.

<table>
<tr>
    <td><img src="images/oldwashingboard.png" alt="Old" width="200"/></td>
    <td><img src="images/washingmachine.jpg" alt="New" width="200"/></td>
</tr>
</table>

> **Transportation** 
> 
> One of the more convenient pieces of technology you likely use everyday would be some kind of vehicle for transportation. Without a vehicle to drive around it would take you a lot more time when traveling. Modern vehicles are enclosed with air conditioners and heaters making a drive much more comfortable than being exposed to the outside temperature. 
>
> In the past vehicles would have used a steam engine to move. The steam engine worked by burning some fuel source to generate thermal energy that was transferred to water which would boil and generate steam to be used to move the vehicle. As history moved forward the modern combustion engine was invented that used fuel like gasoline to create combustion when ignited which was used to move the vehicle. The modern combustion engine is much more efficient than the steam engine in moving a vehicle. From the invention of the modern combustion engine till now there have been great advancements in its design and efficiency to use less fuel while traveling the same distance. 

<table>
<tr>
    <td><img src="images/oldcar.jpg" alt="Old" width="300"/></td>
    <td><img src="images/moderncar.jpg" alt="New" width="300"/></td>
</tr>
</table>


#### Electrical Energy Generation

Heat-related materials and technologies have long been used to generate mechanical, electrical and thermal energy. Without electrical energy all of the devices that we have become so accustomed to and use everyday would not work.Electricity is typically generated from an electrical generator that converts mechanical energy into electrical energy. The mechanical energy comes from a turbine being rotated and its rotation comes from the generation of thermal energy. The thermal energy used can be generated using various methods outlined below.

> **Steam**
> 
> A turbine is rotated from the steam generated from heating up water. The thermal energy used in heating up the water can be generated from burning coal or some other material. Another alternative for the thermal energy is using a nuclear reactor that generates thermal energy from nuclear fission which is the used to heat up the water.
>
> **Combustion**
> 
> A combustion turbine uses the combustion generated from igniting some type of gas or fuel to rotate the turbine. A gas like natural gas is commonly used as well as gasoline or diesel fuel for combustion. Smaller generators that are similar to turbines can generate electricity in the same manor through the combustion of gasoline or diesel.
>
> **Geothermal Energy**
>  
> Geothermal energy is the thermal energy we find deep within the ground. As seen in the image below the hot water found deep underground is pumped up to the surface and is then used to generate steam which then turns a turbine to generate electrical energy. 

<img src="images/geothermal3.png" alt="" width="400" align="middle"/>

> Another use of the geothermal energy is using it to heat and cool your home using a heat pump. The heat pump uses the thermal energy from the water pumped up to either heat or cool your house.

<img src="images/geothermal2.gif" alt="" width="400" align="middle"/>

### Exercise

We have touched on some of the broader purposes of heat-related materials and technologies that have to do with survival, convenience and electrical energy generation above. As an exercises try to think of any other heat-related devices, materials or technologies that we haven't discussed and determine what their purpose and function is. If you are having trouble with the purpose or function you can always ask your teacher or do a web search to find it out.

## Conclusion

In this notebook we have addressed what thermal energy is and how heat and temperature are related to it. We discussed multiple devices, technologies and materials that are used to generate, transfer or control thermal energy and heat in some fashion. The purposes of the devices, technologies and materials were discussed in detail and the broader purposes of how they relate to survival, convenience and energy creation were looked at. We also look at how houses, food/water and clothing and the devices and technology associated with them developed throughout history. This notebook gives a lot of information about the various heat-related devices, materials and technologies that are used in our everyday lives and how much of an impact they have. A more indepth look into thermal energy and how the devices, materials and technologies function will be given in later notebooks.

## Image Sites

0. https://chem.libretexts.org/LibreTexts/Mount_Royal_University/Chem_1202/Unit_5%3A_Fundamentals_of_Thermochemistry/5.2%3A_Heat
1. http://outside-in.me/vintage-cook-stoves-for-sale/vintage-cook-stoves-for-sale-old-kitchen-wood-stoves-for-sale-old-cook-stove-yahoo-image-search-results-old-kitchen-cook-vintage-gas-cook-stoves-for-sale/
2. https://pixabay.com/en/kids-stove-children-toys-tin-stove-434916/
3. http://angels4peace.com/modern-kitchen-stove.html/modern-kitchen-stove-simple-popular
4. https://pixabay.com/en/ginsburgconstruction-kitchen-3-330737/
5. http://collections.musee-mccord.qc.ca/scripts/printtour.php?tourID=CW_InuitClothing_EN&Lang=2
6. https://pixabay.com/en/washboard-wash-tub-old-formerly-982990/
7. https://pixabay.com/en/auto-renault-juvaquatre-pkw-old-1661009/
8. https://pixabay.com/en/car-audi-auto-automotive-vehicle-604019/
9. http://photonicswiki.org/index.php?title=Survey_of_Renewables
10. https://sintonair.com/geothermal-heat-pump/
11. http://ca.audubon.org/conservation/geothermal-power
12. https://de.wikipedia.org/wiki/Waschmaschine

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)