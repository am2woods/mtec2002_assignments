import random

scores = {"Player":0, "Computer":0}

jajanken = ["r","s","p"]

rock = """  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
          _______)             ~Jajanken!!!!~
         _______)
---.__________)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print "Hello, what's your name?"
name = raw_input('> ')
print "Hello %s lets play Jajanken! (rock, paper, scissors)" % (name)
print "Type 'r' for rock, 'p' for paper, and 's' for scissors."
print "Type quit to leave the game."

while True:
	print "play or quit?"
	command = raw_input("> ")
	if command == "play":
		print scores
		print "Choose (r)ock, (p)aper or (s)cissors"
		player_pc = raw_input("> ")
		NPC_pc = random.choice(jajanken)
		if player_pc == "r" and NPC_pc == "s":
			print "%s beats %s" % (rock, scissors)
			print "You WIN!"
			scores["Player"] += 1
		elif player_pc == "p" and NPC_pc == "r":
			print "%s beats %s" % (paper, rock)
			print "You WIN!"
			scores["Player"] += 1
		elif player_pc == "s" and NPC_pc == "p":
			print "%s beats %s" % (scissors, paper)
			print "You WIN!"
			scores["Player"] += 1
		elif player_pc == NPC_pc:
			print "TIE"
		elif player_pc == "r" and NPC_pc == "p":
			print "%s beats %s" % (paper, rock)
			print "You LOOSE!"
			scores["Computer"] += 1
		elif player_pc == "s" and NPC_pc == "r":
			print "%s beats %s" % (rock, scissors)
			print "You LOOSE!"
			scores["Computer"] += 1
		elif player_pc == "p" and NPC_pc == "s":
			print "%s beats %s" % (scissors, paper)
			print "You LOOSE!"
			scores["Computer"] += 1
			
	elif command == "quit":
		print "Thank you for playing %s" %(name)
		exit()
	else:
		print "Select the right command, please."
		

