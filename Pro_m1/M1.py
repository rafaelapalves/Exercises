import pytest
import mult

var = int(input("Insira um número natural: "))

class Test_div:
    def setup(self):
        pass

    def test(self):
        result = mult.div(var)
        return result

        assert result == "miss"

final = Test_div.test(var)
print(final)