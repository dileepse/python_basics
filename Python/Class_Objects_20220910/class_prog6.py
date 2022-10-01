
class Student:
    school = "Sri Chaitanya" # class or static varibale
    def __init__(self,full_name, student_id, teacher_name): 
        self.name =  full_name  # instance variable
        self.roll_no = student_id
        self.teacher = teacher_name
    
    def display_details(self): # method
        result_str = """
I am {student_name} bearing roll no {stu_roll}. 
Currently I am studying in {stu_school} School and my teacher is {teacher_name}
                    """.format(
                                student_name = self.name, 
                                stu_roll = self.roll_no,
                                teacher_name = self.teacher,
                                stu_school = self.school
                              )
        print(result_str)

student_obj1 = Student("Adi",1, "Ansari") # By default executes constructor
student_obj1.display_details()

print(student_obj1.name)
print(student_obj1.roll_no)
print(student_obj1.teacher)
print(student_obj1.school)

student_obj2 = Student("Chandu",2, "Acharyulu") # By default executes constructor
student_obj2.display_details()
print(student_obj2.name)