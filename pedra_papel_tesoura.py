import random
while True:

    selection = ["papel", "pedra", "tesoura"]
    restart = ["y", "n"]
    jogada_PC = random.choice(selection)

    jogada_player = ''

    input_message = "digite sua jogada:\n"

    for index, item in enumerate(selection):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Você escolheu: '

    while jogada_player.lower() not in selection:
        jogada_player = input(input_message)

    print("pc jogou: " + "" + jogada_PC)

    # empates
    if jogada_player == "papel" and jogada_PC == "papel":
        print("empate")
    else:
        if jogada_player == "pedra" and jogada_PC == "pedra":
            print("empate")
        else:
            if jogada_player == "tesoura" and jogada_PC == "tesoura":
                print("empate")

    # papel
    if jogada_player == "papel" and jogada_PC == "tesoura":
        print("PC ganhou")
    else:
        if jogada_player == "papel" and jogada_PC == "pedra":
            print("Player ganhou")

    # pedra
    if jogada_player == "pedra" and jogada_PC == "tesoura":
        print("Player Ganhou")
    else:
        if jogada_player == "pedra" and jogada_PC == "papel":
            print("PC ganhou")

    # tesoura
    if jogada_player == "tesoura" and jogada_PC == "pedra":
        print("PC ganhou")
    else:
        if jogada_player == "tesoura" and jogada_PC == "papel":
            print("Player ganhou")

    # main program
    while True:
        answer = str(input('jogar novamente? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        jogada_player
    else:
        print("até a próxima")
        break
