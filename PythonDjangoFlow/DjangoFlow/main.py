# Step 1: Confirm Django is installed

# Run: in bash

# * python -m pip install django


# python -m django --version




#  Step 2
#  USE THIS INSTEAD:

#  python -m django startproject projectname


#    This bypasses PATH completely.







#   Step 3: Enter project folder
#     cd backend
#   ls


#   You must see:

#         manage.py
#         backend/ -ctrl+ click on folder







#  Step 4

# Open browser:

#   http://127.0.0.1:8000/


#   Django success page = DONE










#   CREATE TASK APP + ORM MODELS

#  Step 1.1: Create app

#  In terminal (VS Code / Git Bash):

#     python manage.py startapp tasks


#   Folder structure now:

#  backend/
#  ├── backend/
#  ├── tasks/
#  │   ├── models.py
#  │   ├── views.py
#  │   └── apps.py
#  └── manage.py











#    Step 1.2: Register app

#    Open:

#    backend/settings.py


#    Add tasks at bottom of INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tasks',   # 👈 our app
]











#    Step 1.3: Create ORM Model (TABLE)

#   Open:

#   tasks/models.py


#  Add

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


    # Django    	   Database
   #  Task	            table
   # title	            column
#BooleanField	        boolean
#auto_now_add	   created timestamp








#  Step 1.4: Create table in DB (SQLite)
  
  # In Terminal 

#  python manage.py makemigrations tasks
#  python manage.py migrate
#  python manage.py showmigrations


#   Table created in db.sqlite3















#   2️⃣ BUILD REST APIs (CRUD)
# Step 2.1: Create serializer (DTO)

#   Create file:

#   tasks/serializers.py


#    Add:

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'









#  Step 2.2: Enable REST Framework

#  Open:

#  backend/settings.py


#  Add:

INSTALLED_APPS += ['rest_framework']

















#  Step 2.3: Create API Views

#   Open:

#   tasks/views.py


#   Replace everything with:

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer





# CREATE TASK
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)





# READ TASKS
@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)






#UPDATE TASK
@api_view(['PUT'])
def update_task(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)








# DELETE TASK
@api_view(['DELETE'])
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return Response({"message": "Deleted"})








#    Step 2.4: URL Mapping

 #     Create file:

#     tasks/urls.py


#         Add:

from django.urls import path
from .views import create_task, list_tasks, update_task, delete_task

urlpatterns = [
    path('tasks/', list_tasks),
    path('tasks/create/', create_task),
    path('tasks/update/<int:id>/', update_task),
    path('tasks/delete/<int:id>/', delete_task),
]





#    backend/urls.py
 #    Replace with:

from django.urls import path, include

urlpatterns = [
    path('api/', include('tasks.urls')),
]














    #  Step 2.5: Run Server

#   python manage.py runserver











#   Step 2.6: Test APIs (Postman / Thunder Client)


#  CREATE


 #   POST http://127.0.0.1:8000/api/tasks/create/


#Body (JSON):

{
  "title": "Learn Django",
  "completed": false
}



#  READ
#GET http://127.0.0.1:8000/api/tasks/



# UPDATE90
#PUT http://127.0.0.1:8000/api/tasks/update/1/




#  DELETE
#DELETE http://127.0.0.1:8000/api/tasks/delete/1/



# Full CRUD API working
#  CURRENT STATUS

#  ✔ App created
#  ✔ ORM model
#  ✔ SQLite DB
#  ✔ REST CRUD APIs























#   4️⃣ API OPTIMIZATION
#   Pagination, Filtering, Ordering, Search
#   WHY API OPTIMIZATION IS NEEDED (REAL LIFE)

#   Imagine:

#   1,00,000 tasks in DB

#   Mobile app calls /tasks0

#   Backend sends all tasks at once ❌

#   ❌ Slow
#   ❌ Memory waste
#   ❌ Bad UX

#   ✅ Solution:

#   Pagination (send small chunks)

#   Filtering (only required data)

#    Ordering & Search












# STEP 4.1: ENABLE PAGINATION (GLOBAL)

# Open:

# In backend/settings.py


#  Add at bottom:

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
}







INSTALLED_APPS += ['django_filters']








#   Change this


@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)




# with this 


# Add this in import(IN VIEWS)

from rest_framework import generics






# LIST TASKS (Now Optimized)
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Filtering
    filterset_fields = ['completed']

    # Ordering
    ordering_fields = ['created_at', 'title']

    # Searching
    search_fields = ['title']










   # UPDATE URLS

# Open:

#tasks/urls.py

# Replace:
from django.urls import path
from .views import create_task, update_task, delete_task, TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),   # 👈 updated
    path('tasks/create/', create_task),
    path('tasks/update/<int:id>/', update_task),
    path('tasks/delete/<int:id>/', delete_task),
]












