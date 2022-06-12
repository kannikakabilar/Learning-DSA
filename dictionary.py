# Dictionary basics in Python

import this


thisdict = {"key": "value", "brand": "Ford", "model": "Mustang", "year": 1964}

print(thisdict)
#>> {'key': 'value', 'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Below prints the value of brand only
# Dictionaries look like lists but each value is not accesed by indexin, rather accessed by it's keys

print(thisdict["brand"])
#>> 'Ford'

# Below will also do the same thing
print(thisdict.get("brand"))

# Dictionaries are mutable, they can be changed after being declared

# 2 items with the same keys are not allowed
# Duplicate values will overwrite existing values

thisdict = {"key": "value", "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}

print(thisdict)
#>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'year': 2020}

print(len(thisdict))
#>> 3

# The keys() method will return a list of all the keys in the dictionary
print(thisdict.keys())

x = thisdict.keys()

print(x) # before the change
#>> dict_keys(['brand', 'model', 'year'])

# Adding a new item to the original dictionary, updates the key list as well
thisdict["color"] = "white"

print(x) # after the change
#>> dict_keys(['brand', 'model', 'year', 'color'])

# Similary, list of all the values of the dictionary can also be collected
x = thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list
print(thisdict.items())
#>> dict_itmes([('brand', 'Ford'), ('model', 'Mustang'), ('year': 2020), ('color', 'white')])

# Check if key exists in dictionary
if "model" in thisdict: # - this lookup happens in O(1) time on average
    print("yes!")

# Copying Dictionaries
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1
# and so, changes made to dict1 will also be made in dict2

mydict = thisdict.copy()
mydict = dict(thisdict) # does the same as above

# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value

x = thisdict.setdefault("speed", 300)
print(x)
#>> 300

# Removing Dictionary items
thisdict.pop("model") # Removes the item with the specified key name

thisdict.popitem() # Removes the last inserted item

del thisdict["brand"] # Removes the item with the specified key name

thisdict.clear() # empties the dictionary