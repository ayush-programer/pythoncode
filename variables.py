# Variables are containers for storing data values. Unlike other programming languages
# Python has no command for declaring a variable. A variable is created the moment you 
# first assign a value to it.

"""
These keywords are *not* available for use as variable names

and except lambda with as finally nonlocal while assert
false None yield break for not try class from or is
continue global pass else
def if elif raise True
del import return in

"""


# bad
@dont_at_me

= 1
#   File "c:/python/tutorialstuff/pythonvariables.py", line 1
#     @dont_at_me = 1
#                 ^
# SyntaxError: invalid syntax

7
pot_club = True
#   File "c:/python/tutorialstuff/pythonvariables.py", line 1
#     7pot_club = True
#      ^
# SyntaxError: invalid syntax

time
of
day = 'Lunch Time'
#   File "c:/python/tutorialstuff/pythonvariables.py", line 1
#     time of day = 'Lunch Time'
#          ^
# SyntaxError: invalid syntax


# avoid typos
name = 'Jesse'
print('Hi ', nam)

# good
my_variable = 'is good'

# types
print(type(1))
# <class 'int'>

print(type(True))
# <class 'bool'>

print(type('Hi!'))
# <class 'str'>

print(type(3.14))
# <class 'float'>

print(type(['this', 'is', 'a', 'list']))
# <class 'list'>

print(type(('this', 'is', 'a', 'tuple')))
# <class 'tuple'>

print(type({'key': 'value'}))
# <class 'dict'>
