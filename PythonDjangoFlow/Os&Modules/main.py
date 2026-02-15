# Built-in Modules

# Python provides powerful built-in modules to solve real-world problems efficiently.





# 🔹 datetime Module

# Used for handling date and time.






# 📌 Real-life Example:

# Calculate age from date of birth

# Calculate days remaining for deadline

# from datetime import datetime, timedelta

# today = datetime.now()
# print("Current Date & Time:", today)

# # Calculate future date
# future = today + timedelta(days=10)
# print("After 10 days:", future)









# 📌 Calculate Age
# from datetime import datetime

# dob = datetime(1998, 5, 20)
# today = datetime.now()

# age = today.year - dob.year
# print("Age:", age)








# 🔹 math Module

# Used for mathematical operations.

# import math

# print("Square root:", math.sqrt(25))
# print("Power:", math.pow(2, 3))
# print("Ceil:", math.ceil(4.3))
# print("Floor:", math.floor(4.8))
# print("Pi:", math.pi)

# Real-life Example:

# Loan EMI calculation requires power and math functions.











# 🔹 random Module

# Used for generating random values.

# import random

# print("Random number:", random.randint(1, 10))
# print("Random choice:", random.choice(["Apple", "Banana", "Mango"]))

# Real-life Example:

# OTP generation

# Lottery system

# Game dice

# otp = random.randint(1000, 9999)
# print("Generated OTP:", otp)

















# 🔹 collections Module

# Advanced data structures.

# Counter
# from collections import Counter

# data = ["apple", "banana", "apple", "orange"]
# count = Counter(data)

# print(count)

# Real-life Example:

# Count word frequency in a sentence.



















# 2️⃣ OS & Sys Module

# Used for interacting with system and operating system.







# 🔹 os Module
# File Path Handling
# import os

# print("Current Working Directory:", os.getcwd())

# file_path = os.path.join("folder", "file.txt")
# print(file_path)

# Create Folder
# os.mkdir("new_folder")








# 🔹 sys Module

# Used to interact with Python runtime.

# import sys

# print("Python Version:", sys.version)
# print("Command Line Arguments:", sys.argv)

# Real-life Example:

# Creating a script that takes user input from command line.

# import sys

# name = sys.argv[1]
# print(f"Hello {name}")


# Run:

# python script.py Basant

















# 3️⃣ Regular Expressions (re)

# Used for pattern matching and validation.

# 🔹 Email Validation
# import re

# email = "test@gmail.com"

# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")













# 🔹 Extract Phone Numbers
# text = "Call me at 9876543210"

# numbers = re.findall(r'\d{10}', text)
# print(numbers)

# Real-life Uses:

# Form validation

# Password validation

# Log file analysis

# Data scraping














# 4️⃣ Problem Solving

# Focus: Logical thinking + data constraints





# 🔹 Problem 1: Find Duplicate Elements
# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()

#     for num in lst:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)

#     return list(duplicates)

# print(find_duplicates([1,2,3,2,4,1]))







# 🔹 Problem 2: Count Word Frequency
# from collections import Counter

# sentence = "python is powerful and python is easy"
# words = sentence.split()

# frequency = Counter(words)
# print(frequency)














# 🔹 Problem 3: Check Palindrome
# def is_palindrome(text):
#     return text == text[::-1]

# print(is_palindrome("madam"))









# 🔹 Problem 4: Validate Strong Password
# import re

 # def validate_password(password):
  #    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    #  return bool(re.match(pattern, password))

# print(validate_password("Test@123"))