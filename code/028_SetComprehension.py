# Set Comprehension
# Usefule when converting other data types to a set
set_x = {x**2 for x in range(10)}
print(f"\nSet Comprehension: {set_x}")

set_y = {char.upper() for char in 'hello'}
print(f"\nSet Comprehension of 'hello': {set_y}")

# Set Comprehension Via A Function
def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

string = "hello"
print(f"\nAre All Vowels In The String: {are_all_vowels_in_string(string)}")