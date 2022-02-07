print('Hello Pi!')
print('Qual precisão de Pi você deseja?')
n = int(input())
soma = 0
for i in range(0, n):
    impar = i * 2 + 1
    sinal = (-1)**i
    termo = sinal * 1/impar
    soma = soma + termo
    pi = 4 * soma
    print(pi)