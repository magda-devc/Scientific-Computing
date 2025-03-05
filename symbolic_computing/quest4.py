import sympy as sp
x = sp.Symbol('x')
C = 5*x**3 - 10*x**2 + 4*x + 3

#Symbolic derivative
deriv = sp.diff(C, x)
print("The symbolic derivative is ", deriv)

#Solve x when cost is minimized
minCost = sp.solve(deriv, x)
print("The value of x when cost is minimized is ", minCost)

# Interpret the result for decision-making
secondDeri = sp.diff(deriv, x)
print("The second derivative is ", secondDeri)

# Interpret the result for decision-making
print("Minimum cost: ", minCost[0]) 



