# factoral(7) = 7*6*5*4*3*2*1
# factoral(6) = 6*5*4*3*2*1
# factoral(5) = 5*4*3*2*1
# factoral(4) = 4*3*2*1
# factoral(3) = 3*2*1
# factoral(2) = 2*1
# factoral(1) = 1


# factorial(n)=n * factorail(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 
    
print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4)) 
print(factorial(3))
print(factorial(2))
print(factorial(1)) 
