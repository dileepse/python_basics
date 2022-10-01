
class Focus_Institute:
    sql_trainer = "Mahesh"
    python_trainer = "Dileep"
    def __init__(self, stu_id, stu_name, category):
        self.id = stu_id
        self.name = stu_name
        self.category = category
    
    def set_trainers(self):
        pass
        
    def display_student_details(self):
        print("{stu_nm} details : ".format(stu_nm = self.name))
        print("Student Id is : {st_id}".format(st_id = self.id))
        print("Student Name is : {name}".format(name = self.name))
        if self.category != "job_training":
            self.sql_trainer = "No One"
        print("SQL Trainer name is : {sql_name}".format(sql_name = self.sql_trainer))
        print("Python Trainer name is : {python_name}".format(python_name = self.python_trainer))
        print("His training comes under category : {which_category}".format(which_category = self.category))
    
    def caluclate_fee(self):
        if self.category == "learning":
            print("Fee will be subject to your satisfaction")
            print()
        elif self.category == "job_training":
            print("Fee will be one month full salary excluding PF and Variable Pay")
            print("25% of you joining bonus")
            print()
        else:
            print("Job Category Unknow, Contact Dileep/Mahesh ")
            print()
        
    
student_obj1 = Focus_Institute(1, "Adi Narayana", "job_training")

student_obj2 = Focus_Institute(2, "Aruna", "learning")

student_obj3 = Focus_Institute(3, "Azeez", "learning")

student_obj4 = Focus_Institute(4, "Chandu", "job_training")

student_obj5 = Focus_Institute(5, "Jyoshna", "job_training")

student_obj6 = Focus_Institute(6,"Rakesh","learning")

student_obj7 =  Focus_Institute(7, "Kasi", "TBD")

lst = [student_obj1, student_obj2, student_obj3, student_obj4, student_obj5, student_obj6, student_obj7]

for student_object in lst : # temp = student_obj1
    student_object.display_student_details()
    student_object.caluclate_fee()
    


# student_obj1.display_student_details()

# student_obj1.caluclate_fee()