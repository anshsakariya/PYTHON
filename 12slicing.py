name = "Harry,shubham"
print(name[0:5])
print(len(name))


fruit = "Mango"
len1= len(fruit)
print(len1)
print(fruit[0:4])   #including 0 but not 4
print(fruit[:4])    #including 1 but not 4
print(fruit[1:4])
print(fruit[:])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])   #5-3=2
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])       #5-3=2 and 5-1=4     so[2:4]
print("mango is a",len1,"letter world")


nm = "harry"
print(nm[-4:-2])