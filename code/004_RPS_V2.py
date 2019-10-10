print("Rock, Paper, Scissors...")

player1 = input("Player 1, Make Your Move: \n")
player2 = input("Player 2, Make Your Move: \n")

if player1 == player2:
	print("It's A Tie!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player1 Wins!")
	elif player2 == "paper":
		print("Player2 Wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("Player1 Wins!")
	elif player2 == "scissors":
		print("Player2 Wins!")
elif player1 == "scissors":
	if player2 == "rock":
		print("Player2 Wins!")
	elif player2 == "paper":
		print("Player1 Wins!")
		
else:
	print("Something Went Wrong...")