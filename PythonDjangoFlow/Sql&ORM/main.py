# Every backend system depends on:

# Data storage

# Efficient retrieval

# Relationships

# Performance

# Scalability

# Real-world systems:

# Banking system

# E-commerce (Amazon)

# Social media (Instagram)

# Task management systems

# All rely heavily on database design + query optimization.










# 1️⃣ SQL Fundamentals (Deep Understanding)
#  What is a Relational Database?

# A relational database stores data in tables.

# Each table:

# Rows → Records

# Columns → Fields




# Example:
# Users table:

# id	name	email
# 🔹 Creating Tables (Real Example: E-commerce)
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );



# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER REFERENCES users(id),
#     total_amount DECIMAL(10,2),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );


# Here:

# user_id → Foreign Key

# Ensures referential integrity










# 🔹 Joins (Real-life Scenario)

# Problem:
# Show all orders with user name.

# SELECT users.name, orders.total_amount
# FROM orders
# JOIN users ON users.id = orders.user_id;







# Types of Joins:
# 1. INNER JOIN

# Returns matching records only.





# 2. LEFT JOIN

# Returns all left records + matched right.

# Example:
# Show all users even if no orders.

# SELECT users.name, orders.total_amount
# FROM users
# LEFT JOIN orders ON users.id = orders.user_id;








# 🔹 Indexing (Performance Optimization)

# Imagine:

# 10 million users

# Searching by email

# Without index → Full table scan
# With index → B-tree lookup

# CREATE INDEX idx_email ON users(email);

# When to use index?

# Frequently searched columns

# Foreign keys

# WHERE conditions

# When NOT to overuse?

# Small tables

# Columns frequently updated












# 🔹 Normalization (Database Cleanliness)
# 1NF

# No repeating groups.

# Bad:

# user	phones
# John	123,456

# Good:
# Separate phone table.





# 2NF

# No partial dependency.






# 3NF

# No transitive dependency.





# Bad:
# User → Zip → City





# Good:
# Separate city table.







# 2️⃣ Python + SQL (Real Implementation)
# 🔹 sqlite3 Example (Local App)




# Use case:
# Small desktop app or internal tool.

# import sqlite3

# conn = sqlite3.connect("app.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     email TEXT
# )
# """)

# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
#                ("Basant", "basant@gmail.com"))

# conn.commit()




# 🔹 Fetching Data
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)















# 🔹 PostgreSQL (Production Use)

# Used in:

# Startups

# Enterprise systems

# Django apps

# import psycopg2

# conn = psycopg2.connect(
#     dbname="ecommerce",
#     user="postgres",
#     password="password",
#     host="localhost"
# )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
























# 3️⃣ ORM Basics (Deep Concept)
#  What is ORM?

# ORM maps:

# Python class → Database table
# Object → Row





# 🔹 Without ORM

# You write SQL manually.







# 🔹 With ORM

# You write Python.






# 🔹 Django ORM Example (Real-life)
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)










# Create user:

# User.objects.create(name="Mohit", email="mohit@gmail.com")


# Fetch all users:

# users = User.objects.all()


# Filter:

# User.objects.filter(name="mohit")







# 4 Django ORM Advanced
#  The N+1 Problem (Very Important for Interviews)



# Problem:

# orders = Order.objects.all()

# for order in orders:
#     print(order.user.name)




# This triggers:

# 1 query for orders

# N queries for users

# Total → N+1 queries

# ✅ Solution: select_related
# orders = Order.objects.select_related('user').all()








# Now only 1 JOIN query.


# 🔹 prefetch_related (Many-to-Many)
# users = User.objects.prefetch_related('orders').all()







# Optimized query using separate query + in-memory mapping.








# 🔹 annotate (Computed Field)

# Count number of orders per user:

# from django.db.models import Count

# users = User.objects.annotate(order_count=Count('order'))










# 🔹 aggregate (Global Calculation)
# from django.db.models import Avg

# avg_age = User.objects.aggregate(Avg('age'))










# 5️⃣ Query Optimization (Production Thinking)
# 🔹 Avoid SELECT *

# Bad:

# SELECT * FROM users;


# Good:

# SELECT name, email FROM users;














# 🔹 Use EXPLAIN
# EXPLAIN ANALYZE
# SELECT * FROM users WHERE email='basant@gmail.com';


# Check:

# Sequential scan?

# Index scan?

# Cost?










# 🔹 Use Proper Data Types

# Bad:

# Store date as VARCHAR

# Good:

# Use DATE or TIMESTAMP








# 6️⃣ Schema Design (Architecture Thinking)
# 🔹 One-to-Many

# User → Orders

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



# 🔹 Many-to-Many

# Students ↔ Courses

# class Student(models.Model):
#     courses = models.ManyToManyField("Course")




# 🔹 Constraints
# email VARCHAR(100) UNIQUE NOT NULL


# Constraints ensure:

# Data integrity

# No duplicates

# Valid relationships