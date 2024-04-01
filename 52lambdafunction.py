def double(x):
    return x*2
print(double(5))


double = lambda x:x*2
print(double(6))

cube = lambda x:x*x*x
print(cube(5))

avg = lambda x,y:(x+y)/2
print(avg(3,5))

def appl(fx, value):
    return 6 + fx(value)
print(appl(cube,2))
print(appl(lambda x:x*x*x,2))
print(appl(lambda x:x*x,2))
