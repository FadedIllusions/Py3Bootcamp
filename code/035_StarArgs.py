# *args
# Special operator we can pass to functions
# Gathers remaining arguments as a tuple
#
# def sum_all_nums(num1, num2, num3):
# 	return num1+num2+num3
# 
# But, what if we wanted to only use two arguments... or ten?

def sum_all_nums(*args):
	total = 0
	
	for num in args:
		total += num
		
	return total

def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome Back, Colt!"
	return "Not sure who you are..."

num_total = sum_all_nums(1,2,3,4,5,6,7,8,9)

print(ensure_correct_info())
print(ensure_correct_info(1, True, "Steele", "Colt", num_total))