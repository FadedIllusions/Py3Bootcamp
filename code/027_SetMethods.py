# Add
# Adds an element to a set
# If element already in set, set doesn't change
s = set([1,2,3])
print(f"\nOriginal Set: {s}")

s.add(4)
print(f"'4' Added To Set: {s}")

# Remove
# Removes value from set
# KeyError if value not found
# Use 'discard()' to remove without KeyError
s.remove(4)
print(f"'4' Removed From Set: {s}")

# Copy
s2 = s.copy()
print(f"Copy Of Set: {s2}")

# Clear
s2.clear()
print(f"Cleared Set: {s2}")



# Set Math
# Including 'intersection', 'symmetric_difference', 'union', etc
# Union: Combination of sets without duplicates
# Intersection which set elements are shared between sets

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
print("\n...Students...")
print(f"Math: {math_students}")
print(f"Biology: {biology_students}")

# Union of Sets
print("\nAll Students (Union)")
print(math_students|biology_students)

# Intersections
print("\nStudents In Both Classes (Intersection)")
print(math_students&biology_students)

