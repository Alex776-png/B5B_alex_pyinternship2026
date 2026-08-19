no = [12, 5, 12, 7, 5, 20, 7, 3, 15, 20, 8, 3, 69, 21, 3]

no2 = []

for no in no:
    if no not in no2:
        no2.append(no)

print(no2)