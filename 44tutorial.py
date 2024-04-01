import math
result =math.sqrt(9)
print(result)


from math import sqrt,pi
result = sqrt(9)*pi
print(result)


from math import *
result =sqrt(9)*pi
print(result)

#as keyword
from math import pi,sqrt as s
result = s(9)*pi
print(result)


import math as m
result = m.sqrt(9)*m.pi
print(result)


#dir function
import math
print(dir(math))
print(math.nan)
print(type(math.nan))

print("---------------")
from tutorial1 import welcome ,harry
import math
welcome()
print(harry)

print("---------------")
from tutorial1 import *
import math
welcome()
print(harry)


print("---------------")
import tutorial1 as hr
import math
hr.welcome()
print(hr.harry)