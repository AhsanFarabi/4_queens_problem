class Queen:
    def __init__(self, queen_locations):
        self.N = len(queen_locations)
        self.state = dict()
        self.initialize_chess_board(queen_locations)

    def initialize_chess_board(self, queen_locations):
        self.chess_board = [[0] * self.N for _ in range(self.N)]
        for i, (row, col) in enumerate(queen_locations):
            queen_label = f"Q{i}"
            self.state[queen_label] = [row, col]
            self.chess_board[row][col] = queen_label

    def get_neighbor(self, row, col):
        neighbor = []
        if 0 <= row - 1 < self.N and self.chess_board[row - 1][col] == 0:
            neighbor.append([row - 1, col])
        if 0 <= row + 1 < self.N and self.chess_board[row + 1][col] == 0:
            neighbor.append([row + 1, col])
        return neighbor

def conflict(r1, c1, r2, c2):
    if r1 == r2:
        return True
    if c1 == c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    return False

def get_conflict(Q, state):
    count = 0
    for q in state:
        if q != Q:
            r1, c1 = state[Q]
            r2, c2 = state[q]
            if conflict(r1, c1, r2, c2):
                count += 1
    return count

def calc_cost(state):
    cost = 0
    max_conflicts = -999
    maxQ = None
    for Q in state:
        q_conflicts = get_conflict(Q, state)
        cost += q_conflicts
        if q_conflicts > max_conflicts:
            max_conflicts = q_conflicts
            maxQ = Q
    return cost // 2, max_conflicts, maxQ

def goal_test(state):
    return calc_cost(state)[0] == 0

def hill_climbing(q, cur_cost):
    while not goal_test(q.state):
        cost, _, max_conflicts_queen = calc_cost(q.state)
        r, c = q.state[max_conflicts_queen]
        q.chess_board[r][c] = 0

        choices = q.get_neighbor(r, c)
        for ch in choices:
            q.state[max_conflicts_queen] = ch
            cost, _, _ = calc_cost(q.state)
            if cost < cur_cost:
                cur_cost = cost
                r, c = ch
                q.chess_board[r][c] = max_conflicts_queen
                break

# Example usage:
queen_locations = [[2, 0], [1, 1], [2, 2], [1, 3]]
queen_instance = Queen(queen_locations)

print("Initial State:")
for row in queen_instance.chess_board:
    print(row)

initial_cost, _, _ = calc_cost(queen_instance.state)
hill_climbing(queen_instance, initial_cost)

print("Final State:")
for row in queen_instance.chess_board:
    print(row)
