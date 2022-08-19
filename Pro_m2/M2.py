import pytest

num = int(input("Número de elementos:"))

class Fibonacci:
    def __iter__(self):
        self.var = 0
        self.var2 = 1
        self.num = num
        return self

    def __next__(self):
        result = self.var
        self.var += self.var2
        self.var2 = result
        self.num -= 1

        if self.num < 0:
            raise StopIteration

        return result

        assert len(sequence) == num

fibo = Fibonacci()

for c in iter(fibo):
    print(c)