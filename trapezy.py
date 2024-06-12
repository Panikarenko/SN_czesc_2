import sympy as sp

x = sp.symbols('x')
f=x**2

a=0.0
b=1.0

# h = sp.Rational(1, 5)
# n = int((b - a) / h)

n=5
h=sp.Rational((b-a), n)

Q_f=(h / 2) * ((f.evalf(subs={x: a})) + 2 * sum([f.evalf(subs={x: a + i * h}) for i in range (1, n)]) + f.evalf(subs={x: b}))

I_f = sp.integrate(f, (x, a, b))

print(f'Całkowanie przybliżone Q(x): {Q_f}\nWynik całkowania I(x): {I_f}\nBłąd: {I_f-Q_f}')