#Parker Wong 30019077 T11
'''
Program that simulates the life of a student in CPSC 231. The simulated world will be represented by a 2D Python list of single character strings. A student 'S' can either choose to maximize his/her fun times 'f' during the term or the person can choose to expend time working 'w' in order to maximize the term grade point (GPA) and letter graded awarded. Each 'f' or 'w' is worth 1 point each. However the simulation will run for a maximum of 13 turns (weeks). Each time that the user is prompted to move the student (or if the choice is given up) a time unit will be expended. The pavol and the taminator are special events in the program that directly affects the amount of time the student has in the semester.
'''


import random

SIZE = 10
NUM_TURNS = 13
STUDENT = "S"
WORK = "w"
FUN = "f"
TAMINATOR = "T"
gridinput = """\
          
 w        
          
  ff      
  wS      
          
          
wfw       
          
          
"""
#function opens and writes the input which contains the letters for the grid
#no parameters
#no return values
def createworld():
  fd = open("gridinput.txt" , "w")
  fd.write(gridinput)
  fd.close

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @display()
# @Argument: a reference the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: Mone
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# '''
def display(world):
    for r in range (0, SIZE, 1): 
    # Row of dashes before each row 
        for i in range (0, SIZE, 1): 
            print(" -", end="")
        print()
        for c in range (0, SIZE, 1): 
            # Vertical bar before displaying each element
            print("|" + world[r][c], end="")
        print("|") # Vertical bar right of last element + CR to
		           # move output to the next line

    # A line of dashes before each row, one line after the last
    # row.
    for i in range (0, SIZE, 1): 
        print(" -", end="")
    print()

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @ This function works in conjunction with readFromFile()
# @intialize()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element
# @is set to an exclamation mark).
# '''
def initialize():
    world = []                  
    for r in range (0, SIZE, 1):   
        world.append ([])       
        for c in range (0, SIZE, 1): 
            world[r].append ("!")
    return(world)
	
# '''
# @ This method works in conjunction with initialize. Initialize creates
# @ the list with list elements containing a default value '!'. This method
# @ relies on the list already being created and sets each list element to
# @ a corresponding value read in from the input file e.g. the string at
# @ row 2 and column 4 in the input file will initialize the list element
# @ at this same location in the 2D list (game world).
# @readFromFile()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element
# @will now be initialized to the values read in from the input file
# '''
def readFromFile():
    r = -1
    c = -1
    world = initialize() # Needed to create the 2D list
    createworld() #calls function containing the input
    inputvalid = True
    while inputvalid == True:
      inputFilename = input("Name of input file: ")
      
      try:
          inputFile = open(inputFilename,"r")
          r = 0
          # Read one line at a time from the 2Dfile into a string
          for line in inputFile:  
              c = 0
              # Iterate 1 char at a time through the string
              for ch in line:  
                  # Including EOL there's 11 characters per line
                  # 10x10 list , exclude the EOL to avoid reading
                  # outside the bounds of the list (10 columns)
                  if (c < SIZE):
                      # Set list element to the single char 
                      # read from file
                      world[r][c] = ch 
                      # Advance to next element along row 
                      c = c + 1  
                  # Entire row has been set to values read in from 
                  # file, move to next row
              r = r + 1  
          inputFile.close()
          inputvalid = False
      except IOError:
          print("Error reading from " + inputFilename)
          print("\n")
    return(world) 
    
#the function controls the movement of the student in which the location is stored as a list and is constantly being altered by the movement of the student, the new location "S" represents the list, function also error checks at every input and loops until a valid input is provided
#parameters world,row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron
#returns world[row][column],row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron
def movementoptions(world,row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron,pavoluse):
  print("MOVEMENT OPTIONS")
  print("7 8 9")
  print("4 5 6")
  print("1 2 3")
  print("Type a number on the keypad to indicate direction of movement.")
  print("Type 5 to pass on movement.")
  inputvalid = True
  while inputvalid == True:
    try:
      inputselection = int(input("Selection:"))
      world[row][column],row,column,GPA,funpoints,debugOn = firstfiveoptions(world,row,column,inputselection,GPA,funpoints,debugOn)
      world[row][column],row,column,GPA,funpoints,debugOn = lastfouroptions(world,row,column,inputselection,GPA,funpoints,debugOn)
      if inputselection > 9 or inputselection < 0:
        print("Must be within range of 1 to 9.\n")
      else:
        print("\n")
        debugOn,rowtam,columntam,taminatoron = cheatmenu(inputselection,debugOn,rowtam,columntam,world,taminatoron,pavoluse)
        inputvalid = False
    except ValueError:
      print("Invalid character, please select from the numbers listed.\n")
  return world[row][column],row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron

