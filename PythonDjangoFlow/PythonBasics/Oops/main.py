# What is OOP?

# Object-Oriented Programming is a programming paradigm based on objects.

# Real-life example:

# Car → Object


# Car blueprint → Class



# Driving → Method


# Color, model → Attributes

# 🔹 Classes & Objects

# class Car:
#     def start(self):
#         print("Car has started")

# my_car = Car()
# my_car.start()




# Explanation:


# Car → Blueprint



# my_car → Object (instance)



# start() → Behavior (method)



# 🔹 Constructor (__init__)

# Constructor initializes object data.

# Real-life example:
# When you buy a car, you assign color, model, engine type.

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display(self):
#         print(f"{self.brand} car in {self.color} color")

# car1 = Car("BMW", "Black")
# car1.display()





# 🔹 Encapsulation

# Encapsulation = Restricting access to data.

# Real-life example:

# ATM machine hides internal processing.

# You only use interface (withdraw, deposit).

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # Private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())
# 🔹 __balance cannot be accessed directly.







# 2️⃣ Inheritance & Polymorphism
# 🔹 Inheritance

# Inheritance = Child class inherits Parent class features.

# Real-life example:

# Animal → Parent

# Dog → Child

# Cat → Child

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.eat()
# d.bark()












# 🔹 Method Overriding (Polymorphism)

# Same method, different behavior.

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.sound()










# 🔹 Output changes based on object type.

# 🔹 Multiple Inheritance
# class Father:
#     def skills(self):
#         print("Gardening")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()








# Python uses MRO (Method Resolution Order).

# Check with:

# print(Child.__mro__)














# 3️⃣ Advanced OOP
# 🔹 Abstract Classes (Using ABC)

# Used when you want to force child classes to implement methods.

# Real-life example:
# Payment system:

# Every payment must implement pay() method.

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")

# p = CreditCardPayment()
# p.pay(500)





















# 🔹 Composition (HAS-A relationship)

# Preferred over inheritance in many real systems.

# Real-life example:
# Car HAS-A Engine.

# class Engine:
#     def start(self):
#         print("Engine started")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def drive(self):
#         self.engine.start()
#         print("Car is moving")

# c = Car()
# c.drive()





















# 4️⃣ Operator Overloading

# Python allows redefining operators.

# Real-life example:
# Adding two bank accounts means combining balances.

# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def __add__(self, other):
#         return Account(self.balance + other.balance)

#     def __str__(self):
#         return f"Balance: {self.balance}"

# a1 = Account(1000)
# a2 = Account(2000)

# a3 = a1 + a2
# print(a3)


# Common Magic Methods:

# __add__

# __sub__

# __str__

# __eq__

























# 5️⃣ Decorators

# Decorator = Function that modifies another function.

# 🔹 @property

# Used to create getter method like attribute.

# class Employee:
#     def __init__(self, salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary

# emp = Employee(50000)
# print(emp.salary)
















# 🔹 @staticmethod & @classmethod
# class Company:

#     company_name = "TechCorp"

#     @staticmethod
#     def greet():
#         print("Welcome to company")

#     @classmethod
#     def get_company_name(cls):
#         return cls.company_name

# Company.greet()
# print(Company.get_company_name())














# Difference:

# Type	Access to
# instance method	self
# class method	cls
# static method	nothing













# 🔹 Custom Decorator (Logging Example)
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper





# @logger
# def add(a, b):
#     return a + b

# print(add(5, 3))


# Real-life use:

# Logging

# Authentication

# Performance measurement




















# 6️⃣ Python Internals
# 🔹 Mutable vs Immutable
# Immutable (Cannot change)

# int

# float

# string

# tuple

# a = 10
# b = a
# b = 20

# print(a)  # 10

# Mutable (Can change)

# list

# dict

# set

# x = [1, 2]
# y = x
# y.append(3)

# print(x)  # [1, 2, 3]

















# 🔹 Memory Model & References

# Everything in Python is an object.

# a = 100
# b = 100

# print(id(a))
# print(id(b))


# # Small integers are cached.




















# 🔹 Passing Arguments (Object Reference)
# def modify(data):
#     data.append(10)

# lst = [1, 2, 3]
# modify(lst)

# print(lst)


# # Python uses pass-by-object-reference.