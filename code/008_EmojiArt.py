"""
	msg = input("What's The Secret Password? ")
	
	while msg != "bananas":
		print("WRONG!")
		msg = input("What's The Secret Password? ")
		
	print("Correct!")
"""

smiley = "\U0001f600"
times = 10
	
for num in range(1,11):
	print(smiley * num)
	
while times > 0:
	print(smiley * times)
	times-=1