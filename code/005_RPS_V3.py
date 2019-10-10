import random

rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"


print("Rock, Paper, Scissors...")

player = input("Player, Make Your Move: \n").lower()

print(f"Computer Played: {computer}")

if player == computer:
	print("It's A Tie!")
	
elif player == "rock":
	if computer == "scissors":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player == "paper":
	if computer == "rock":
		print("Player Wins!")
	else:
		print("Computer Wins!")
elif player == "scissors":
	if computer == "rock":
		print("Computer Wins!")
	else:
		print("Player Wins!")
		
else:
	print("Something Went Wrong...")