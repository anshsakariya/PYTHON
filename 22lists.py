marks=[3,5,6,"Harry",True,6,7,2,32,345,23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


print(marks[-3])   #negative index
print(marks[len(marks)-3])   #positive index
print(marks[5-3])
print(marks[2])



if "Harry" in marks:
    print("yes")
else:
    print("No")


if 7 in marks:
    print("yes")
else:
    print("No")

if 3 in marks:
    print("yes")
else:
     print("No")

#same thing applies for string as well

if "arry" in "Harry":
     print("yes")
else:
     print("No")

if "ary" in "Harry":
    print("yes")
else:
     print("No")

if "Ha" in "Harry":
    print("yes")
else:
     print("No")


print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:-1])
print(marks[1:4])
print(marks[1:4:2])
print(marks[1:8:2])
print(marks[1:8:3])
print(marks[1:9])
print(marks[1:9:3])
print(marks[1:len(marks)])
print(marks[:7])
print(marks[0:7])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)