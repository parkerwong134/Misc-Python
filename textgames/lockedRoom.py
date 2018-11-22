'''
@author Parker Wong
@purpose indigenous boys and girls club game
this program begins with the user being in the entrace of the house and has the choice to try unlocking the door by solving the puzzles in all other rooms
Any room action can be committed an infinite number of times but the ultimate goal is to unlock the door in the centre room
in order to unlock the door, the player must decode the messages on both walls and then use the messages to solve the puzzle in the other room (provided a binary chart and ascii table)
'''
def mainRoom():
  doorUnlock = False
  keypadCorrect = False
  message = ""
  masterKey = False
  exceedTry = 0
  tpMade = False
  while True:
    print("You are in: Centre Room")
    print("In front of you there is a locked door that contains the code needed for your lock. You also see that there is a room to your left and right along with a path leading upstairs and the basement.\n")
    print("Actions:")
    print("1: Try opening the door")
    print("2: Go to the left room")
    print("3: Go to the right room")
    print("4: Go to the basement")
    print("5: Go upstairs")
    
    if keypadCorrect == True and message == "Mohawk" and tpMade == True: doorUnlock = True
    userin = input()
    if (userin == "1" and doorUnlock == True) or (userin == "1" and masterKey == True): 
      print("Congratulations you have opened the door!")
      print("There is a note left on the table.")
      print("The message says: Use the decimals this time, not the hex.\n")
      print("95-8       64+9          44*2-3\n")
      print("Once you have unlocked your lock on the table, please feel free to attempt the bonus room if you did not have the chance before.")
      print("Type in the word 'try' to attempt or type anything else to stop the game.")
      tryRoom = input()
      if tryRoom == "try":
        quiz()
      break

    elif userin == "1" and doorUnlock == False:
      print("Door is currently locked, it seems that you might have forgetten something in the rooms.")

    elif userin == "2":
      message = leftRoom(message)

    elif userin == "3":
      keypadCorrect = rightRoom(keypadCorrect)
    
    elif userin == "4":
      masterKey,exceedTry = basement(masterKey,exceedTry)
    
    elif userin == "5":
      tpMade = upstairs(tpMade)

    else:
      print("Incorrect input, please select type '1', '2', '3', '4' or '5' then press enter.\n")

def leftRoom(message):
  typeWrite = message
  while True:
    print("You are in: Left Room")
    print("There are a few things you notice when you walk in. You notice that there is a typewriter on the desk. On the other side you see a message on the table.\n")
    print("Actions:")
    print("1: Investigate the typewriter")
    print("2: See the message written on the table")
    print("3: Go back to the Centre Room")
    leftin = input()
    if leftin == "1": 
      print("The current message of the typewriter is", typeWrite)
      print("You have the option to typewrite a message, what do you want to typewrite?")
      userin = input("Please enter the message or typeWrite 'exit' to leave it as is.\n")
      if userin == "exit": continue
      else: 
        typeWrite = userin
        print("The current message of the typewriter is now", typeWrite)
        print("------------------------------------\n")
      print("")  

    elif leftin == "2":
      print("On the table you see that the message says:")
      print("Use the hex, not the decimal")
      print("0001   1001    0110    0000\n")
  
    elif leftin == "3":
      return typeWrite

    else: print("Please enter a valid action")

def rightRoom(keypadCorrect):
  keyCor = False
  while True:
    print("You are in: Right Room")
    print("There seems to be some interesting things to observe. You notice there is a strange picture on the wall with some things written on it. On the other side you see that there is a keypad with four entry slots.\n")
    print("Actions:")
    if keypadCorrect == False:
      print("1: Try entering numbers into the keypad")
      print("2: Inspect the painting")
      print("3: Go back to the Centre Room")
    else: 
      print("2: Inspect the painting")
      print("3: Go back to the Centre Room")

    userin = input()
    if userin == "1" and keypadCorrect == False: 
      print("It seems that the keypad is colored red and looking for four numbers, what are they?\n")
      keypad = input("Enter numbers here:")
      if keypad == "1960": 
        print("The keypad turns green and closes")
        print("---------------------------------\n")
        keypadCorrect = True
        keyCor = True
      else: 
        print("Keypad remains red")
        print("------------------\n")

    elif userin == "2": 
      print("The painting has something written on it")
      print("4D   6F   68   61   77   6B\n")
      
    elif userin == "3":
      return keyCor

    else: print("Please enter a valid action")

