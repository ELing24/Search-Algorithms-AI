from Problem import Problem
from misplacedHeuristic import misplacedHeuristic
from euclidianHeuristic import euclideanHeuristic
from uniformCost import uniformCost
puzzle = [[4,1,2],[5,3,0],[7,8,6]]

print("Welcome to XXX (change this to your student ID) 8 puzzle solver.\n")
print("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
puzzleOptionInput = int(input())
print("\n")

if puzzleOptionInput == 2:
    print("Enter your puzzle, use a zero to represent the blank \n")
    
    for i in range(0, 3):
        column = []

        if i == 0:
            print("Enter the first row, use space or tabs between numbers     ")
        elif i == 1:
            print("Enter the second row, use space or tabs between numbers    ")
        elif i == 2:
            print("Enter the third row, use space or tabs between numbers     ")
        
        for j in range(0, 3):
            columnInput = int(input())
            column.append(columnInput)
        puzzle.append(column)
    print("\n")
    

print("Enter your choice of algorithm")
print("Uniform Cost Search\nA* with the Misplaced Tile heuristic.\nA* with the Euclidean distance heuristic.\n")
algorithmChoice = int(input())
print("\n")

if algorithmChoice == 1:
    problem = Problem(puzzle)
    uniformCost(problem)
elif algorithmChoice == 2:
    problem = Problem(puzzle)
    misplacedHeuristic(problem)
elif algorithmChoice == 3:
    problem = Problem(puzzle)
    euclideanHeuristic(problem)