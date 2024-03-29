# Argument Unpacking Using * As An Argument
# We can use * as an argument to a function to "unpack" values

def sum_all_values(*args):
	total = 0
	
	for num in args:
		total += num
		
	print(total)
	
# sum_all_values(1,30,2,5,6)

nums = list(range(1,11))
sum_all_values(*nums)

# Without the *, we are passing in a list, 
# *args collects the list as the left of a tuple
# and we get an error:
# "Unsupported Operand Type(s) for +=: 'int' and 'list'
# So, we must 'unpack' the collection and pass them in one-by-one

# Further Example:
# def count_sevens(*args):
#     return args.count(7)
#
# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,
#         1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,
#         5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,
#         15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6, 7,8,9,8,7,
#         6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
#
# num_of_sevens = count_sevens(*nums)