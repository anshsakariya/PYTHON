a=4
b="4"
print(a is b)# exact location of object in memory
print(a==b)# value

c=[1,2,43]
d=[1,2,43]
print(c is d)
print(c==d)

e=1
f=1
print(e is f)
print(e==f)

g="harry"
h="harry"
print(g is h)
print(g==h)

i=(1,2)
j=(1,2)
print(i is j)
print(i==j)

k=None
l=None
print(k is l)
print(k is None)
print(k==l)