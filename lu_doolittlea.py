#!/usr/bin/env python
from sympy import *

init_printing()

A = Matrix([
    [-1, 2, -2],
    [0, 1, -1],
    [2, -3, 2]
])

assert(A.is_square)

L=eye(A.rows)
U=zeros(A.rows)

for i in range(A.rows):
    for k in range(A.rows):
        if i <= k:
            U[i, k] = A[i, k] - sum([L[i, j] * U[j, k] for j in range(0, i)])
        else:
            L[i, k] = (A[i, k] - sum([L[i, j] * U[j, k] for j in range(0, i)])) / U[k, k]
   
        print(f"i: {i}, k: {k}\n")
        print(f"L:\n{pretty(U)}\n\nU:\n{pretty(L)}\n\n-------------------\n")
        
assert(A == L * U)

inv_A = Matrix()
for k, e in enumerate(eye(A.rows).columnspace()):
    print(f"e{k+1}:\n{pretty(e)}\n")
    Lz = L.col_insert(L.cols, e)
    Z = zeros(1, Lz.rows)
        
    # podstawianie w przód
    for i in range(Lz.rows):
        Z[i] = Lz[i, -1]
        for j in range(i):
            Z[i] -= L[i, j] * Z[j]
        Z[i] /= L[i, i]
        
    print(f"Lz=e{k+1}:\n{pretty(Lz)}\n")
    print(f"{pretty(Z)}\n")
    
    Ux = U.col_insert(U.cols, Z.T)
    X = zeros(1, Ux.rows)
    
    # podstawianie w tył
    for i in range(Ux.rows - 1, -1, -1):
        X[i] = Ux[i, -1]
        for j in range(i + 1, Ux.rows):
            X[i] -= Ux[i, j] * X[j]
        X[i] /= Ux[i, i]
        
    print(f"Ux=z:\n{pretty(Ux)}\n")
    print(f"{pretty(X)}\n")
    
    print("--------------------------------\n\n")

    inv_A = inv_A.col_insert(inv_A.cols, X.T)

assert(inv_A == A.inverse_LU())

print(f"{pretty(inv_A)}\n\n{pretty(inv_A * A)}")