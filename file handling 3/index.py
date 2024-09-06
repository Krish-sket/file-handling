import os

with open('sample.txt','w') as file:
  file.write("hello world")
file.close()
with open('sample.txt','r') as file:
  data=file.readlines()
  print("The words in this file are:")
  for i in data:
    word=i.split()
    print(word)
file.close()
print("Checking if new_file exists:")
if os.path.exists("New_File.txt"):
  os.remove("New_File.txt")
else:
  print("File does not exist")