#the function counts the amount of funpoits and work points(converted to GPA) that the student finds on the grid
#parameters world,row,column,GPA,funpoints,debugOn\
#returns world[row][column],row,column,GPA,funpoints,debugOn
def points(world,row,column,GPA,funpoints,debugOn):
  world[row][column] = world[row][column]
  if world[row][column] == "w":
    world[row][column] = " " #must replace with an empty string in order to prevent switching
    GPA += 1
  elif world[row][column] == "f":
    world[row][column] = " "
    funpoints += 1
  if debugOn == True:
    print("<< points() Avoid the taminator as much as you can! I'm sensing extensions! >>")
  return world[row][column],row,column,GPA,funpoints,debugOn
  
#function controls the first five options of the student movement, this is to make the overall function slightly shorter. Each selection has a slightly different alteration to the student location by adding or subtracting the row or column number and if the player is at the edge of the grid, there will be no changes to the student location and a turn will still pass
#parameters world,row,column,inputselection,GPA,funpoints,debugOn
#returns world[row][column],row,column,GPA,funpoints,debugOn
def firstfiveoptions(world,row,column,inputselection,GPA,funpoints,debugOn):
  if inputselection == 1:
    if "S" in world[9]:
      print("You are at the end of the road.\n")
    elif "S" in world[row][0]:
      print("You are at the end of the road.\n")
    else:
      column -= 1
      row += 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
  
  if inputselection == 2:
    if "S" in world[9]:
      print("You are at the end of the road.\n")
      
    else:
      row += 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 3:
    if "S" in world[9]:
      print("You are at the end of the road.\n")
      
    else:
      column += 1
      row += 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 4:
    if "S" in world[row][0]:
      print("You are at the end of the road.\n")
    else:
      column -= 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 5:
    if debugOn == True:
      print("<< Toggle debug message >>")
  return world[row][column],row,column,GPA,funpoints,debugOn
  
#function controls the last four options of the student movement, this is to make the overall function slightly shorter. Each selection has a slightly different alteration to the student location by adding or subtracting the row or column number and if the player is at the edge of the grid, there will be no changes to the student location and a turn will still pass
#parameters world,row,column,inputselection,GPA,funpoints,debugOn
#returns world[row][column],row,column,GPA,funpoints,debugOn  
def lastfouroptions(world,row,column,inputselection,GPA,funpoints,debugOn):  
  if inputselection == 6:
    if "S" in world[row][9]:
      print("You are at the end of the road.\n")
    else:
      column += 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 7:
    if "S" in world[row][0]:
      print("You are at the end of the road.\n")
    elif "S" in world[0]:
      print("You are at the end of the road.\n")
    else:
      column -= 1
      row -= 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 8:
    if "S" in world[0]:
      print("You are at the end of the road.\n")
    else:
      row -= 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  if inputselection == 9:
    if "S" in world[0]:
      print("You are at the end of the road.\n")
    elif "S" in world[row][9]:
      print("You are at the end of the road.\n")
    else:
      column += 1
      row -= 1
      world[row][column],row,column,GPA,funpoints,debugOn = points(world,row,column,GPA,funpoints,debugOn)
      
  return world[row][column],row,column,GPA,funpoints,debugOn
  
