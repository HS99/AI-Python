# Open a file
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.readline()
print ("Read Line: %s" % (line))
line = fo.readline(5)
print ("Read Line: %s" % (line))
# Close opened file
fo.close()