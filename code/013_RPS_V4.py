import random

player_wins = 0
computer_wins = 0

play_again = None


while play_again != 'n':
    print("\n-------------------------")
    print("Rock, Paper, Scissors...")
    print("Best 2 Out Of Three!")
    print("-------------------------\n")

    while player_wins < 2 and computer_wins < 2:

        player = input("\nPlayer, Make Your Move: ").lower()

        rand_num = random.randint(0, 2)
        if rand_num == 0:
            computer = "rock"
        elif rand_num == 1:
            computer = "paper"
        else:
            computer = "scissors"

        print(f"Computer Played: {computer}")

        if player == computer:
            print("It's A Tie!")
            player_wins += 1
            computer_wins += 1

        elif player == "rock":
            if computer == "scissors":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player Wins!")
                player_wins += 1
            else:
                print("Computer Wins!")
        elif player == "scissors":
            if computer == "rock":
                print("Computer Wins!")
                computer_wins += 1
            else:
                print("Player Wins!")
                player_wins += 1
        else:
            print("\nSomething Went Wrong...")
            break

    if player_wins > computer_wins:
        print("\nPLAYER WINS GAME!\n")
    elif player_wins == computer_wins:
        print("\nTIED GAME!\n")
    else:
        print("\nCOMPUTER WINS GAME!\n")

    play_again = input("Would You Like To Play Again? (y/n) ").lower()
    player_wins = 0
    computer_wins = 0
