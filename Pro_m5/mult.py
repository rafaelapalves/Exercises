'''Conferir de o numero é divisivel por 5 ou 7'''


def div(var):
    if(var % 5 == 0) and (var % 7 == 0):
        resposta = "fizzbuzz"

    if var % 5 == 0:
        resposta = "fizz"

    if var % 7 == 0:
        resposta = "buzz"

    if(var % 5 != 0) and (var % 7 != 0):
        resposta = "miss"
    return resposta
