def f(x):
    return x**4 -2*x + 1

def F(x):
    return x**5/5 - x**2 + x

a=0.0
b=2.0

exact = F(b) - F(a)
approx = (1/6)*(b-a)*(f(a)+ (4 * f(0.5* (a+b))) + f(b))

err = abs(exact - approx)

print("exact: ",exact)
print("approx: ",approx)
print("err: ",err)


