import sympy as sp

x = sp.symbols('x')
f=x**4+1
a=0.0
b=1.0

# h = 0.125
# n = int((b - a) / (2 * h))

n=4
h=sp.Rational((b - a), 2 * n)

Q_f=(h/3) * (f.evalf(subs={x: a}) + 4 * sum([f.evalf(subs={x: (a + (2 * i - 1) * h)}) for i in range (1, n+1)]) + 2 * sum([f.evalf(subs={x: (a + (2 * i) * h)}) for i in range(1, n)]) + f.evalf(subs={x: b}))

I_f = sp.integrate(f, (x, a, b))

print(f'Całkowanie przybliżone Q(x): {Q_f}\nWynik całkowania I(x): {I_f}\nBłąd: {I_f-Q_f}')