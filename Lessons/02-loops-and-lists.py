# =============================================================================
# Lesson 02 - Loops and Lists (Collections)
# -----------------------------------------------------------------------------
# Collections store several values in one variable:
#   list       [ ]  - ordered, changeable, allows duplicates
#   dictionary { }  - key/value pairs, look values up by key
#   tuple      ( )  - ordered, read only (cannot be changed after creation)
#   set        { }  - unordered, only unique values (duplicates are removed)
# Loops (for) let us repeat code for every item in a collection or range.
# =============================================================================


# -----------------------------------------------------------------------------
# Lists
# -----------------------------------------------------------------------------

# A list of strings
services = ["server01", "server02", "server03", "db01", "db02", "db03"]

# Loop over every item in the list
for server in services:
    print(f"Checking {server}...")

# Add an item to the end of the list
services.append("server04")
print(services[6])  # Lists are indexed from 0, so index 6 is the 7th item

# Remove an item by its value
services.remove("server03")
print(services)

# Remove an item by its index and return it
removed_service = services.pop(1)
print(removed_service)


# -----------------------------------------------------------------------------
# Loops with range()
# -----------------------------------------------------------------------------

# range(start, stop) - counts from start up to, but NOT including, stop
for i in range(1, 10):
    print(i)  # 1, 2, 3 ... 9

# range(start, stop, step) - step 2 skips every other value
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9


# -----------------------------------------------------------------------------
# Dictionaries (key/value pairs)
# -----------------------------------------------------------------------------

service = {
    "name": "nginx",
    "status": "Running",
    "port": 8080
}
print(service)

# Get a value by its key (raises a KeyError if the key doesn't exist)
print(service["name"])
print(service["status"])
print(service["port"])

# get() returns a fallback value instead of crashing when a key is missing
empty_dictionary = {}
print(empty_dictionary.get("name", "noname"))
print(empty_dictionary.get("status", "unknown"))
print(empty_dictionary.get("port", 0))

# Loop over a dictionary and print every key and value
for key, value in service.items():
    print(f"{key}: {value}")


# -----------------------------------------------------------------------------
# Tuples (read only list)
# -----------------------------------------------------------------------------

coordinates = (23, 45, 23)
print(coordinates)
# coordinates[0] = 10  # Would raise a TypeError - tuples can't be changed


# -----------------------------------------------------------------------------
# Sets (unique values only)
# -----------------------------------------------------------------------------

# "dev" is added twice, but a set only keeps one copy
environments = {"dev", "test", "prod", "dev"}
print(environments)  # e.g. {'test', 'dev', 'prod'} - order is not guaranteed
