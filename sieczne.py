import sympy as sp

x = sp.symbols('x')

f=600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1
eps=1e-4

przedzial=[0.1, 1]
x0=przedzial[0]
x1=przedzial[1]
x2=0
k=1

print(f'x0 = {przedzial[0]}, x1 = {przedzial[1]}')

while True:
    k += 1
    x2 = x1 - ((x0 - x1) / (f.evalf(subs={x: x0}) - f.evalf(subs={x: x1})) * f.evalf(subs={x: x1}))

    print(f'\nx{k}: {x2}\nf(x)={f.subs(x, x2)}')

    if abs(f.subs(x, x2)) < eps or f.subs(x, x2)==0:
        break

    x0 = x1
    x1 = x2

