# Open a file
fo = open("text2.txt", "wb")
print ("Name of the file: ", fo.name)
ret = fo.isatty()
print ("Return value : ", ret)
# Close opend file
fo.close()