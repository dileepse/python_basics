"""
student marks
100 above - Fake Marks
91 to equal to 100 - Excellent
81 to upto 90 - Very Good
71 to 80 - Good
61 to 70 - okay
35 to 60 - average
35 below - Fail
"""

# Definition - onetime
def get_student_grade(marks):
    if marks > 100:
        return 'Fake Marks'
    elif marks > 90 and marks <= 100:
        return 'Excellent'
    elif marks > 80 and marks <=90 :
        return "Very Good"
    elif marks > 70 and marks <=80:
        return 'Good'
    elif marks >= 61 and marks <= 70:
        return 'Okay'
    elif marks <= 60 and marks >= 35:
        return """Average"""
    else :
        return '''Fail'''

grade = get_student_grade(75)

print("Student grade : ",grade)