#Growing up in Ocarina of Time

from sys import exit

#dead
def dead(reason):
	print reason, "Game Over!"
	exit(0)

	
#start
def start():
	for i in range(0,20):
		print ""
	print "Welcome to Growing up in Ocarina of Time!"
	print "\ta Zelda themed game."
	print ""
	print "The goal of this mini Python game is to grow up."
	print "I made it as an excercise to learn some Python basics."
	print "I am still a beginner so nothing is optimized, it only works."
	print "\nType anything to start!\n"
	input = raw_input("Type anyting: ")
	for i in range(0,7):
		print ""
	kokiri()

#kokiri forest
def kokiri():
	print "Hello! Wake up!"
	print "Please help!"
	print "You should get your equipment."
	print "What are you going to get?"
	
	#Getting Equipment
	input_equipment = False
	sword = False
	shield = False
	
	while not input_equipment:
		input = raw_input("Equipment: ")
	
		if "sword" in input and not sword:
			print "We got our sword!"
			sword = True
		elif "shield" in input and not shield:
			print "We got our shield!"
			shield = True
		elif "sword" in input and sword:
			print "We already got our sword!"
		elif "shield" in input and shield:
			print "We already got our shield!"
		else:
			print "A %s is not a valid piece of equipment!" % input
			
		if sword and shield:
			print "We got all the equipment we need."
			input_equipment = True
			deku_tree()


#Deku Tree			
def deku_tree():
	for i in range(0,7):
		print ""
	print "You should now continue and follow your path."
	print "We need to go to the Deku Tree."
	print ""
	print "Do you want to enter or go away?"
	input_deku_enter = False
	
	#checking for enter
	while not input_deku_enter:
		input = raw_input("Choose: ")
		
		if "enter" in input or "inside" in input:
			input_deku_enter = True
			print "You entered the Deku Tree!"
		elif "go" in input or "away" in input:
			input_deku_enter = True
			dead("You are an hero and died.")
		else:
			print "I don't know what you mean."

	#Gohma
	print "\nTo defeat Gohma you need to attack."
	print "\nKill her."
	
	input_gohma = False
	while not input_gohma:
		input = raw_input("What are you going to do? ")
		
		if input == "attack":
			input_gohma = True
			print "\nYou defeated Gohma!\nYou got the Kokiri's Emerald!"
			for i in range(0,8):
				print ""
			print "We should head to Dodongo's Cavern now."
			dodongo()
		else:
			print "What are you doing? You should be attacking!"
			
			
			
#Dodongo's Cavern
def dodongo():
	
	#entering
	print "\nOh no! Some rocks are blocking the entrance."
	print "We should use one of our items, but which?"
	print "\nWe have the following items:"
	for item in items:
		print item
	print ""
	
	input_dodongo_enter = False
	while not input_dodongo_enter:
		input = raw_input("Item: ")
		
		if "Bomb" in input or "bomb" in input:
			print "You blew up the rocks and entered Dodongo's Cavern."
			input_dodongo_enter = True
		else:
			print "That's not the item you need to use."
	
	#Dodongo
	print "\n\nThere he is, Dodongo!"
	print "Use your bombs to weaken him. Throw them by typing 'throw bomb'."
	
	fail = 0
	dodongo = False
	for i in range(0,3):
		if not dodongo:
			input = raw_input("What to do: ")
		
			if "throw bomb" in input:
				print "You weakened Dodongo! Now attack him to kill him."
				dodongo = True
			else:
				print "That's not what you want to do!"
				fail += 1
		
			if fail == 3:
				dead("You died because you weren't doing anything!")

	dodongo_attack = False
	while not dodongo_attack:
		input = raw_input("What are you going to do? ")
		if input == "attack":
			print "\nYou killed him!\nYou got the Goron's Ruby!"
			dodongo_attack = True
			jabu()
		else:
			print "I don't understand that!"
	

	
#Inside Jabu-Jabu's Belly	
def jabu():
	for i in range(0,8):
		print ""
	print "You are very close to getting the Master Sword!"
	print "\nYou go to Jabu-Jabu."
	print "You meet King Zora and he tells you that you can only go inside if you give him a fish."
	print "King Zora gives you a fishing rod!"
	
	#Give Fishing Rod.
	items.append("Fishing Rod")
	
	print "\n\nWhich item are you going to use, you have the following items:"
	for item in items:
		print item
	
	#Fishing
	input_fishing = False
	while not input_fishing:
		input = raw_input("Item to use: ")
		if "fishing" in input or "rod" in input:
			print "\nYou successfully captured a fish!"
			print "Lord Jabu-Jabu will eat you now so you get inside."
			input_fishing = True
		else:
			print "You are doing nothing useful!"
	
	#Princess Ruto
	print "\n\n\n\n"
	print "You meet Princess Ruto."
	print "Are you going to help her out or do you leave here here?"
	
	ruto = False
	while not ruto:
		input = raw_input("Are you going to help her out? ")
		if "y" in input:
			ruto = True
			print "\n\nBy helping her you manage to get to Barinade!"
			print "Quick, kill it! Before it kills you!"
		elif "n" in input:
			dead("You were almost there, but you were selfish! You get stuck and never get out.")
		else:
			print "I don't understand %s!" % input
	
	#Barinade
	print "\nBarinade has some tentacles you need to destroy!"
	print "Which item are you going to use? You have the following items:"
	for item in items:
		print item
	
	input_barinade = False
	while not input_barinade:
		input = raw_input("Item to use: ")
		
		if input == "boomerang" or input == "Boomerang":
			print "\nYou stunned barinade, kill it now!"
			print "You only need to attack it!"
			input_barinade = True
		else:
			print "Don't do so dangerous!"
	
	input_barinade_2 = False
	while not input_barinade_2:
		input = raw_input("What are you going to do? ")
		if input == "attack":
			input_barinade_2 = True
			print "\n\nYou killed Barinade!"
			print "\nWith that, you got the final Spiritual Stone, the Zora's Sapphire."
			print "You should be able to access the Temple of Time now!"
			temple_of_time()
		else:
			print "Are you still making such mistakes?"
	


#Temple of Time	
def temple_of_time():
	print "\n\nYou have arrived at the Temple of time and opened the door of time."
	print "You are able to see the Master Sword!"
	print "What are you going to do, draw it or just leave it?"
	
	input = raw_input("Choose: ")
	if "draw" in input:
		print "\n\n\nYou get trapped in a dream for 7 years. You wake up and you're finally adult!"
		print "YOU WIN!"
	else:
		dead("You stay here and die of starvation.")
	
		
items = ["Slingshot", "Bombs", "Boomerang"]	
	
start()