def basement(masterKey,exceedTry):
  while True:
    print("You are in: Basement")
    if masterKey == False and exceedTry < 2:
      print("Welcome to the bonus room! If you continue to stay in this room you will have the choice to take a trivia quiz that can give you immediate access to the locked door back in the centre room.")
      print("Given a set of questions from computer science and Canadian aboriginal history you must answer 8 out of 10 questions right to get the key.")
      print("There is no time limit but if you cannot answer it correctly, you lose time on getting the key.")
      print("You are only given 2 tries and you won't know which questions are incorrect.\n")
      print("Actions:")
      print("1: Start the quiz")
      print("2: Go back to the centre room")
      userin = input()
      if userin == "1" and exceedTry < 2:
        exceedTry += 1
        masterKey = quiz()
      elif userin == "2": return masterKey, exceedTry
      else: print("Please enter a valid action\n")
    else: 
      print("There is nothing else to do here.\n")
      print("Actions:")
      print("2: Go back to the centre room")
      userin = input()
      if userin == "2": return masterKey, exceedTry
      else: print("Please enter a valid action\n")

def quiz():
  correct = 0
  print("WARNING: TYPING SOMETHING OTHER THAN THE LETTERS STATED WILL BE MARKED AS INCORRECT!")
  print("Input can be capitals or lowercase!\n")
  print("Question 1:")
  print("How many bits are in one byte?")
  print("-----------------------------\n")
  print("A) 1")
  print("B) 2")
  print("C) 4")
  print("D) 8")
  answer1 = input("Answer: ")
  if answer1.lower() == "d": 
    correct += 1
  
  print("")
  print("Question 2:")
  print("What was the main purpose of Section 35 of the Constitution Act in 1982?")
  print("-----------------------------------------------------------------------\n")
  print("A) It imposed government control over all Natives focusing on band councils, reserves, and status")
  print("B) Protection to the indigenous and treaty rights of indigenous peoples in Canada")
  print("C) Allow for the federal government responsibility for Aboriginals and their land")
  print("D) Remove discriminatory rules including a ban on native consumption on alcohol")
  answer2 = input("Answer: ")
  if answer2.lower() == "b":
    correct += 1

  print("")
  print("Question 3:")
  print("Which one of these is not a programming language?")
  print("------------------------------------------------\n")
  print("A) Ruby")
  print("B) Python")
  print("C) MySQL")
  print("D) Java")
  answer3 = input("Answer: ")
  if answer3.lower() == "c":
    correct += 1  

  print("")
  print("Question 4:")
  print("What year were natives given the right to vote in federal elections?")
  print("--------------------------------------------------------------------\n")
  print("A) 1960")
  print("B) 1973")
  print("C) 1975")
  print("D) 1982")
  answer4 = input("Answer: ")
  if answer4.lower() == "a":
    correct += 1  
  
  print("")
  print("Question 5:")
  print("Which part of the computer has the purpose of executing instructions (programs)?")
  print("-------------------------------------------------------------------------------\n")
  print("A) Graphics Processing Unit")
  print("B) Central Processing Unit")
  print("C) Random Access Memory")
  print("D) Motherboard")
  answer5 = input("Answer: ")
  if answer5.lower() == "b":
    correct += 1

  print("")
  print("Question 6:")
  print("Which two Aboriginal groups were most affected from the James Bay and Northern Quebec Agreement?")
  print("----------------------------------------------------------------------------------------------\n")
  print("A) Metis and Inuit")
  print("B) Cree and Metis")
  print("C) Inuit and Cree")
  print("D) Nakota and Stoney-Nakoda")
  answer6 = input("Answer: ")
  if answer6.lower() == "c":
    correct += 1

  print("")
  print("Question 7:")
  print("Which one of these is not an operating system?")
  print("------------------------------------------------\n")
  print("A) Mac OS X")
  print("B) Windows 10")
  print("C) Ubuntu")
  print("D) Assembly")
  answer7 = input("Answer: ")
  if answer7.lower() == "d":
    correct += 1
  
  print("")
  print("Question 8:")
  print("Which historical figure led the Red River Rebellion in 1869?")
  print("------------------------------------------------\n")
  print("A) Gabriel Dumont")
  print("B) James Isbister")
  print("C) Louis Riel")
  print("D) John Bruce")
  answer8 = input("Answer: ")
  if answer8.lower() == "c":
    correct += 1

  print("")
  print("Question 9:")
  print("How many times does this loop execute?")
  print("int count = 1;")
  print("while (count <= 10)")
  print("{")
  print("count++;")
  print("}")
  print("------------------------------------------------\n")
  print("A) 9")
  print("B) 10")
  print("C) 11")
  print("D) Syntax error, does not run")
  answer9 = input("Answer: ")
  if answer9.lower() == "b":
    correct += 1

  print("")
  print("Question 10:")
  print("What major event happened in 1763?")
  print("-----------------------------------\n")
  print("A) The Royal Proclamation was issued by King George III")
  print("B) Major changes to the Indian Act including rules for band councils")
  print("C) The Quebec Act was set in place")
  print("D) Nothing significant happened")
  answer8 = input("Answer: ")
  if answer8.lower() == "a":
    correct += 1

  print("")
  print("You have scored", correct, "out of 10")
  if correct < 8:
    print("Unfortunately you have not passed, please try again or exit the basement.")
    print("------------------------------------------------------------------------\n")
    return False
  else:
    print("Congratulations! You have passed the quiz and now have access to the locked door!")
    print("---------------------------------------------------------------------------------\n")
    return True

