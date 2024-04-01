def my():
    for i in range(10000):
        yield i 

gen = my()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for j in gen:
    print(j)


