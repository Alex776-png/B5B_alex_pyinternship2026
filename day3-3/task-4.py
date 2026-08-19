words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

grouped_words = {}

for word in words:
    first_letter = word[0]
    grouped_words.setdefault(first_letter, []).append(word)

print(grouped_words)