# Se importan las librerias requeridas
import random
from Prueba1 import Prueba1
# ERR1x2 -3
# ERR2x4 -10 Los test positivos no verifican el valor de las operaciones
# los casos negativos nunca verifican que el error retornado sea el esperado


# Caso de exito del metodo multiple_op
def test_prueba():
    # Se crean valores aleatorios de entrada
    num = random.randint(1, 100)
    # Se revisa que la entrada es un numero
    assert isinstance(num, int)
    # Se revisa que la salida sea una lista
    assert isinstance(Prueba1.multiple_op(num), list)


# Caso de error del metodo multiple_op
def test_prueba2():
    # Se define una entrada erronea
    num = "s"
    # Se revisa que la entrada es un numero
    assert isinstance(num, int)
    # Se revisa que la salida sea una lista
    assert isinstance(Prueba1.multiple_op(num), list)


# Caso de exito del metodo verify_array_op
def test_prueba3():
    # Se define i como contador y se inicializan las variables
    i = 0
    entrada = []
    # Se crea el parametro de entrada
    for i in range(2):
        valor = random.randint(1, 100)
        # Verificar que son numeros
        assert isinstance(valor, int)
        entrada.append(valor)
    # Verificar que es una lista
    assert isinstance(entrada, list)
    # Verifica el resultado
    assert isinstance(Prueba1.verify_array_op(entrada), list)


# Caso de error del metodo verify_array_op
def test_prueba4():
    # Se define i como contador y se inicializan las variables
    entrada = []
    i = 0
    # Se crea el parametro de entrada erroneo
    for i in range(2):
        valor = "a"
        # Verificar que son numeros
        assert isinstance(valor, int)
        entrada[i] = valor
    # Verificar que es una lista
    assert isinstance(entrada, list)
    # Verifica el resultado
    assert isinstance(Prueba1.verify_array_op(entrada), list)
