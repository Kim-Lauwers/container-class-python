class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def printname(self):
        print("Person", self._first_name, self._last_name)


class Student(Person):

    def printname(self):
        print("Student", self._first_name, self._last_name)


person = Person("Frank", "Stein")
person.printname()

student = Student("Frank", "Stein")
student.printname()
