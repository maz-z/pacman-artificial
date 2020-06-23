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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 0
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################

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
    "print ( problem.getStartState() )"
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***" 
    fringe = util.Stack()
    x = problem.getStartState()
    visited = []
    visited.append(x)
    fringe.push((x,[]))

    while not fringe.isEmpty():
        node, actions= fringe.pop()
        
        
        if problem.isGoalState(node):
            return actions
        
        visited.append(node)

        for child,direction,stpes in problem.getSuccessors(node):
            if not child in visited:
                fringe.push((child, actions + [direction]))
                visited.append(node)
                "print(actions)"

    return actions






def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    x = problem.getStartState()
    visited = []
    visited.append(x)
    fringe.push((x,[]))

    while not fringe.isEmpty():
        node, actions= fringe.pop()
        
        
        if problem.isGoalState(node):
            return actions
        
        visited.append(node)

        for child,direction,stpes in problem.getSuccessors(node):
            if not child in visited:
                fringe.push((child, actions + [direction]))
                visited.append(child)
                

    return actions

        



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
   

    fringe = util.PriorityQueue()
    x = problem.getStartState()
    visited = []
    #visited.append(x)
    #fringe.update(x,0)
    fringe.push((x,[],[]), nullHeuristic(x,problem))
    cost = {}
    cost[x] = 0

    while not fringe.isEmpty():
        index, actions, curcost = fringe.pop()
        visited.append(index)
        if problem.isGoalState(index):
            return actions
        
        for child, direction, steps in problem.getSuccessors(index):
            if not child in visited:
                priority = problem.getCostOfActions(actions) + steps + heuristic(child, problem)
                if child in cost:
                    if cost[child] <= priority:
                        continue
                fringe.update((child, actions + [direction],curcost+ [steps]),priority)
                cost[child] = priority
                #visited.append(child)
                
                

    return actions

    
    
        
    


def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    x = problem.getStartState()
    visited = []
    visited.append(x)
    fringe.push((x,[]),0)

    while not fringe.isEmpty():
        node, actions= fringe.pop()
        
        
        if problem.isGoalState(node):
            return actions
        
        visited.append(node)

        for child,direction,stpes in problem.getSuccessors(node):
            if not child in visited:
                depth = len(actions)
                fringe.push((child, actions + [direction]),depth)
                visited.append(node)
                "print(actions)"

    return actions


def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    x = problem.getStartState()
    visited = []
    visited.append(x)
    fringe.push((x,[]),0)
    count = 0

    while not fringe.isEmpty():
        node, actions= fringe.pop()
        
        
        if problem.isGoalState(node):
            return actions
        
        visited.append(node)

        for child,direction,stpes in problem.getSuccessors(node):
            if not child in visited:
                fringe.push((child, actions + [direction]), count)
                visited.append(child)
                

    return actions



#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""
<Your discussion goes here>
The course so far is engaing and informative. The total hour I spent with this project is approximatly 48 hours. 

"""



#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch