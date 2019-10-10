# Clear Dictionary
artist = {
			"First": "Neil",
			"Last": "Young"
	     }

print("Create Artist Dictionary:")
print(artist)

artist.clear()
print("\nClear Artist Dictionary:")
print(artist)


# Copy Dictionary
item = 	{
			"product": "cat litter",
			"quantity": 4,
		}
print("\nCreate Item Dictionary:")
print(item)

item2 = item.copy()
print("\nPrint Copied Dictionary:")
print(item2)


# fromkeys Method
#{}.fromkeys(["email"], "unknown")
# Will go more into later
# Above example iterates through list 'email' and sets to 'unknown'
# Such as when setting many keys to a default value of 'unknown'

new_user = {}.fromkeys(["name", "score", "email", "bio"], "unknown")
print("\nDefault new_user Dictionary Created 'fromkeys':")
print(new_user)
# new_dict.fromkeys(range(1,11), 'unknown')


# Get Method
# Retrieves a key in an object and return 'None', instead of KeyError,
# if key does not exist
print("\nGet Method: ")
print(new_user.get("name"))


# fromkeys Example
game_properties = [
					"current_score", "high_score", "number_of_lives", 
					"items_in_inventory", "power_ups", "ammo", 
					"enemies_on_screen", "enemy_kills", "enemy_kill_streaks", 
					"minutes_played", "notifications", "achievements"
				   ]

initial_game_state = dict.fromkeys(game_properties, 0)

print("\nGame Properties:")
print(game_properties)
print("\nInitial Game State:")
print(initial_game_state)