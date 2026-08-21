import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()
        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@timer
def sum_to_million():
    total = 0

    for i in range(1, 1000001):
        total += i

    return total


print("Sum:", sum_to_million())