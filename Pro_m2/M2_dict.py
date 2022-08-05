import pytest

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

        assert {k : v} == {5 : 3}

num = int(input("Número de elementos:"))

fibo = Fibonacci()

sequence = {k+1 : v for k, v in enumerate(iter(fibo))}

print(sequence)