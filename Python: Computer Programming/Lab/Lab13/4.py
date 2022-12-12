filename = input("Enter a filename: ")


class FileInputError(BaseException):
    pass


try:
    textfile = open(filename, "r")
except FileNotFoundError:
    print("Nonexistent file!")
    exit()

old_str = input("Enter the old string to be replaced: ")
new_str = input("Enter the new string to replace the old string: ")

try:
    if old_str == new_str:
        raise FileInputError
except FileInputError:
    print("The new string and old string are the same input string!")
    quit()

file = textfile.read().replace(old_str, new_str)
newFile = open(filename, "w")
newFile.write(file)
