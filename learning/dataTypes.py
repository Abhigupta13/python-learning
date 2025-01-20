# Integer (int): Whole numbers, positive or negative, without decimals
age = 25
print("Integer Example:")
print(age)  # Output: 25
print(type(age))  # Output: <class 'int'>

# Float: Numbers with decimal points
price = 99.99
print("\nFloat Example:")
print(price)  # Output: 99.99
print(type(price))  # Output: <class 'float'>

# String (str): Sequence of characters enclosed in quotes
name = "Abhishek"
greeting = 'Hello, World!'
print("\nString Example:")
print(name)  # Output: Abhishek
print(type(name))  # Output: <class 'str'>

# List: Ordered, mutable collection of items (can hold mixed data types)
fruits = ["apple", "banana", "cherry"]
print("\nList Example:")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>
print(fruits[0])  # Accessing first element: Output: apple

# Tuple: Ordered, immutable collection of items
coordinates = (10.0, 20.0)
print("\nTuple Example:")
print(coordinates)  # Output: (10.0, 20.0)
print(type(coordinates))  # Output: <class 'tuple'>

# Dictionary (dict): Unordered collection of key-value pairs
student = {"name": "Abhishek", "age": 25, "skills": ["Python", "Django"]}
print("\nDictionary Example:")
print(student)  # Output: {'name': 'Abhishek', 'age': 25, 'skills': ['Python', 'Django']}
print(type(student))  # Output: <class 'dict'}
print(student["name"])  # Accessing value by key: Output: Abhishek

# Set: Unordered, mutable collection of unique items
unique_numbers = {1, 2, 3, 3, 4}
print("\nSet Example:")
print(unique_numbers)  # Output: {1, 2, 3, 4} (duplicates removed)
print(type(unique_numbers))  # Output: <class 'set'>

# Boolean (bool): Represents True or False values
is_active = True
print("\nBoolean Example:")
print(is_active)  # Output: True
print(type(is_active))  # Output: <class 'bool'>

# NoneType: Represents the absence of a value or null
nothing = None
print("\nNoneType Example:")
print(nothing)  # Output: None
print(type(nothing))  # Output: <class 'NoneType'>
