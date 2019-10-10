# Syntax
# {___:___ for ___ in ___}

# Iterates over keys, by default
# Use '.items()' to iterate over keys and values

# numbers = dict(first=1, second=2, third=3)
#
# squared_numbers = {key: value **2 for key, value in numbers.items()}
# print(squared_numbers)

# {num: num**2 for num in [1,2,3,4,5]}

str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print("Dictionary Comprehension From Two Strings:")
print(combo)



num_list = list(range(0,7))
print(f"\nNumber List: {num_list}")
print("Number List Via Dictionary Comprehension:")
comp_dict = {num:("even" if num%2 == 0 else "off") for num in num_list}
print(comp_dict)



list_abbr = ["CA", "NJ", "RI"]
list_states = ["California", "New Jersey", "Rhode Island"]
print(f"\nState Abbreviation List: {list_abbr}")
print(f"State List: {list_states}")
print("Concatenated Dictionary Via Zip Function:")
#dict_states = {list_abbr[i]:list_states[i] for i in range(0,len(list_abbr))}
print(dict(zip(list_abbr,list_states)))



person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
people = {val[0]: val[1] for val in person}
# people = {k:v for k,v in person}
# people = dict(person)

print("\nPerson List: ")
print(person)
print("DC People Dictionary: ")
print(people)


ascii_dict = {key:chr(key) for key in range(65,91)}
ascii_dict.update({key:chr(key) for key in range(97,123)})
print("\nASCII Dictionary")
print(ascii_dict)