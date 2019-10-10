# Adding Data To List


# Append: Add Item To End Of List
nums = list(range(1,5))
print("List: " + str(nums))

nums.append(5)
print("Append: " + str(nums))
				
# Extend: Add All Passed Values To End Of List
nums.extend([6,7,8])
print("Extend: " + str(nums))

# Insert: Insert Item At Given Position
nums.insert(0,0) # At idx 0, Insert 0
print("Insert: " + str(nums))



# Remove Data From List


# Clear: Removes All Items From List
# Such as clearing a shopping cart
print("\n")

lets = ['A','B','C','D']
print("List: " + str(lets))

lets.clear()
print("Clear: " + str(lets))

# Pop: Remove Item At Given Position And Return It
# If Not Any idx Specified, Removes And Returns Last Item In List
nums2 = list(range(1,6))
print("List: " + str(nums2))

nums2.pop()
print("Popped: " + str(nums2))

nums2.pop(0)
print("Popped: " + str(nums2))

# Remove: Removes First Item Whose Value Is X.
# Throws ValueError If Item Not Found
words = ["one", "two", "mistake", "three"]
print("List: " + str(words))

words.remove("mistake")
print("Removed: " + str(words))