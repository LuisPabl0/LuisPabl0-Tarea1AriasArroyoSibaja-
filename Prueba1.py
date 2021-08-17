# Para que un while true? Eso es mala práctica
# ERR3 -1.5 EL error es el mismo en ambos casos, debia ser único

class Prueba1:
    # Se define la funcion multiple_op
    def multiple_op(numero):
        # Se inicializa el ciclo
        while True:
            try:
                # La entrada debe ser un numero
                int(numero)
                # Se realizan las operaciones solicitas
                op1 = numero * numero
                op2 = 2 ** numero
                # Operacion de factorial
                op3 = 1
                for i in range(1, numero + 1):
                    op3 = op3 * i
                resultado = [op1, op2, op3]
                # Retrona la lista del resultado
                return (resultado)
            # Cualquier error se recibe en el Exception
            except Exception:
                return "Debe escribir un numero entero y positivo"

    def verify_array_op(entrada):
        # Se inicializa el ciclo
        while True:
            try:
                # Determinar la cantidad de valores de la lista
                rango = len(entrada)
                resultado = []
                salida = []
                # Se define i como contador
                i = 0
                # Se realizan las operaciones solicitas
                for i in range(rango):
                    numero = int(entrada[i])
                    salida = Prueba1.multiple_op(numero)
                    resultado.append(salida)
                # Retorna la lista del resultado
                return (resultado)
            # Cualquier error se recibe en el Exception
            except Exception:
                return "Debe escribir un numero entero y positivo"
