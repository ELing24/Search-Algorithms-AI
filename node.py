class Node:
    #for A* g(n) + h(n) = cost to get to node + estimated distance to goal 
    def __init__(self, costOfNode = 0, estimatedDistance = 0, position = None, parent = None, state = None):
        self.costOfNode = costOfNode
        self.estimatedDistance = estimatedDistance
        self.position = position
        self.parent = parent
        self.state = state

    def setCostOfNode(self, cost):
        self.costOfNode = cost

    def setEstimatedDistance(self, distance):
        self.estimatedDistance = distance
    
    def setPosition(self, position):
        self.position = position

    def setParent(self, parent):
        self.parent = parent
        
    def getcostOfNode(self):
        return self.costOfNode
    
    def getState(self):
        return self.state
    
    def getEstimatedDistance(self):
        return self.estimatedDistance
    
    def getPosition(self):
        return self.position
    
    def getSolutionPath(self):
        pathStartingFromLeaf = []
        curr = self
        while curr is not None:
            pathStartingFromLeaf.append(curr)
            for i in curr.getState():
                print(i)
            print("g(n) = " + str(curr.getcostOfNode()) + " and " + "h(n) = " + str(curr.getEstimatedDistance()))
            print("\n")
            curr = curr.parent
        return pathStartingFromLeaf
    def __lt__(self, other):
        return (self.costOfNode + self.estimatedDistance) < (other.costOfNode+ other.estimatedDistance)
