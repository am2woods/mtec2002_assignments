"""
dice_wars.py
===
Break down your problem using a flow chart, pseudocode, etc.  Here's a basic list of what should happen:
1. Print out ASCII art!!!
   ------
 /      /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------
2. Keep track of scores using a dictionary
3. Loop forever
4. Ask for command
5. If command is roll, roll random dice for computer and player
6. Determine who wins (3 states: computer wins, player wins or tie)
7. For each state add scores appropriately, and print out both rolls and scores
8. If command is quit, then exit the game
9. If the command is not quit or roll, say "I don't know that command"
"""
print """
   ------
 /      /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------"""
 
scores = {"player":0, "Computer":0}
import random

while True:
	print scores
	print "roll or quit?"
	command = raw_input("> ")
	if command == "roll":
		playa_roll = random.randint(1,6)
		computer_roll = random.randint(1,6)
		if playa_roll > computer_roll:
			print "You won!"
			scores['player'] += 1
		elif playa_roll < computer_roll:
			print "Computer won"
			scores['Computer'] += 1
		else:
			print "TIED!"
	elif command == "quit":
		exit()
	
 		