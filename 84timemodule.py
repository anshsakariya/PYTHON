import time
def usingWhile():
    i=0
    while i <40000:
     i=i+1
     print(i)
def usingFor():
   for i in range(4000):
       print(i)
init=time.time()
usingFor()
t1=time.time()-init
init=time.time()
usingWhile()
print(time.time()-init)
print(t1)


import time
print(4)
time.sleep(3)
print("this is printed after 3 seconds")

import time
t=time.localtime()
formatted=time.strftime("%Y-%m-%d %h %M %S",t)
print(formatted)