def cube(x):
    return x*x*x
print(cube(2))



l=[1,2,4,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)


print("----------MAP---------")
#MAP
l=[1,3,4,6,4,3]
new = list(map(cube,l))
print(new)



l=[1,2,4,6,4,3]
new = list(map(lambda x:x*x*x,l))
print(new)



print("------------FILTER---------")
#FILTER
b=[1,3,4,6,5,4,3]
def filter_function(a):
    return a>3
new1=list(filter(filter_function,b))
print(new1)



print("-----------REDUCE-----------")
#REDUCE

from  functools import reduce
num=[1,2,3,4,5]
def mysum(x,y):
    return x+y
sum=reduce(mysum,num)
print(sum)

