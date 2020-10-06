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
from util import *

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
    
#def genericSearch(problem, structure):
    

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
        
    stack = Stack()
    
    stack.push(([problem.getStartState()],[]))
    
    while 1:
        if stack.isEmpty():
            return []
            
        path, actions = stack.pop()
        state = path[-1]
        
        if problem.isGoalState(state):
            return actions
        
        succs = problem.getSuccessors(state)
        for succ in succs:
            if succ[0] not in path:
                new_path = list(path)
                new_path.append(succ[0])
                new_actions = list(actions)
                new_actions.append(succ[1])
                stack.push((new_path,new_actions))
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
        
    queue = Queue()
    queue.push(([problem.getStartState()],[]))
    seen = []
    
    while 1:
        if queue.isEmpty():
            return []
            
        path, actions = queue.pop()
        state = path[-1]
        
        if problem.isGoalState(state):
            return actions
            
        succs = problem.getSuccessors(state)
        for succ in succs:
            if succ[0] not in path and succ[0] not in seen:
                seen.append(succ[0])
                new_path = list(path)
                new_path.append(succ[0])
                new_actions = list(actions)
                new_actions.append(succ[1])
                queue.push((new_path,new_actions))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
    p_queue = PriorityQueue()
    p_queue.push(([problem.getStartState()],[]),0)
    seen = []
    while 1:
        if p_queue.isEmpty():
            return []
            
        path, actions = p_queue.pop()
        state = path[-1]
        
        if problem.isGoalState(state):
            return actions
            
        succs = problem.getSuccessors(state)
        
        for succ in succs:
            if succ[0] not in path and succ[0] not in seen:
                seen.append(succ[0])
                new_path = list(path)
                new_path.append(succ[0])
                new_actions = list(actions)
                new_actions.append(succ[1])
                priority = problem.getCostOfActions(new_actions)
                p_queue.push((new_path,new_actions),priority)
                
            elif succ[0] not in path and succ[0] in seen:
                old_priority = -1
                for item in p_queue.heap:
                    if item[2][0][-1] == succ[0]:
                        old_priority = problem.getCostOfActions(item[2][-1])
                        
                new_priority = problem.getCostOfActions(actions + [succ[1]])
                
                if old_priority > new_priority:
                    new_actions = actions + [succ[1]]
                    new_path = list(path)
                    new_path.append(succ[0])
                    p_queue.update((new_path,new_actions),new_priority)
        

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
    
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    class myComp:
        def  __init__(self,g,h):
            self.g = g
            self.h = h
            
        def __lt__(self, other):
            if (self.g + self.h) < (other.g + other.h): return True
            if (self.g + self.h) == (other.g + other.h):
                if self.h < other.h: return True
            return False

    if problem.isGoalState(problem.getStartState()): return []
    p_queue = PriorityQueue()
    p_queue.push(([problem.getStartState()],[]),myComp(0,heuristic(problem.getStartState(), problem)))
    seen = {}
    while 1:
        if p_queue.isEmpty(): return []
        path, actions = p_queue.pop()
        state = path[-1]
        if problem.isGoalState(state): return actions
        if state in seen:
            if seen[state] < problem.getCostOfActions(actions): continue
        seen[state] = problem.getCostOfActions(actions)
        
        succs = problem.getSuccessors(state)
        for succ in succs:
            if succ[0] not in seen or problem.getCostOfActions(actions+[succ[1]]) < seen[succ[0]]:
                new_path = path + [succ[0]]
                new_actions = actions + [succ[1]]
                p_queue.push(([new_path,new_actions]),myComp(problem.getCostOfActions(new_actions),heuristic(succ[0], problem)))
                seen[succ[0]] = problem.getCostOfActions(new_actions)
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
