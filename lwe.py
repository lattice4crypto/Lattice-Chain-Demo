import numpy as np

n = 230
q = 2063
A = np.random.randint(q, size=(n, n))
alpha = 8.0

def randint_from_gaussian(size):
    sigma = alpha/np.sqrt(2*np.pi)
    x = np.random.normal(0, sigma, size)
    return np.rint(x)

s = np.random.randint(q, size=n)
G = A.dot(s) % q
e = randint_from_gaussian(size=n)
T = (G + e) % q

plain_bit = 1

r = randint_from_gaussian(size=n)
C1 = r.dot(A) % q
M = (q+1)/2 * plain_bit
C2 = (r.dot(T) - M) % q


# decryption
p = (C1.dot(s) - C2) % q
decrypted_bit = int((q+1)/4 < p < 3*(q+1)/4)
print "[+] decrypted_bit = %d" % decrypted_bit
