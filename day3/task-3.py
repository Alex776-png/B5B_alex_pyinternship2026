random_int=[1,1,2,3,4,6,5,5,69,8,21,4,9,10,21]

for random_int in ran_int:
    if random_int not in ran_int:
        ran_int.append(random_int)

print(ran_int)