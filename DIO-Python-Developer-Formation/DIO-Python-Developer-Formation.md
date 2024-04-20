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

# Assignment Operators

These are operators used to define an initial value or overwrite the value of a variable.

```python
# Simple assignment operator
balance = 500

print(balance)

# Assignment operator with addition

balance = 500
balance += 200

print(balance)

# Assignment operator with subtraction

balance = 500
balance -= 100

print(balance)

# Assignment operator with multiplication

balance = 500
balance *= 2

print(balance)

# Assignment operator with division

balance = 500
balance /= 5

print(balance)

balance = 500
balance //= 5

print(balance)

# Assignment operator with modulus

balance = 500
balance %= 480

print(balance)

# Assignment operator with exponentiation

balance = 80
balance **= 2

print(balance)
```

`output`

```
>>> balance = 500
>>> print(balance)
500
>>> # Assignment operator with addition
>>> 
>>> balance = 500
>>> balance += 200
>>> print(balance)
700
>>> # Assignment operator with subtraction
>>> 
>>> balance = 500
>>> balance -= 100
>>> print(balance)
400
>>> # Assignment operator with multiplication
>>> 
>>> balance = 500
>>> balance *= 2
>>> print(balance)
1000
>>> # Assignment operator with division
>>>
>>> balance = 500
>>> balance /= 5
>>> print(balance)
100.0
>>> balance = 500
>>> balance //= 5
>>> print(balance)
100
>>> # Assignment operator with modulus
>>>
>>> balance = 500
>>> balance %= 480
>>> print(balance)
20
>>> # Assignment operator with exponentiation
>>>
>>> balance = 80
>>> balance **= 2
>>> print(balance)
6400
```

# Logical Operators

These are operators used in conjunction with comparison operators to form a logical expression. When a comparison operator is used, the returned result is a boolean, thus we can combine comparison operators with logical operators.

```python
# Logical operators
balance = 1000
withdraw = 200
limit = 100
special_account = True

print(balance >= withdraw)
print(balance <= limit)

# and operator (both arguments must be true to be true)

print(balance >= withdraw and balance <= limit)

# or operator (only one argument must be true to be true)

print(balance >= withdraw or balance <= limit)

# not operator

not 1000 > 1500

# Using parentesis to organize logical operators

print(balance >= withdraw and balance <= limit or special_account and balance >= withdraw)
print((balance >= withdraw and balance <= limit) or (special_account and balance >= withdraw))

# Avoid long logical operations, you can just organize as below
normal_account_with_enough_balance = balance >= withdraw and balance <= limit
special_account_with_enough_balance = special_account and balance >= withdraw

exp_3 = normal_account_with_enough_balance or special_account_with_enough_balance
print(exp_3)
```

# Identity Operators

These are operators used to compare whether the two tested objects occupy the same position in memory.

```python
course = "Python Course"
course_name = course
balance, limit = 200, 200

print(course is course_name)
print(course is not course_name)
print(balance is limit)
```

# Membership Operators

These are operators used to check if an object is present in a sequence.

```python
course = "Python Course"
fruits = ["orange", "grape", "lemon"]
withdraws = [1500, 100]

print("Python" in course)
print("apple" not in fruits)
print(200 in withdraws)
```

# Indentation and Blocks

Indenting the code is a way to keep it more readable and maintainable. In Python, indentation plays a second role because through indentation the interpreter can determine where a block of code begins and where it ends.

Programming languages often use characters or reserved words to determine the start and end of a block. In Java and C, for example, braces are used. See an example below:

```java
void withdraw(double value) { // Beginning of method block
    if (this.balance >= value) { // Beginning of if block
        
        this.balance -= value;
    } // Ending of if block
    
} // Ending of method block
```

## Using spaces

There is a convention in Python that defines best practices for writing code in the language. In this document, it is indicated to use **4 white spaces per indentation level**, which means that for each new block, 4 new white spaces are added. See the previous example in Java, but now with how indentation would be in Python:

```python
def withdraw(self, value: float) -> None: # Beginning of method block
    if self.balance >= value: # Beginning of if block
        self.balance -= value
    # Ending of if block

# Ending of method block
```

