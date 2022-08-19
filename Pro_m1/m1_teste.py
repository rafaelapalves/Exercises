import pytest
import mult

var = 15

class Test_div:
    def setup(self):
        pass

    def test(self):
        result = mult.div(var)
        assert result == "fizz"
        return result



final = Test_div.test(var)
print(final)