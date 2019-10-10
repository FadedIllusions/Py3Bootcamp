# Argument Unpacking Using ** As An Argument
# We can use ** as an argument to a function to "unpack" values
#
# See 038_UnpackingTuples.py for further reference

def display_names(first, second):
	print(f"{first} says hello to {second}")

names = {"first": "Colt", "second":"Rusty"}

display_names(**names)

# Without **, we get a TypeError:
# "display_names() missing 1 required positional argument: 'second'
# As the entire names dictionary is passed in as the argument 'first'