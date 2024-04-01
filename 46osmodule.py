# folder banavava mate
import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range (0,100):
    os.mkdir(f"data/Day{i+1}")



# folder name rename karava  mate
import os
for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")



#folder nu name janava mate
import os
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(folder)



#folder ni under file janava mate
import os
folders = os.listdir("data")
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))



#folder ni dictionary 
import os
folders = os.listdir("data")
print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

