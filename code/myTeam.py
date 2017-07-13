from captureAgents import CaptureAgent
import random
import game
from game import Directions

#################
# Team creation #
#################

# do not change this function
def createTeam(firstIndex, secondIndex, isRed, first = 'AgentA', second = 'AgentB'):
	return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########

class AgentA(CaptureAgent):

	def registerInitialState(self, gameState):
		# do not delete the following line
		CaptureAgent.registerInitialState(self, gameState)

		'''
		Your initialization code goes here, if you need any.
		'''


		
		
	def chooseAction(self, gameState):
		'''
		This method must return one of the following values:
		Directions.NORTH
		Directions.SOUTH
		Directions.EAST
		Directions.WEST
		Directions.STOP
		'''

		width = self.getFood(gameState).width
		height = self.getFood(gameState).height
		score = self.getScore(gameState)
		
		actions = gameState.getLegalActions(self.index)
		enemies = self.getOpponents(gameState)
		enemy1Position = gameState.getAgentPosition(1)
		enemy2Position = gameState.getAgentPosition(3)
		teammatePosition = gameState.getAgentPosition(0)		
		
		#wall = gameState.hasWall(x, y)
		
		myPosition = gameState.getAgentPosition(self.index)
		
		food = gameState.getAgentState(self.index).numCarrying
		foodToEat = self.getFood(gameState).asList(True)
		foodToProtect = self.getFoodYouAreDefending(gameState).asList(True)
		
		capsulesToProtect = self.getCapsulesYouAreDefending(gameState)
		capsulesToEat = self.getCapsules(gameState)	
		
		scared = gameState.getAgentState(self.index).scaredTimer
		
		distanceToClosestFood = self.getMazeDistance(myPosition, getClosestFood(self, myPosition, foodToEat))
		pacman = gameState.getAgentState(self.index).isPacman
		
		print distanceToClosestFood
		
		if len(foodToEat) > 0 and myPosition[0] < width - 2 and ((distanceToClosestFood <= 18 and food == 0) or (distanceToClosestFood <= 5 and food > 0)):
			if scared and enemy1Position != None:
				return getBestDirection(self, myPosition, enemy1Position, actions)
			
			elif scared and enemy2Position != None:
				return getBestDirection(self, myPosition, enemy2Position, actions)
			
			elif enemy1Position == None and enemy2Position == None:
				return getBestDirection(self, myPosition, getClosestFood(self, myPosition, foodToEat), actions)
			elif (enemy1Position != None and enemy1Position[0] <  width/2) or (enemy2Position != None and enemy2Position[0] <  width/2):
				return getBestDirection(self, myPosition, getClosestFood(self, myPosition, foodToEat), actions)
			#elif ((enemy1Position != None and enemy1Position[0] <  (width/2)+2 and enemy1Position[0] >  (width/2)-1 and myPosition[0] >= enemy1Position[0] and myPosition[0] < enemy1Position[0]+1) or (enemy2Position != None and enemy2Position[0] <  (width/2)+2 and myPosition[0] >= enemy2Position[0] and myPosition[0] < enemy2Position[0]+1) and enemy2Position[0] <  (width/2)-1) and myPosition[0] <= (width/2) and myPosition[0] > (width/2)-2 :
				#return Directions.STOP
			else:	
				'''
				option = random.randint(1,10)
				if option > 9 and len(foodToProtect) > 0 and len(capsulesToEat) > 0:
					return getBestDirection(self, myPosition, getClosestFood(self, myPosition, capsulesToEat) , actions)
				else:
				'''
				d1 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)+3))
				d2 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)))
				d3 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)-3))
				if d1 <= d2 and d1 <= d3:
					return getBestDirection(self, myPosition, ((width/2)-1,(height/2)+3) , actions)
				elif d2 <= d1 and d2 <= d3:
					return getBestDirection(self, myPosition, ((width/2)-1,(height/2)) , actions)
				else:
					return getBestDirection(self, myPosition, ((width/2)-1,(height/2)-3) , actions)					
				
			
		else:
			d1 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)+3))
			d2 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)))
			d3 = self.getMazeDistance(myPosition, ((width/2)-1,(height/2)-3))
			if d1 <= d2 and d1 <= d3:
				return getBestDirection(self, myPosition, ((width/2)-1,(height/2)+3) , actions)
			elif d2 <= d1 and d2 <= d3:
				return getBestDirection(self, myPosition, ((width/2)-1,(height/2)) , actions)
			else:
				return getBestDirection(self, myPosition, ((width/2)-1,(height/2)-3) , actions)
			
			
	

def getClosestFood(agent, pos, foodToEat):
	smallestDistance = 999999
	target = None
	for i in foodToEat:
		d = agent.getMazeDistance(pos, i)
		if d < smallestDistance:
			smallestDistance = d
			target = i
	return target
	
def getBestDirection(agent, pos, target, actions):
	smallestDistance = 999999
	bestDirection = None
	actions.remove(Directions.STOP)
	for i in actions:
		otherPoint = getPoint(pos, i)	
		d = agent.getMazeDistance(otherPoint, target)
		if d < smallestDistance:
			smallestDistance = d
			bestDirection = i
	return bestDirection
	
def getPoint(pos, direction):
	if direction == Directions.NORTH:
		return pos[0], pos[1] + 1
	elif direction == Directions.SOUTH:
		return pos[0], pos[1] - 1
	elif direction == Directions.EAST:
		return pos[0] + 1, pos[1]
	elif direction == Directions.NORTH:
		return pos[0] - 1, pos[1]
	else:
		return pos
	
	

class AgentB(CaptureAgent):

	def registerInitialState(self, gameState):
		# do not delete the following line
		CaptureAgent.registerInitialState(self, gameState)

		'''
		Your initialization code goes here, if you need any.
		'''


	
		
	def chooseAction(self, gameState):
		'''
		This method must return one of the following values:
		Directions.NORTH
		Directions.SOUTH
		Directions.EAST
		Directions.WEST
		Directions.STOP
		'''
		width = self.getFood(gameState).width
		height = self.getFood(gameState).height
		score = self.getScore(gameState)
		
		actions = gameState.getLegalActions(self.index)
		enemies = self.getOpponents(gameState)
		enemy1Position = gameState.getAgentPosition(1)
		enemy2Position = gameState.getAgentPosition(3)
		teammatePosition = gameState.getAgentPosition(0)		
		
		#wall = gameState.hasWall(x, y)
		#d = self.getMazeDistance((x1, y1), (x2, y2))
		myPosition = gameState.getAgentPosition(self.index)
		
		food = gameState.getAgentState(self.index).numCarrying
		foodToEat = self.getFood(gameState).asList(True)
		foodToProtect = self.getFoodYouAreDefending(gameState).asList(True)
		
		capsulesToProtect = self.getCapsulesYouAreDefending(gameState)
		capsulesToEat = self.getCapsules(gameState)	
		
		scared = gameState.getAgentState(self.index).scaredTimer
		
		if scared == False and  myPosition[0] +1 < width/2:
		
			if enemy1Position != None:
				return getBestDirection(self, myPosition, enemy1Position, actions)
			elif enemy2Position != None:
				return getBestDirection(self, myPosition, enemy2Position, actions)
			else:	
				option = random.randint(1,10)
				if option > 9 and len(foodToProtect) > 0:
					return getBestDirection(self, myPosition, getClosestFood(self, myPosition, foodToProtect) , actions)
				else:
					return getBestDirection(self, myPosition, ((width/2)-1,height/2) , actions)
					
			
		else:
			return getBestDirection(self, myPosition, ((width/2)-1,height/2) , actions)
			