# 4. Using filter() and lambda to keep usernames
# that are at least 6 characters long

usernames = ["raj", "rahul123", "admin", "python", "student"]

long_usernames = list(
    filter(lambda username: len(username) >= 6, usernames)
)

print(long_usernames)