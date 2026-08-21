usernames = ["Norington", "Fernando", "Johan", "Hiddleston", "Bartholomew"]

long_usernames = list(
    filter(lambda username: len(username) >= 6, usernames)
)

print(long_usernames)