import numpy as np
import math
import random

class Queen:
    def __init__(self, L, N):
        self.L = L
        self.N = N
        self.queen_loc = dict()
        self.initialize = False

        self.chess_board = [[0] * self.N for _ in range(self.N)]

    def add_queen(self):
        if not self.initialize:
            number_Q = 0
            while True:
                Q = f"Q{number_Q}"
                self.queen_loc[Q] = [] 
                self.queen_loc[Q].append(self.L[number_Q][0])
                self.queen_loc[Q].append(self.L[number_Q][1])
                r, c = self.L[number_Q]
                self.chess_board[r][c] = Q
                number_Q += 1
                if number_Q == self.N:
                    break
            self.initialize = True

    def get_neighbor(self, row, col):
        neighbor = []
        if 0 <= row - 1 < self.N and self.chess_board[row - 1][col] == 0:
            neighbor.append([row - 1, col])
        if 0 <= row + 1 < self.N and self.chess_board[row + 1][col] == 0:
            neighbor.append([row + 1, col])
        return neighbor

def calculate_cost(state):
    def conflict(r1, c1, r2, c2):
        return r1 == r2 or c1 == c2 or r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2

    def get_conflict(Q, state):
        count = 0
        for q in state:
            if q is not Q:
                r1, c1 = state[Q]
                r2, c2 = state[q]
                if conflict(r1, c1, r2, c2):
                    count += 1
        return count

    cost = 0
    max_cost = -999
    max_cost_queen = None
    for Q in state:
        q_cost = get_conflict(Q, state)
        cost += q_cost
        if q_cost > max_cost:
            max_cost = q_cost
            max_cost_queen = Q

    return cost // 2, max_cost, max_cost_queen


def goal_test(state):
    return calculate_cost(state)[0] == 0


def local_search(state,cur_cost):
  while(goal_test(state) is False):
    cost, max_cost, max_cost_queen = calculate_cost(state)
    print("cost:",cost)
    # print(goal_test(state))
    r,c = state[max_cost_queen]
    q.chess_board[r][c] = 0

    choices = q.get_neighbor(r,c)
    for ch in choices:
      state[max_cost_queen] = ch
      
      cost, _, _ = calculate_cost(state)
      if(cost < cur_cost): # Hill-Climbing
         cur_cost = cost
         r,c = ch
         q.chess_board[r][c] = max_cost_queen
         break
    # print(state)

# Create an instance of the Queen class
L = [[2, 0], [1, 1], [2, 2], [1, 3]] # 4 Queens Locations
N = len(L)
q = Queen(L,N)
q.add_queen()

# Print the initial chess board
print("Initial Chess Board:")
for row in q.chess_board:
    print(row)

cur_cost, _, _ = calculate_cost(q.queen_loc)
local_search(q.queen_loc,cur_cost)


# Print Final Cost
final_cost, _, _ = calculate_cost(q.queen_loc)
print("Final Cost",final_cost)
# Print the initial chess board
print("Final Chess Board:")
for row in q.chess_board:
    print(row)

