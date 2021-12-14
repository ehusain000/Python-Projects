def f(x):
    return x**4 -2*x + 1

def F(x):
    return x**5/5 - x**2 + x

a=0.0
b=2.0

exact = F(b) - F(a)
approx = 0.5*(b-a)*(f(a)+f(b))

err = abs(exact - approx)

print("exact: ",exact)
print("approx: ",approx)
print("err: ",err)


