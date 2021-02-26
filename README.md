# Pac-Man

## Test Procedures

### Depth First Search 
`python pacman.py -l tinyMaze -p SearchAgent`, `python pacman.py -l mediumMaze -p SearchAgent`, `python pacman.py -l bigMaze -z .5 -p SearchAgent`


### Breadth First Search
`python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`, `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5`

### Uniform Cost Search
`python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`, `python pacman.py -l mediumDottedMaze -p StayEastSearchAgent`, `python pacman.py -l mediumScaryMaze -p StayWestSearchAgent`

### A* search
`python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

### Comparison
`python pacman.py -l openMaze -p SearchAgent`, `python pacman.py -l openMaze -p SearchAgent -a fn=bfs`, `python pacman.py -l openMaze -p SearchAgent -a fn=ucs`, `python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

### Corners Problem: Heuristic
`python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`

### Eating All The Dots: Heuristic
`python pacman.py -l trickySearch -p AStarFoodSearchAgent`, `python pacman.py -l oneDotFocus -p AStarFoodSearchAgent`, `python pacman.py -l largeGrid -z 0.25 -p AStarFoodSearchAgent`

### Suboptimal Search
`python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 `
