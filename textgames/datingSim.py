#Parker Wong 30019077 T11
'''
There are two types of Tims in this simulation: a 'Pursuer' and a 'Target'. The target is the object of the pursuer's desire. The behaviour of both types of Tims is purely random. The date consists of a number of social interactions between two Tims broken down into discrete time units. Each type of Tim will engage in one of two types of interactions: type X-behaviour and type Y-behaviour. If the two Tims engage in the same type of interaction then that interaction is deemed as successful (in this simulation opposites do not attract) otherwise the interaction is deemed as a failure. A summary report will be generated after each interaction briefly showing the result of the interaction for that time unit. At the end of the simulation a more detailed report will show overall results.
'''


import random
class Pursuer:
  #The initialize method defines probabilityX and probabilityY which control the probability of the behaviour for the pursuer being either x or y along with displaying the statistics of how many x's and y's there are.
  #parameters are probabilityX and probabilityY
  def __init__(self,probabilityX,probabilityY):
    self.probabilityX = probabilityX
    self.probabilityY = probabilityY
    self.counterX = 0
    self.counterY = 0
  #pursuerInteracts method produces a random number between 0 and 100 and if that number is less than or equal to the probability specified by the user, then the behaviour for the pursuer will be x, otherwise it will be y.
  #parameters passed is self.probabilityX and self.counterX
  #returns self.behaviour
  def pursuerInteracts(self):
    self.probability = random.randrange(0,100)
    if self.probability <= self.probabilityX:
      self.behaviour = "x"
      self.counterX += 1
    else:
      self.behaviour = "y"
      self.counterY += 1
    return self.behaviour
  #pursuerStats method displays the number of x's and y's for the pursuer
  #parameters passed are self.counterX and self.counterY
  #no return values
  def pursuerStats(self):
    print("Pursuer statistics:")
    print("Number of X's:" , self.counterX, "\tNumber of Ys:", self.counterY,"\n")
  
class Target:
  #The initialize method defines probabilityX and probabilityY which control the probability of the behaviour for the target being either x or y along with displaying the statistics of how many x's and y's there are.
  #parameters are probabilityX and probabilityY
  def __init__(self,probabilityX,probabilityY):
    self.probabilityX = probabilityX
    self.probabilityY = probabilityY
    self.counterX = 0
    self.counterY = 0
  #targetInteracts method produces a random number between 0 and 100 and if that number is less than or equal to the probability specified by the user, then the behaviour for the pursuer will be x, otherwise it will be y.
  #parameters passed is self.probabilityX and self.counterX
  #returns self.behaviour
  def targetInteracts(self):
    self.probability = random.randrange(0,100)
    if self.probability <= self.probabilityX:
      self.behaviour = "x"
      self.counterX += 1
    else:
      self.behaviour = "y"
      self.counterY += 1
    return self.behaviour
  #targetStats method displays the number of x's and y's for the pursuer
  #parameters passed are self.counterX and self.counterY
  #no return values    
  def targetStats(self):
    print("Target statistics:")
    print("Number of X's:" , self.counterX, "\tNumber of Y's:", self.counterY,"\n")
    
