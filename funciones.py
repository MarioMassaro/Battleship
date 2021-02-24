import random
import numpy as np


def posicion(tablerojugador,listabarcos):
    i=9
    while i>0:
        barcoX = int(input("Introduzca la cordenada del eje x:  "))
        barcoY = int(input("introduzca la cordenada del eje y:  "))
        pregunta = int(input("0 para vertical, 1 para horizontal:   "))
        if pregunta == 0:
            tablerojugador[barcoY:barcoY+(listabarcos[9-i]), barcoX] = "1"
            listabarcos[9-i]
            i -= 1
        elif pregunta == 1:
            tablerojugador[barcoY][barcoX:barcoY+(listabarcos[9-i])] = "1"
            listabarcos[9- i]
            i -= 1
        else:
            print("por favor introduzca 1 o 2")
        print(tablerojugador)


def disparo(tableropc, tablerodisparojugador, vidaspc):
    turnoJugador = True
    while turnoJugador:
        disparoX = int(input("cordenada X del disparo:  "))
        disparoY = int(input("cordenada Y del disparo:  "))
        if tableropc[disparoX][disparoY] == "1":

            tableropc[disparoX][disparoY] = 'X'
            tablerodisparojugador[disparoX][disparoY] = 'X'
            vidaspc -= 1
            print("has dado en el objetivo\n", tablerodisparojugador)

        elif tableropc[disparoX][disparoY] == "0":

            tablerodisparojugador[disparoX][disparoY] = "-"
            tableropc[disparoX][disparoY]="-"
            print("has fallado\n", tablerodisparojugador)
            turnoJugador = False

        elif tableropc[disparoX][disparoY] == 'X':
            print("ya has impactado aqui", tablerodisparojugador)

        elif tableropc[disparoX][disparoY] == "-":
            print("ya has impactado aqui", tablerodisparojugador)

    return vidaspc


def disparopc (tablerojugador,vidasjugador):
    turnopc = True
    while turnopc:

        disparopcx = np.random.randint(10)
        disparopcy = np.random.randint(10)

        if tablerojugador[disparopcx][disparopcy] == "1":
            tablerojugador[disparopcx][disparopcy] = 'X'
            vidasjugador -= 1
            print("te han dado\n", tablerojugador)

        elif tablerojugador[disparopcx][disparopcy] == "0":
            tablerojugador[disparopcx][disparopcy] = "-"
            turnopc = False

        elif tablerojugador[disparopcx][disparopcy] == 'X':
            turnopc = False

    return vidasjugador

def menu():

	print ("Selecciona una opción")
	print ("\t1 - seguir jugando")
	print ("\t2 - salir")


def barcosrandom(tableropc, listabarcos):
    for eslora in listabarcos:
        while True:
            orient = random.choice(['N', 'S', 'E', 'O'])
            current_pos = np.random.randint(10,size=2)
            fila = current_pos[0]
            col = current_pos[1]
            coors_posiN = tableropc[fila:fila - eslora:-1, col]
            coors_posiE = tableropc[fila, col: col + eslora]
            coors_posiS = tableropc[fila:fila + eslora, col]
            coors_posiO = tableropc[fila, col:col - eslora:-1]
            if (orient == 'N') and (len(coors_posiN) == eslora) and ('1' not in coors_posiN):
                tableropc[fila:fila - eslora:-1, col] = '1'
                break
            elif (orient == 'E') and (len(coors_posiE) == eslora) and ('1' not in coors_posiE):
                tableropc[fila, col: col + eslora] = '1'
                break
            elif (orient == 'S') and (len(coors_posiS) == eslora) and ('1' not in coors_posiS):
                tableropc[fila:fila + eslora, col] = '1'
                break
            elif (orient == 'O') and (len(coors_posiO) == eslora) and ('1' not in coors_posiO):
                tableropc[fila, col:col - eslora:-1] = '1'
                break

