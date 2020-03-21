from random import randint

wins = {
    "Tijeras": ["Papel", "Lagarto"],
    "Piedra": ["Tijeras", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Lagarto": ["Papel", "Spock"],
    "Spock": ["Piedra", "Tijeras"],
}
player = 0
npc = 0


def new_game():
    global player, npc
    player = 0
    npc = 0


def get_mano():
    while True:
        try:
            mano = input("Tu jugada: ").strip().lower()
        except KeyboardInterrupt:
            print("\nSaliendo del juego.")
            exit()

        if mano in "t tijeras tijera scizors".split():
            jugada = "Tijeras"
        elif mano in "pi piedra piedras r rock".split():
            jugada = "Piedra"
        elif mano in "pa papel p paper".split():
            jugada = "Papel"
        elif mano in "s spock spok".split():
            jugada = "Spock"
        elif mano in "l lizard lagarto lag liz lizzard".split():
            jugada = "Lagarto"
        elif mano in "salir exit":
            print("Saliendo del juego.")
            exit()
        else:
            print('Jugada no encontrada')
            continue
        print(f"Has sacado {jugada}")
        return jugada


def rand_mano():
    manos = list(wins.keys())
    return manos[randint(0, len(manos)-1)]


def get_win(player, npc):
    global wins
    # print(player, npc)
    if npc in wins[player]:
        print("El jugador gana la ronda!")
        return 1
    elif npc == player:
        print("Habéis sacado lo mismo, se repite!")
        return 0
    else:
        print("El ordenador gana la ronda!")
        return -1


def get_winner():
    global player, npc
    if player > npc:
        print("Ha ganado el jugador.")
        return True
    elif player == npc:
        print("Ha habido un empate.")
        if input("¿Desea jugar una ronda de desempate?: ").strip().lower() in 'n no'.split():
            print("="*50)
            print("La partida terminó en tablas.")
            return True
        else:
            return False
    elif npc > player:
        print("Ha ganado la máquina.")
        return True


def play():
    global player, npc
    player_win = 0
    while player_win == 0:
        player_win = turn()
    if player_win == 1:
        player += 1
    elif player_win == -1:
        npc += 1

    print("="*50)
    print(f"Puntuación: Player {player} - {npc} Computer")
    print("="*50)


def turn():
    player = get_mano()
    npc = rand_mano()
    print("El ordenador sacó "+npc)
    return get_win(player, npc)


def main(turns):
    global player, npc
    new_game()
    print("="*50)
    print("¡Nueva partida!")
    print("="*50)
    for i in range(turns):
        print(f"Turno {i+1} de {turns}.")
        play()
    acabar = get_winner()
    if acabar != True:
        print("Ronda de desempate!")
        play()
    print("="*50)
    print(f"Resultado final: Player {player} - {npc} Computer")
    print("="*50)


if __name__ == "__main__":
    while True:
        while True:
            try:
                turnos = int(input("Número de turnos: "))
                break
            except ValueError as e:
                print("Valor incorrecto.")

        main(turnos)
        if input("¿Nueva partida?: ") not in "y s yes si sí".split():
            print("Saliendo del juego.")
            exit()
