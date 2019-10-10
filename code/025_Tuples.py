# Tuple: An immutable ordered collection or grouping of items.
# nums = (1,2,3,4)

# Why Use A Tuple?
# Faster Than List
# Immutable (Data Security)
# Valid Keys In Dictionary

# Can Nest Tuples, Can Use Slicing

# Common Examples
# Months Of Year, Days Of Week, Etc -- Unchanging

# Create / Access
# first = (1,2,3,4,5)
# first[0]  ... 1
# first[-1] ... 5


# Tuples As Dictionary Keys
locations = {
			 (35.6895, 39.6917): "Tokyo Office",
			 (40.7128, 74.0060): "New York Office",
			 (37.7749, 122.4194): "San Francisco Office"
			}

print("\nTuples As Dictionary Keys:")
print(locations)


# Tuple Method -- Count
# Returns number of times a value appears in a tuple
t_count = (1,2,3,3,3)
print(f"\nTuple: {t_count}")
print("\nCount How Many Times '3' Appears: ")
print(t_count.count(3))

# Tuple Method -- Index
# Returns index at which a value is found
print(f"\nThe Index Of '2': {t_count.index(2)}")