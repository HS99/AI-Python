# Open a file
fo = open("text2.txt", "r+")
str = fo.read(5)
print ("Read String is : ", str)
# Check current position
position = fo.tell()
print ("Current file position : ", position)
# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(5)
print ("Again read String is : ", str)
# Close opened file
fo.close()