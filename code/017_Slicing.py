# Slicing: Make New Lists Using Slices Of Old List
# list[start:end:step]

nums = list(range(0,11))
print("List: " + str(nums))

evens = nums[0:len(nums):2]
print("Evens: " + str(evens))

odds = nums[1:len(nums):2]
print("Odds: " + str(odds) + "\n")


# Tricks With Slices
# Reversing Lists/Strings
string = "This is fun!"
print("String: " + string)

print("Reversed: " + str(string[::-1]) + "\n")


# Modifying Portions Of List
nums2 = [0,4,5,6]
print("List: " + str(nums2))

nums2[1:3] = [1,2,3]
print("Modified: " + str(nums2))


# Swapping Values In List
names = ["Tiffany", "James"]
names[0], names[1] = names[1], names[0]
print(names)
# Example Uses...
# Shuffling, Sorting (In Place), Later Algorithms