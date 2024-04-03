#/usr/bin/env python3

# Example - Dictionaries

alice = dict()               # Declaring a dictionary
alice['role'] = 'White Mage' # Define mappings
alice['hp'] = 100
alice['mp'] = 200
alice['atk'] = 5
alice['def'] = 10
alice['mag'] = 30
alice['speed'] = 12


# Declaring and defining at the same time
bob = {
  'role': 'Black Mage',
  'hp': 100,
  'mp': 200,
  'atk': 7,
  'def': 10,
  'mag': 27,
  'speed': 12
}


carol = {
  'role': 'Thief',
  'hp': 70,
  'mp': 100,
  'atk': 13,
  'def': 12,
  'mag': 10,
  'speed': 25
}


# Put individual characters in main data structure
# Note that we capitalize the names on the left-side for display purposes.
# The right-side refers to the variables we just defined above.
vgchars = {
  'Alice': alice,
  'Bob': bob,
  'Carol': carol
}


# Set up a "PrettyPrinter" instance to view our data structures
import pprint
pp = pprint.PrettyPrinter(indent=2)
ppp = pp.pprint

# View final data structure
ppp(vgchars)

# Copying Python objects

vgchars2 = vgchars
dan = {
  'role': 'Warrior',
  'hp': 200,
  'mp': 70,
  'atk': 30,
  'def': 25,
  'mag': 7,
  'speed': 13
}


# Copy this next section line-by-line (or type them).
# It's important to see the results before moving on.'

vgchars2['Dan'] = dan
# You might expect that only vgchars2 will carry the new character we created.

ppp(vgchars2)
ppp(vgchars)
# Notice “Dan” appears in both objects. This is because we copied by reference.

# How to copy by value
vgchars3 = vgchars.copy()
vgchars3.keys()
vgchars3.pop('Dan')
vgchars3.keys() # Notice “Dan” was removed
vgchars.keys()  # Notice the original wasn’t changed

# Some helper functions to print stats in a nicer format
def print_stats(char_db, char_name):
    char_info = char_db.get(char_name)
    if char_info is None:
        print("Character not found in char_db")
    else:
        print(f"Name: {char_name}")
        print(f"Role: {char_info['role']}")
        print(f"HP: {char_info['hp']}")
        print(f"MP: {char_info['mp']}")
        print(f"Attack: {char_info['atk']}")
        print(f"Defense: {char_info['def']}")
        print(f"Magic: {char_info['mag']}")
        print(f"Speed: {char_info['speed']}")

def summarize_roles(char_db):
    for key, value in char_db.items():
        print(f"{key} is a {value['role']}")
