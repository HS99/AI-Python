fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.readline()
print ("Read Line: %s" % (line))
pos=fo.tell()
print ("current position : ",pos)
# Close opened file
fo.close()