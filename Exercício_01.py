#1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.
num = int(input('Digite um número inteiro: '))
if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
elif num == 0:
    print('O número digitado é "0"')