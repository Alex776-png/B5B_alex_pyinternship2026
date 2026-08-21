class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()

print("Total Counter :", Counter.get_count())