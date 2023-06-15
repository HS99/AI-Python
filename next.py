# Open a file
fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)
for index in range(5):
    try:
        line = next(fo)
        print ("Line No %d - %s" % (index, line))
    except StopIteration:
        break
# Close opened file
fo.close()