# Open a file
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.read(10)
print ("Read Line: %s" % (line))
# Close opened file
fo.close()