# STEP 4.2: TEST PAGINATION (NO CODE CHANGE!)




# Run server:

# python manage.py runserver


#  Call API:

# GET http://127.0.0.1:8000/api/tasks/


Response:

{
  "count": 12,
  "next": "http://127.0.0.1:8000/api/tasks/?page=2",
  "previous": null,
  "results": [
    { "id": 1, "title": "Task 1" }
  ]
}


#  📌 This is REAL production-style response













# STEP 4.3: FILTERING (completed / not completed)

# Install django-filter (if not installed)
# python -m pip install django-filter

# Register in settings.py

INSTALLED_APPS += ['django_filters']

# Update View (IMPORTANT)

# Open:

# tasks/views.py


# Add imports:

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create new optimized view:

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']





# Update tasks/urls.py


from .views import TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
]










#  TEST FILTERING
#  GET /api/tasks/?completed=true
#  GET /api/tasks/?completed=false


#  Real life

#  “Show only completed tasks”















# STEP 4.4: ORDERING & SEARCH

# Add imports:

from rest_framework.filters import OrderingFilter, SearchFilter


# Update view:

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]

    filterset_fields = ['completed']
    ordering_fields = ['created_at', 'title']
    search_fields = ['title']

# TEST

# Search

#  /api/tasks/?search=django


#  Order

#   /api/tasks/?ordering=created_at
#   /api/tasks/?ordering=-created_at



















#  UNDERSTANDING FIRST (Very Important)

# Authentication = Who are you?


# Login system


# JWT token

# Session login


# Authorization = What are you allowed to do?


# Only admin can delete


# Only owner can update


# User cannot see others’ data




# 🚀 STEP 1 — Install JWT Package

# In VS Code terminal:

# python -m pip install djangorestframework-simplejwt







# 🚀 STEP 2 — Configure JWT

# Open:

# backend/settings.py

# Add inside INSTALLED_APPS (if not already):

# INSTALLED_APPS += ['rest_framework']







# Now update REST_FRAMEWORK:+


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),

#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),

#     'DEFAULT_PAGINATION_CLASS': 
#         'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 5,
# }


















# 👉 Now every API requires login by default.



# 🚀 STEP 3 — Add JWT URLs

# Open:

# backend/urls.py

# Add:

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('api/', include('tasks.urls')),

#     # JWT endpoints
#     path('api/token/', TokenObtainPairView.as_view()),
#     path('api/token/refresh/', TokenRefreshView.as_view()),
# ]
















# 🚀 STEP 4 — Create Superuser

# In VS Code terminal:

# python manage.py createsuperuser


# Enter:

# username

# email

# password

# Run server:

# python manage.py runserver










# 🚀 STEP 5 — Get JWT Token

# POST request:

# POST http://127.0.0.1:8000/api/token/


# Body:

# {
#   "username": "yourusername",
#   "password": "yourpassword"
# }


# Response:

# {
#   "refresh": "...",
#   "access": "..."
# }











#  Copy the access token.

#  STEP 6 — Use JWT in Requests (Thunder Client / Postman)

# Go to:

# Authorization tab
# Select:

# Bearer Token

# Paste:

# access_token_here


# Now call:

# GET /api/tasks/


# It will work.

# Without token → 401 Unauthorized ❌

















# Create User Registration API


# STEP 1: Create Serializer

# Create file:

# tasks/user_serializers.py

# Add:





# from django.contrib.auth.models import User
# from rest_framework import serializers

 class RegisterSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['username', 'password', 'email']
         extra_kwargs = {
             'password': {'write_only': True}
         }

     def create(self, validated_data):
         user = User.objects.create_user(
             username=validated_data['username'],
             password=validated_data['password'],
             email=validated_data['email']
         )
         return user

# STEP 2: Create Register View

# Open:

# tasks/views.py

# Add:

 from django.contrib.auth.models import User
 from .user_serializers import RegisterSerializer
 from rest_framework import generics
 from rest_framework.permissions import AllowAny

 class RegisterView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = RegisterSerializer
     permission_classes = [AllowAny]









# STEP 3: Add URL

# Open:

# tasks/urls.py

# Add:

 from .views import RegisterView

 urlpatterns += [
     path('register/', RegisterView.as_view()),
 ]














#  TEST REGISTRATION

# POST:

# http://127.0.0.1:8000/api/register/


# Body:

 {
   "username": "mohit",
   "password": "123456",
   "email": "mohit@email.com"
 }








# 🔐 PART 4: Login & Get JWT Token

# POST:

# http://127.0.0.1:8000/api/token/


# Body:

 {
   "username": "mohit",
   "password": "123456"
 }


# Response:





 {
   "access": "xxxxx",
   "refresh": "xxxxx"
 }







# 🔐 PART 5: Use Token

