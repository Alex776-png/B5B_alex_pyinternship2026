with open("my_story.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        print(line, "-", len(line), "characters")