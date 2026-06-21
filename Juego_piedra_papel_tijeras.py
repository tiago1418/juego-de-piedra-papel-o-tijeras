import random

# Marcador
victorias = 0
derrotas = 0
empates = 0

# Opciones del juego
opciones = ["piedra", "papel", "tijeras"]

print("================================")
print(" JUEGO PIEDRA, PAPEL O TIJERAS ")
print("================================")

while True:

    jugador = input("\nElige piedra, papel o tijeras: ").lower()

    # Validar la opción ingresada
    if jugador not in opciones:
        print("Opción no válida. Intenta nuevamente.")
        continue

    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)

    print("Tú elegiste:", jugador)
    print("La computadora eligió:", computadora)

    # Determinar el ganador
    if jugador == computadora:
        print("¡Empate!")
        empates += 1

    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):

        print("¡Ganaste!")
        victorias += 1

    else:
        print("¡La computadora gana!")
        derrotas += 1

    # Mostrar marcador
    print("\n--- MARCADOR ---")
    print("Victorias:", victorias)
    print("Derrotas:", derrotas)
    print("Empates:", empates)

    # Preguntar si desea continuar
    respuesta = input("\n¿Deseas jugar otra vez? (s/n): ").lower()

    if respuesta != "s":
        break

print("\nGracias por jugar.")
print("Resultado final:")
print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)
