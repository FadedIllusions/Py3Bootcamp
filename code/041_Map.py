# Map
# Standard function that accepts at least two arguments, a function and an iterable
# (Common Usecase of Lambdas)  -- (Iterable: Lists, Strings, Dicts, Sets, Tuples, Etc)
#
# Runs lambda for each value in iterable and returns map object which can
# be converted into another data structure

nums = list(range(0,11,2))
doubles = list(map(lambda dbl: dbl*2, nums))
print(doubles)

print("\n")

names = [
		 {'first':'Rusty', 'last':'Steele'},
		 {'first':'Colt', 'last':'Steele'},
		 {'first':'Blue', 'last':'Steele'}
		]

first_names = list(map(lambda x: x['first'], names))
print(first_names)