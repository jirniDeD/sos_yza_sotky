from Tools.scripts.generate_sre_constants import sre_constants_header


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hell(self):
        print(f"Hello!My name is {self.name}")


    def get_info(self):
        return f"{self.name};{self.age}"


vasya = Student("vasya", 15)
petya = Student("petya", 17)
anna = Student("anna", 111)
print(vasya)
print(vasya.age, vasya.name)
print(petya.age, petya.name)
print(anna.age, anna.name)
vasya.say_hell()
print(vasya.get_info())

del vasya