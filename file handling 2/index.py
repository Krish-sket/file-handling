file= open('sample.txt','r')
print(file.read())
file.close()
file= open('sample.txt','r')
print("\n First 10 letters \n")
print(file.read(10))
file.close()
file = open('sample.txt','r')
print("Reading the first line...")
print(file.readline())
file=open('sample.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file=open('sample.txt','r')
print("Looping through the lines...")
for i in file:
  print(i)

