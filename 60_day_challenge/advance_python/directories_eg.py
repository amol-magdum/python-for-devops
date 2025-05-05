import os

## current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

## change directory
os.chdir("..")
print(f"Changed Directory: {os.getcwd()}")

## list directories
directories = os.listdir()
print("Directories:")
for directory in directories:
    print(directory)