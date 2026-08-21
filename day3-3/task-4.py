words = ["alpha", "ant", "browns", "bat", "chris", "carrot"]

grouped_words = {}

for word in words:
    first_letter = word[0]
    grouped_words.setdefault(first_letter, []).append(word)

print(grouped_words)