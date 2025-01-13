# 81. Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# 82. Class Circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(7)
print("Area:", circle.area())
print("Circumference:", circle.circumference())

# 83. Class BankAccount
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")

    def check_balance(self):
        return self.balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

# 84. Class Student
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Alice", "S123", [85, 90, 78])
print("Average Grade:", student.average_grade())

# 85. Class Car and Inheritance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(f"{electric_car.make} {electric_car.model}, Battery: {electric_car.battery_size} kWh")

# 86. Class ComplexNumber
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)

# 87. Class Point
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point(1, 2)
point2 = Point(4, 6)
print("Distance:", point1.distance(point2))

# 88. Classmethod and Staticmethod
class MyClass:
    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print("This is a class method.")

    @staticmethod
    def static_method():
        print("This is a static method.")

obj = MyClass()
obj.instance_method()
MyClass.class_method()
MyClass.static_method()

# 89. Property Decorators
class PropertyExample:
    def __init__(self):
        self._attribute = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        if value > 0:
            self._attribute = value
        else:
            print("Value must be positive!")

obj = PropertyExample()
obj.attribute = 10
print("Attribute:", obj.attribute)
obj.attribute = -5  # Invalid value

# 90. Class Employee with Inheritance
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

manager = Manager("John", "M001", 80000, "Sales")
manager.display_details()
