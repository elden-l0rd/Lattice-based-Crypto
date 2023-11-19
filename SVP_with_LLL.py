import numpy as np
from scipy.linalg import cholesky
import numpy as np
import sympy as sym

def SVP_LLL(B):
    n, m = B.shape

    # Initialize the LLL reduction constants (mu) and basis vectors.
    B = B.astype(float)
    U = np.identity(n)
    mu = np.zeros((n, n))

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            mu[i, j] = np.round(B[:, i].dot(U[:, j]) / B[:, j].dot(U[:, j]))
            B[:, i] -= mu[i, j] * B[:, j]

    # LLL reduction main loop
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            mu[k, j] = np.round(B[:, k].dot(U[:, j]) / B[:, j].dot(U[:, j]))
            B[:, k] -= mu[k, j] * B[:, j]

        # Check for Lovász condition and swap if necessary
        if B[:, k].dot(B[:, k]) < 0.75 - mu[k, k] ** 2:
            B[:, k], B[:, k - 1] = B[:, k - 1], B[:, k]
            U[:, k], U[:, k - 1] = U[:, k - 1], U[:, k]
            k = max(k - 1, 1)
        else:
            k += 1

    return B

# Example usage
n = 3  # Dimension of the lattice
m = 3  # Number of basis vectors
B = np.random.randint(1, 10, (n, m))  # Initialize the lattice basis
reduced_B = SVP_LLL(B)
print("Reduced Basis:")
print(reduced_B)

# Step 1: Run the LLL lattice reduction code on your original lattice basis
# (Assuming you have obtained the reduced basis 'reduced_B' from the LLL code)

# Your LLL code goes here

# Step 2: Store the reduced basis
# (Assuming 'reduced_B' contains the reduced basis obtained from LLL)
# You can access the rows of 'reduced_B' as the basis vectors for your reduced lattice.

# Step 3: Modify the code you provided to use the reduced basis for the shortest vector search

a = reduced_B[0]  # First vector of the reduced basis
b = reduced_B[1]  # Second vector of the reduced basis

m = sym.Symbol('m')
l = sym.Symbol('l')

L = m * a + l * b
print("Vectors belonging in the grid have the following form: L =", L)
print("(Brute Force) Starting calculations to solve the SVP for L...")
print("")

m, l = -10, -10
shortest_vector = np.array([100, 100])
shortest_m, shortest_l = 100, 100
while m <= 10:
    while l <= 10:
        L = m * a + l * b
        if m == 0 and l == 0:
            l += 1
            continue
        elif np.linalg.norm(L) < np.linalg.norm(shortest_vector):
            shortest_vector = L
            shortest_m, shortest_l = m, l
        l += 1
    l = -10
    m += 1

print("m = ", shortest_m, "l = ", shortest_l, "vector = ", shortest_vector)
print("The shortest vector norm of the grid is: ", np.linalg.norm(shortest_vector))

print(B)