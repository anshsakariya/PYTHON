dic={
    344:"Harry",
    56:"shubham",
    678:"zakir",
    567:"neha"
}
print(dic[567])

info ={ 'name':'karan','age':19,'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))
print(info['eligible'])
print(info.get('name2'))
# print(info['name2'])  #error show
print(info.keys())
print(info.values())

for value in info.keys():
    print(info[value])


for value in info.keys():
    print(f" the value corresponding to the key {value} is  {info[value]}")

print(info.items())
for key, value in info.items():
        print(f" the value corresponding to the key {key} is  {value}")


