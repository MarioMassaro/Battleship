from funciones import *
from variables import *
vidasjugador=20
vidaspc=20

#1- generar barcos enemigos
barcosrandom(tableropc,listaBarcos)

#2-intrucciones del juego
print("           \n Bienvenido a hundir la flota \n A continuacion debera introducir los barcos en las pocisiones que desea\n")
print(" por favor, sigue las siguientes instrucciones durante la creacion de tu tablero\n")
print(" Crea:\n UN barco 4\n DOS barcos de 3\n TRES barcos de 2\n CUATRO barcos de 1")
print(" procura no poner 2 barcos en la misma posicion, si no quieres repetir el proceso\n")

#3- creacion del tablero del jugador
posicion(tablerojugador,listaBarcos)

#4-juego
while vidaspc>0 or vidasjugador>0:

    vidaspc = disparo(tableropc,tablerodisparojugador,vidaspc)

    vidasjugador = disparopc(tablerojugador,vidasjugador)
    print(vidasjugador)
    print(vidaspc)

vidaspc == 0
print('HAS GANADO')
vidasjugador == 0
print('GAME OVER')





