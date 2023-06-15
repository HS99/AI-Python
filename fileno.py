# Open a file
fo = open("text2.txt", "wb")
print ("Name of the file: ", fo.name)
fid = fo.fileno()
print ("File Descriptor: ", fid)
# Close opend file
fo.close()