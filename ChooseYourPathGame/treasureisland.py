import pyfiglet 

def start():
  ASCII_ART = pyfiglet.figlet_format("Treasure Island",font = 'isometric1')
  print(ASCII_ART)
  print("\n\n")

def gameLoop():
  print("You crash landed on an island after going through a terrible storm.\nAs you wake up you find yourself on the beach.\nYou may go into the jungle or continue along the beach in search of others.\nType jungle to go to the jungle or beach to go along the beach.")

  choice1 = "jungle"
  choice2 = "beach"
  userChoice = getInput()

  if userChoice == choice1:
    print("Now in the jungle, you see a trail up ahead with a stone statue.\nYou also see to your right a game trail with large paw prints.\nWhich path do you take?\nSay statue for that path or game trail for the other.")
    choice1 = "statue"
    choice2= "gametrail"
    userChoice = getInput()
    
    if userChoice == choice1:
      print("You continue past the statue to find a group of indigenous people.\n They are friendly to outsiders and welcome you in.\nThe chief speaks of a great treasure and gives you a map directly to it.")
      return 0
    elif userChoice == choice2:
      print("Going down the game trail you stumble upon a temple\nDo you go into the temple or continue following the paw prints.\nType temple to go inside or continue to follow the trail")
      choice1 = "temple"
      choice2= "continue"
      userChoice = getInput()

      if userChoice == choice1:
        print("Once inside the temple you see a chest at the end of the tunnel.\nAs you step forward you actiavte a spike trap.")
        return 0
      elif userChoice == choice2:
        print("After following the prints for an hour, you stumble upon a puma.\nIt turns out the puma is a spirt and has led you to the treasure.")
        return 1
    else:
      return 1
  
  elif userChoice == choice2:
    print("As you continue along the beach you see a washed up life boat.\nYou approach and hear screams coming from behind the boat.\nDo you wish to see who is screaming or do you fall back into the jungle? Type continue to see whats behind the boat or type jungle to flee.")
    choice1 = "continue"
    choice2 = "jungle"
    userChoice = getInput()

    if userChoice == choice1:
      print("As you turn the corner of the boat you see a strange being.\nIt pounces on you before you can scream.")
      return 0
    elif userChoice == choice2:
      print("As you flee into the jungle a strange being chases you from behind the boat.\nYou trip over a root and look up to see the beast above you.")
      return 0
      
  else:   
    return 1

def getInput():
  userChoice = input()
  userChoice = userChoice.lower()
  return userChoice

def startGame():
  print("Welcome to Treasure Island\n")
  print("You'll always have a choice to go either\nleft right or straight.")
  print("Choose wisely as each choice matters and \nmay kill you.")
  print("Please say yes if you wish to continue, \notherwise, the game will end...")

  start = "yes"
  userChoice = getInput()
  
  if start == userChoice: 
    success = gameLoop()
    if success == 0:
      print("\nYou won and found the treasure, congrats!")
    else:
      print("\nYou failed to choose correctly and die...")
  else:
    return 0

start()
startGame()
