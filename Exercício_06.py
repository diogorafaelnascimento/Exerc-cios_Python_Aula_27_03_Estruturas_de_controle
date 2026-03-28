'''6. Faça uma calculadora simples contendo as operações:
soma, subtração, divisão e multiplicação.
Solicite ao usuário que informe dois número e que informe também a operação
que deseja realizar (+, -, /, *) e depois exiba o resultado.'''
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while True:
    operacao = input('''Escolha uma das operações abaixo para calcular entre os números escolhidos:
    [A] somar
    [B] subtrair
    [C] dividir
    [D] multiplicar
    ''').strip().upper()
    if operacao == 'A':
        print(f'A soma entre {n1} e {n2} resulta em {n1 + n2}')
        break
    elif operacao == 'B':
        print(f'A diferença entre {n1} e {n2} resulta em {n1 - n2}')
        break
    elif operacao == 'C':
        print(f'A divisão entre {n1} e {n2} resulta em {n1 / n2}')
        break
    elif operacao == 'D':
        print(f'O produto entre {n1} e {n2} resulta em {n1 * n2}')
        break
    else:
        print('Resposta inválida, tente novamente.')