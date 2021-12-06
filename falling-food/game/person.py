class Person:
    def __init__(self):
        self._first_name = ""
        self._last_name = ""

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):    
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

class Student(Person):
    def __init__(self):
        self._gpa = 0.0

    def set_gpa(self, gpa):
        self._gpa = gpa

    def get_gpa(self):
        return self._gpa

person1 = Student()
person1.set_first_name('Blake')
person1.set_last_name('Mickelsen')
person1.set_gpa(4.0)

person2 = Student()
person2.set_first_name('Courtney')
person2.set_last_name('Mickelsen')
person2.set_gpa(3.2)

person3 = Student()
person3.set_first_name('Mallory')
person3.set_last_name('Lamoreaux')
person3.set_gpa(3.8)

people = []

people.append(person1)
people.append(person2)
people.append(person3)

for p in people:
    print(f"{p.get_first_name()} {p.get_last_name()}: {p.get_gpa()}")
    