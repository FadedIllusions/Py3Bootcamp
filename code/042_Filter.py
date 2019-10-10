# Filter
# There Is A Lambda For Each Value In The Iterable
# Returns Filter Object Which Can Be Converted Into Other Iterables
# Object Contains Only The Values That Return True To Lambda -- Filters

# nums = [1,2,3,4,5,6]
# evens = list(filter(lambda x: x%2==0, nums))
# print(evens)

names = ["Austin", "Penny", "Anthony", "Angel", "Billy"]
a_names = list(filter(lambda name: name[0]=='A', names))
print(a_names)

print("\n")

# /Can/ Use List Comprehension
[print(name) for name in names if name[0] == 'A']