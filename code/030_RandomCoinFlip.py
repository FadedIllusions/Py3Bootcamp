from random import random

def flip_coin():
	if random() > 0.5:
		return "\nHeads"
	else:
		return "\nTails"
	
print(flip_coin())