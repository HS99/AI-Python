# Open a file in read/write mode
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
str = "\nThis is a new new new last line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write( str )
# Now read complete file from beginning.
fo.seek(0,0)
for index in range(5):
    line = next(fo)
    print ("Line No %d - %s" % (index, line))
# Close opened file
fo.close()