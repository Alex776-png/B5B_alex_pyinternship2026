std = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

std = sorted(std, key=lambda item: item[1], reverse=True)

print(std)