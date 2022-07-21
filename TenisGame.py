'''Escriba un programa para manejar cada uno de estos requisitos de puntuación: 
    Los jugadores deben ser capaces de sumar puntos.
    El juego debe ser capaz de terminar con un ganador.
    El caso de "deuce" debe ser manejado.
    El caso de “Tie Brake” debe ser manejado también.
    Después de que un juego haya sido ganado, se debe poder determinar al ganador.
    Se debe poder obtener la puntuación actual de cualquier jugador en cualquier momento 
    durante el juego. '''

import random
from re import T
import time 

class Game():
    def __init__(self):
        self.secuenciaPuntos = [0, 15, 30, 40]
        self.puntosJugador_1 = 0
        self.puntosJugador_2 = 0
        self.deuce = False
        self.ganador = None

    def puntoPara(self):
        return random.randint(1, 2)
    
    def jugar(self):
        ganador = self.puntoPara()
        print('Punto para Jugador %s' % (ganador))

        puntosAntesDelGame = getattr(self, 'puntosJugador_'+str(ganador))

        if self.deuce:
            if self.puntosJugador_1 > self.puntosJugador_2 and ganador == 1:
                setattr(self, 'puntosJugador_'+str(ganador), puntosAntesDelGame+1)
                print('Punto para el Jugador 1')
            elif self.puntosJugador_1 > self.puntosJugador_2 and ganador == 2:
                self.puntosJugador_1 = self.puntosJugador_1 - 1
            elif self.puntosJugador_2 > self.puntosJugador_1 and ganador == 2:
                setattr(self, 'puntosJugador_'+str(ganador), puntosAntesDelGame+1)
                print('Punto para el Jugador 2')
            elif self.puntosJugador_2 > self.puntosJugador_1 and ganador == 1:
                self.puntosJugador_2 = self.puntosJugador_2 - 1
            else:
                setattr(self, 'puntosJugador_'+str(ganador), puntosAntesDelGame+1)
                print('El Jugador %s está en ventaja' % (ganador))
        else:
            setattr(self, 'puntosJugador_'+str(ganador), puntosAntesDelGame+1)

        self.check_deuce()

    def check_deuce(self):
        if not self.deuce and (self.puntosJugador_1 == self.puntosJugador_2 == len(self.secuenciaPuntos)-1):
            self.deuce = True
    
    def fin(self):
        final = False

        x = (self.puntosJugador_1 > self.puntosJugador_2 and self.puntosJugador_1 == len(self.secuenciaPuntos)) or (self.
            puntosJugador_2 > self.puntosJugador_1 and self.puntosJugador_2 >= len(self.secuenciaPuntos))
        
        if not self.deuce and x:
            final = True

        if self.deuce and (self.puntosJugador_1 > self.puntosJugador_2 and self.puntosJugador_1 == len(self.
        secuenciaPuntos)+1) or (self.puntosJugador_2 > self.puntosJugador_1 and self.puntosJugador_2 >= len(self.secuenciaPuntos)+1):
            final = True
        
        if final:
            if self.puntosJugador_1 > self.puntosJugador_2:
                self.ganador = 1
            else:
                self.ganador = 2
        return final

    def verPuntuacion(self):
        if self.deuce and self.puntosJugador_1 > self.puntosJugador_2:
            puntosJ1 = 'V'
        elif self.puntosJugador_1 < len(self.secuenciaPuntos)-1:
            puntosJ1 = self.secuenciaPuntos[self.puntosJugador_1]
        else:
            puntosJ1 = self.secuenciaPuntos[len(self.secuenciaPuntos)-1]
        
        if self.deuce and self.puntosJugador_2 > self.puntosJugador_1:
            puntosJ2 = 'V'
        elif self.puntosJugador_2 < len(self.secuenciaPuntos)-1:
            puntosJ2 = self.secuenciaPuntos[self.puntosJugador_2]
        else:
            puntosJ2 = self.secuenciaPuntos[len(self.secuenciaPuntos)-1]

        print('====================')
        print('JUGADOR 1 | %s ' % (puntosJ1))
        print('JUGADOR 2 | %s ' % (puntosJ2))
        print('====================')

