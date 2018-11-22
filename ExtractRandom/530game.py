from array import *
import random
def menu():

  print("Welcome to Hide and Seek! Please select the mode you want to play!")
  print("Type in the number and press enter\n")
  while(True):
    print("1. Human vs AI (Human is hider)")
    print("2. AI vs Human (AI is hider)")
    print("3. Human vs Human")
    print("4. Simulation")

    selection = int(input())
    print("")
    if (selection == 1):
      gameGrid,copyGrid = gridCreate()
      humanvsAI(gameGrid,copyGrid)
      break
    elif (selection == 2):
      gameGrid,copyGrid = gridCreate()
      AIvshumans(gameGrid,copyGrid)
      break
    elif (selection == 3):
      gameGrid,copyGrid = gridCreate()
      humans(gameGrid,copyGrid)
      break
    elif (selection == 4):
      gameGrid,copyGrid = gridCreate()
      simulate(gameGrid,copyGrid)
      break
    else: print("Invalid selection!")

def printGrid(grid):
  for r in grid:
      for c in r:
          print(c,end = " ")
      print()

def example():
  example = [[0,0],[0,0]]
  print("For the example below, if you want to choose to hide at the top right corner, type in '1,0'\n")
  printGrid(example)
  print("\n")
  example[0][1] = "x"
  print("The grid will then become the following:\n")
  printGrid(example)
  print("\n")
  print("Please type in 5 different coordinates. Press enter after each one.")

def gridCreate():
  initialGrid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
  copyGrid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
  print("This is the current grid:\n")
  printGrid(initialGrid)
  print("\n")
  return initialGrid, copyGrid

def humanvsAI(grid,copy):
  example()
  for i in range(5):
    while(True):
      userin = input()
      if (len(userin) != 3) or int(userin[0]) > 7 or int(userin[2]) > 7: print("Coordinate not valid!")
      else: 
        x = int(userin[0])
        y = int(userin[2]) 
        if (grid[y][x] == "X"): print("Coordinate taken already")
        else: 
          grid[y][x] = "X"
          break
       
  print("The grid is now:\n")
  printGrid(grid)
  print("\n")
  print("Is this okay? Type 'yes' or 'no'")
  userin = input()
  
  if userin == "yes":
    counter = 0
    print("Computer is guessing!")
    for i in range(5):
      x = random.randint(0, 7)
      y = random.randint(0, 7)
      if grid[y][x] == "X": counter += 1
    print("The computer found ", counter)
  else:
    printGrid(copy)
    grid = copy
    humanvsAI(grid,copy)

def AIvshumans(grid,copy):
  example()
  for i in range(5):
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if grid[y][x] == "X": i -=1
    else: grid[y][x] = "X"
    #print(x,y) debugging purposes
    
  counter = 0
  for i in range(5):
    while(True):
      userin = input()
      if (len(userin) != 3) or int(userin[0]) > 7 or int(userin[2]) > 7: print("Coordinate not valid!")
      else: 
        x = int(userin[0])
        y = int(userin[2]) 
        if (grid[y][x] == "X"): counter += 1
        break
  print("You have found ",counter)

def humans(grid,copy):
  print("Determine who will start off as the hider or seeker")
  print("The seeker must leave the room or turn away from the computer screen\n")
  
  example()
  for i in range(5):
    while(True):
      userin = input()
      if (len(userin) != 3) or int(userin[0]) > 7 or int(userin[2]) > 7: print("Coordinate not valid!")
      else: 
        x = int(userin[0])
        y = int(userin[2]) 
        if (grid[y][x] == "X"): print("Coordinate taken already")
        else: 
          grid[y][x] = "X"
          break
  print("The grid is now:\n")
  printGrid(grid)
  print("\n")
  print("Is this okay? Type 'yes' or 'no'")
  userin = input()
  
  if userin == "yes":
    for i in range(100):
      print("\n")
    print("It is now the seeker's turn to find the hider.")
    print("Seeker, please choose 5 different spots.")
    count = 0
    for i in range(5):
      while(True):
        userin = input()
        if (len(userin) != 3) or int(userin[0]) > 7 or int(userin[2]) > 7: print("Coordinate not valid!")
        else: 
          x = int(userin[0])
          y = int(userin[2]) 
        if (grid[y][x] == "X"): count += 1
        else: break
    print("You have found: ", count)

  else:
    printGrid(copy)
    grid = copy
    humans(grid,copy)

def simulate(grid, copy):
  number0 = 0
  number1 = 0
  number2 = 0
  number3 = 0
  number4 = 0
  number5 = 0
  number6 = 0
  number7 = 0
  Number0 = 0
  Number1 = 0
  Number2 = 0
  Number3 = 0
  Number4 = 0
  Number5 = 0
  Number6 = 0
  Number7 = 0
  numSim = 0
  counter = 0
  while(True):
    grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(5):
      x = random.randint(0, 7)
      y = random.randint(0, 7)
      if grid[y][x] == "X": i -=1
      else: 
        grid[y][x] = "X"
        if x == 0 or y == 0:   number0 += 1
        elif x == 1 or y == 1: number1 += 1
        elif x == 2 or y == 2: number2 += 1
        elif x == 3 or y == 3: number3 += 1
        elif x == 4 or y == 4: number4 += 1
        elif x == 5 or y == 5: number5 += 1
        elif x == 6 or y == 6: number6 += 1
        elif x == 7 or y == 7: number7 += 1
 
      a = random.randint(0, 7)
      b = random.randint(0, 7)
      if grid[a][b] == "X":  counter += 1
      if a == 0 or b == 0:   Number0 += 1
      elif a == 1 or b == 1: Number1 += 1
      elif a == 2 or b == 2: Number2 += 1
      elif a == 3 or b == 3: Number3 += 1
      elif a == 4 or b == 4: Number4 += 1
      elif a == 5 or b == 5: Number5 += 1
      elif a == 6 or b == 6: Number6 += 1
      elif a == 7 or b == 7: Number7 += 1
       
    
    numSim += 1
    if numSim == 10000: break
   
  print("Total numbers for CPU1:")
  print(number0 , "0's")
  print(number1 , "1's")
  print(number2 , "2's")
  print(number3 , "3's")
  print(number4 , "4's")
  print(number5 , "5's")
  print(number6 , "6's")
  print(number7 , "7's")
  print("Total numbers for CPU2:")
  print(Number0 , "0's")
  print(Number1 , "1's")
  print(Number2 , "2's")
  print(Number3 , "3's")
  print(Number4 , "4's")
  print(Number5 , "5's")
  print(Number6 , "6's")
  print(Number7 , "7's")
  print("There were ", counter , "matches")
menu()