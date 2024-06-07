import sympy as sp

x = sp.symbols('x')
f = 600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1
f_prime = sp.diff(f, x)
f_double_prime=sp.diff(f_prime, x)
eps=1e-4
k=0
xk=0
przedzial_poczatkowy=[0.1, 1]

def wybierz_x0(x0):
    if(f.evalf(subs={x: x0})*f_double_prime.evalf(subs={x: x0})>0):
        return True
    
def oblicz_xk_plus_1():
    global xk
    return xk-f.evalf(subs={x: xk})/f_prime.evalf(subs={x: xk})

def main():
    global xk
    global k
    global przedzial_poczatkowy
    if(wybierz_x0(przedzial_poczatkowy[0])):
        xk=przedzial_poczatkowy[0]
    elif(wybierz_x0(przedzial_poczatkowy[1])):
        xk=przedzial_poczatkowy[1]
    print (f'Wybrany punkt startowy x0: {xk}\n')
    while(abs(f.evalf(subs={x: xk}))>eps and k<100):
        print(f'k={k}\nx{k}: {xk}\nf: {f.evalf(subs={x: xk})}')
        xk=oblicz_xk_plus_1()
        k+=1
    print(f'\nWynik końcowy:\nLiczba iteracji: {k+1}\nx{k}: {xk}\nf: {f.evalf(subs={x: xk})}')

main()

# Wybrany punkt startowy x0: 1

# k=0
# x0: 1
# f: 229.000000000000
# k=1
# x1: 0.797345132743363
# f: 73.9130983660018
# k=2
# x2: 0.638917666419202
# f: 24.3999275523909
# k=3
# x3: 0.509110162859368
# f: 8.38825523350715
# k=4
# x4: 0.393687494474308
# f: 2.97766999437548
# k=5
# x5: 0.288036070151957
# f: 0.818860050102212
# k=6
# x6: 0.235796132289098
# f: 0.0482224152686086
# k=7
# x7: 0.232362291559353
# f: 0.000130271741712246

# Wynik końcowy:
# Liczba iteracji: 9
# x8: 0.232352964818264
# f: 9.54624006005788E-10