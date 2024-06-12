import sympy as sp

x = sp.symbols('x')

f=3 * x**3 - 25
eps=1e-4

k=1
przedzial=[-1, 3]
p=0

while True:
    p=(przedzial[0] + przedzial[1])/2

    print(f'\nprzedzial: [{przedzial[0]};{przedzial[1]}]\np{k} = {p}\nf(x)={f.evalf(subs={x: p})}')
    if (abs(f.evalf(subs={x: p})) < eps or f.evalf(subs={x: p}) == 0):
        break

    if sp.sign(f.evalf(subs={x: przedzial[0]}))==sp.sign(f.evalf(subs={x: p})):
        przedzial[0]=p
    else:
        przedzial[1]=p
    
    k+=1