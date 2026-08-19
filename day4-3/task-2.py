def get_value(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None


numbers = [10, 20, 30]

print(get_value(numbers, 1))   # 20
print(get_value(numbers, 5))   # None