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
