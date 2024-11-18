from queue import PriorityQueue
from Problem import Problem
from node import Node
def euclideanHeuristic(Problem):
    Position = Problem.getInitialState()
    priorityQueue = PriorityQueue()
    priorityQueue.put((0, Node(0, 0, Position, None, Problem.getPuzzle())))
    exploredState = set()

    while priorityQueue:
        priority, node = priorityQueue.get()


        if Problem.getEuclideanHeuristic(node.getState()) == 0:
            node.getSolutionPath()
            break

        exploredState.add(tuple(tuple(row) for row in node.state))

        for move in Problem.getAllMoves(node.getPosition()):
            nodeState, Position = Problem.result(node.state, move, node.position)
            estimate = Problem.getEuclideanHeuristic(nodeState)
            cost = node.getcostOfNode() + 1
            newNode = Node(cost, estimate, Position, node, nodeState)
            if tuple(tuple(row) for row in nodeState) not in exploredState:
                priorityQueue.put((cost + estimate, newNode))

