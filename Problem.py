class Problem:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.goalState = [[1,2,3],[4,5,6],[7,8,0]]
    def getInitialState(self):
        for i in range(3):
            for j in range(3):
                initialStateValue = self.puzzle[i][j]
                if(initialStateValue == 0):
                    return [i, j]
                
    def getGoalState(self):
        return self.goalState
    
    def getPuzzle(self):
        return self.puzzle

    def getMisplacedHeuristic(self, puzzle):
        totalMisplacedTiles = 0
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] != self.goalState[i][j]:
                    totalMisplacedTiles+=1
        return totalMisplacedTiles
    
    def getEuclideanHeuristic(self, puzzle):
        totalEuclidean = 0
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] != self.goalState[i][j]:
                    n = 0
                    m = 0
                    for y in range(3):
                        for z in range(3):
                            if puzzle[i][j] == self.goalState[y][z]:
                                n = y
                                m = z
                    n = (n - m) * (n - m)
                    m = (i - j) * (i - j)
                    while (n != 0) or (m != 0):
                        if n < 0:
                            totalEuclidean += 1
                            n += 1
                        if n > 0:
                            totalEuclidean += 1
                            n -= 1
                        if m < 0:
                            totalEuclidean += 1
                            m += 1
                        if m > 0:
                            totalEuclidean += 1
                            m -= 1
        return totalEuclidean

    def getAllMoves(self, position):
        xPos, yPos = position[0], position[1]

        listOfMoves = []
        if xPos > 0:
            listOfMoves.append("Up")
        if xPos < 2:
            listOfMoves.append("Down")
        if yPos > 0:
            listOfMoves.append("Left")
        if yPos < 2:
            listOfMoves.append("Right")
        return listOfMoves
    
    def result(self, state, move, zeroPosition):
        newState = [row[:] for row in state]
        xPos, yPos = zeroPosition
        newXPos, newYPos = 0,0
        if move == 'Up':
            newXPos = xPos - 1
            newYPos = yPos
        if move == 'Down':
            newXPos = xPos + 1
            newYPos = yPos
        if move == 'Left':
            newYPos = yPos - 1
            newXPos = xPos
        if move == 'Right':
            newYPos = yPos + 1
            newXPos = xPos
        valToSwap = newState[newXPos][newYPos]
        newState[newXPos][newYPos] = newState[xPos][yPos]
        newState[xPos][yPos] = valToSwap
        return [newState, [newXPos, newYPos]]

