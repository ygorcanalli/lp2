itens = ['cadeira', 'mesa', 'sofá', 'estante', 'banco', 'tapete']
quantidades = [10, 50, 0, 3, 8, 21]

print('Consulta ao estoque, digite o nome do item desejado')
busca = input()
print('Digite a quantidade de itens a serem retirados')
qtd = int(input())

compra_efetivada = False

for i in range(len(itens)):
    if busca == itens[i]:
        if qtd <= quantidades[i]:
            print('Você acaba de adquirir', qtd, busca)
            quantidades[i] = quantidades[i] - qtd
            compra_efetivada = True
        else:
            print('Infelizmente não temos a quantidade desejada')
if compra_efetivada == False:
    print('Infelimente não temos o item desejado na quantidade pedida')