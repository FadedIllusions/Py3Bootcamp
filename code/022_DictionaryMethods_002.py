# Pop
# Takes a single argument, corresponding to a key, and removes that key-value pair.
# Returns the value corresponding to the key that was removed.

pop_dict = {
			"A":1, "B":2, "C":3,
			"D":4, "E":5, "F":6
		   }

print("Original Popped Dictionary:")
print(pop_dict)

print("\nPopped Value For Key 'B':")
print(pop_dict.pop("B"))


# PopItem
# Removes a random key in a dictionary

popitem_dict = {"A":1, "B":2, "C":3}

print("\nOriginal Pop Item Dictionary:")
print(popitem_dict)

popitem_dict.popitem()
print("\nPopped Item (Random):")
print(popitem_dict)


# Update
# Update keys and values in a dictionary with another set of key/value pairs
# Can be used on an empty dictionary or to add to a populated dictionary
# If key already exists, will be updated to new value  -- overwritten
first_dict = {"B":2, "C":3, "D":4}
second_dict = {"A":1}

print("\nFirst Dictionary:")
print(first_dict)
print("\nSecond Dictionary:")
print(second_dict)

second_dict.update(first_dict)
print("\nUpdated Second Dictionary:")
print(second_dict)


