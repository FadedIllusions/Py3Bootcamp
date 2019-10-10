# def square(num): return num * num
# 	print(square(9))

square2 = lambda num: num * num
print(square2(7))
#
# add = lambda a,b: a + b
# print(add(3,10))
#
# Lambda's haven't any name:
# print(square.__name__)
# print(square2.__name__)

# Most commonly used 
# when you need to pass a function into a function as a parameter
# and that function will never be used again

# Syntax
# lambda paramaters: body of function