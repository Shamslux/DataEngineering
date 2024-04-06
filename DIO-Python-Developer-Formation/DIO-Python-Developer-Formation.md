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

