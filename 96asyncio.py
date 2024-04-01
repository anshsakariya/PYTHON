import time
def function1():
    time.sleep(3)
    print("func 1")
def function2():
    time.sleep(3)
    print("func 2")
def function3():
    time.sleep(3)
    print("func 3")
function1()
function2()
function3()


import time
import asyncio
async def function4():
    time.sleep(3)
    print("func 4")
async def function5():
    time.sleep(3)
    print("func 5")
async def function6():
    time.sleep(3)
    print("func 6")
async def  main():
  await function4()
  await function5()
  await function6()
asyncio.run(main())


import time
import asyncio
async def function7():
    await asyncio.sleep(1)
    print("func 7")
async def function8():
    await asyncio.sleep(1)
    print("func 8")
async def function9():
    await asyncio.sleep(4)
    print("func 9")
async def  main():
  task=asyncio.create_task(function7())
  # await function7()
  await function8()
  await function9()
asyncio.run(main())


import time
import asyncio
async def function10():
    time.sleep(3)
    print("func 10")
    return "HARRY"
async def function11():
    time.sleep(3)
    print("func 11")
async def function12():
    time.sleep(3)
    print("func 12")
async def  main():
 L=await asyncio.gather(
     function10(),
     function11(),
     function12()
     )
 print(L)
asyncio.run(main())


import time
import asyncio
import requests
async def function13():
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8NYnGDqrQm-gbf4fbXkaMBzmVLlf2rZdOLA&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(r.content)
    print("func 13")
    return "HARRY"
async def function14(): 
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCZlf5lc5tX-0gY-y94pGS0mQdL-D0lCH2OQ&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google1.jpg', 'wb').write(r.content)
    print("func 14")
async def function15():
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMaz52mMM1jE_pBAruYZ1mTJ9_KX0KIXyw-A&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
    print("func 15")
async def  main():
  await  function13(),
  await  function14(),
  await  function15(),
asyncio.run(main())


import time
import asyncio
import requests

async def function16():
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8NYnGDqrQm-gbf4fbXkaMBzmVLlf2rZdOLA&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(r.content)
    print("func 16")
    return "HARRY"
async def function17(): 
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCZlf5lc5tX-0gY-y94pGS0mQdL-D0lCH2OQ&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google1.jpg', 'wb').write(r.content)
    print("func 17")
async def function18():
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMaz52mMM1jE_pBAruYZ1mTJ9_KX0KIXyw-A&usqp=CAU'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
    print("func 18")
async def  main():
 M=await asyncio.gather(
     function16(),
     function17(),
     function18()
     )
 print(M)
asyncio.run(main())