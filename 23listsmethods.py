l=[11,45,1,2,4,6]
print(l)
l.sort()
print(l)

print("================")
l=[11,45,1,2,4,6]
print(l)
l.sort(reverse=True)
print(l)

print("===============")
l=[1,2,3,4,6]
print(l)
l.append(7)
print(l)

print("===============")
l=[11,45,1,2,4,6,1]
print(l)
print(l.index(1))
print(l)

print("===============")
l=[1,11,45,1,2,4,6,1]
print(l)
print(l.count(1))
print(l)


print("===============")
l=[11,45,1,2,4,6,1,1]
print(l)
m=l
m[0]=0
print(l)

print("===============")
l=[11,45,1,2,4,6,1,1]
print(l)
m=l.copy()
m[0]=0
print(l)

print("===============")
l=[11,45,1,2,4,6,1,1]
print(l)
l.insert(1,899)
print(l)

print("===============")
l=[11,45,1,2,4,6,1,1]
print(l)
m=[900,1000,1100]
l.extend (m)
print(l)

print("===============")
l=[11,45,1,2,4,6,1,1]
print(l)
m=[900,1000,1100]
k=l+m
print(k)
print(l)