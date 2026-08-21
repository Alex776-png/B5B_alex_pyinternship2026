import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print("Time passed:", end - self.start, "seconds")


with Timer():
    for i in range(1000000):
        pass