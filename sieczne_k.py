#!/usr/bin/env python
from sympy import *
from sympy.calculus.util import *

init_printing()

x = symbols('x')
f = Lambda(x, 600 * x**4 - 550 * x**3 + 200 * x**2 - 20 * x - 1)

a, b = (S(0.1), S(1))
c0, c1, c2 = (a, b, S(0))

k = 1
eps = 10**-4
while true:
    if k > 100:
        break

    c2 = c1 - ( (c0 - c1) / (f(c0) - f(c1)) ) * f(c1)

    print(f"{k}\n\tf(c = {c2.evalf()}) = {f(c2.evalf())}\n")

    if abs(f(c2)) < eps:
        break

    c0 = c1
    c1 = c2

    k = k + 1