#function controls the cheat menu in which the player can toggle the debug message which provides a simple message after each turn or can immediately invoke the taminator at any location as long as it's not already on the grid, quitting the function just passes the turn
#parameters inputselection,debugOn,rowtam,columntam,world,taminatoron
#returns debugOn,rowtam,columntam,taminatoron
def cheatmenu(inputselection,debugOn,rowtam,columntam,world,taminatoron,pavoluse):
  if inputselection == 0:
    validinput = True
    while validinput == True:
      print("Cheat menu options:")
      print("(t)oggle debug mode on")
      print("(m)ake the taminator appear")
      print("(q)uit cheat menu")
      
      userinput = input("Your selection:")
      if userinput == "q":
        validinput = False
        
      elif userinput == "t":
        if debugOn == False:
          print("Toggle debug mode is on")
          debugOn = True
        else:
          print("Toggle debug mode is off")
          debugOn = False
        
        
      elif userinput == "m":
        inputvalid = True
        for rows in range(len(world)):
          for columns in range(len(world[1])): #algorithm that searches the location of 'T' if it exists
            if world[rows][columns] == "T": 
              taminatoron = True
        if pavoluse == True:
          print("The taminator will not appear thanks to the presence of the pavol!")
        elif pavoluse == False and taminatoron == False:
          while inputvalid == True:
            try:
              rowtam = int(input("Enter the row:"))
              columntam = int(input("Enter the column:"))
              print("Beware the Taminator has appeared!")
              world[rowtam][columntam] = "T"
              if world[rowtam][columntam] == "S":
                print("It'd be too easy if the taminator spawned on the student\n")
              
              inputvalid = False
            except ValueError:
              print("Invalid input, must be within bounds of grid.")
        
        else:
          print("The taminator is already too powerful for another one to appear!")
          
      else:
        print("Invalid option please press 't', 'm' or 'q'")
      print("\n")
  return debugOn,rowtam,columntam,taminatoron    

#function controls the turn counter and will stop once it reaches past 13
#parameters currentturn
#returns currentturn
def turn(currentturn):
  currentturn += 1
  if currentturn >= 14:
    pass
  else:
    print("Current turn:" , currentturn)
  return currentturn

#function displays the current funpoints and GPA
#parameters funpoints,GPA
#returns no values
def funpointsGPA(funpoints,GPA):
  print("Fun points:" , funpoints,"\t" , "GPA:" , GPA)

#function controls the probability of either the pavol or the taminator showing up at any given point, to balance the probability, a random number in the range of 100 is preferable to avoid one taking priority over the other
#parameters currentturn,world,rowtam,columntam,taminatoron
#returns currentturn,taminatoron,rowtam,columntam,world[rowtam][columntam]
def thepavolandtaminator(currentturn,world,rowtam,columntam,taminatoron):
  pavoluse = False
  probability = random.randrange(0,100) 
  if probability <= 10: #10% chance of the pavol appearing
    print("The Pavol has appeared before you! Extension by one week! Hurray!")
    currentturn -= 1
    pavoluse = True
  elif (probability > 10) and (probability < 36): #25% chance for the taminator to appear
    print("Beware the taminator has appeared!")
    dontspawnstudent = True
    while dontspawnstudent == True:
      rowtam = random.randrange(0,10)
      columntam = random.randrange(0,10)
      if world[rowtam][columntam] == "S":
        pass
      else:
        dontspawnstudent = False
        
    world[rowtam][columntam] = "T"
    taminatoron = True
  return currentturn,taminatoron,rowtam,columntam,world[rowtam][columntam],pavoluse

#function is the conclusion of the game which provides the total amount of funpoints and the GPA that the student has
#parameters funpoints,GPA
#returns no values
def endgame(funpoints,GPA):
    print("Unfortunately the semester has ended.")
    print("The amount of fun points you have collected is:" , funpoints)
    print("Your GPA for this semester is:" , GPA)
    grade = " "
    if GPA == 0:
      print("Your grade letter for this semester is a F")
      grade = "F"
    elif GPA == 1:
      print("Your grade letter for this semester is a D")
      grade = "D"
    elif GPA == 2:
      print("Your grade letter for this semester is a C")
      grade = "C"
    elif GPA == 3:
      print("Your grade letter for this semester is a B")
      grade = "B"
    elif GPA == 4:
      print("Your grade letter for this semester is a A")
      grade = "A"
    try:
      fd = open("stats.txt", "w")
      fd.write("The amount of fun points you have collected is:" + str(funpoints))
      fd.write("Your GPA for this semester is:" + str(GPA))
      fd.write("Your grade letter for this semester is:" + str(grade))
    except FileNotFoundError:
      print("Wrong file")
    
