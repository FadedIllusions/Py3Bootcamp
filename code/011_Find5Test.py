"""
	Generate Random Number 1-10
	Break If 5
"""

from random import randint

num = 0
i = 0

while num != 5:
	num = randint(1,10)
	i += 1
	
	print(f"{num}")
	
print(f"Looped {i} Times")