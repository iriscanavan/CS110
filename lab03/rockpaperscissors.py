# Iris Canavan, Section 3

import random

def main():
	print("Welcome to Rock, Paper, Scissors!")
	user_choice = input("Enter Rock, Paper, or Scissors: ")
	computer_choice = fComputerRPS()

	while user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissors":
		print("Invalid choice, please try again")
		user_choice = input("Enter Rock, Paper, or Scissors: ")

	print("User's choice:", user_choice)
	print("Computer's choice:", computer_choice)
	print("Who is the winner?", fDetermineWinner(user_choice, computer_choice))

	play_again = input("Do you want to play again? (y/n): ")
	if (play_again == "y" or play_again == "Y"):
		main()

def fComputerRPS():
	return random.choice(["Rock", "Paper", "Scissors"])

def fDetermineWinner(user_choice, computer_choice):
	if user_choice == computer_choice:
		return "It is a tie"
	elif user_choice == "Rock" and computer_choice == "Paper":
		return "Computer wins (Paper beats Rock)"
	elif user_choice == "Paper" and computer_choice == "Scissors":
		return "Computer wins (Scissors beat Paper)"
	elif user_choice == "Scissors" and computer_choice == "Rock":
		return "Computer wins (Rock beats Scissors)"
	elif user_choice == "Paper" and computer_choice == "Rock":
		return "User wins (Paper beats Rock)"
	elif user_choice == "Scissors" and computer_choice == "Paper":
		return "User wins (Scissors beat Paper)"
	elif user_choice == "Rock" and computer_choice == "Scissors":
		return "User wins (Rock beats Scissors)"

main()