#function searches the grid for the taminator represented by letter 'T' and if true, it will add two numbers representing the respective coordinates of its location
#parameters world,tamlocation
#returns tamlocation
def taminator(world,tamlocation):
  for rows in range(len(world)):
  		for columns in range(len(world[0])):
  			if world[rows][columns] == "T":
  			  tamlocation = []
  			  tamlocation.append(rows)
  			  tamlocation.append(columns)
  return tamlocation

#function searches the grid for the student represented by letter 'S' and if true, it will add two numbers representing the respective coordinates of its location
#parameters world,studentlocation
#returns studentlocation
def student(world,studentlocation):
  for rows in range(len(world)):
  		for columns in range(len(world[0])):
  			if world[rows][columns] == "S":
  			  studentlocation = []
  			  studentlocation.append(rows) 
  			  studentlocation.append(columns)
  return studentlocation  

#function controls if the space that the taminator will about to occupy contains either a work and fun point, if true it will get replaced by an empty string 
#parameters world,rowtam,columntam
#returns world[rowtam][columntam]
def destroypath(world,rowtam,columntam):
  if world[rowtam][columntam] == "f" or "w":
    world[rowtam][columntam] = " "
  return world[rowtam][columntam]

#note - I decided not to split this into more functions for the sake of simplicity and readability since it's repetition with slight changes (math add/subtract)
#function calculates the difference between the taminator's location and student location in terms of coordinates represented by xdelta and ydelta. The movement for the taminator is calculated by splitting up each scenario and seeing the relativity between them at any given point. 
#parameters tamlocation,studentlocation,world,rowtam,columntam,xdelta,ydelta
#returns world[rowtam][columntam],rowtam,columntam,xdelta,ydelta
def tammovement(tamlocation,studentlocation,world,rowtam,columntam,xdelta,ydelta):
  xdelta = tamlocation[1] - studentlocation[1]
  ydelta = tamlocation[0] - studentlocation[0]
  
  if xdelta < 0 and ydelta < 0: #tam NW of student
    if xdelta == -2 and ydelta == -2:
      rowtam += 1
      columntam += 1
      
    elif xdelta == -1 and ydelta == -2:
      rowtam += 1
     
    elif xdelta == -2 and ydelta == -1:
      columntam += 1
      
    else:
      rowtam += 2
      columntam += 2
    
  elif xdelta < 0 and ydelta > 0: #tam SE of student
    if xdelta == -1 and ydelta == 2:
      rowtam -= 1
      
    elif xdelta == -2 and ydelta == 2:
      rowtam -= 1
      columntam += 1
      
    elif xdelta == -2 and ydelta == 1:
      columntam += 1
     
    else:
      rowtam -= 2
      columntam += 2
    
  elif xdelta > 0 and ydelta > 0: #tam SW of student
    if xdelta == 2 and ydelta == 1:
      columntam -= 1
      
    elif xdelta == 2 and ydelta == 2:
      rowtam -= 1
      columntam -= 1
      
    elif xdelta == 1 and ydelta == 2:
      rowtam -= 1
      
    else:
      rowtam -= 2
      columntam -= 2
    
  elif xdelta > 0 and ydelta < 0: #tam NE of student
    if xdelta == 1 and ydelta == -2:
      rowtam += 1
      
    elif xdelta == 2 and ydelta == -2:
      rowtam += 1
      columntam -= 1
      
    elif xdelta == 2 and ydelta == -1:
      columntam -= 1
     
    else:
      rowtam += 2
      columntam -= 2
    
  elif xdelta == 0 and ydelta < 0: #tam directly above student
    if ydelta == -2:
      rowtam += 1
      
    else:
      rowtam += 2
    
  elif xdelta == 0 and ydelta > 0: #tamdirectly below student
    if ydelta == 2:
      rowtam -= 1
      
    else:
      rowtam -= 2
    
  elif xdelta < 0 and ydelta == 0: #tam to the left
    if xdelta == -2:
      columntam += 1
      
    else:  
      columntam += 2
    
  elif xdelta > 0 and ydelta == 0: #tam to the right
    if xdelta == 2:
      columntam -= 1
     
    else:
      columntam -= 2
  
  world[rowtam][columntam] = world[rowtam][columntam]
  return world[rowtam][columntam],rowtam,columntam,xdelta,ydelta

