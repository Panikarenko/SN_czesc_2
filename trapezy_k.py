#!/usr/bin/env python
from sympy import *
from sympy.calculus.util import *

init_printing()

x, a, b, i = symbols('x a b i')
f = Function('f')

a = 0.0
b = 1.0

h = Rational(1, 5)
n = int((b - a) / h)

#n = 4
#h = (b - a) / S(n)

S = Mul(UnevaluatedExpr(( h / 2 ).simplify()), Add(f(x).subs(x, a), f(x).subs(x, b), Mul(2, Sum(f(x).subs(x, a + i * h), (i, 1, n - 1)).doit(), evaluate=False), evaluate=False), evaluate=False)

f_actual = x**2
S_actual = S.replace(f, Lambda(x, f_actual))
S_result = S_actual.doit()

pprint(Equality(S, S_result), order="none")
print(S_result.evalf())

I = integrate(f_actual, (x, a, b))
pprint(I)
