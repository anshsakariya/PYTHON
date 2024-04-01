def average(a,b):
    print("the average is ", (a+b)/2)
average(4,6)

print("------------------")

def average(a=9,b=1):
    print("the average is ", (a+b)/2)
average()

print("------------------")
print("default arguments")

def average(a=9,b=1):
    print("the average is ", (a+b)/2)
average(1,5)

print("------------------")
print("default arguments")

def average(a=9,b=1):
    print("the average is ", (a+b)/2)
average(5)


print("------------------")
print("default arguments")

def average(a=9,b=1):
    print("the average is ", (a+b)/2)
average(b=9)



print("------------------")
print("keyword arguments")

def average(a=9, b=1):
    print("the average is ",(a+b)/2)
average(b=9,a=21)

print("------------------")
print("required arguments")

def average(a, b,c=1):
    print("the average is ",(a+b+c)/2)
average(5,6)


print("------------------")
print("variable-length  arguments")

def average(*numbers):
    print(type(numbers))
    sum  = 0
    for i in numbers:
        sum = sum + i
    print("average is: ",sum / len(numbers))
average(5,6,7,1)


print("------------------")
print("variable-length  arguments")

def average(*numbers):
    sum  = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
c=average(5,6,7,1)
print(c)


print("------------------")
print("variable-length  arguments")

def average(*numbers):
    sum  = 0
    for i in numbers:
        sum = sum + i
    return 7
    return sum / len(numbers)
c=average(5,6,7,1)
print(c)