#!/usr/bin/env python
from sympy import *

init_printing()

# [A | b]
A = Matrix([
    [2, -3, -4, -5],
    [-1, 2, 1, -1],
    [3, -2, -1, 5],
])

'''
A = Matrix([
    [7, -5, -1, 16, -4],
    [-10, -4, -2, -17, 2],
    [-16, 13, -19, -6, -9],
    [4, 2, 19, 18, 7]
])
'''

U = A.copy()
for i in range(U.rows - 1):
    print(f"krok{i}:")  
    for j in range(i + 1, U.rows):
        l = U[j, i] / U[i, i]
        print(f"({j + 1}) <= ({j + 1}) - ({i + 1}) * {l}")
        for k in range(U.cols):
            U[j, k] = U[j, k] - U[i, k] * l
            assert(U.diagonal().cols == len(U.diagonal().values())) # wszystkie elementy na przekątnej != 0
     
    print(f"\n{pretty(U)}")
    

print("\n----------------------------------\n")

X = symbols(f'x1:{A.rows + 1}')
Y = {}

for i in range(U.rows - 1, -1, -1):
    Y[X[i]] = U[i, -1]  # b to ostatnia kolumna
    for j in range(i + 1, U.rows):
        Y[X[i]] -= U[i, j] * Y[X[j]]
    Y[X[i]] /= U[i, i]

print(f"{pretty(U)}\n")
print(pretty(Y))