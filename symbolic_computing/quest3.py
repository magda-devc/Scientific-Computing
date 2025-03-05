import sympy as sp
s = sp.Symbol('s')
H = 1/(s**2 + 3*s + 2)

#factor denominator
fac = sp.factor(sp.denom(H))
print("The factored function is ", fac)

#Inverse Laplace Transform to fint h(t)
t = sp.Symbol('t')
h = sp.inverse_laplace_transform(H, s, t)
print("The inverse Laplace transform is ", h)

#poles of the system
poles = sp.solve(fac, s)
print("The poles are:", poles)