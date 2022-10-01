
"""
Classes -
    user-defined classes 
    pre-defined classes - strings, list, int, float
Syntax - 

class <CUSTOM CLASS NAME>: # Always start your class name in capital
    def __init__(self): # constructor
        <blcak box>
    <common attributes>
    <some functions/methods>
    
2 steps :
    - Class definition
    - Object Creation

class
constructor
object

How to create an object
    
    * custom-class-name(args1, arg2,...) # arguments are not mandatory RHS,
                                         # don't pass self during object creation
    * If we assign above object to any variable  # LHS
"""

class Student:
    def __init__(self):
        print("I am Inside Student Class Construtor Method")
        print("Another statement in the constructor")
    def hello_world(): 
        # hello_world is student class method
        print("I am inside Student class hello_world method")


Student() # Object creation