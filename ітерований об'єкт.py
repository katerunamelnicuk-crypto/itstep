class It_obg:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
class Ret_it:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return It_obg(self.start, self.end)
numbers = Ret_it(1, 8)
for num in numbers:
    print(num)