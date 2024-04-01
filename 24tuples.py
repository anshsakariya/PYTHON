tup=(1,5,76,342,32,"green",True)

print(tup[-1])
print(tup[0])
print(tup[1])
print(tup[2])


if 342 in tup:
    print("yes 342 is present in this tuple")

tup2 = tup[1:4]
print(tup2)

print(len(tup))
print(type(tup),tup)

tup=(1,5)
print(type(tup),tup)

tup=(1,)
print(type(tup),tup)
