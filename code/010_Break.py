"""
	while True:
		command = input("Type 'exit' to exit: ")
		if(command == "exit"):
			break
"""

times = int(input("How Many Times Do I Have To Tell You? "))
print("\n")

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	
	if time >=2:
		print("Do You Even Listen Anymore?")
		break