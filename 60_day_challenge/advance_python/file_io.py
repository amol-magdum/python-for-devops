
### reading and printing the file
#f = open("sample.txt", "r")
# print(f.read())
# f.close()

## reading and printing the file line by line
#f = open("sample.txt", "r")
# for line in f:
#     print("line:", line, end="")
# f.close()


# ## append mode  ##if not file present it will create a new file
# f = open("sample1.txt", "a")
# f.write("\nThis is a new line added to the file.")
# f.close()

# # ## write mode  ## if file present overwrite content, no file then it will create a new file
# f = open("sample3.txt", "w")
# f.write("This is a new line added to the file.")
# f.close()

## os lib to check if file esists
import os
if os.path.exists("sample4.txt"):
    print("File exists")
else:
    print("File does not exist")
 