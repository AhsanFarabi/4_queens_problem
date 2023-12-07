# 4 Queens Problem

This Python script solves the N-Queens problem using a local search algorithm called hill climbing.

## Introduction

The N-Queens problem is a classic combinatorial problem where the challenge is to place N chess queens on an N×N chessboard so that no two queens threaten each other. The solution provided here uses a local search approach, specifically hill climbing.

## Usage

To run the script, provide the initial locations of queens in the `queen_locations` list. The script will output the initial and final states of the chessboard along with the cost.

```python
# Example usage:
queen_locations = [[2, 0], [1, 1], [2, 2], [1, 3]]
queen_instance = Queen(queen_locations)

print("Initial State:")
for row in queen_instance.chess_board:
    print(row)

initial_cost, _, _ = calc_cost(queen_instance.state)
local_search(queen_instance, initial_cost)

print("Final State:")
for row in queen_instance.chess_board:
    print(row)
