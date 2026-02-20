
# Basic Rock Paper Scissors Game
# Name: Sean Siska
# Date: 2/19/2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

def get_user_choice(): 
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	console.print("[green]You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.[/green]")
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			return num_to_choice[user_input]
		elif user_input in choices:
			return user_input
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")
	pass

def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	return random.choice(choices)

def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		return 'tie'
	elif (user_choice == 'rock' and computer_choice == 'scissors') or \
			 (user_choice == 'paper' and computer_choice == 'rock') or \
			 (user_choice == 'scissors' and computer_choice == 'paper'):
		return 'user'
	else:
		return 'computer'

def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
	if winner == 'tie':
		console.print("[blue]It's a tie![/blue]")
	elif winner == 'user':
		console.print("[bold green]You win this round![/bold green]")
	else:
		console.print("[bold red]Computer wins this round![/bold red]")

	pass

def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()

		winner = determine_winner(user_choice, computer_choice)
		print_round_result(user_choice, computer_choice, winner)
		if winner == 'user':
			user_score += 1
		elif winner == 'computer':
			computer_score += 1

	console.print("\n[bold underline]Game Over![/bold underline]")
	console.print(f"[cyan]Your score: {user_score}[/cyan]")
	console.print(f"[magenta]Computer score: {computer_score}[/magenta]")
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
	elif computer_score > user_score:
		console.print("[bold red]Computer wins the game![/bold red]")
	else:
		console.print("[blue]The game is a tie![/blue]")
	pass

if __name__ == "__main__":
	main()
