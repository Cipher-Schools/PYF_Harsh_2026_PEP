#variables and datatypes

# Variable creation
name = "Rahul"        # string
age = 21              # integer
height = 5.8          # float
is_student = True     # boolean

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Checking data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


#input/output

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)

#if else and elif 
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

#loops in python

print("Loop Example:")

for i in range(1, 11):

    if i == 5:
        continue   # skip number 5

    if i == 9:
        break      # stop loop at 9

    print(i)


#functions in python

# Function definition
def add(a, b):
    return a + b     # returning result

result = add(10, 20)
print("Addition:", result)

# Lambda function 
square = lambda x: x * x
print("Square of 4:", square(4))

#data structures in python

# List (mutable)
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[1:4])   # slicing

numbers.append(60)
print(numbers)

# Tuple (immutable)
names = ("Rahul", "Aman", "Rohit")
print(names)

# Set (unique values)
unique_numbers = {1, 2, 2, 3, 4}
print(unique_numbers)

# Dictionary (key-value)
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])


#string manipulation and file handling
text = "python is easy"

print(text.upper())
print(text.capitalize())
print(text.replace("easy", "awesome"))

file = open("data.txt", "w")
file.write("Hello Rahul, welcome to Python")
file.close()


file = open("data.txt", "r")
print(file.read())
file.close()


#Exception handling 

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter a valid number")

finally:
    print("Exception handling completed")

# Custom exception
age = int(input("Enter age for voting: "))

if age < 18:
    raise Exception("Not eligible for voting")
else:
    print("Eligible for voting")