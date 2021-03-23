"""
Створіть класову структуру на Python, яка представляє людей в школі.
Почніть з базового класу Person, потім класу Student і ще одного класу Teacher.
Є список атрибутів, які можуть бути присвоєні цим класам: first_name, last_name, birth_date,
university, course, salary.
"""
"""
Створіть класову структуру на Python, яка представляє людей в школі.
Почніть з базового класу Person, потім класу Student і ще одного класу Teacher.
Є список атрибутів, які можуть бути присвоєні цим класам: first_name, last_name, birth_date,
university, course, salary.
"""

class Person():

    def __init__(self, first_name='N/A', last_name='N/A', birth_date='N/A'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def set_first_name(self, first_name):
        if Person.validate(self, first_name) == True:
            self.first_name = first_name.lower()
        else:
            raise TypeError ("Class is working with strings only")

    def set_last_name(self, last_name):
        if Person.validate(self, last_name) == True:
            self.last_name = last_name.lower()
        else:
            raise TypeError ("Class is working with strings only")

    def set_birth_date(self, birth_date):
        if Person.validate(self, birth_date) == True:
            self.birth_date = birth_date.lower()
        else:
            raise TypeError ("Class is working with strings only")

    def validate(self, item):
        if type(item) == str:
            return True
        else:
            return False


class Student(Person):

    def __init__(self, first_name='N/A', last_name='N/A', birth_date='N/A', university='N/A', course='N/A'):
        super().__init__(first_name, last_name, birth_date)
        self.university = university
        self.course = course

    def set_university(self, university):
        if Person.validate(self, university) == True:
            self.university = university.lower()
        else:
            raise TypeError ("Class is working with strings only")

    def set_course(self, course):
        if Person.validate(self, course) == True:
            self.course = course.lower()
        else:
            raise TypeError ("Class is working with strings only")


class Teacher(Student):

    def __init__(self, first_name='N/A', last_name='N/A', birth_date='N/A', university='N/A', course='N/A', salary='N/A'):
        super().__init__(first_name, last_name, birth_date, university, course)
        self.salary = salary

    def set_salary(self, salary):
        if Person.validate(self, salary) == True:
            self.salary = salary.lower()
        else:
            raise TypeError ("Class is working with strings only")
