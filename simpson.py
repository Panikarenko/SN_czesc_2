import sympy
x = sympy.Symbol("x")

func = x**4 + 1
start = 0.0
end = 1.0
step = 1/8


n = int((end - start) / (2 * step))
q1 = 0
q2 = 0
for k in range(n):
    q1 += func.subs(x, start + step * (2 * k + 1))
for k in range(n - 1):
    q2 += func.subs(x, start + step * 2 * (k + 1))
    
q = (step / 3) * (func.subs(x, start) + (4 * q1) + (2 * q2) + func.subs(x, end))
r = -((end - start)**5 / (2880 * n**4)) * func.diff(x).diff(x).diff(x).diff(x).subs(x, end)

print("Kwadratura (Q) =", q)
print("Błąd przybliżenia (R) =", r)