# In Postman:

# Authorization → Bearer Token → paste access token

# Now call:

# GET /api/tasks/












# Now secured ✅

#  Create User Registration API

#  We will create registration from code.

# Create: tasks/serializers.py

#  Add below TaskSerializer:

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

#  Create Register View

Open:

tasks/views.py

Add:

from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User created successfully"}, status=201)







#  Update tasks/urls.py


from .views import register_user

urlpatterns = [
    path('register/', register_user),
    path('tasks/', TaskListView.as_view()),
]

# TEST REGISTRATION

# POST

http://127.0.0.1:8000/api/register/


# Body:

{
  "username": "rohan",
  "email": "rohan@gmail.com",
  "password": "StrongPassword123"
}



# JWT Login

# POST:

http://127.0.0.1:8000/api/token/


#Body:

{
  "username": "rohan",
  "password": "StrongPassword123"
}


# Response:

{
  "access": "JWT_TOKEN",
  "refresh": "REFRESH_TOKEN"
}

# : Use JWT Token



#  Role-Based Access Control (RBAC)

#  We will create roles:

#  ADMIN

#  MANAGER

#  USER






#  We will use Django Groups (from code, not admin panel).

# Create Roles Automatically

#  Open tasks/apps.py

# Modify:

from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from django.contrib.auth.models import Group
        Group.objects.get_or_create(name='ADMIN')
        Group.objects.get_or_create(name='MANAGER')
        Group.objects.get_or_create(name='USER')











#  Assign Role During Registration

#  Update RegisterSerializer:

from django.contrib.auth.models import Group

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.pop('role')

        user = User.objects.create_user(**validated_data)

        group = Group.objects.get(name=role.upper())
        user.groups.add(group)

        return user
    





# Now register like:

{
  "username": "manager1",
  "email": "m@gmail.com",
  "password": "Password123",
  "role": "manager"
}



#  Custom Role Permission

# Create custom permission.







# Create file:

#  tasks/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(
            name__in=['ADMIN', 'MANAGER']
        ).exists()
    




# Apply Permission to Create Task

#  Open tasks/views.py

#  Modify create_task:

from .permissions import IsAdminOrManager

@api_view(['POST'])
@permission_classes([IsAdminOrManager])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)








#  Now:

# Role	Can Create Task?
# ADMIN	✅
# MANAGER	✅
# USER	❌




















# Why Async Matters in Django

# Web apps spend most time:

# Waiting for database

# Waiting for external APIs

# Waiting for file I/O

# Waiting for network




# Async helps when:

# ✔ You are waiting
# ❌ Not when doing heavy CPU work





# ⚙️  How Django Works Normally

# Django was traditionally synchronous.

# Example:

# def home(request):
#     data = User.objects.all()
#     return JsonResponse({"count": data.count()})







# This blocks until query finishes.





#  3️⃣ Async in Django (Django 3.1+)

# Django supports async views using:

# async def

#  Basic Async View Example
# import asyncio
# from django.http import JsonResponse

# async def test_async(request):
#     await asyncio.sleep(3)
#     return JsonResponse({"message": "Done"})






# Now:

# Server does not block

# Other requests can be handled





#  What is await?

# await means:

# Pause this function, but don’t block the entire server.

# 🧠 Important Rule

# You can only use await inside:

# async def function():

# 🧩  Real Example — Calling External API





# Imagine Mini LMS:

# You want to verify assignment plagiarism using external API.

# ❌ Sync Version
# import requests

# def check_plagiarism(request):
#     response = requests.get("https://api.example.com/check")
#     return JsonResponse(response.json())






# ⚠️ Problem: requests blocks server.

# ✅ Async Version
# import httpx
# from django.http import JsonResponse

# async def check_plagiarism(request):
#     async with httpx.AsyncClient() as client:
#         response = await client.get("https://api.example.com/check")
#     return JsonResponse(response.json())






# Now:

# While waiting for API

# Server handles other users



#   Async Database in Django

# ⚠ Very Important:

# Django ORM is still mostly synchronous.

# This will block:

# users = User.objects.all()

# Solution: Use sync_to_async
# from asgiref.sync import sync_to_async
# from django.contrib.auth.models import User

# async def get_users(request):
#     users = await sync_to_async(list)(User.objects.all())
#     return JsonResponse({"count": len(users)})





# 🎓 Real-Life LMS Example

# Imagine:

# 500 students submit assignments

# Each submission checks plagiarism API

# Without async → server slows down

# With async → multiple API calls handled eff   iciently





# 🔥  Async vs Sync Comparison
# Feature	Sync	Async
# Handles multiple users	Limited	Better
# Good for API calls	❌	✅
# Good for CPU heavy work	✅	❌
# Code complexity	Simple	Slightly advanced








#   When NOT to Use Async

