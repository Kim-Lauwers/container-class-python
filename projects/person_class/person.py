class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def hello(self):
        print("Hello my name is " + self._name)


person = Person("Jan", 39)
person.hello()