class Manager:
  #The initialize method defines the respective probabilities to both the pursuer and the target having both x and y values. It also defines there is a match or failure. 
  #parameters are pursuerX,pursuerY,targetX,targetY
  #no return values
  def __init__(self,pursuerX,pursuerY,targetX,targetY):
    self.pursuerX = pursuerX
    self.pursuerY = pursuerY
    self.targetX = targetX
    self.targetY = targetY
    self.pursuer = Pursuer(self.pursuerX,self.pursuerY)
    self.target = Target(self.targetX,self.targetY)
    self.match = 0
    self.nomatch = 0
  #simulateRange method asks the user for input for a number between 1 and 100 and if the user inputs either an incorrect range or input, it will repeat itself via recursion.
  #no parameters being passed to method
  #returns self.simulate
  def simulateRange(self):
    try:
      self.simulate = int(input("Enter the number of simulations (1-100): "))
      if self.simulate >= 1 and self.simulate <= 100:
        return self.simulate
      else:
        print("Please enter number within the correct range.\n")
        self.simulateRange()
      
    except ValueError:
      print("Must be an integer number.")
      self.simulateRange()
  #display method shows the results for each turn by displaying the result of each behaviour type for both the pursuer and the target by referring back to the pursuerInteracts() and targetInteracts() method. If there is a match, x=x or y=y then it will display that there is a match and tally it. 
  #parameters passed is self.match and self.nomatch, self.pursuer and self.target are also being referred
  #returns no values
  def display(self):
    for i in range(self.simulate):
      pursuerBehaviour = self.pursuer.pursuerInteracts()
      targetBehaviour = self.target.targetInteracts()
      if pursuerBehaviour == targetBehaviour:
        print("Turn #" , i+1, "\t", "Match:" , "Pursuer", pursuerBehaviour, "Target", targetBehaviour , "\n")
        self.match += 1
      else:
        print("Turn #" , i+1, "\t", "No Match:" , "Pursuer", pursuerBehaviour, "Target", targetBehaviour , "\n")
        self.nomatch += 1
  #results method displays the respective statistics for both the pursuer and target along with calculating the Proportions of matches and mismatches
  #parameters passed are self.match,self.nomatch and self.simulate along with referring back to self.pursuer and self.target
  #returns no values
  def results(self):   
    self.pursuer.pursuerStats()
    self.target.targetStats()
    print("End of simulation, final results:")
    print("# of Matches:", self.match , "\t# of mismatches:", self.nomatch)
    print("Proportions of matches:" , "% 0.2f" % (self.match/self.simulate*100) ,"%")
    print("Proportions of mismatches:", "% 0.2f" % (self.nomatch/self.simulate*100) ,"%")
  #start method gives the user the input to enter the probabilities for the Pursuer and the target and checks to see if it equals to 100. If it does not or there is an value error, then it will repeat itself via recursion until there is correct input. Then it will call the other methods in the Manager class which goes from the input for number of simulations to displaying the turns and finally displaying the results.
  #parameters being passed are pursuerX, pursuerY,targetX,targetY
  #no return values
  def start(self):
    try:
      print("Entering the probabilities for the 'Pursuer' type of Tim. The sum of the two probabilities must be 100%.")
      pursuerX = int(input("Enter the probability that X-type of behaviours will occuring during an interaction during the date:"))
      pursuerY = int(input("Enter the probability that Y-type of behaviours will occuring during an interaction during the date:"))
      
      sumPursueXY = pursuerX + pursuerY
      if sumPursueXY != 100:
        print("The probabilities must sum to 100%. Please try again.")
        self.start()
      else:
        print()
    except ValueError:
      print("Numbers must be integers. Please try again.")
      self.start()
    try:
      print("Entering the probabilities for the 'Target' type of Tim. The sum of the two probabilities must be 100%.")
      targetX = int(input("Enter the probability that X-type of behaviours will occuring during an interaction during the date:"))
      targetY = int(input("Enter the probability that Y-type of behaviours will occuring during an interaction during the date:"))
      
      sumTargetXY = targetX + targetY
      if sumTargetXY != 100:
        print("The probabilities must sum to 100%. Please try again.")
        self.start()
      else:
        print()
    except ValueError:
      print("Numbers must be integers. Please try again.")
      self.start()
    simulation = Manager(pursuerX,pursuerY,targetX,targetY)
    simulation.simulateRange()
    simulation.display()
    simulation.results()
#main function creates a manager object to call the Manager class which holds the program
#no parameters
#no return values
def main():
  pursuerX = 0
  pursuerY = 0
  targetX = 0
  targetY = 0
  manager = Manager(pursuerX,pursuerY,targetX,targetY)
  manager.start()


main()