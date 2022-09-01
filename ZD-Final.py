'''Aluna: Leticia Nunes Carelli
Curso: Análise e Desenvolvimento de Sistemas
Projeto: Jogo Zombie Dice
Entrega: 17/04/2022'''

from collections import namedtuple
from random import shuffle, choice
from time import sleep

def linha():
    print('-'*39)


#definindo os dados
def dados():
    Dado = namedtuple('dado', ['cor', 'faces'])
    DadoVerde = Dado('VERDE', ['CEREBRO', 'CEREBRO', 'CEREBRO', 'PASSOS', 'PASSOS', 'TIRO']) #tupla para definir dado verde
    DadoAmarelo = Dado('AMARELO', ['CEREBRO', 'CEREBRO', 'PASSOS', 'PASSOS', 'TIRO', 'TIRO']) #tupla para definir dado amarelo
    DadoVermelho = Dado('VERMELHO', ['CEREBRO', 'PASSOS', 'PASSOS', 'TIRO', 'TIRO', 'TIRO']) #tupla para definir dado vermelho

    # colocando os dados no tubo
    tubo = []
    for i in range(6):
        tubo.append(DadoVerde)
    for i in range(4):
        tubo.append(DadoAmarelo)
    for i in range(3):
        tubo.append(DadoVermelho)

    # embaralhando os dados do tubo
    shuffle(tubo)
    return tubo

print('BEM VINDO AO JOGO ZOMBIE DICE!!\n')
sleep(1.2)
print('-> O objetivo do jogo é devorar cerebros e desviar dos tiros\n')
sleep(1.2)
print('-> Quem devorar 13 CEREBROS primeiro ganha o jogo\n')
sleep(1.2)
print('-> Tirar "PASSOS" significa que possiveis vítimas escaparam\n')
sleep(1.2)
print('-> Levando 3 TIROS você perde os cerebros devorados na rodada, então tome cuidado! \n')
linha()
sleep(1.2)


#definindo jogadores
def jogadores():
    ListaJog = []

    while True:
        try:
            QuantJog = int(input('\nDigite a quantidade de jogadores: '))
            if QuantJog > 1:
                break
            else:
                print('É necessário o mínimo de 2 jogadores para iniciar a partida') #condição para iniciar partida
        except ValueError:
            print('Por favor, digite um número inteiro')

    for i in range(QuantJog):
        nome = input(f'\nDigite o nome do {i + 1}° jogador: ').strip().upper()  #padroniza os nomes em letra maiuscula
        jogador = {'nome': nome, 'pontuação': 0}
        ListaJog.append(jogador)  #função para adicionar jogadores a lista

    shuffle(ListaJog) #define uma ordem aleatoria para os jogadores
    print('\n...........INICIANDO PARTIDA...........')
    sleep(1)
    print('\n\n----------ORDEM DOS JOGADORES----------')
    cont = 1
    for jogador in ListaJog:
        print(f"\n{cont}° jogador -> {jogador['nome']}")
        cont += 1
        sleep(0.6)
    return ListaJog


#definindo dinâmica das rodadas
def rodada(jogador):
    linha()
    print(f"\nVez do jogador {jogador['nome']}")
    sleep(0.5)

    tubo = dados()
    PontosRodada = {'CEREBROS': 0, 'TIROS': 0}
    DadosRodada = []

    while True:
        while len(DadosRodada) < 3:
            DadosRodada.append(tubo.pop()) #retirando os dados do tubo

        cont = 1
        for dado in reversed(DadosRodada):
            print(f'\n------------JOGANDO {cont}° DADO------------\n')
            cont += 1

            cor = dado.cor
            shuffle(dado.faces)
            face = choice(dado.faces)
            sleep(0.7)
            print(f'Cor: {cor}\nFace: {face}')
            sleep(0.7)


            #verificação de dados
            if face == "CEREBRO":
                PontosRodada['CEREBROS'] += 1
                tubo.append(DadosRodada.pop(DadosRodada.index(dado))) #devolvendo os dados para o tubo
            elif face == "TIRO":
                PontosRodada['TIROS'] += 1
                tubo.append(DadosRodada.pop(DadosRodada.index(dado))) #devolvendo os dados para o tubo
            shuffle(tubo)
        linha()
        print(f"CEREBROS: {PontosRodada['CEREBROS']}\nTIROS: {PontosRodada['TIROS']}")
        linha()
        if PontosRodada['TIROS'] < 3:
            resp = input('\nDeseja continuar jogando? [S/N] ').strip().upper()
            if resp != 'S':
                print(f"Você conseguiu {PontosRodada['CEREBROS']} cérebros!")
                jogador['pontuação'] += PontosRodada['CEREBROS']
                break
        else:
            print(f"\nVocê levou muitos tiros e perdeu os {PontosRodada['CEREBROS']} cerebros conquistados na rodada, tome mais cuidado na próxima vez")
            sleep(1)
            break


def placar(ListaJog):
    print('\n----------------PLACAR-----------------')
    for jogador in ListaJog:
        print(f"{jogador['nome']} --> {jogador['pontuação']} pontos.")


ListaJog = jogadores()

FimJogo = False
while not FimJogo:
    for jogador in ListaJog:
        rodada(jogador)
        if jogador['pontuação'] >= 13:
            vencedor = jogador['nome']
            FimJogo = True
    if not FimJogo:
        placar(ListaJog)
    else:
        linha()
        print(f'\nFIM DE JOGO!!')
        sleep(0.5)
        print(f'\nO vencedor foi: {vencedor}\n')
        placar(ListaJog)
