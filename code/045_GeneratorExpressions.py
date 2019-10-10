# Generator Expressions
# (Notice lack of list comprehension brackets
# Creates generator expression instead

print(all(num for num in [2,4,5,6,8,10] if num%2==0))

def is_all_strings(lst):
    print(all(type(l) == str for l in lst))

is_all_strings(['a','b','c'])
is_all_strings([2, 'a','b','c'])
is_all_strings(["hello", "goodbye"])