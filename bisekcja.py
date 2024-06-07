#!/usr/bin/env python
from sympy import *
from sympy.calculus.util import *

init_printing()

x = symbols('x')
f = Lambda(x, x**2 - 11)

a, b = (S(3), S(4))
c = (a + b) / 2

k = 1
eps = 10**-5
while true:
    if k > 15:
        break

    print(f"{k}\n\tf(c = {c.evalf()}) = {f(c.evalf())}\n")

    c = (a + b) / 2

    if abs(f(c)) < eps:
        break

    if sign(f(c)) == sign(f(a)):
        a = c
    else:
        b = c

    k = k + 1
