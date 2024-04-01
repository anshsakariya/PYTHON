a ="!!!!Harry!! !!!! Harry"
print(len(a))
print(a)
print(a.rstrip("!"))
print(a.upper())
print(a.lower())
print(a.replace("Harry","john"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())


str1="welcome to the console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

print(a.count("Harry"))

str1="welcome to the console!!!"
print(str1.endswith("!!!"))



str1="welcome to the console!!!"
print(str1.endswith("to",4,10))


str1="He's name is Dan, He is an honest man"
print(str1.find("is"))

str1="He's name is Dan, He is an honest man"
print(str1.find("iss"))
# print(str1.index("iss"))   #show error

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) 

str1 = "Welcome"
print(str1.isalpha()) 

str1 = "Welcome00"
print(str1.isalpha()) 

str1="hello world"
print(str1.islower())

str1="hello World"
print(str1.islower())


str1="We wish you a Merry Christmas"
print(str1.isprintable())

str1="We wish you a Merry Christmas\n"
print(str1.isprintable())

str1="We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

str1="           " #using Spacebar
print(str1.isspace())   

str1="  "            #using tab
print(str1.isspace())


str1="World Health Oragnization"
print(str1.istitle())

str1= "To Kill a Mocking bird"
print(str1.istitle())

str1 = "python is a Interpreted Language"
print(str1.startswith("python"))


str1 = "python is a Interpreted Language"
print(str1.startswith("eng"))


str1 = "Python is a Interpreted Language"
print(str1.swapcase())


str1 = "Python is a Interpreted language"
print(str1.title())