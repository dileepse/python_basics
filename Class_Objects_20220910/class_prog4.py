
"""
Classes -
    user-defined classes 
    pre-defined classes - strings, list, int, float
Syntax - 

class <CUSTOM CLASS NAME>: # Always start your class name in capital
    def __init__(self): # constructor
        variable assignments using self 
    <some methods>
    
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
    
attributes (variable and methods)
    class or static variables
    instance variables
"""

class Student:
    def __init__(self, full_name): 
        self.school = "Sri Chaitanya"
        self.name = full_name
        
    def display_name(self): 
        print("Name of the student is : ", self.name)
    
    def method_student(self):
        print("School Name of student ",self.name, " is ", self.school)



student_obj1 = Student("Adi Narayana") 

student_obj1.method_student() # This is ver very very very important

student_obj2 = Student("Dileep Dasari") 
student_obj2.display_name()

student_obj2.method_student()


