# 4-Queens Local Search

This Python script uses a local search algorithm to solve the N-Queens problem. The N-Queens problem is a classic combinatorial problem where the goal is to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other.

## Queen Class

The `Queen` class is used to represent the chessboard and the placement of queens on it. It provides methods to add queens to the chessboard and get neighbors for a given queen.

## Local Search Algorithm

The `local_search` function implements a basic local search algorithm, specifically hill-climbing, to find a solution to the N-Queens problem. The algorithm starts with an initial placement of queens and iteratively moves queens to reduce conflicts until a solution is found.

## Usage

To use the script, create an instance of the `Queen` class by providing the initial queen locations in the form of a list of coordinates. Then, call the `add_queen` method to initialize the chessboard. Finally, call the `local_search` method to apply the local search algorithm and find a solution.

```python
# Example Usage
L = [[2, 0], [1, 1], [2, 2], [1, 3]]  # 4 Queens Locations
N = len(L)
q = Queen(L, N)
q.add_queen()
cur_cost, _, _ = calculate_cost(q.queen_loc)
local_search(q.queen_loc, cur_cost)
