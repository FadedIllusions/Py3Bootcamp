# Functions
# def name_of_function():
#	block of runnable code

def happy_birthday(name):
	print("\nHappy Birthday To You.\n" +
		  "Happy Birthday To You.\n"  +
		  f"Happy Birthday, Dear {name}!\n" +
		  "Happy Birthday To You!")
	
happy_birthday(input("What Is Your Name? "))


# Returning Values From Functions
# Returns, Exits Function, Pops Function Off Call Stack
def square_of_7():
	return 7**2

result = square_of_7()
print("\n" + str(result))