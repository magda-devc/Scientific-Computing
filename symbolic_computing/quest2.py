import sympy as sp
A = sp.Matrix([[2,1], [1,3]])
#Finding the determinant
det = A.det()
print("The determinant is ", det)

#Eigenvalues
eigen = A.eigenvals()
print("The eigenvalues are ", eigen)

#Verifying that the eigenvalues satisfy the characteristic equation
charEquation = A.charpoly()
print("The characteristic equation is ", charEquation)