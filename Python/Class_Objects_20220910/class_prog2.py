
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
    
    * custom-class-name(args1, arg2,...) # arguments are not mandatory  - RHS
                                         # don't pass self during object creation
    * If we assign above object to any variable  # LHS

How to call methods for the created class ?
    * create class object and assign to a variable
    * Then call the respective class methods with the help of the created object
    * calling will be always object_name.method_name()
    * we will "." to for calling a method with the help of object
    * object_name.method_name
"""

class Student:
    def __init__(self):
        print("I am Inside Student Class Construtor Method")
        print("Another statement in the constructor")
    def hello_world(self): 
        # hello_world is student class method
        print("I am inside Student class hello_world method")


# student_obj1 - this is a object of class type Student
student_obj1 = Student() # Object creation, constructor will be called automatically
# print(type(student_obj1))
student_obj1.hello_world() # This is ver very very very important

