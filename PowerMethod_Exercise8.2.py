import numpy as np

u = np.arange(1.,33.)
v = np.arange(1., 31.)
v = np.concatenate((v, np.array([30., 32.])))

A = np.diag(u)
B = np.diag(v)

x = np.concatenate((np.ones((32, 1))))

for k in range(100):
    x = A@x
    x = x / np.linalg.norm(x)
    lam = np.dot(x.T, A@x)
    print(k+1, lam)
    
print(" ")

x = np.concatenate((np.ones((32, 1))))
for k in range(100):
    x = B@x
    x = x / np.linalg.norm(x)
    lam = np.dot(x.T, B@x)
    print(k+1, lam)

