#!/usr/bin/env python
from sympy import *

init_printing()


def jacobi(A, b, eps=1e-10, kmax=1000):
    x = zeros(A.rows, 1)
    x_new = x.copy()

    for k in range(kmax):
        for i in range(A.rows):
            s = sum(A[i, j] * x[j] for j in range(A.rows) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]

        if all(abs(x_new[i] - x[i]) < eps for i in range(A.rows)):
            print(f"osiagnieto zbieznosc {eps} w {k + 1} krokach\n")
            return x_new

        x = x_new.copy()

    print(f"NIE osiagnieto zbieznosci {eps} w {k + 1} krokach\n")
    return x_new


def gauss_seidel(A, b, eps=1e-10, kmax=1000):
    x = zeros(A.rows, 1)

    for k in range(kmax):
        x_new = x.copy()

        for i in range(A.rows):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, A.rows))
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        if all(abs(x_new[i] - x[i]) < eps for i in range(A.rows)):
            print(f"osiagnieto zbieznosc {eps} w {k + 1} krokach\n")
            return x_new

        x = x_new

    print(f"NIE osiagnieto zbieznosci {eps} w {k + 1} krokach\n")
    return x_new


# przkylad z L06.pdf dla kmax=2 dla porownania wynikow (zgadzaja sie)
A = Matrix([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4,]
])

b = Matrix([2, 6, 2])

print(f"jacobi:\n\n{pretty(jacobi(A, b, kmax=2).evalf())}\n\n")
print(f"gauss-seidel:\n\n{pretty(gauss_seidel(A, b, kmax=2).evalf())}")