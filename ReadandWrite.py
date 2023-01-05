file = open('test.txt')
#Read all the contents from the text file
#print(file.readline(5))  #Read lines by line which means single line at a time

line = file.readline()
#while line!="":
 #   print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)
#print(file.readlines())
# print(file.read())
file.close()