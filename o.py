f = open("file.txt","r")
#data = f.read()
data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()