# All
# Return True if all elements of the iterable are truthy 
# (Or iterable is empty)

print(all([num for num in [2,4,5,6,8,10] if num%2==0]))

#Any
# Return True if any element of the iterable is truthy.
# (Returns False for empty iterable.)

print(any(val for val in [1,2,3] if val >2]))