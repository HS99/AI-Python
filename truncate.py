fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.readline()
print ("Read Line: %s" % (line))
fo.truncate()
line = fo.readlines()
print ("Read Line: %s" % (line))
# Close opened file
fo.close()