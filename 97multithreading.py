import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleeping for {seconds} second")
    time.sleep(seconds)
    return seconds
def main():
 time1 = time.perf_counter()
 t1=threading.Thread(target=func, args=[3])
 t2=threading.Thread(target=func, args=[2])
 t3=threading.Thread(target=func, args=[5])
 t1.start()
 t2.start()
 t3.start()
 t1.join()
 t2.join()
 t3.join()
 time2=time.perf_counter()
 print(time2-time1)
def poolingDemo():
    with ThreadPoolExecutor() as executor:
     l=[3,5,1,2]
     results = executor.map(func,l)
     for result in results:
        print(result)
poolingDemo()


import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleeping for {seconds} second")
    time.sleep(seconds)
def main():
 time1 = time.perf_counter()
 t1=threading.Thread(target=func, args=[3])
 t2=threading.Thread(target=func, args=[2])
 t3=threading.Thread(target=func, args=[5])
 t1.start()
 t2.start()
 t3.start()
 t1.join()
 t2.join()
 t3.join()
 time2=time.perf_counter()
 print(time2-time1)
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
poolingDemo()


import threading
import time
def func(second1):
    print(f"sleeping for {second1} second1")
    time.sleep(second1)
time1=time.perf_counter()
t1=threading.Thread(target=func, args=[3])
t2=threading.Thread(target=func, args=[2])
t3=threading.Thread(target=func, args=[5])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(time2-time1)


import threading
import time
def func(second1):
    print(f"sleeping for {second1} second2")
    time.sleep(second1)
time1=time.perf_counter()
t1=threading.Thread(target=func, args=[5])
t2=threading.Thread(target=func, args=[2])
t3=threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
time2=time.perf_counter()
print(time2-time1)


import threading
import time
def func(second1):
    print(f"sleeping for {second1} second3")
    time.sleep(second1)
time1=time.perf_counter()
func(6)
func(7)
func(8)
time2=time.perf_counter()
print(time2-time1)


import threading
import time
def func(Seconds):
    print(f"sleeping for {Seconds} seconds4")
    time.sleep(Seconds)
func(4)
func(2)
func(1)


import threading
import time
def func(Second):
    print(f"sleeping for {Second} second5")
    time.sleep(Second)
t1=threading.Thread(target=func, args=[8])
t2=threading.Thread(target=func, args=[4])
t3=threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