def upstairs(tpMade):
  while True:
    print("You are in: Upstairs room 1")
    print("In the first room you see, there is an overhead projector in the middle of the room with some buttons. Beside the projector is a laptop ready to be used.")
    print("There are also some scrambled pieces of code attached to the walls.\n")
    print("Actions:")
    print("1: Go look at the projector")
    print("2: Inspect the walls")
    print("3: Look at the laptop")
    print("4: Go back downstairs")
    userin = input()
    if userin == "1": 
      print("The buttons on the projector seems like it will produce something with specific input. What should it be?")
      sequence = input()
      for i in sequence:
        if i == "1":
          horizontal() 
        if i == "2": 
          diagonal()
        if i == "3":
          vertical()
      print("")
    elif userin == "2":
      print("At the top of each part of the wall there is a number written there along with some code underneath it.\n")
      print("At the northern wall we find:")
      print("0010")
      print("diagonals\n")
      print("At the western wall we find:")
      print("0001")
      print("horizontal\n")
      print("At the eastern wall we find:")
      print("0011")
      print("top\n")
    elif userin == "3":
      if tpMade == True: print("There is nothing to look at, the laptop is shut down")
      else:
        print("Looking for a sequence of hexidecimal numbers. Please do not use spaces and using capitals do not matter")
        hexSeq = input()
        if hexSeq == "74697069" or hexSeq == "54697069" or hexSeq == "746565706565" or hexSeq == "546565706565":    
          tpMade = True
          print("The laptop beeps and shuts down.")
          print("-------------------------------\n")
        else:
          print("Laptop is still open")
          print("---------------------")

    elif userin == "4":
      return tpMade
    else:
      print("Please select a valid action\n")
    
def horizontal():
  print("---------------------------")

def diagonal():
  i=1 
  j=11     
  while (i<=20):
    print((" "*j)+ "/",(" "*i)+ "\\")
    j -= 1
    i += 2
    if i > 19:
      print(" /           /\\         \\")
      print("/           /  \\         \\")
  

def vertical():
  print("          ", "\\  /")
  print("           ", "\\/")
  print("           ", "/\\")

mainRoom()