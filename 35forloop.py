for i in range(5):
    print(i)
else:
    print("sorry number i")

for i in []:
    print(i)
else:
    print("sorry number i")




for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry number i")


print("while loop")
i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("sorry number i")

i=0
while i<7:
    print(i)
    i=i+1
else:
    print("sorry number i")


for x in range(5):
    print("iteration no {} in for loop.".format(x+1))
else:
    print("else block in loop")
print("out of loop")
