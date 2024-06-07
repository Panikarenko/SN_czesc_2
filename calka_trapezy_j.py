import sympy
x = sympy.Symbol("x")

func = x**2
start = 0.0
end = 1.0
step = 0.2

n = int((end - start) / step)
q = func.subs(x, start) + func.subs(x, end)
for k in range(n):
    q += 2 * func.subs(x, start + k * step)
q *= 0.5 * step

r = -((end - start)**3 / (12 * n**2)) * func.diff(x).diff(x).subs(x, end)

print("Kwadratura (Q) =", q)
print("Błąd przybliżenia (R) =", r)