class Set():
    def __init__(self, cant_games = 6):
        self.puntosJugador_1 = 0
        self.puntosJugador_2 = 0

        self.cant_games = cant_games
        self.games = []
        self.game_actual = 0

        self.ganador = None

    def jugarSet(self):
        game_nuevo = Game()
        self.game_actual+=1
        while not game_nuevo.fin():
            game_nuevo.jugar()
            game_nuevo.verPuntuacion()
            time.sleep(0)
        
        setattr(self, 'puntosJugador_'+str(game_nuevo.ganador), getattr(self, 'puntosJugador_'+str(game_nuevo.ganador))+1)

        self.games.append(game_nuevo)

    def verPuntuacion(self):
        print('\n+++++GAME%s++++++++'% (self.game_actual))
        print('JUGADOR 1 | %s ' % (self.puntosJugador_1))
        print('JUGADOR 2 | %s ' % (self.puntosJugador_2))
        print('++++++++++++++++++\n')

    def fin(self):
        final = False
        if self.game_actual >= self.cant_games:
            if self.puntosJugador_1 > self.puntosJugador_2:
                self.ganador = 1
                final = True  
            elif self.puntosJugador_2 > self.puntosJugador_1:
                self.ganador = 2
                final = True
            elif self.puntosJugador_1 == self.puntosJugador_2: ###
                print('\n_-_-_-_TIE BREAK_-_-_-_\n')
                tieBreak = TieBreakGame()
                while not tieBreak.finalTB():
                    tieBreak.jugarTieBreak()
                    tieBreak.verPuntosTB()
                self.ganador = tieBreak.ganadorTB
                final = True
        return final


class TieBreakGame():  ###
    def __init__(self):
        self.puntosJ1 = 0
        self.puntosJ2 = 0
        self.ganadorTB = None
        self.secuenciaTB = [0, 1, 2, 3, 4, 5, 6, 7]

    def jugarTieBreak(self):
        self.ganadorTB = random.randint(1, 2)

        if self.ganadorTB == 1:
            self.puntosJ1 += 1
        else:
            self.puntosJ2 += 1

        puntosJ1 = self.secuenciaTB[self.puntosJ1]
        puntosJ2 = self.secuenciaTB[self.puntosJ2]
        
        if puntosJ1 == puntosJ2 == len(self.secuenciaTB)-1:
            self.secuenciaTB.append(len(self.secuenciaTB)) 
        elif puntosJ1 > puntosJ2 and puntosJ1 == len(self.secuenciaTB)+1:
           self.secuenciaTB.append(self.puntosJ1+1)
        elif puntosJ2 > puntosJ1 and puntosJ2 == len(self.secuenciaTB)+1:
            self.secuenciaTB.append(self.puntosJ2+1)

    def verPuntosTB(self):
        if self.ganadorTB == 1:
            print('Punto para JUGADOR %s' % (self.ganadorTB))
        else:
            print('Punto para JUGADOR %s' % (self.ganadorTB))

        print('--------------------------')
        print('JUGADOR 1 | %s ' % (self.puntosJ1))
        print('JUGADOR 2 | %s ' % (self.puntosJ2))
        print('------------------------\n')


    def finalTB(self):
        fin = False
       
        if self.puntosJ1 > self.puntosJ2 and (self.puntosJ1 >= len(self.secuenciaTB)-1) or (self.
        puntosJ2 > self.puntosJ1 and (self.puntosJ2 >= len(self.secuenciaTB)-1)):
            fin = True

        if fin:
            if self.puntosJ1 > self.puntosJ2:
                self.ganadorTB = 1 
            else:
                self.ganadorTB = 2    
        return fin
        


class Partido():
    def __init__(self, sets = 3, games = 6):
        self.puntosJ1 = 0
        self.puntosJ2 = 0

        self.games = games
        
        self.cantidadSets = sets
        self.sets = []

        self.ganador = None
        self.set_actual = 0
    
    def verPuntuacion(self):
        print('===========SET %s ===========' % (self.set_actual))
        print('\tJUGADOR 1 | %s ' % (self.puntosJ1))
        print('\tJUGADOR 2 | %s ' % (self.puntosJ2))
        print('============================\n')

    def jugar(self):
        for numSet in range(1, self.cantidadSets+1):
            self.set_actual = numSet
            nuevo_set = Set(cant_games=self.games)
            while not nuevo_set.fin():
                nuevo_set.jugarSet()
                nuevo_set.verPuntuacion()
                time.sleep(0)

            if nuevo_set.ganador == 1:
                self.puntosJ1+=1
            else:
                self.puntosJ2+=1
            
            self.verPuntuacion()
        self.sets.append(nuevo_set)

        if self.puntosJ1 > self.puntosJ2:
            self.ganador = 1
        else:
            self.ganador = 2


partido = Partido()
partido.jugar()

print('FIN DEL JUEGO')
print('GANADOR')
print('JUGADOR' + str(partido.ganador))

#Implementar Tie Break:    
'''Tie Break>> La partida gana cuando un jugador gana 3 sets. Cada set se gana si un jugador llega a 6 games, 
siempre y cuando tenga diferencia de 2 games con su contrincante. En caso de que ambos lleguen a 6 games ese 
set se definirá por Tie brake. Aquí la secuencia de puntos es de 1 en 1 y gana el primero que llega a 7 puntos 
con diferencia de 2. En caso de llegar a 6-6 el ganador deberá estirarse hasta 8-6 y así sucesivamente.'''
###Tie Break impementado##

