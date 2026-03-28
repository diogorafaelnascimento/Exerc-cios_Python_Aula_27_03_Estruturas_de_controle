#5. Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
elif n1 < n2:
    print(f'O número {n2} é maior que {n1}')
else:
    print('Os números digitados são iguais')