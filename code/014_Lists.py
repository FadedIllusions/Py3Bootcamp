# Print With For Loop
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

for sound in sounds:
    result += sound.upper()
	
print(f"{result}\n")


# Print With While Loop
numbers = list(range(1,5))
idx = 0

while idx < len(numbers):
	print(numbers[idx])
	idx += 1
	
print("\n")


# Use Case Of While Loop Printing
items = ["Socks", "Shirt", "Pants"]
i = 0

while i < len(items):
	print(f"Item {i+1}: {items[i]}")
	i += 1
	

