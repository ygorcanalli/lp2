import datetime
import time
import os

# se estiver no windows substituir o clear por cls
def limpar():
    os.system('clear')

natal = datetime.datetime(2021, 12, 25, 0, 0, 0, 0)
segundos = None
while segundos is None or segundos > 0:
    agora = datetime.datetime.now()
    restante = natal - agora
    segundos = restante.seconds
    print('Faltam', segundos, 'segundos para o Natal')
    time.sleep(1)
    limpar()
print('Hohoho feliz Natal!')