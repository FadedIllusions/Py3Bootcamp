# Can be applied to lists, dictionaries, tuples, generators, etc.
# [__for__in__]


#Long Form...
# nums = list(range(0,5))
# dbl_nums = []
#
# for num in nums:
#	dbl_num = num*2
# 	dbl_nums.append(dbl_num)

nums = list(range(0,5))
nums2 = [x*2 for x in nums]
print(nums)
print(nums2)

print("\n")

# String example
friends = ["ashley", "matt", "michael"]
upper_friends = [friend[0].upper() + friend[1::] for friend in friends]
print(friends)
print(upper_friends)

print("\n")

# List Comprehension With Conditional Logic
numbers = list(range(1,11))
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(numbers)
print(evens)
print(odds)

print("\n")

# Further Conditional Logic
new_numbers = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(numbers)
print(new_numbers)

print("\n")

# Removing Values (Vowels)
string = "This is so much fun!"
new_string = ''.join(char for char in string if char not in "aeiou")
print(string)
print(new_string)

print("\n")