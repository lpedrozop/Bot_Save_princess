
[![N|Py](https://macondolab.com/wp-content/uploads/2021/07/Python-logo-600x174.png)](https://macondolab.com/wp-content/uploads/2021/07/Python-logo-600x174.png)
# Bot Save the Princess



A common problem when starting out with AI is achieving a specific goal in a grid environment. Although the challenge of "Bot Save the Princess" is simple, it stands out for its clarity of objective, which consists of making the Bot reach the princess with the least amount of movements, since it is a dynamic grid and has obstacles, it must Reach your target (the princess).

### Description of the solution

#### Environment
- Structure: Two-dimensional matrix, which will simulate a grid of size N * N, this will act as a board and determine how the Bot moves and where the princess is.
- Cell: Each cell represents a state through characters.
- ‘-‘: Indicates that the cell is empty and is traversable by the Bot.
- 'm': Denotes the current position of the Bot on the grid.
- 'p': Position of the princess.
- 'X': Represents an obstruction. This cell is impassable for the Bot.
#### Princess and Bot.
- Princess ( p ): Objective of the Bot. Located in a static position within the board.
- Bot (m): Agent that requires finding and reaching the princess. With an initial position that will be affected by the breadth-finding algorithm to find the shortest path to the princess.

#### Moves
- Restrictions: The Bot's movements will have movement restrictions on the board as long as there are obstacles (X), and it will not be able to move outside the structure.
- Types: The Bot can move in 4 directions, Left, Right, Down, Up.
#### Breadth Search Algorithm
- Queue: Essential data structure for the management of nodes to be explored, guaranteeing that the nodes are visited in the order they are discovered.
- Visited: This matrix has the same size as the environment, this allows marking the cells that have already been visited to prevent the nodes from being visited more than once.
- Path: List of movements that the Bot requires to reach its objective, this is built as the exploration of nodes is carried out.
