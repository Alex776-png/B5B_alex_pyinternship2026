def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


print(read_file_safely("example.txt"))