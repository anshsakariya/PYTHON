#as keywords
a=input("enter the number: ")
print(f"multiplication table of {a} is : ")
try:
  for i in range (1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print("sorry some error occurred")


print("some lines of code")
print("end program")

a=input("enter the number: ")
print(f"multiplication table of {a} is : ")
try:
  for i in range (1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("invalid input")


print("some lines of code")
print("end program")


try:
  num = int(input("enter an integer "))
  A=[6,3]
  print(A[num])
except ValueError:
  print("number entered is not an integer.")
except IndexError:
  print("Index Error")
