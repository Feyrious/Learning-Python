# =============================================================================
# Lesson 01 - Variables and Conditions
# -----------------------------------------------------------------------------
# A variable is a name that points to a value. Python figures out the type
# automatically from the value you assign (dynamic typing).
# Conditions (if / elif / else) let the program choose what code to run.
# =============================================================================


# -----------------------------------------------------------------------------
# Variables and basic data types
# -----------------------------------------------------------------------------

# String (str) - text, written inside quotes
greeting = "Hello"

# Integer (int) - whole numbers
this_is_a_number = 32

# Float (float) - decimal numbers (Python's version of a "double")
this_is_a_float = 3.42

# Boolean (bool) - either True or False
is_active = True

# type() tells you what data type a variable holds
print(type(greeting))           # <class 'str'>
print(type(this_is_a_number))   # <class 'int'>
print(type(this_is_a_float))    # <class 'float'>
print(type(is_active))          # <class 'bool'>


# -----------------------------------------------------------------------------
# Conditions (if / else)
# -----------------------------------------------------------------------------

# The indented block under "if" only runs when the condition is True,
# otherwise the "else" block runs instead
if is_active:
    print("is active")
else:
    print("is not active")


# -----------------------------------------------------------------------------
# User input and string interpolation
# -----------------------------------------------------------------------------

# input() pauses the program and always returns what the user typed as a string
your_name = input("Enter your name: ")

# f-strings: put an f before the quotes and insert variables inside {}
print(f"{greeting} {your_name}")
