# x=4   #global variable 
# print(x)

# def hello():
#     x=5 # local variable
#     print(f"the local x is  {x}")
#     print("Hello harry")
# print(f"the global x is {x}")
# hello()
# x=5
# print(f"the global x is {x}")



x=10 #global variable

def my():
    global x
    x=4
    y=5 #local variable
    print(y)
my()
print(x)
