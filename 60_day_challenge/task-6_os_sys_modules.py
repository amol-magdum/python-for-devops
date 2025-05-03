import os

# # current working directory
# cwd = os.getcwd() 
# print("Current working directory:", cwd)

# # change dir
# def current_path(): 
#     print("Current working directory before") 
#     print(os.getcwd()) 
#     print() 
# current_path() 
# os.chdir('../') 
# current_path() 

# ## create dir
directory = "GeeksforGeeks"
parent_dir = "/test/"
path = os.path.join(parent_dir, directory)

os.mkdirs(path)
print("Directory '% s' created" % directory)
directory = "Geeks"
parent_dir = "/test/"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

## listing dir
dir_list = os.listdir(path) 

## delete files in dir if dir contain another dir the OSerror raised
for file in dir_list: 
    os.remove(file)
print("Files in '% s' deleted" % directory)

## delete dir - delete empty directories
os.rmdir(path)
print("Directory '% s' deleted" % directory)
