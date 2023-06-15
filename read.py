#Open a file
fo = open("myfile.txt", "r+")
str = fo.read(20)
print ("Read String is : ", str)
# Close opened file
fo.close()