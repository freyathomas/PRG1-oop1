# Version 2

class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute with getter/setter
        self._date_of_birth = date_of_birth  # Private attribute, read-only
        self._place_of_birth = place_of_birth  # Private attribute, read-only
    
    # Properties for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.strip()
    
    # Properties for date_of_birth (read-only - you can't change when you were born!)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    # Properties for place_of_birth (read-only - you can't change where you were born!)
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."
    
####TESTS FOR PERSON CLASS######
    
# # Creating two instances of the Person class
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")

# # Using the objects
# print(steve.talk())
# print(aqil.talk())
# print(f"Name: {steve.name}")
# print(f"Date of birth: {steve.date_of_birth}")
# print(f"Place of birth: {steve.place_of_birth}")

# # We can change the name
# steve.name = "Stephen Rich"
# print(f"Updated name: {steve.name}")

#######################################
    
class AdaStaff(Person):  # AdaStaff inherits from Person
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)  # Call parent constructor
        self._employee_id = employee_id
        self._department = department
    
    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    def work(self):
        return f"{self.name} is working in the {self.department} department."
    
    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"
    
####TESTS FOR ADASTAFF CLASS#######

# Create AdaStaff objects
teacher = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
teacher2 = AdaStaff("Fahad Wasim", "14/12/2006", "Pakistan", "EMP002", "Maths")
teacher3 = AdaStaff("Sam Spence", "33/5/2068", "Leeds", "EMP003", "Arts and Crafts")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP004", "Administration")
admin2 = AdaStaff("Joseph Heckingbottom", "19/10/2008", "London", "EMP005", "Administration")

# # Test the objects
# print(teacher3.talk())  # Inherited from Person
# print(teacher3.work())  # New method in AdaStaff
# print(teacher3.get_employee_info())

####################################


class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []  # Private list to store grades

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def grades(self):
        return self._grades

    def study(self):
        return f"{self.name} is studying {self.course}."

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def get_average_grade(self):
        if self._grades:
            return sum(self._grades) / len(self._grades)
        return 0

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Course: {self.course}, Average: {self.get_average_grade():.1f}"

######TESTS FOR ADASTUDENT########

# Create AdaStudent objects
student1 = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
student2 = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
student3 = AdaStudent("Samuel Spence", "12/03/2007", "Leeds", "STU003", "Software Engineering")
student4 = AdaStudent("Fahad Wasim", "14/12/2007", "Pakistan", "STU004", "Software Engineering")
student5 = AdaStudent("Freya Thomas", "16/07/2007", "Leeds", "STU005", "Cyber Security")
student6 = AdaStudent("Chioma Ndu", "20/09/2006", "London", "STU006", "Cyber Security")

# # Test the functionality
# print(student4.talk())  # Inherited from Person
# print(student4.study())  # New method in AdaStudent

# # Add some grades
# student4.add_grade(85)
# student4.add_grade(92)
# student4.add_grade(78)

# print(student4.get_student_info())

#########################################



class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self.students = []  # List to store AdaStudent objects
    
    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self.students.append(student)
            print(f"Added {student.name} to {self.cohort_code}")
        else:
            print("Can only add AdaStudent objects to cohort")
    
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Removed {student_name} from {self.cohort_code}")
                return
        print(f"Student {student_name} not found in {self.cohort_code}")
    
    def list_students(self):
        if not self.students:
            return f"No students in {self.cohort_code}"
        
        result = f"Students in {self.cohort_code}:\n"
        for student in self.students:
            result += f"- {student.name} ({student.course})\n"
        return result
    
    def search_student(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student
        return None
    
    def get_cohort_average(self):
        if not self.students:
            return 0
        
        total_average = 0
        students_with_grades = 0
        
        for student in self.students:
            avg = student.get_average_grade()
            if avg > 0:
                total_average += avg
                students_with_grades += 1
        
        return total_average / students_with_grades if students_with_grades > 0 else 0


########## TESTS FOR COHORT ###########

# Create a cohort and add students
cohort1 = Cohort("DEV2024A")
cohort2 = Cohort("123456")
cohort3 = Cohort("7891011")

# Add our existing students
cohort1.add_student(student1)
cohort1.add_student(student2)
cohort2.add_student(student3)
cohort2.add_student(student4)
cohort3.add_student(student5)
cohort3.add_student(student6)

# Test the cohort functionality
print(cohort1.list_students())
print(cohort2.list_students())
print(cohort3.list_students())

# Add some grades to the new students
student1.add_grade(67)
student2.add_grade(20)
student2.add_grade(90)
student5.add_grade(79)
student5.add_grade(89)

print(f"Cohort average: {cohort1.get_cohort_average():.1f}")
print(f"Cohort average: {cohort2.get_cohort_average():.1f}")
print(f"Cohort average: {cohort3.get_cohort_average():.1f}")


####################################