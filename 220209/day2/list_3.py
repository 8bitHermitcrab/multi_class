n, m = map(int, input().split())

borad = [list(map(int, input().split())) for _ in range(n)]

print(borad)

""" 
5 6
0 1 3 2 4 5
3 4 2 3 4 4
3 4 5 2 1 6
2 1 2 3 4 4
2 4 5 2 3 3

[[0, 1, 3, 2, 4, 5], [3, 4, 2, 3, 4, 4], [3, 4, 5, 2, 1, 6], [2, 1, 2, 3, 4, 4], [2, 4, 5, 2, 3, 3]]
"""