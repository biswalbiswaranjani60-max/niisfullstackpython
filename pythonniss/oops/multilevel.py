class Person:
    def display_person(self):
        print("This is a Person")
class Student(Person):
    def display_student(self):
        print("This is a Student")
class Engineering(Student):
    def display_engineering(self):
        print("This is an Engineering Student")
e=Engineering()
e.display_person()
e.display_student()
e.display_engineering()