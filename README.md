# Lattice-based-Crypto

### Implementation of Coppersmith Attack on RSA

This implementation demonstrates its application in factoring RSA moduli when there is a partial key exposure. It checks the Coppersmith condition, constructs a lattice matrix, and applies the LLL algorithm to find potential roots of a polynomial. Then, filter and validate these roots to discover potential factors of the RSA modulus.

Nonetheless, RSA remains secure when implemented with strong key lengths and proper random prime numbers.

Inspired by:
- Twenty Years of Attacks on the RSA Cryptosystem (Dan Boneh 1999)

References:
- Small Solutions to Polynomial Equations, and Low Exponent RSA vulnerabilities (Don Coppersmith 1995).
- Coppersmith’s Method and Related Applications (Steven Galbraith 2012)
- https://github.com/mimoo/RSA-and-LLL-attacks.git