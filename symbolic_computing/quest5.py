import sympy as sp
P, e, N = sp.symbols('P e N')

C = P**e % N 

#Find C
P = 7
e = 3
N = 33

cipher = P**e % N 
print("The value of C is ", cipher)

# Compute the modular inverse of P (mod N)
mod_inverse = sp.mod_inverse(7, 33)
print("The modular inverse is ", mod_inverse)