# Do NOT use async for:

# Heavy calculations

# Image processing

# ML model training

# CPU intensive tasks

# For that → use:

# Celery

# Background workers




#  Multiple Tasks Example
# import asyncio

# async def task1():
#     await asyncio.sleep(2)
#     return "Task 1 done"

# async def task2():
#     await asyncio.sleep(3)
#     return "Task 2 done"

# async def main():
#     results = await asyncio.gather(task1(), task2())
#     print(results)


# Output after 3 seconds:

# ["Task 1 done", "Task 2 done"]


# Instead of 5 seconds 




# Sync = One person cooking one dish at a time
# Async = One chef managing multiple dishes while they cook




























# First: What is Redis?
#  Simple Definition

# Redis is an in-memory data store used as a cache to make applications faster.



# Very important:


# 👉 Redis stores data in RAM, not on disk.
# 👉 RAM is much faster than database queries.

# 🏫 Real-Life Example 1 — Library 📚





# Imagine:

# You ask librarian for a book.

# ❌ Without Cache

# Librarian goes to storage room

# Searches shelf

# Brings book

# Every time you ask → same process

# Slow 🐢

# ✅ With Cache

# If 10 students ask same book:

# Librarian keeps book on desk

# Next student → instantly gives it

# Fast 🚀

# Redis = The desk
# Database = The storage room






# 🖥️ Real-Life Example 2 — E-commerce Website

# Imagine:

# Homepage shows:

# Top 10 products

# Best sellers

# Categories

# If 10,000 users visit homepage:

# Without cache:

# Database queried 10,000 times 😨

# With Redis:

# Query once

# Store result in Redis

# Serve from memory

# Huge performance boost 







# ⚡ Why Redis is Fast?

# Because:

# Database → disk-based (slower)

# Redis → RAM-based (very fast)

# RAM speed ≈ nanoseconds
# Disk speed ≈ milliseconds

# That’s 100x+ faster.




#  What is Caching?

# Caching means storing frequently used data temporarily in fast storage.



# 🎯 What Should Be Cached?

# Good candidates:

# Homepage data

# Leaderboards

# Dashboard stats

# Course list

# Frequently accessed API responses

# Not good for:

# Rarely used data

# Highly dynamic data (changes every second)



# 🔥 Basic Redis Working Flow

# 1️⃣ User requests data
# 2️⃣ Server checks Redis
# 3️⃣ If found → return instantly
# 4️⃣ If not found → fetch from DB
# 5️⃣ Store in Redis
# 6️⃣ Return response

#  Django Example Without Cache

 def course_list(request):
     courses = Course.objects.all()
     return JsonResponse({"courses": list(courses.values())})


# Every request → database hit.

# 🚀 Django Example With Redis Cache

# First install:

# pip install django-redis


# settings.py
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }



# View With Cache
# from django.core.cache import cache
# from django.http import JsonResponse
# from .models import Course

 def course_list(request):

     data = cache.get("course_list")

     if not data:
         courses = Course.objects.all()
         data = list(courses.values())
         cache.set("course_list", data, timeout=60)  # 60 seconds

#     return JsonResponse({"courses": data})

#  What Happens Now?

# First request:

# DB query

# Stored in Redis

# Next 60 seconds:

# No DB query

# Served from Redis

#  Faster response
#  Reduced DB load

# 📊 Performance Comparison
# Without Redis	With Redis
# 1000 DB queries	1 DB query
# High CPU usage	Low CPU
# Slow response	Very fast
# DB overload risk	Stable
# 🏫 LMS Real-Life Example

# Imagine your Mini LMS:

# 2000 students

# Everyone loads dashboard at 9 AM

# Dashboard shows:

# Total students

# Total courses

# Total submissions

# Without Redis:

# 2000 DB calculations 😨

# With Redis:

# Calculate once

# Store in cache

# Serve 2000 users instantly



#  Redis Use Cases in Real World

# Instagram timeline

# Netflix recommendations

# Uber ride matching

# E-commerce carts

# Session storage

# Rate limiting



#  Redis Can Also Be Used For:

# Not just cache:

# Message broker (Celery)

# Real-time chat

# Pub/Sub

# Leaderboards

# Session storage



#  Cache Expiry (Important Concept)
# cache.set("key", value, timeout=300)


# After 5 minutes → auto deleted.

# Why?

# Because cached data can become outdated.

#  Cache Invalidation (Very Important)

# If data changes:

# Example:

# New course created

# You must clear cache:

# cache.delete("course_list")


# Otherwise users see old data.







# Redis vs Database


# Database	         Redis
# Persistent	  Mostly temporary
# Disk storage	  Memory storage
# Complex queries  	Key-value
# Slower	        Extremely fast




# Redis is like keeping frequently used answers in your brain
# Instead of checking the book every time.