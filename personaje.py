class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0  # Ajustar el valor numérico correcto : 0


    @property
    def estado(self):
        # Método para obtener el estado del personaje. La expresión correcta es EXP: {self.experiencia}
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"



    @estado.setter
    def estado(self, exp):
        # Método para asignar experiencia al personaje y ajustar nivel en consecuencia
        tmp_exp = self.experiencia + exp

        # Asegura que la experiencia se mantenga en un rango válido
        while tmp_exp >= 100:
            self.nivel += 1  # Incrementamos el nivel en 1
            tmp_exp -= 100  # Reducimos la experiencia en 100 por cada nivel ganado
        
        while tmp_exp < 0:
            if self.nivel > 1:
                self.nivel -= 1  # Decrementamos el nivel en 1
                tmp_exp += 100  # Aumentamos la experiencia en 100 por cada nivel perdido
            else:
                tmp_exp = 0  # Mantenemos la experiencia en 0 si el nivel es 1

        self.experiencia = tmp_exp

    
    def __lt__(self, other):
        # Comparación basada en nivel y no en experiencia
        return self.nivel < other.nivel

    def __gt__(self, other):
        # Comparación basada en nivel y no en experiencia
        return self.nivel > other.nivel

    def __eq__(self, other):
        # Comparación basada en nivel y no en experiencia
        return self.nivel == other.nivel

    def get_probabilidad_ganar(self, other):
        # Método para determinar la probabilidad de ganar
        if self < other:
            return 0.33  # Menor nivel, menor probabilidad
        elif self > other:
            return 0.66  # Mayor nivel, mayor probabilidad
        else:
            return 0.5  # Mismo nivel, probabilidad intermedia

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        # Método estático para mostrar opciones de juego
        return int(input(
            f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100} % "
            "de probabilidades de ganar contra el Orco.\n"
            "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\n" # Agregar las "" faltantes al final de la línea y modificar puntuación
            "\nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n" # Agregar /n al principio de la línea y modificar puntuación
            "\n¿Qué deseas hacer?\n"
            "1. Atacar\n" # Modificar el orden 
            "2. Huir\n"   # Modificar el orden
        ))
