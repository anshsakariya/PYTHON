# walrus operactor
number = [1,2,3,4,5]
while(n:=len(number))>0:
    print(number.pop())

happy = False
print(happy)
print(happy:=True)

foods=list()
while True:
    food=input("whts food do you like: ")
    if food == "quit":
        break
    foods.append(food)

foods = list()
while(food:=input("ehat food do you like: "))!="quit":
    foods.append(food)

