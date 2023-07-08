# PathPlanning-Py

Single robot path planning algorithms implemented in Python. Including heuristic search and incremental heuristic search methods.

## Methods

- A* (can turn into Dijkstra by changing the heuristic function)
- LPA*(Life Long Planning A*)
- D*Lite

## Run

- Go into the methods directory.
- Run the **RUN_[Methods_name].m** file
  - AStar/RUN_Astar.py
  - LPAStar/RUN_LPAstar.py
  - DStarLite/RUN_DstarLite.y

## General

Apart from each path planning method's directory, there are other general directories:

- **common**: common functionalities used in all planning methods
- ...

## Dependencies

- python3
- numpy
- matplotlib