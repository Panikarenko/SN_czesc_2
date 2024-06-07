import sympy as sp

x = sp.symbols('x')
f = 600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1
przedzial_poczatkowy = [0.1, 1]
epsilon=1e-4
liczba_iteracji=100

xa=przedzial_poczatkowy[0]
xb=przedzial_poczatkowy[1]
k=1

def metoda_siecznych():
    global xa
    global xb
    global k

    while (abs(f.evalf(subs={x: oblicz_xk()}))>epsilon and k<100):
        temp = xb
        xb = oblicz_xk()
        xa=temp
        k+=1
    print(f'x={oblicz_xk()}\nk={k}\nf={f.evalf(subs={x: oblicz_xk()})}')
    return

def oblicz_xk():
    global xa
    global xb
    f_xa = f.evalf(subs={x: xa})
    f_xb = f.evalf(subs={x: xb})
    if f_xa == f_xb:
        print("Podział przez zero, przerwanie obliczeń.")
        return xb
    return xb - ((xa - xb) / (f_xa - f_xb)) * f_xb

print(f'Wybrany punkt startowy: x₀={xa}, x₁={xb}')
metoda_siecznych()
