# jogo da velha com dicionarios:
tabuleiro: dict = {
    1: '', 2: '', 3: '',
    4: '', 5: '', 6: '',
    7: '', 8: '', 9: ''
}
player1: str = 'X'
player2: str = 'O'
ok = True
try:
    escolha: int = int(input('1) Player1 : X\n2) Player2 : O'))
    if escolha == 1:
        print('Player 1 escolhido -- X')
    elif escolha == 2:
        print('Player 2 escolhido -- O')
    else:
        print('Opção inválida')
        exit(1)
    print('Player1 começa: ')
    while ok:
        print('Escolha uma posição no tabuleiro: ')
        try:
            print('Player1:')
            posicao: int = int(input('>>> '))
            tabuleiro.get(posicao, 'X')
            print('Player2:')
            posicao: int = int(input('>>> '))
            tabuleiro.get(posicao, 'O')
            print('Player1:')
            posicao: int = int(input('>>> '))
            tabuleiro.get(posicao, 'X')
            print('Player2:')
            posicao: int = int(input('>>> '))
            tabuleiro.get(posicao, 'O')
            print('Player1:')
            posicao: int = int(input('>>> '))
            tabuleiro.get(posicao, 'X')
            if tabuleiro[1] != 'X' and tabuleiro [2] != 'X' and tabuleiro[3] != 'X' or tabuleiro[4] != 'X' and tabuleiro [5] != 'X' and tabuleiro[6] != 'X' or tabuleiro[7] != 'X' and tabuleiro [8] != 'X' and tabuleiro[9] != 'X' or tabuleiro[1] != 'O' and tabuleiro [2] != 'O' and tabuleiro[3] != 'O':
                ok = False
                print(tabuleiro.items())
        except ValueError or TypeError:
            print('Valor incorreto')
except ValueError or TypeError:
    print('Houve um erro inesperado')
