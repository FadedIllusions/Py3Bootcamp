# Limits Of Lists:
# Work to store a particular type/set of data that would make sense in a list.
# Users, Data, Items, etc.
# Though, if using something that is 'unclear' as to what it represents, such as the following:
# instructor = ["Colt", True, 4, "Python", False],
# wherein things are unclear due to a lack of information.

# In example...
# Shopping Cart
# 	Item
#		name
#		quantity
#		price
#
# We /could/ use: cart = [['cat litter', 3, 19.99]]; but, it would have to be known
# what each index value represents. We need a way of describing the data and encoding
# more information than just an order (such as with a list). Enter Dictionaries...
#
# Dictionaries consist of key/value pairs
# Keys Describe Data, Values represent Data

# Create a dictionary...
item = 	{
			"product": "cat litter",
			"quantity": 4,
		}

# Add additional items (vs del item['key'])
item["price"] = 19.99

print("Dictionary:")
print(item)

# Print price
print(f"\nPrice: {item['price']}\n")

# Print Dictionary (Again) -- Using Comprehension:
print("Printed Via Comprehension:")
[print(f"{key}: {item[key]}") for key in item]
# item.keys(): item.values()
# item.items() -- dict.items() ... Returns list of touples


# F-String Concatenation Example
artist = {
			"First": "Neil",
			"Last": "Young"
	     }

full_name = f"{artist['First']} {artist['Last']}"

print("\nNew Dictionary:")
print(artist)

print(f"\nFull Name Via F-String Concatenation:\n{full_name}\n")


# Print Items Via 'items()'
print("Artist Diction Via 'items()':")
[print(f"{key}: {value}")for key, value in artist.items()]


# Summating Values From Dictionary
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
 
total_donations = sum(donations.values())
# Or total_donations = sum(donation for donation in donations.values())
print("\nDonations Dictionary:")
[print(f"{key}: {value}")for key, value in donations.items()]
print(f"\nTotal Donations {total_donations}")


# Test In Key Is In Dict
# Use .value() to check values
print("\nCheck If \"Audrey\" In Donations List: ")
if "audrey" in donations.keys():
	print(f"Audrey Donated ${donations['audrey']}\n")
else:
	print("Audrey Did Not Donate\n")