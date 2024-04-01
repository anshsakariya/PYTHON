a=int(input("enter the value"))
print("your age is: ",a)

if(a>18):
    print("you can drive")

else:
    print("you can not drive")




num=int(input("enter the value: "))
if(num < 0):
    print("number is negative")
elif(num == 0):
    print("number is zero")
else:
    print("number is positive")



num=18
if(num < 0):
    print("number is negative")
elif(num > 0):
    if(num <=10):
        print("number is between 1-10")
    elif(num > 10 and  num <= 20):
        print("number is between 11-20")
    else:
        print("number is greather than 20")
else:
    print("number is zero")


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
