countries = ("spain","italy","india","england","germany")
print(countries)
temp = list(countries)
print(temp)
temp.append("Russia")
print(temp)
temp.pop(3)
print(temp)
temp[2]="Finland"
print(temp)
countries=temp
print(countries)
countries=tuple(temp)
print(countries)



countries =("pakishan","afghanistan","Bangaladesh","shrilanka")
countries1=("vietan","india","china")
countries2=countries+countries1
print(countries2)


tuple1= (0,1,2,3,2,3,1,3,2,3)
res=tuple1.count(3)
print('count of 3 in tuple is:',res)


tuple1= (0,1,2,31,2,3,1,3,2,3)
res=tuple1.index(3)
print('count of 3 in tuple is:',res)

tuple1= (0,1,2,3,2,3,1,3,2,3)
res=tuple1.index(3,4,8)
print('count of 3 in tuple is:',res)


tuple1= (0,1,2,3,2,3,1,3,2,3)
res=len(tuple1)
print('count of 3 in tuple1 is:',res)