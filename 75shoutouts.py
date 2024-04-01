import os

# os.rename("./file.txt", "./75shoutouts.txt")

# os.rename("abc/abc.txt", "abc/file.txt")


# files=os.listdir("abc")
# for file in files:
#     print(file)

files=os.listdir("abc")
for file in files:
    if file.endswith(".txt"):
     print(file)