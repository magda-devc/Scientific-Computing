import sympy as sp
x = sp.Symbol('x')
#Loss function
L = 3*x**2 + 2*x - 5

#Finding the gradient
gradient = sp.diff(L,x)
print("The gradient is ", gradient)

#When gradient is 0
grad0 = sp.solve(gradient, x)
print("The value of x when gradient is 0 is ", grad0)

#Second derivative
secondDeri = sp.diff(gradient, x)
print("The second derivative is ", secondDeri)