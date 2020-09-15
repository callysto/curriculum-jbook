![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=TechnologyStudies/IntroductionToPython/introduction-to-python-classes.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Python - Classes

In this lesson, we are going to introduce a powerful programming language technique called Object-Oriented Programming, or OOP for short, using Python Classes. First, we will introduce Python classes, and then, we will provide the motivation for OOP and how Python Classes fit into OOP.

#### Table of Contents:
[Python Classes](#Python_Classes) <br />
[Getters and Setters](#Getters_and_Setters) <br />
[Practice Project](#Practice_Project) <br />
[Class Inheritance](#Class_Inheritance) <br />
[Introduction to Object Oriented Programming](#Intro_to_OOP) <br />
[Conclusion](#Conclusion) <br />

To run a cell, select the cell you wish to run, then either:
1. Find the run button at the top of the page, and click it or,
2. Hit shift+enter.

<a id='Python_Classes'></a>
## Python Classes

A **Python Class** is a structure that can group together relevant variables and functions. The variables and functions in this structure are designed to be used only in the context of that class.

To give more accurate terminology, the functions defined inside a class are called **methods** and the variables are called **attributes**. 

Sound familiar? We have already seen Python structures with methods, such as lists, dictionaries and strings. (See introduction to data structures in Python). If we wanted to access these methods, we used the dot operator. This is also true for Python classes. To use the actual functions, or methods, inside a Python class, we use the dot operator. 

As a matter of fact, classes make up the Python standard library, such as the string class, but are also a central programming technique used in Python, as well as C and C++.

Now, we cannot actually do anything with our class just by defining it and adding attributes and methods. If we want to do some work, we have to define an **instance** of our class. To see what we mean, suppose we define a class called Person. This class has attributes that we would associate with a person, such as height, age, weight, gender, etc. The methods in the person class would be actions a person would do, such as Work(), DoHomework(), Eat(), etc.

We cannot say, Person.Work(), as Person is a definition and not an instance. We would have to declare an instance of that class. Say Person Sally. Now, Sally is an instance of the Person class, and Sally can have **unique values**. If we were to create another instance of Person, such as Person Frank, the values of Frank and Sally's attributes would be different.

Notice that we declared Sally and Frank just as normal variables of type Person. Python classes allow you to create your own data types, with specified attributes and methods. This allows for a larger range of problem solving abilities, as well as more robust data handling and organization.

### Remark:

There are many languages that support classes such as C, C++ and Java. A major difference between Python classes and classes in C++ and Java is in the way data inside a class is handled and accessed.

In C++ and Java, we are allowed to create what are know as private and public variables. Private variables are variables which cannot be accessed from outside the class. In order to access them, we need to create methods inside the class, which allows a user to modify the variables. These methods are explored later on in this notebook. We use private variables when there is sensitive data inside a class. We do not want a user to directly access the data, as it would threaten the integrity of the program or privacy of another user. 

In contrast, a public attribute is a attribute that can be accessed from outside the class. In general, all attributes in a Python class or instance are public -- but it can be a good practice to treat them like they're not.

## An example ##

## The syntax for declaring a class is class Class_Name ##
class Employee:
    # This first function here is called the initializer, or, if we are in C++, #
    # the default constructor. It is reqiured in every class you make #
    # This function will be called everytime a new instance is created #
    def __init__(self, Name, Salary, Age):
        self.Employee_Name = Name
        self.Employee_Salary = Salary
        self.Employee_Age = Age
        
    # Functions in a Python class are defined as normal. Self is always a required parameter #
    # However, when we call these methods, we do not need to pass self explicitly #
    # These functions allow the user to print variables inside a given instance of a class #
    def Display_Name(self):
        print("Employee Name:", self.Employee_Name)
    
    def Display_Salary(self):
        print("Employee Salary:", self.Employee_Salary)
        
    def Display_Employee_Age(self):
        print("Employee Age:", self.Employee_Age)

# Creating a new instance #
# To create a new instance of a class, simply declare it as a normal variable #
# and pass your desired information to the initializer, note that self is not passed #

Emp1 = Employee("Frank", 20000, 25)
Emp2 = Employee("Sarah", 40000, 34)

# Accessing class methods #
# We can access the methods in the class employee using the dot operator #
# Because these are two different instances, they will print two different values #
Emp1.Display_Name()
Emp2.Display_Name()

# Accessing Data inside the class #
# In Python, it is possible to have access to the actual values inside the class using the dot operator #
# This is not the case in other languages such as Java and C++ #

print(Emp1.Employee_Name)
print(Emp2.Employee_Name)

<a id='Getters_and_Setters'></a>
### Getters and Setters:

In many cases, we will want to access or change the variables inside a class. This is where functions called **Getters** and **Setters** come into play. A getter is a class method which returns the value of a variable inside a class. A setter is a class method which allows a variable to be updated.

We will illustrate with an example.

## Example with Getters and Setters ##

class Better_Employee:
    

    def __init__(self, Name, Salary, Age):
        self.Employee_Name = Name
        self.Employee_Salary = Salary
        self.Employee_Age = Age
        
    # These are the get functions, functions which allow values that are hidden in a class to be used outside of it #    
    def Get_Name(self):
        return self.Employee_Name
    
    def Get_Salary(self):
        return self.Employee_Salary
    
    def Get_Age(self):
        return self.Employee_Age
    
    # These are the set functions, functions which allow the user to update values inside an instance #
    def Set_Name(self, new_name):
        self.Employee_Name = new_name
    
    def Set_Salary(self, new_salary):
        self.Employee_Salary = new_salary
    
    def Set_Age(self, new_age):
        self.Employee_Age = new_age

    def Display_Name(self):
        print("Employee Name:",self.Get_Name())
    
    def Display_Salary(self):
        print("Employee Salary:",self.Get_Salary())
        
    def Display_Age(self):
        print("Employee Age:",self.Get_Age())
        


# Now we create new instances #

Emp1 = Better_Employee("Frank", 20000, 25)
Emp2 = Better_Employee("Sarah", 40000, 34)

Emp1.Display_Name()
Emp1.Display_Salary()
Emp1.Display_Age()

print(Emp1.Employee_Name)

Emp2.Display_Name()
Emp2.Display_Salary()
Emp2.Display_Age()

# Suppose that everyone turns one year older and because of existing they get a 40000 dollar raise. #
# Now, the current age and salary information in each class is outdated. Thus, we need to update #
# the information in the class using setters #

# These will update the age and salaries #
Emp1.Set_Age(26)
Emp1.Set_Salary(60000)

Emp2.Set_Age(35)
Emp2.Set_Salary(80000)

Emp1.Display_Salary()
Emp1.Display_Age()

Emp2.Display_Salary()
Emp2.Display_Age()

# Now suppose we want to use the values in the class elsewhere, such as another file. #
# We can access those values by using the get functions. Note that these are not the original #
# variables, just the values associated with them are returned. The original variables are #
# unaccessable. #

Salary_To_Be_Used_Elsewhere = Emp2.Get_Salary()
Age_To_Be_Used_Elsewhere = Emp1.Get_Age()

print(Salary_To_Be_Used_Elsewhere) # Now we have access to values we extracted from the instance
print(Age_To_Be_Used_Elsewhere)

<a id='Practice_Project'></a>
### Practice Project

Make a Bank Account class with the following attributes:

> Name of owner <br />
> ID (Integer of your choice, greater than 0) <br />
> Total balance <br />
> Savings account balance <br />
> Checking account balance <br />

And create the following methods:

> Deposit money into savings <br />
> Deposit money into checking account <br />
> Withdraw money from savings or checking <br />
> Get Total Balance <br />
> Get Owner Name <br />
> Set ID <br />

## Code Goes Here ##

### Extra Resources:

[Very detailed introduction to classes](https://docs.python.org/3/tutorial/classes.html) <br />
[Another introduction to classes](https://www.learnpython.org/en/Classes_and_Objects)<br />
[First part in a series on classes](https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/)<br />
[Second Part](https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-2-data-hiding-and-object-printing/)

<a id='Class_Inheritance'></a>
## Class Inheritance

Suppose we create a class called Car, and a class called Truck, each with its own attributes and methods.

# Car Class #

class Car:
    
    # Attributes: #
    Car_Name = " "
    Model_Year = 0
    Cost = 0
    Max_Speed = 0
    Horse_Power = 0
    Torque = 0
    isStandard = False
    Has_AC = False
    Other = " "
    # Has Methods: #
    def __init__(self, Name, Year, Other_Stuff):
        self.Car_Name = Name
        self.Model_Year = Year
        self.Other = Other_Stuff
        # ... #
    def Get_Model_Year(self):
        return self.Model_Year
    #etc#

# Truck Class #

class Truck:
    
    # Attributes: #
    Truck_Name = " "
    Model_Year = 0
    Cost = 0
    Max_Speed = 0
    Horse_Power = 0
    Torque = 0
    Towing_Capacity = 0
    isStandard = False
    Has_AC = False
    Other = " "
    # etc #
    
    # Has Methods: #
    def __init__(self, Name, Year, Other_Stuff):
        self.Truck_Name = Name
        self.Model_Year = Year
        self.Other = Other_Stuff
        # ... #
    def Get_Model_Year(self):
        return self.Model_Year
    #etc#

my_car = Car("Herbie", 1969, "A movie star that's also a car!")
print(my_car.Get_Model_Year())

my_truck = Truck("Optimius Prime", 1986, "The animated one was DEFINITELY better.")
print(my_truck.Get_Model_Year())

For the most part, these classes are identical, save for a few unique attributes. This is redundant! We have just done more work creating the same thing with a different name.

So what can we do? Well, we can create what's know as a **generic class**, a class that can describe both a car and a truck, as well as other vehicles. Call this class vehicle, with all the attributes a vehicle possesses.

Then, when we go to create a class of something more specific, we can **inherit** attributes and methods from the vehicle class.
This method is called **Class Inheritance**. Class inheritance allows us to make classes with the same implementation as another class. This removes redundant work and allows for more general classes.

The class which we inherit from is called a **base class**. Classes which inherit from the base class are called **derived classes**. Base classes and derived classes can be called **parent classes** and **child classes** respectively.

# Vehicle Class, carries all attributes associated with any vehicle #

class Vehicle:
    # Attributes #
    Vehicle_Name = " "
    Model_Year = 0
    Cost = 0
    Max_Speed = 0
    Other = " "
    # etc #
    
    # Has Methods #
    
    def __init__(self, Name, Year, Other_Stuff):
        self.Vehicle_Name = Name
        self.Model_Year = Year
        self.Other = Other_Stuff
        # ... #
        
    def Display_info(self):
        print("'%s' was built in %d. Other information: '%s'" %
              (self.Vehicle_Name, self.Model_Year, self.Other))
    # etc #

# Now, we can derive a more specific car class, without having to redefine most of our attributes ##

# To inherit, we add an extra parameter to the class declaration #

class Car(Vehicle):
    # Now we have access to the attributes and methods in the Vehicle class #
    # In the class constructor, all attributes unique to the Vehicle Class will #
    # be initiated in the vehicle class, and all unique attributes in the Car class #
    # will be initiated in the car class #
    
    def __init__(self, Name, Year, Can_Talk, Other_Stuff):
        super().__init__(Name, Year, Other_Stuff) # The super() function passes things on to the parent class
        self.Can_Talk = Can_Talk

    def Display_info(self):             
        super().Display_info() # Again, super passes things up to the parent class
        if self.Can_Talk:
            print("It can talk!")
        else:
            print("It can't talk.")

class Truck(Vehicle):
    
    def __init__(self, Name, Year, Carries_Cargo, Other_Stuff):
        super().__init__(Name, Year, Other_Stuff)
        self.Carries_Cargo = Carries_Cargo

    def Display_info(self):             
        super().Display_info() # Again, super passes things up to the parent class
        if self.Carries_Cargo:
            print("It can carry cargo!")
        else:
            print("Don't ask it to carry cargo.")

my_car = Car("Herbie", 1969, False, "A movie star that's also a car!")
my_car.Display_info()
print()

another_car = Car("Kitt", 1986, True, "From the TV Smash hit 'Knight Rider'")
another_car.Display_info()
print()

my_truck = Truck("Optimius Prime", 1986, False, "The animated one was DEFINITELY better.")
my_truck.Display_info()

### Extra Resources:

[Introduction to class inheritance](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3) <br />
[Another introduction](https://www.programiz.com/python-programming/inheritance)<br />
[Introduction to Python Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)<br />
[Third Part in the series](https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super) <br />

<a id='Intro_to_OOP'></a>
## A word on Object Oriented Programming and Data

So what exactly is Object Oriented Programming (Or OOP for short)? OOP is a programming method in which the primary building blocks used to create the program are objects, and the objects interact with each other through methods. Inside these objects are variables and functions that are related to each other in some way. 

OOP allows for better code organization, as we can group related functions and variables in one spot under one name.

OOP also allows for what is called **data abstraction**. Data abstraction is a way of separating the way we have written the object, and the way a user interacts with said object.

OOP allows for whats known as **data encapsulation**. Data encapsulation allows us to hide sensitive information from the user. If the user wants to change that information, they must go through the objects methods to do so, instead of modifying the value directly. Doing this will ensure that our data does not get unwanted values which cause the object to break in some way. A more extreme version of data encapsulation is **data hiding**. Data hiding occurs when the user can neither see nor access certain information through the objects methods. You would do something like this if the information is very sensitive or important for the program to function.

For example, when we are working with strings, we have access to string functions and methods. However, as a user of these methods and functions, we don't really need to know how these methods or functions work to use them. This is an example of data abstraction. 

If you wanted to access the constants in a string class, such as the ascii string, which is defined to be "abcdefghi...xyz", we would have to explicitly state that we want to use it. We would have to say: string.ascii_lowercase. This is an example of data encapsulation. If we want to use a piece of information, we have to use the object to obtain it.



### Extra Resources:

[Introduction to OOP and Inheritance](https://realpython.com/python3-object-oriented-programming/) <br />
[Another Introduction](https://www.tutorialspoint.com/python/python_classes_objects.htm) <br />
[Wikipedia entry on OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) <br />
[Disadvantages of OOP](https://www.quora.com/What-are-the-disadvantages-of-object-oriented-programming-languages)

<a id='Conclusion'></a>
## Conclusion

We have seen in this notebook how to construct and use classes in Python, as well as class inheritance. We expect that reader has a basic understanding of the following concepts:

> 1. Basic classes and class syntax. <br />
> 2. Accessing class attributes and class methods using the dot operator. <br / >
> 3. Using getters and setters to modify attributes. <br />
> 4. Class inheritance and the motivation for inheritance. <br />
> 5. Syntax for creating an inherited class <br/ >
> 6. Data abstraction and data hiding. <br />

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)