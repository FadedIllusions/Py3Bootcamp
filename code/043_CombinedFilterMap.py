# Given a list of names:
# names = ["Lassie", "Colt", "Rusty", "Bob"]
# Return new list with the string "Your instructor is" + each value in the array
# where the value is less than 5 characters

names = ["Lassie", "Colt", "Rusty", "Bob"]

print(list(map(lambda name: f"Your instructor is {name}", 
			   filter(lambda value: len(value) < 5, names))))

# Or, out of the user list, collect the user names of inactive users

users = [
			{"username":"Samuel", "tweets": ["I love cake", "I love pie"]},
			{"username":"Katie", "tweets": ["I love love my cat"]},
			{"username":"Jeff", "tweets": []},
			{"username":"Bob123", "tweets": []},
			{"username":"Doggo_Luvr", "tweets": ["Dogs are the best"]},
			{"username":"Guitar_Gal", "tweets": []}
		]

print(list(map(lambda user: user['username'], 
			   filter(lambda u: not u['tweets'], users))))


# Why Not Use List Comprehension?
#
# [print(f"Your instructor is {name}" for name in names if len(name)<5)]
# [print(user["username"] for user in users if not user["tweets"])]
#
# /USE/ List Comprehension when able.
# Have knowledge of Map and Filter

