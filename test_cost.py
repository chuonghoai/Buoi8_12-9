import random
n = 8
pos_random = [[(i, j) for j in range( n)] for i in range( n)]
_ = [pos for row in  pos_random for pos in row]
random.shuffle(_)
pos_random = [_[i* n:(i+1)* n] for i in range( n)]

node_goal = []

for i in range(n):
    while True:
        j = 0
        for (_, _j) in node_goal:
            if j == _j:
                j += 1
        if j == 0:
            node_goal.append((i, j))
            

print(node_goal)


# node = [[0, 2], [1, 2]]

# row = [x for (x, _) in node]
# col = [y for (_, y) in node]

# row_g = [x_g for (x_g, _) in node_goal]
# col_g = [y_g for (_, y_g) in node_goal]

# cost = 0
# i, j = 0, 0
# while i < len(node):
#     cost += abs(col[i] - col_g[j])
#     i += 1
#     j += 1

# print(col)
# print(col_g)
# print(cost)