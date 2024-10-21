def fib():
    a, b = 0,1 
    while True:
        yield a #by this we can make a loop 
        a, b = b, a+b
        

for f in fib():
    if f>100:
        break
    print(f)