#function controls the close range scenario of the taminator and the student by taking their location differences and splitting up the scenarios once again. As long as the student remains moving, the taminator will not catch the student, if he stops at any point and the taminator is adjacent, the student gets caught and any work or fun functions will be destroyed in the process
#parameters xdelta,ydelta,world,rowtam,columntam,run
#returns world[rowtam][columntam],run
def proximity(xdelta,ydelta,world,rowtam,columntam,run):
  run = False
  if xdelta == 1 and ydelta == 1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == 1 and ydelta == -1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == -1 and ydelta == -1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == -1 and ydelta == 1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == 0 and ydelta == 1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == 0 and ydelta == -1:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == 1 and ydelta == 0:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  elif xdelta == -1 and ydelta == 0:
    world[rowtam][columntam] = destroypath(world,rowtam,columntam)  
    world[rowtam][columntam],run = caught(world,rowtam,columntam,run)
  return world[rowtam][columntam],run

#controls the notification that the student is caught by the taminator and disappears immediately after
#parameters world,rowtam,columntam,run
#returns world[rowtam][columntam],run
def caught(world,rowtam,columntam,run):
  print("The taminator has caught up to you!")
  world[rowtam][columntam] = " "
  run = True
  return world[rowtam][columntam],run
#################################################################
# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
def start():
    row = 4
    column = 3
    rowtam = 0
    columntam = 0
    currentturn = 0
    funpoints = 0
    GPA = 0
    xdelta = 0
    ydelta = 0
    counter = 0
    tamlocation = []
    studentlocation = []
    inputvalid = True
    taminatoron = False
    debugOn = False
    run = False
    world = readFromFile()
    while inputvalid == True:
      currentturn = turn(currentturn)
      for rows in range(len(world)):
          for columns in range(len(world[0])): #searches for the taminator
            if world[rows][columns] == "T":
              taminatoron = True
      if taminatoron == False:
        currentturn,taminatoron,rowtam,columntam,world[rowtam][columntam],pavoluse = thepavolandtaminator(currentturn,world,rowtam,columntam,taminatoron)
        
      else:
        pass
      if currentturn > 13:
        endgame(funpoints,GPA)
        inputvalid = False
      else:
        funpointsGPA(funpoints,GPA)
        display(world)
        
        world[row][column],row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron = movementoptions(world,row,column,GPA,funpoints,debugOn,rowtam,columntam,taminatoron,pavoluse)
        world[row][column] = "S"
        
        if taminatoron == True:
          counter += 1
          tamlocation = taminator(world,tamlocation)
          studentlocation = student(world,studentlocation)
          
          world[rowtam][columntam],rowtam,columntam,xdelta,ydelta = tammovement(tamlocation,studentlocation,world,rowtam,columntam,xdelta,ydelta)
          tamlocation = taminator(world,tamlocation)
          studentlocation = student(world,studentlocation)
          xdelta = tamlocation[1] - studentlocation[1]
          ydelta = tamlocation[0] - studentlocation[0]
          world[rowtam][columntam],run = proximity(xdelta,ydelta,world,rowtam,columntam,run)
          if run == True: #represents if the player gets caught by the taminator and adds two turns
            currentturn += 2
            taminatoron = False
            world[rowtam][columntam] = " "
          else:
            world[rowtam][columntam] = "T"
            
          if counter == 3 and run == False: #taminator maxes out at 3 turns
            taminatoron = False
            counter = 0
            print("Phew, we escaped him for now!\n")
            world[rowtam][columntam] = " "
          
start()
