# Open a file
fo = open("text2.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.readlines()
print ("Read Line: %s" % (line))
line = fo.readlines(2)
print ("Read Line: %s" % (line))
# Close opened file
fo.close()