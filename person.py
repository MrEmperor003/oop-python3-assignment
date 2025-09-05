import datetime
print("{1},{},{}".format("name",25, "Male"))
year = datetime.date.today().year
name  = input("Enter your name: ")
age = int(input("Enter year of birth: "))
age = year - age
print()
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def say_hi(self):
        print(f"hello, my name is, {self.name} and i am {self.age} years old")
p1 = person(name, age)
p1.say_hi()