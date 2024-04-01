name = "Harry"
friend="rohan"
anotherfriend = 'lovish'
apple = "he said ,\"I want to eat an apple"
apple1 = 'he said ,"I want to eat an apple'
apple2='''he said ,
hi harry
hey i am good
"I want to eat an apple'''
apple3="""he said ,
hi harry
hey i am good
"I want to eat an apple"""
print("hello, "+name)
print(apple)
print(apple1)
print(apple2)
print(apple3)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) #throws an error
print("lets use a for loop\n")
for character in name:
    print(character)