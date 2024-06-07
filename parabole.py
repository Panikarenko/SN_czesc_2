#!/usr/bin/env python
from sympy import *
from sympy.calculus.util import *

init_printing()

x, a, b, i = symbols('x a b i')
f = Function('f')

a = 0.0
b = 1.0

h = Rational(1, 8)
n = int((b - a) / h)

print(n)

#n = 4
#h = (b - a) / n

S = Mul(UnevaluatedExpr(( h / 6 ).simplify()), Add( f(x).subs(x, a), f(x).subs(x, b), Mul(2, Sum(f(x).subs(x, a + i * h), (i, 1, n - 1)).doit(), evaluate=False), Mul(4, Sum(f(x).subs(x, a + i * h + h / 2), (i, 0, n - 1)).doit(), evaluate=False), evaluate=False), evaluate=False)

f_actual = x**4 + 1
S_actual = S.replace(f, Lambda(x, f_actual))
S_result = S_actual.doit()

pprint(Equality(S, S_result), order="none")
print(S_result.evalf())
