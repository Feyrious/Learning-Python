# =============================================================================
# Lesson 03 - Functions, Methods and Modules
# -----------------------------------------------------------------------------
# A function is a named block of code you can run (call) again and again.
#   function - called on its own:            print("hi"), len(services)
#   method   - a function that belongs to a value and is called with a dot:
#                                            "hi".upper(), services.append(x)
# A module is a .py file with code you can import and reuse in other files.
# =============================================================================

# Imports go at the top of the file
import math                                 # Import a whole built-in module
import random as rnd                        # Import a module with a shorter name (alias)
from datetime import date                   # Import one specific thing from a module
from modules import server_tools            # Import our own module from Lessons/modules/
from modules.server_tools import build_address, DEFAULT_PORT


# -----------------------------------------------------------------------------
# Calling built-in functions
# -----------------------------------------------------------------------------

services = ["server01", "server02", "db01"]

# Call a function by writing its name followed by () with arguments inside
print(len(services))        # 3 - number of items
print(max(4, 12, 7))        # 12 - largest value
print(round(3.14159, 2))    # 3.14 - round to 2 decimals


# -----------------------------------------------------------------------------
# Calling methods
# -----------------------------------------------------------------------------

# Methods are called on a value using a dot: value.method()
name = "nginx"
print(name.upper())                 # NGINX
print(name.replace("n", "N"))       # NgiNx

# Some methods change the value itself (like list methods from lesson 02)
services.append("db02")
print(services)

# Others return a new value and leave the original unchanged
print(" Running ".strip())          # "Running" without the spaces


# -----------------------------------------------------------------------------
# Defining your own functions
# -----------------------------------------------------------------------------

# "def" creates a function. The indented block runs each time it is called
def say_hello():
    print("Hello!")

say_hello()
say_hello()


# Parameters are inputs to the function, the values you pass in are arguments
def greet(person):
    print(f"Hello {person}")

greet("Kim")


# "return" sends a value back to the caller so it can be stored or used
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8


# Default values are used when an argument is left out
def connect(host, port=22):
    return f"Connecting to {host} on port {port}"

print(connect("server01"))          # Uses the default port 22
print(connect("server01", 8080))    # Overrides the default

# Keyword arguments - name the parameter so the order doesn't matter
print(connect(port=443, host="web01"))


# Functions are great with loops - write the logic once, use it many times
def is_database(server_name):
    return server_name.startswith("db")

for server in services:
    if is_database(server):
        print(f"{server} is a database")


# -----------------------------------------------------------------------------
# Using imported modules
# -----------------------------------------------------------------------------

# "import math" - use module_name.function_name
print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.141592653589793

# "import random as rnd" - use the alias instead of the full name
print(rnd.choice(services))     # A random server from the list
print(rnd.randint(1, 6))        # A random number from 1 to 6

# "from datetime import date" - use the name directly, no module prefix
print(date.today())


# -----------------------------------------------------------------------------
# Using our own module (Lessons/modules/server_tools.py)
# -----------------------------------------------------------------------------

# Imported with "from modules import server_tools" - use the module prefix
print(server_tools.check_server("server01"))

# Imported with "from modules.server_tools import ..." - use names directly
print(build_address("db01"))            # db01:8080
print(build_address("db01", 5432))      # db01:5432
print(DEFAULT_PORT)

# dir() lists everything a module contains, handy for exploring
print(dir(server_tools))
