from random import choice
from os import system

print('# Jogo do Pedra Tesoura e Papel #')

lista_de_maos = ['Pedra', 'Tesoura', 'Papel']

print('Digite 1 para pedra')
print('Digite 2 para tesoura')
print('Digite 3 para papel')

escolher_mao = int(input('Qual quer escolher para jogada: '))
mao_escolhida = choice(lista_de_maos)
system('cls')

print('# Jogo do Pedra Tesoura e Papel #')
def maos():
    print(f'Sua mão: {escolher_mao}')
    print(f'Mão escolhida pela maquina: {mao_escolhida}')


if escolher_mao == 1 and mao_escolhida == 'Pedra':
    escolher_mao = 'Pedra'
    maos()
    print('Empate tente novamente')
elif escolher_mao == 1 and mao_escolhida == 'Tesoura': 
    escolher_mao = 'Pedra'
    maos()
    print('Parabens voce venceu siiuuu')
elif escolher_mao == 1 and mao_escolhida == 'Papel':
    escolher_mao = 'Pedra'
    maos()
    print('Voce perdeuu')
elif escolher_mao == 2 and mao_escolhida == 'Pedra':
    escolher_mao = 'Tesoura'
    maos()
    print('Voce perdeuuuuu')
elif escolher_mao == 2 and mao_escolhida == 'Tesoura':
    escolher_mao = 'Tesoura'
    maos()
    print('Empate tente novamente')
elif escolher_mao == 2 and mao_escolhida == 'Papel':
    escolher_mao = 'Tesoura'
    maos()
    print('Voce venceu siuuuu')
elif escolher_mao == 3 and mao_escolhida == 'Pedra':
    escolher_mao = 'Papel'
    maos()
    print('Voce venceuu siuuu')
elif escolher_mao == 3 and mao_escolhida == 'Tesoura':
    escolher_mao = 'Papel'
    maos()
    print('perdeu kkkk')
elif escolher_mao == 3 and mao_escolhida == 'Papel':
    escolher_mao = 'Papel'
    maos()
    print('Empate tente novamente')