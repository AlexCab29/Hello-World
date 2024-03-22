"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
#Definicion de las cartas de la memorama "Aqui se deben de colocar los emojis ejemplo tiles= nombrepor filaf"""

tiles = '''\U0001F1E6\U0001F1E9
\U0001F1E6\U0001F1EB
\U0001F1E6\U0001F1F1
\U0001F1E6\U0001F1F7
\U0001F1E6\U0001F1F9
\U0001F1E6\U0001F1FA
\U0001F1E6\U0001F1E7

\U0001F1E7\U0001F1EA
\U0001F1E7\U0001F1F4
\U0001F1E7\U0001F1F7
\U0001F1E7\U0001F1F8
\U0001F1E7\U0001F1FB
\U0001F1E7\U0001F1E6
\U0001F1E7\U0001F1ED
\U0001F1E7\U0001F1F0
\U0001F1E7\U0001F1F1
\U0001F1E7\U0001F1F2
\U0001F1E7\U0001F1F3
\U0001F1E7\U0001F1F4
\U0001F1E7\U0001F1F5
\U0001F1E7\U0001F1F5
\U0001F1E7\U0001F1F7
\U0001F1E7\U0001F1FF
\U0001F1E7\U0001F1EA
\U0001F1E7\U0001F1F0
\U0001F1E7\U0001F1F4
\U0001F1E7\U0001F1E6
\U0001F1E8\U0001F1E8
\U0001F1E8\U0001F1EA
\U0001F1E8\U0001F1EC
\U0001F1E8\U0001F1FA
\U0001F1E8\U0001F1E7'''
tiles = tiles.split('\n') *2

#Indica si ya tengo una carta destapada, si es None es la primera carta 
state = {'mark': None}
#Cartas tapadas en un inicio
hide = [True] * 64
#Inicializar el contador de taps con 0
Taps = 0
lapiz1 = Turtle(visible = False)
lapiz2 = Turtle(visible = False)

def nombres():
    #levantar lapiz
    lapiz2.up()
    #mover el lapiz a la ubicacion donde vas a escribir 
    lapiz2.goto(-300,218)
    #esribir nombre
    lapiz2.write("Alvaro Alejandro Cabañas Calvillo A01625742",font=('Times New Roman', 19, 'normal'))
    lapiz2.goto(-300,240)
    lapiz2.write("Alejandro Guzmán Bortoni A01740787",font=('Times New Roman', 19, 'normal'))
    lapiz2.goto(-300,262)
    lapiz2.write("Sebastián Peñafiel Félix A01198539",font=('Times New Roman', 19, 'normal'))
    
    lapiz2.goto(-50,-300)
    lapiz2.write("Memorama",font=('Times New Roman', 19, 'normal'))

def square(x, y):
    """Draw white square with black outline at (x, y). esq. inferior izq"""
    up()
    goto(x, y)
    down()
    color('white', 'gray')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    
    """Update mark and hidden tiles based on tap."""
    global Taps
    
    #Validar el área de los taps
    if (x >= -200 and x <= 200)  and (y >= -200 and y <= 200):
    #Posicion de la ultima carta seleccionada
        Taps += 1
        lapiz1.clear()
        lapiz1.up()
        lapiz1.goto(-80,-250)
        lapiz1.write(f"Taps = {Taps}",font=('Times New Roman', 30, 'normal'))
        spot = index(x, y)
        mark = state['mark']
    #Posicion de la carta anterior o None
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        #Si fue par, destapar 2 cartas
        hide[spot] = False
        hide[mark] = False
        #Ya no existe carta destapada
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    #Plasma la imagen en el punto 0,0
    shape(car)
    stamp()

    #Encargado de dibujar los cuadros de las cartas tapadas
    for count in range(64):
        if hide[count]:
            #Trae a llamar la posicion de el lado inferior izq
            x, y = xy(count)
            
            square(x, y)
            #Coordenadas de inicio -200,-200
            

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('white')
        write(tiles[mark], font=('Times New Roman', 30, 'normal'))

    update()
    
    if hide.count(True)== 0:
        up()
        color("black")
        goto(-300,-150)
        write(" \U0001F3C6¡Felicidades!\U0001F3C6 ganaste un Auto",font=('Times New Roman', 30, 'normal'))
        #Desactivamos la funcion callbakc  del mouse
        onscreenclick(None)
    
    ontimer(draw, 100)
    
#Desactiva los clicks
    
#onscreenclick(None)
    #update()
    #ontimer(draw,100)
#shuffle(tiles)

bgcolor("brown")#Instruccion 1
setup(620, 620, 370, 0)
title("Semana Tec: Sebastian, Alejandro, Alvaro")
lapiz1.color("red")
lapiz2.color("black")
nombres()
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

