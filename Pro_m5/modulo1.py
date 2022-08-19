'''Código para imprimir uma palavra em caso de numero divisivel por 5 ou 7'''
import mult

var = int(input("Insira um número natural: "))

class TestDiv:

    '''Verificar se o numero é divisivel por 5 ou 7 e retornar a palavra'''
    def __init__(self):
        pass

    def test(self):
        ''' Retorno da palavra '''
        result = mult.div(var)
        return result


FINAL = TestDiv.test(var)
print(FINAL)
