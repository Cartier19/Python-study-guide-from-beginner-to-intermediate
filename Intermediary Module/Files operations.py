# Opening a file
# The argument of the open function is the path to the file
myfile = open("filename.txt")

# You can specify the mode used to open a file by applying a second argument to the open function.
# "r"- default mode, means open in read mode.
# "w"- means write mode for editing and rewriting the contents of a file.
# "a"- mean append mode for adding new content to the end of the file.
# "b"- means to open a file in binary mode, which is used for non-text files(such as images and sound files)

# To close
file = open("filename.txt", "w")
#do stuff to the file
file.close()

# Reading a file
# Assuming we have a books.txt file on the server which includes the titles of books.
# Let's read the file and output the content
file = open("/usercode/files/books.txt")
cont = file.read()
print(cont)
file.close()

# Reading a certain amount of a file
file = open("/usercode/files/books.txt")
print(file.read(5))
print(file.read(7))
file.close()

# Retrieving lines in a file
file = open("/usercode/files/books.txt")
for line in file.readlines():
    print(line)
file.close()

# Writing Files
file = open("/usercode/files/books.txt", "a")
file.write("This has been written to a file")
file.close()
# Using the append mode
file = open("newfile.txt", "w")
file.write("\nThe Da Vinci Code")
file.close()
# Getting the number of bytes written to  file
msg = "Hello World"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()