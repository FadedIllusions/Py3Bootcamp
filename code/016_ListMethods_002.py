# Index: Returns Idx Of Specified Item

# Can Specify Start And End Point
# list.index(item, start)
# list.index(item, start, end)
words = ["zero", "one", "two", "three"]
print("List: " + str(words))

print("Idx Of 'three': " + str(words.index('three')) + "\n")



# Count: Return Number Of Times X Appears In List
nums = [0,1,1,2,3,1]
print("List: " + str(nums))

print("Count of 1: " + str(nums.count(1)))
print("Count of 4: " + str(nums.count(4)) + "\n")


# Reverse: Reverse Elements Of List (In-Place)
# That Is, Without Creating A New List
words = ["!", "backwards", " ", "is", " ", "list", " ", "This"]
print("List: " + str(words))

words.reverse()
print("Reversed: " + str(words))

# Further Fun
w = ""

for word in words:
	w += word
	
print("String: " + w )

# Using Joined (String Method: Concatenation)
wordsStr = ''.join(words)
print("Joined String: " + wordsStr + "\n")


# Sort: Sort Items Of List (In-Place)
nums2 = [5,2,3,1,4]
print("List: " + str(nums2))

nums2.sort()
print("Sorted: " + str(nums2) + "\n")