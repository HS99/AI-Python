import os
# Rename a file from test1.txt to test2.txt
os.rename( "text4.txt", "text5.txt" )
# Delete file test2.txt
os.remove("text1.txt")
# Create a directory "test"
os.mkdir("test")
# Changing a directory to "/home/newdir"
#os.chdir("test")
# This would give location of the current directory
#os.getcwd()
# This would remove "/tmp/test" directory.
os.rmdir( "test" )