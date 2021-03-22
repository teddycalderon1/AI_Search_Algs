# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    posPath = util.Stack() # keep track of fringe nodes as possible Path
    posPath.push((problem.getStartState(), [], 1)) # add first state to stack
    explored = [] #make list of explored nodes
    
    while not posPath.isEmpty(): #include a flag as while loop
        node = posPath.pop()
        state = node[0]
        path = node[1]

        if problem.isGoalState(state): #ouput if in goal state
            return path
        if state not in explored: #move on and repeat if not in goal state
            explored.append(state)
            successors = problem.getSuccessors(state)
            for child in successors:
                childState = child[0]
                childPath = child[1]
                if childState not in explored:
                    childPath = path + [childPath]
                    posPath.push((childState, childPath, 1))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    posPath = util.Queue() #bfs uses queue
    posPath.push((problem.getStartState(), [], 1)) # add first state to stack
    explored = [] #make list of explored nodes
    
    while not posPath.isEmpty(): #include a flag as while loop
        node = posPath.pop()
        state = node[0]
        path = node[1]

        if problem.isGoalState(state): #output if in goal state
            return path
        if state not in explored: #move to next if not in goal state
            explored.append(state)
            successors = problem.getSuccessors(state)
            for child in successors:
                childState = child[0]
                childPath = child[1]
                if childState not in explored:
                    childPath = path + [childPath]
                    posPath.push((childState, childPath, 1))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first.
    Important functions to implement
    1 - PriorityQueue
    2 - problem.getStartState()
    3 - problem.isGoalState(xy)
    4 - problem.getSuccessors(xy)
    5 - problem.getCostOfActions(new_path)
    """
    "*** YOUR CODE HERE ***"
    posPath = util.PriorityQueue() #ucs uses queue
    explored = [] #make list of explored nodes
    posPath.push((problem.getStartState(), []), 1) # add first state to stack
    
    
    while not posPath.isEmpty(): #include a flag as while loop
        node = posPath.pop()
        state = node[0]
        path = node[1]

        if problem.isGoalState(state):
            return path
        if state not in explored:
            explored.append(state)
            successors = problem.getSuccessors(state)
            for child in successors:
                childState = child[0]
                childPath = child[1]
                if childState not in explored:
                  childPath = path + [childPath]
                  cost = problem.getCostOfActions(childPath)
                  posPath.push((childState, childPath), cost)
    util.raiseNotDefined()
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    posPath = util.PriorityQueue() #astar uses priority queue
    posPath.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem)) # add first state to stack
    explored = [] #make list of explored nodes
    
    while not posPath.isEmpty(): #include a flag as while loop
        node = posPath.pop()
        state = node[0]
        path = node[1]

        if problem.isGoalState(state):
            return path
        if state not in explored:
            explored.append(state)
            successors = problem.getSuccessors(state)
            for child in successors:
                childState = child[0]
                childPath = child[1]
                if childState not in explored:
                  childPath = path + [childPath]
                  cost = problem.getCostOfActions(childPath)
                  posPath.push((childState, childPath, 0), cost + heuristic(childState, problem))
    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

