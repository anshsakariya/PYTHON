f=open('50read.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


f=open('50read1.txt','r')
i=0
while True:
    i = i + 1
    line=f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])  
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths is: {m1*2}")
    print(f"Marks of student {i} in english is: {m2*2}")
    print(f"Marks of student {i} in sst is: {m3*2}")
    print(line)



f=open('50read2.txt','w')
lines=['lines 1\n', 'lines 2\n''lines 3\n']
f.writelines(lines)
f.close()
