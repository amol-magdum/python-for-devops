# word_count.py
file_name = input("Enter the file name: ")
try:
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        print(words)
    word_count = len(content.split())
    print(f"✅ The file '{file_name}' contains {word_count} words.")
except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")