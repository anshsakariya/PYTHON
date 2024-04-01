with open('51seektell.txt','r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)


with open('51seektell1.txt','w')as f:
    f.write('HELLO WORLD')
    f.truncate(5)

with open('51seektell1.txt','r') as f:
    print(f.read())
