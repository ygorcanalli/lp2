print('Entre com o valor inicial da PA')
inicial = int(input())
print('Entre com a razão da PA')
r = int(input())
print('Entre com o número de repetições da PA')
n = int(input())

for i in range(0, n + 1):
    print(inicial + r * i)