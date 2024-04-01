s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))

print("**************************************")
s3={1,2,5,6}
s4={3,6,7}
print(s3,s4)

print("**************************************")
x={1,4,25,12}
y={9,12,14}
x.update(y)
print(x,y)


print("**************************************")
a={"Tokyo","Madrid","Berlin","Delhi"}
b={"Tokyo","Seoul","Kabul","Darid"}
c=a.union(b)
print(c)

print("**************************************")
d={"Tokyo","Madrid","Berlin","Delhi"}
e={"Tokyo","Seoul","Kabul","Madrid"}
f=d.intersection(e)
print(f)

print("**************************************")
g={"tokyo","Madrid","Berlin","Delhi"}
h={"tokyo","Seoul","Kabul","Madrid"}
g.intersection_update(h)
print(g)


print("**************************************")
i={"tokyo","Madrid","Berlin","Delhi"}
j={"tokyo","Seoul","Kabul","Madrid"}
k=i.symmetric_difference(j)
print(k)

print("**************************************")
l={"Tokyo","Madrid","Berlin","Delhi"}
m={"Seoul","Kabul","Delhi"}
n=l.difference(m)
print(n)


print("**************************************")
l={"tokyo","Madrid","Berlin","Delhi"}
m={"tokyo","Seoul","Kabul","Madrid"}
print(l.isdisjoint(m))

print("**************************************")
n={"tokyo1","Madrid1","Berlin","Delhi"}
o={"tokyo","Seoul","Kabul","Madrid"}
print(n.isdisjoint(o))

print("**************************************")
p={"Tokyo","Madrid","Berlin","Delhi"}
q={"Seoul","Kabul"}
print(p.issuperset(q))
r={"Seoul","Madrid","Kabul"}
print(p.issuperset(r))
s={"Tokyo","Madrid","Delhi"}
print(p.issuperset(s))
print(s.issubset(p))


print("**************************************")
t={"Tokyo","Madrid","Berlin","Delhi"}
t.add("rajkot")
print(t)


print("**************************************")
u={"Tokyo","Madrid","Berlin","Delhi"}
u.remove("Tokyo")
print(u)

print("**************************************")
v={"Tokyo","Madrid","Berlin","Delhi"}
v.discard("Tokyo2")
print(v)

print("**************************************")
w={"Tokyo","Madrid","Berlin","Delhi"}
x = w.pop()
print(w)
print(x)

print("**************************************")
info = {"carla",19,False,5.9}
if "carla" in info:
    print("carla is present")
else:
    print("carla is absent")

print("**************************************")
A={"Tokyo","Mcities11drid","Berlin","Delhi"}

del A
print(A)