**Note:** As indentation is not optional in Python, this makes the code necessarily more readable than in other languages where indentation is optional (it depends on the programmer's best practices).

<<<<<<< HEAD
# Conditional Structures

A conditional structure allows the control flow to divert when certain logical expressions are met.

## If

To create a simple conditional structure consisting of a single diversion, we can use the reserved word `if`. The command will test the logical expression and, if it returns `True`, the actions within the `if` code block will be executed.

```python
# If
balance = 2000.0
withdraw = float(input("Inform the withdraw value: "))

if balance >= withdraw:
    print("Success!")

if balance < withdraw:
    print("Insufficient funds!")
```

## If else

To create a conditional structure with two diversions, we can use the reserved words `if` and `else`. As we know, if the logical expression tested in `if` is true, then the `if` code block will be executed, otherwise, the `else` code block will be executed.

```python
# If else

balance = 2000.0
withdraw = float(input("Inform the withdraw value: "))

if balance >= withdraw:
    print("Success!")

else:
    print("Insufficient funds!")
```

## If elif else

In some scenarios, we may desire more than two diversions. For this, we can use the reserved word `elif`, which consists of a new logical expression, that will be tested and, if it returns `True`, the `elif` code block will be executed. **There is no maximum number of `elif` we can use, however, avoid creating large conditional structures as they increase the code complexity.

```python
# If elif else

option = int(input("Inform an option: [1] Withdraw \n[2] Statement: "))

if option == 1:
    value = float(input("Inform the withdraw value: "))

elif option == 2:
    print("Showing bank statement... ")
else:
    sys.exit("Unavailable option! Closing...")
```

## Nested If elif else

We can create nested conditional structures, for this, we just need to add `if-elif-else` structures within the code block of `if-elif-else` structures.

```python
# Nested if elif else

normal_account = True
university_student_account = False

balance = 2000
withdraw = 500
overdraft = 450

if normal_account:
    if balance >= withdraw:
        print("Success!")
    elif balance <= (balance + overdraft):
        print("Success with overdraft!")
elif university_student_account:
    if balance >= withdraw:
        print("Success!")
    else:
        print("Insufficient Funds!")
```
=======
# Conditional Structures

The conditional structure allows the flow of control to be diverted when certain logical expressions are met.

## If

To create a simple conditional structure, composed of a single diversion, we can use the reserved word `if`. The command will test the logical expression and, in case of returning `True`, the actions present in the code block of `if` will be executed.

```python
# If
balance = 2000.0
withdraw = float(input("Enter the withdrawal amount: "))

if balance >= withdraw:
    print("Success!")

if balance < withdraw:
    print("Insufficient funds!")
```

## If else

To create a conditional structure with two paths, we can use the reserved words `if` and `else`. As we know, if the logical expression tested in `if` is true, then the code block of `if` will be executed, otherwise, the code block of `else` will be executed.

```python
# If else

balance = 2000.0
withdraw = float(input("Enter the withdrawal amount: "))

if balance >= withdraw:
    print("Success!")

else:
    print("Insufficient funds!")
```

## If elif else

In some scenarios, we may want more than two paths, for this, we can use the reserved word `elif`, which is composed of a new logical expression, that will be tested and, if it returns `True`, the `elif` code block will be executed. **There is no maximum number of `elif` we can use, however, avoid creating large conditional structures, as they increase the complexity of the code.

```python
# If elif else

option = int(input("Enter an option: [1] Withdraw \n[2] Statement: "))

if option == 1:
    value = float(input("Enter the withdrawal amount: "))

elif option == 2:
    print("Showing bank statement... ")
else:
    sys.exit("Unavailable option! Closing...")
```

## Nested If elif else

We can create nested conditional structures, for this, we just need to add `if-elif-else` structures within the code block of `if-elif-else` structures.

```python
# Nested if elif else

normal_account = True
university_student_account = False

balance = 2000
withdraw = 500
overdraft = 450

if normal_account:
    if balance >= withdraw:
        print("Success!")
    elif balance <= (balance + overdraft):
        print("Success with overdraft!")
elif university_student_account:
    if balance >= withdraw:
        print("Success!")
    else:
        print("Insufficient Funds!")
```

# Ternary If

The ternary if allows you to write a condition in a single line. It is composed of 3 parts:

1. Return if the expression is true
2. The logical expression
3. The return if the expression is not met

```python
# Ternary If

status = "Success!" if balance >= withdraw else "Failed!"

print(f"{status} when withdrawing the amount!")
```

# Loops

Loops are structures used to repeat a block of code a certain number of times. This number can be known beforehand or determined through a logical expression.

## For Loop

The `for` loop is used to iterate over an iterable object. It makes sense to use `for` when we know the exact number of times our code block should be executed or when we want to iterate over an iterable object.

```python
# For

text = input("Write a piece of text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")

print() # Just adds a line break

# For else

text = input("Write a piece of text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print() # Just adds a line break
```

## range() Function

`range()` is a built-in Python function used to generate a sequence of integers from a start (inclusive) to an end (exclusive). If we use `range(i,j)`, it will produce:

`i, i+1, i+2, i+3, ..., j-1`

Thus, the function takes 3 arguments: `stop` (*mandatory*), `start` (*optional*), and `step` (*optional*).

```python
# Range()

print(list(range(0,10)))

# For range()

for number in range(0, 11):
    print(number, end=" ")

# 5 times table

for number in range(0, 51, 5):
    print(number, end=" ")
```

## While Loop

The `while` loop is used to repeat a code block several times. It makes sense to use `while` when we do not know the exact number of times our code block should be executed.

```python
# While

option = -1

while option != 0:
    option = int(input("[1] Withdraw \n[2] Bank Statement\n[0] Exit \n: "))

    if option == 1:
        print("Withdrawing...")
    
    elif option == 2:
        print("Showing bank statement"...)

# Using break

while True:
    number = int(input("Guess the number! It is between 0 and 100! While you don't guess it, the program keep running!: "))

    if number == 10:
        break

    print(number)

# Using continue
# This will only show the odd numbers

for number in range(100):

    if number % 2 == 0:
        continue

    print(number, end=" ")
```

# String and Slicing

## General Objective

Learn useful methods for manipulating string objects, such as interpolating variable values and understanding how slicing works.

## Introduction

The Python `string` class is famous for its rich methods and an easy-to-use interface. In some languages, manipulating character sequences is not a trivial task, but in Python, this work is very simple.

## Upper(), lower(), title()

`upper()`, `lower()`, and `title()` are string methods in Python used to manipulate the case of characters within a string. `upper()` converts all characters in the string to uppercase, `lower()` converts all characters to lowercase, and `title()` converts the first character of each word to uppercase and the rest to lowercase, effectively capitalizing the string as if it were a title.

```python
# Upper, lower, title

course = "pYtHon"

print(course.upper())
print(course.lower())
print(course.title())
```

## Join() and center()

`join()` is a method used to concatenate the elements of an iterable, such as a list, into a single string. It takes an iterable as its argument and returns a string where each element of the iterable is joined by the string on which `join()` is called.

`center()` is a method used to center-align a string within a specified width. It takes two arguments: the width of the resulting string and an optional character to use for padding. If no character is specified, it defaults to using whitespace for padding.

```python
# Join and center

course = "Python"

print(course.center(10, "#"))
print(".".join(course))
```

## Strip

`strip()` is a method used to remove leading and trailing whitespace characters (spaces, tabs, newlines) from a string. It doesn't remove whitespace within the string, only from the beginning and end.

```python
# Strip

text = "  Hello, world!  "

print(text + ".")
print(text.strip() + ".")
print(text.rstrip() + ".")
print(text.lstrip() + ".")
```

# Variable Interpolation

In Python, we have three ways to interpolate variables into strings: the first one uses the `%` sign, the second one uses the `format` method, and the last one uses `f strings`.

The first method is not currently recommended, and its usage in Python 3 is rare. Therefore, we will focus on the last two methods.

```python
# Old Style %

name = "William"
age = 28
job = "Programmer"
language = "Python"

print("Hello, I am %s. I am %d years old. I work as %s and I use the %s language!" % (name, age, job, language))

# Format() method

name = "William"
age = 28
job = "Programmer"
language = "Python"

print("Hello, I am {0}. I am {1} years old. I work as {2} and I use the {3} language!" .format(name, age, job, language))

# f-string

name = "William"
age = 28
job = "Programmer"
language = "Python"

print(f"Hello, I am {name}. I am {age} years old. I work as {job} and I use the {language} language!")
```

# String Slicing

It's a technique used to return substrings (parts of the original string), specifying start, stop, and step: `[start:stop[,step]]`.

```python
# Slicing

name = "William Arthur Oak"

name[0]
name[:9]
name[10:]
name[10:10]
name[10:16:2]
name[:]
name[::-1]
```

# Multiline Strings

They are defined by using three single or double quotes during assignment. They can span multiple lines of code, and all white spaces are included in the final string.

```python
# Multiline Strings

name = "William"

message = f"""
Hello, my name is {name}.
I am learning Python."""

print(message)
```
