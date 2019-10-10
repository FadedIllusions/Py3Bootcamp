import random

rand_num = random.randint(1,10)

while True:
	guess = int(input("\nPick A Number From 1 To 10: "))
	
	if guess < rand_num:
		print("Too Low!")
	elif guess > rand_num:
		print("Too High!")
	else:
		print("YOU GOT IT!")
		
		play_again = input("\nDo You Want To Play Again? (y/n) ")
		if play_again == "y":
			rand_num = random.randint(1,10)
			guess = None
		else:
			print("\nThank You For Playing!")
			break
