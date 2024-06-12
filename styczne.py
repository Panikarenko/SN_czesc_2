import sympy as sp

x = sp.symbols('x')
f = 600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1
f_prime = sp.diff(f, x)
f_double_prime=sp.diff(f_prime, x)

przedzial=[0.1, 1]
eps=1e-4
k=0
xk=0

if f.evalf(subs={x: przedzial[0]}) * f_double_prime.evalf(subs={x: przedzial[0]})>0:
    xk=przedzial[0]
else:
    xk=przedzial[1]

print(f'Punkt startowy, x0 = {xk}')

while True:
    k+=1
    xk = xk - (f.evalf(subs={x: xk})/f_prime.evalf(subs={x: xk}))

    print(f'\nx{k}: {xk}\nf: {f.evalf(subs={x: xk})}')

    if abs(f.evalf(subs={x: xk})) < eps or f.evalf(subs={x: xk})==0:
        break