# Calculadora em Python


print("\n******************* Python Calculator *******************")

def inicializacao ():

    print('Selecione o número de operação desejada:\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    return
def soma (x, y):
    return x+y

def sub(x,y):
    return x - y

def mult(x, y):
    return x*y

def div(x, y):
    return x/y

inicializacao()

operacao = 0
while operacao >4 or operacao<1:
    operacao = int(input('Digite sua opção 1/2/3/4: '))
    if operacao >4 or operacao<1:
        print('Operação inválida')


x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if operacao == 1:
    print(x ,'+', y, '=', soma(x,y))
elif operacao == 2:
    print(x, '-', y, '=', sub(x, y))
elif operacao == 3:
    print(x, '*', y, '=',  mult(x, y))
elif operacao == 4:
    print(x, '/', y, '=',  div(x, y))

