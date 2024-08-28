from personaje import Personaje # Corrección del nombre del archivo
import random  # Corrección en el nombre del módulo

# Paso 1: Dar la bienvenida al jugador y solicitar el nombre
print("¡Bienvenido a Gran Fantasía!")
nombre = input( "Por favor indique el nombre de su personaje:\n")

# Paso 2: Crear el personaje del jugador y mostrar su estado
p = Personaje(nombre)
print(p.estado)

# Paso 3: Crear el personaje "Orco"
o = Personaje("Orco")

#Informar por pantalla al jugador que ha aparecido un orco y la probabilidad que tiene de ganarle
print("\n¡Oh no!, ¡Ha aparecido un Orco!")
probabilidad_ganar = p.get_probabilidad_ganar(o)  # Cambio para comparar con el orco

while True:
        # Paso 4: Informar al jugador sobre la probabilidad y las consecuencias
        opcion = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

        if opcion == 1:  # Atacar
            # Obtener el resultado del ataque
            resultado = "G" if random.uniform(0, 1) <= probabilidad_ganar else "P"

            if resultado == "G":
                print("\n¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!\n")
                p.estado = 50   # Sumar 50 puntos al personaje jugador
                o.estado = -30  # Restar 30 puntos al orco
            else:
                print("\n¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n")
                p.estado = -30   # Restar 30 puntos al personaje jugador
                o.estado = 50    # Sumar 50 puntos al orco

            # Mostrar estados actualizados
            print(p.estado)
            print(o.estado)

            # Actualizar la probabilidad de ganar después del ataque
            probabilidad_ganar = p.get_probabilidad_ganar(o)
        
        elif opcion == 2:  # Huir
            # Informar que el orco ha quedado atrás
            print("\nHas decidido huir. El orco ha quedado atrás.")
            break  # Salir del bucle de juego


