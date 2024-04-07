![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

<div align="left">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/947b9e01-1805-49b2-8aaa-5933bbd2611e" alt="Badge" width="150">
</div>

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/0e22e41e-90f5-4ca5-a23f-0b980a1b42a6" alt="Badge" width="150">
</div>

# What is DIO?

DIO is a Brazilian education platform that offers training in various IT areas. Besides courses of various levels, the platform also encourages its community of students and professionals to share knowledge from their study and work routines. With a gamified approach, you can enrich your internal profile with various code challenges, project challenges, and other activities, which, over time, add up to strengthen your professional profile, since the platform brings together a network of recruiters in partnership with DIO, who have access to various profiles of the best and most competent candidates.

# Training Details

Python is one of the most used programming languages in both the national and international markets. It's one of the main technologies used by companies such as Globo, Instagram, Amazon, and Google.

With its great versatility, extensive documentation, and numerous libraries, Python is the first choice in the data field. However, Python is not limited to data; it can also be applied to games, web applications, task automation, and much more! Learn from scratch the basic syntax of the language up to integrations with APIs and practical projects exploring the main frameworks like Flask and Django.

Model your database with Sqlalchemy tools and create even richer applications with data persistence using MongoDB and the Pymongo library.

**Total Course Hours: 64 hours**

# About the Instructor

Guilherme Carvalho has 9 years of experience as a Backend Developer in Python and Java.

# Introduction to Python

Python was born in 1989 as a hobby of the programmer Guido Van Rossum. The initial idea was to continue the ABC language, which was developed by the Dutch Research Center (CWI).

Python was influenced by ABC, which was a language designed for beginners, because of its ease of learning and use.

Van Rossum's goals for the Python language were:

- An easy and intuitive language
- Open source, so everyone could contribute
- Code as intelligible as English.
- Suitable for daily tasks and productive

In 1995, Van Rossum released version `1.2`, while still working at CWI. After ending the link with the research center, he and the main Python development team moved to *BeOpen.com*, thus born the **BeOpen Python Labs**.

In October 2000, version `2.0` of Python is published. In this version, **List Comprehensions** are born and an improvement in the garbage collector for the removal of cyclic references.

In 2001, the Python Software Foundation (PSF) was born, which, from Python `2.1`, owns all the code, documentation, and specifications of the language.

In 2008, version `3.0` is launched. This version solved many design problems of the language and improved performance. Some changes were very profound, which made version `3.x` not backward compatible.

Currently, we are at version `3.12.2` (I updated, but for the original course, the instructor had said that the most current was `3.10.2`).

## Why and Where to Use Python?

Python is a very versatile language, see some characteristics:

- Dynamic and strong typing
- Cross-platform and multi-paradigm
- Huge and active community
- Low learning curve

**Note**: Python is not recommended for mobile development. Although there are some frameworks, they are not as good, since Python itself does not perform well in a mobile environment, therefore, it is much better to use other more established languages for mobile environments.

# "The Recipe"

Programming consists of telling the computer a sequence of routines that should be processed. Imagine a cake recipe; we need to know the ingredients and the preparation method. By correctly following the instructions, at the end of the process, we will have a cake ready.

## Creating our file

To create our "cake recipe" in Python, we need to create a file with the `py` extension. With the file created, we can insert our ingredients and the preparation method.

## The famous "Hello, World!"

As customary in many programming languages, our first "program" will be the "Hello, World!". Let's do it!

```python
print("Hello world!")
```

# Data Types

## What are data types?

Data types serve to define the characteristics and behaviors of a value (object) for the interpreter. For example:

The built-in data types are:

| Type      | Example        |
|-----------|----------------|
| Text      | str            |
| Numeric   | int, float, complex |
| Sequence  | list, tuple, range |
| Map       | dict           |
| Collection| set, frozenset |
| Boolean   | bool           |
| Binary    | bytes, bytearray, memoryview |

## Common and Basic Types

### Integers

Integers are represented by the `int` class and have unlimited precision. Valid examples of integers are: 1, 10, 100, -1, -10, -100...99001823

### Floating-point numbers

Floating-point numbers are used to represent rational numbers and their implementation is done by the `float` class. Valid examples of floating-point numbers are: 1.5, -10.543, 0.76...999278.002

### Boolean

It is used to represent "true" or "false" and is implemented by the `bool` class. In Python, the boolean type is a subclass of `int`, as any number other than 0 represents true and 0 represents false. Valid examples of booleans are: `True` and `False`

### Strings

Strings (or character chains) are used to represent alphanumeric values. In Python, strings are defined using the `str` class. Valid examples of string: "Python", 'Python', """Python""", "p"

### Testing in a New Code

Below is our new code to test what we learned above.
(I added the use of `type` to facilitate, it was not explained in the bootcamp training class).

```python
print(1 + 10)
print(type(1 + 10))

print(1.5 + 1 + 0.5)
print(type(1.5 + 1 + 0.5))

print(True)
print(type(True))

print("Python")
print(type("Python"))
```
# Using Interactive Mode

## What is interactive mode?

The Python interpreter can run in a mode that allows the developer to write code and see the result immediately.

## Starting interactive mode

There are two ways to start interactive mode:

- Calling just the interpreter (`python`)

- Running the script with the `-i` flag (`python -i app.py`)

# Functions dir and help

## dir

It is a function that, without arguments, returns the list of names in the current local scope. With an argument, it returns a list of valid attributes for the object. Examples:

```python
dir()

dir(100)
```

## help

Invokes the built-in help system. It is possible to search in interactive mode or inform by parameter the name of the module, function, class, method, or variable. Examples:

```python
help()

help(100)
```

# Variables and Constants

## Variables

In programming languages, we can define values that can be altered during the execution of the program. These values are called variables because they are initialized with a value and do not necessarily have to remain with the same value throughout the program's execution.

```python
# Using variables

age = 23
name = 'William'
print(f'My name is {name} and I am {age} year(s) old.')

age, name = (23, 'William')
print(f'My name is {name} and I am {age} year(s) old.')
```

## Changing values

Notice that we don't need to define the data type of the variable in Python, as the language does this automatically for us. That's why we can't simply create a variable without assigning a value. To change the value of the variable, you just need to assign a new value to it.

```python
# Using variables

age = 23
name = 'William'
print(f'My name is {name} and I am {age} year(s) old.')

age, name = (23, 'William')
print(f'My name is {name} and I am {age} year(s) old.')

# Changing the values of variables

age = 23
name = 'William'
print(f'My name is {name} and I am {age} year(s) old.')
print(age, name)

age = 27
name = 'Giovanna'
print(f'My name is {name} and I am {age} year(s) old.')
print(age, name)
```

`Output`

```
My name is William and I am 23 year(s) old.
My name is William and I am 23 year(s) old.
My name is William and I am 23 year(s) old.
23 William
My name is Giovanna and I am 27 year(s) old.
27 Giovanna
```

## Constants

Just like variables, constants are used to store values. A constant is born with a value and remains with it until the end of the program execution, meaning the value is immutable.

**Python does not have constants!**

There is no reserved keyword to inform the interpreter that the value is a constant. In some languages, such as Java and C, we use `final` and `const`, respectively, to declare a constant.

In Python, we use the convention that tells the programmer that the variable is a constant. **To do this, you should create the variable with the name all in uppercase letters.**

```python
# Properly creating a constant in Python (convention)

ABS_PATH = '/home/william/Documents/python_course'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2
```

## Best Practices

- The naming convention should be *snake case*

- Choose meaningful names

- Constants should be all uppercase

```python
# Best practices

# The naming convention should be *nake case
new_value = 2

# Choose meaningful names
student_name = 'Peter'
student_last_name = 'Parker'
student_grade = 9.8

# Constants should be all uppercase

ABS_PATH = '/home/william/Documents/python_course
```

# Type Conversion

Sometimes it will be necessary to convert the type of a variable to manipulate it differently. For example, a variable of type `string` stored numbers, but we need to perform some mathematical operation with this value, what to do? We should convert the value to numeric.

## Int to float


```python
# Int to float

price = 10
print(price)

price = float(price)
print(price)

price = 10 / 2
print(price)
print(type(price))
```

## Float to int

```python
# Float to int

price = 10.30
print(price)

price = int(price)
print(price)
print(type(price))
```

## Conversion by division

```python
# Int to float

price = 10
print(price)

price = float(price)
print(price)

price = 10 / 2
print(price)
print(type(price))

# Float to int

price = 10.30
print(price)

price = int(price)
print(price)
print(type(price))

# Conversion by division

price = 10
print(price)
print(type(price))

print(price / 2)
print(type(price))

""" Just commenting the above case, the instructor said it was a conversion by division; however, I used type() to check and prove that the
type remained integer. With that, I believe he may have based it solely on the appearance of the data. To be, in fact, a
float, there would have to be at least one float (it was a division of two integers). """

print(price // 2)
print(type(price))
```

## Number to String

```python
# Number to string

price = 10.50
age = 28
print(type(price))
print(type(age))

print(str(price))
print(str(age))
print(type(str(price)))
print(type(str(age)))

text = f"age {age} price {price}"
print(text)
print(type(text))
```

## String to Number

# String to number

```python
price = "10.50"
age = "28"

print(type(price))
print(type(age))

print(type(float(price)))
print(type(int(age)))
```

## Conversion Error

Occurs when a proper conversion is not possible (for example, converting a string that actually stores text, and not a number in text form, to numeric form).

```python
# Conversion Error

price = "python"
print(float(price))
```

`output`

```
>>> price = "python"
>>> print(float(price))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'python'
```
## Input and Output Functions

## input() Function

The **built-in** `input()` function is used when we want to read standard input data (e.g., from the keyboard). It takes a `string` argument, which is displayed to the user on the standard output (e.g., screen). The function reads the input, converts it to `string`, and returns the value.

## Displaying Values with the print() Function

The *built-in* `print()` function is used when we want to display data on the standard output (e.g., screen). It takes one mandatory *varargs* type argument of objects and 4 optional arguments (*sep, end, file*, and *flush*). All objects are converted to `string`, separated by `sep`, and terminated by `end`. The final `string` is displayed to the user.

```python
# Input function

name = input("Write your name: ")

# Print function

name = input("Write your name: ")
print(name)

# Print function using end and sep

name = input("Write your name: ")
age = input("Write your age: ")

print(name, age)
print(name, age, end=" ... \n")
print(name, age, sep="#", end=" ... \n")
print(name, age, sep="#")
```

`output`

```
>>> name = input("Write your name: ")
Write your name: William
>>> age = input("Write your age: ")
Write your age: 28
>>> print(name, age)
William 28
>>> print(name, age, end=" ... \n")
William 28 ... 
>>> print(name, age, sep="#", end=" ... \n")
William#28 ... 
>>> print(name, age, sep="#")
William#28
>>>
```

# Arithmetic operators

## What are arithmetic operators?

Arithmetic operators perform mathematical operations (e.g., addition, subtraction, etc.).

```python
# Arithmetic operators

# Addition
print(1 + 1)

# Subtraction
print(10 - 2)

# Multiplication
print(4 * 3)

# Division
print(12 / 3)

# Integer Division
print(12 // 2)

# Modulus
print(10 % 3)

# Exponentiation
print( 2 ** 3)
```

## Precedence of Arithmetic Operators

In mathematics, there is a rule that indicates which operations should be performed first. This is useful because when analyzing an expression, depending on the order of operations, the value can be different.

The definition indicates the following correct order:

1. Parentheses
2. Exponents
3. Multiplication and division (from left to right)
4. Addition and subtraction (from left to right)

```python
# Precedence of Arithmetic Operators

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)
```
`output`

```
>>> print(10 - 5 * 2)
0
>>> print((10 - 5) * 2)
10
>>> print(10 ** 2 * 2)
200
>>> print(10 ** (2 * 2))
10000
>>> print(10 / 2 * 4)
20.0
>>>
```

# Comparison Operators

Comparison operators are used to compare two values.

```python
# Equality comparison
balance = 450
withdrawal = 200

print(balance == withdrawal)

# Inequality comparison
balance = 450
withdrawal = 200

print(balance != withdrawal)

# Greater than / Greater than or equal comparison
print(balance > withdrawal)
print(balance >= withdrawal)

# Less than / Less than or equal comparison
print(balance < withdrawal)
print(balance <= withdrawal)
```

