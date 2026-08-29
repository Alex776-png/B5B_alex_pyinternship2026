import os

user_key = os.environ.get("USER_KEY")

if user_key:
    print(user_key)
else:
    print("Key not found")
