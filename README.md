# AI_Search_Algs
## Intro to Artificial Intelligence Search Algorithms covered:
- **Depth First Search**

Implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py.
The code should be able to solve these tasks quickly.
1.	python pacman.py -l tinyMaze -p SearchAgent
2.	python pacman.py -l mediumMaze -p SearchAgent
3.	python pacman.py -l bigMaze -z .5 -p SearchAgent

Evaluation: Run the following command to test your solution: python autograder.py -q q1

- **Breadth- first search**

Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py.
The code should be able to solve these tasks quickly.
1.	python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
2.	python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
Evaluation: Run the following command to test your solution: python autograder.py -q q2. 

- **Uniform Cost Search**

Implement the uniform-cost search (UCS) algorithm in the uniformCostSearch function in search.py 
The should now observe successful behavior in all three of the following layouts.
1.	python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
2.	python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
3.	python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

Evaluation: Run the following command to test your solution: python autograder.py -q q3.

- **A\* Search**

Implement the A* search algorithm in the aStarSearch function in search.py. A* takes a heuristic function as an argument.
Evaluation: Run the following command to test your solution: python autograder.py -q q4. 

- **Minimax search**

Write an adversarial agent in the provided MinimaxAgent class in multiAgents.py.
Minimax agent should work with any number of ghosts, so the algorithm should be a more generalized version of the standard Minimax algorithm that we have studied in the class. Your minimax tree will have multiple min layers (one for each ghost) for each max layer. Your code should also be able to expand the tree to an arbitrary depth which can be accessed from self.depth and score your nodes with the supplied self.evaluationFunction. Make sure your Minimax program refers to these variables since these are populated in response to the command line options.
  
**Hints & Observations**:
1.  The correct implementation of minimax will lead to Pacman losing the game in some tests. This is not a problem: as it is correct behavior, it will pass the tests.
2.  The evaluation function for the Pacman test in this part is implemented for you (self.evaluationFunction). You should not change this function but recognize that now we are evaluating states rather than actions, as compared to the reflex agent. Look-ahead agents evaluate future states whereas reflex agents evaluate actions from the current state.
3.  Pacman is always agent 0, and the agents move (take turns) in order of increasing agent index.
4.  All states in minimax should be GameStates, either passed in to getAction or generated via GameState.generateSuccessor. In this project, you will not be abstracting to simplified states.

Evaluation: The code will be checked to determine whether it explores the correct number of game states. This is the only reliable way to detect some very subtle bugs in implementations of minimax. As a result, the autograder will be very picky about how many times you call GameState.generateSuccessor. If you call it any more or less than necessary, the autograder will complain. Please note that q1 relates to ReflexAgent which is not a part of this homework and can be skipped. We will start with q2 in this homework. To test and debug your code, run python autograder.py -q q2

- **Alpha-beta pruning**:

Write an adversarial agent in the provided AlphaBetaAgent class in multiAgents.py to more efficiently explore the minimax tree. 

Evaluation: The code will be checked to determine whether it explores the correct number of game states. Therefore, it is important that you perform alpha-beta pruning without reordering children. In other words, successor states should always be processed in the order returned by GameState.getLegalActions. Again, do not call GameState.generateSuccessor more than necessary. Additionally, in order to match the set of states explored by the autograder, you must not prune on equality: that is, stop generating children for a max (min) node only if a child's value is strictly greater than (less than) β (α).

To test and debug your code, run
python autograder.py -q q3

This will show what your algorithm does on a number of small trees, as well as a pacman game. To run it without graphics, use:
python autograder.py -q q3 --no-graphics

- **Expectimax Search**

Implement the ExpectimaxAgent, which is useful for modeling probabilistic behavior of agents who may make suboptimal choices. As with the search and constraint satisfaction problems covered in CSE 5120, the impressive feature of this algorithm is its general applicability. 

Note: The correct implementation of expectimax will lead to Pacman losing some of the tests. This is not a problem: as it is correct behavior, it will pass the tests.

Evaluation: You can debug your implementation on small the game trees using the command:
python autograder.py -q q4
