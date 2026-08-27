with open("input.txt", "r") as input_file:
    contents = input_file.read()

with open("copy.txt", "w") as output_file:
    output_file.write(contents)

print("Contents copied successfully.")