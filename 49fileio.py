#READING A FILE
f=open('49fileio.txt','r')
# print(f)
text=f.read()
print(text)
f.close()


#WRITING A FILE

f=open('49fileio1.txt','w')
f.write('Hello World')
f.close()


f=open('49fileio2.txt','a')
f.write('Hello World')
f.close()


with open('49fileio2.txt','a') as f:
 f.write("Hey I am inside with")