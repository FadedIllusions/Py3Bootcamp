# Sets
# Like Formal, Mathematical Sets
# Doesn't Not Permit Duplicates
# Elements Aren't Ordered (Cannot Use Index To Access)
# ex_set {1,2,3,4,} ... ex_set = set({1,2,3,4,5})

nums = {1,2,3,4,5}
print("\nAccessing Values In Set With 'FOR' Loop:")
for num in nums:
	print(num)
	
# Example Use-Case Of Sets:
# Given multiple cities, use a set to remove duplicates and cast to list
cities = ["Los Angeles", "Boulder", "Kyoto", "Santiago", "Los Angeles", "Kyoto"]

print("\nGiven Cities: ")
print(cities)
print("\nList of Cities (Without Duplicates):")
print(list(set(cities)))

print(f"\nHow Many Cities: {len(set(cities))}")